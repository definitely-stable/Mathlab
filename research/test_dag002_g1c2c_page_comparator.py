"""Independent exhaustive small-DAG, page counters, and resource regressions."""
import unittest
from dag002_g1c2c_page_comparator import PagedIndex, independent_dfs, pages_for_bytes


def all_dags(n):
    if n == 0:
        yield ()
        return
    for prefix in all_dags(n - 1):
        for mask in range(1 << (n - 1)):
            yield prefix + (tuple(p for p in range(n-1) if mask & (1 << p)),)


class ComparatorTests(unittest.TestCase):
    def test_exhaust_all_five_vertex_topological_dags(self):
        total = 0
        for graph in all_dags(5):
            total += 1
            for P in (8, 16):
                left = PagedIndex('bitmap', len(graph), P)
                right = PagedIndex('chain', len(graph), P)
                for v, parents in enumerate(graph):
                    for idx in (left, right):
                        old_records = {k: val for k, val in idx.pages.items() if k[0]=='label'}
                        idx.append(parents)
                        self.assertTrue(all(idx.pages[k] == val for k,val in old_records.items()))
                        self.assertEqual(idx.counters().parent_bits, v*(v+1)//2)
                    for u in range(v+1):
                        for target in range(v+1):
                            expected=independent_dfs(graph[:v+1],u,target)
                            self.assertEqual(left.query(u,target),expected,('bitmap',P,graph,u,target))
                            self.assertEqual(right.query(u,target),expected,('chain',P,graph,u,target))
        self.assertEqual(total,1024)

    def test_first_compatible_chain_is_not_felsner_bound(self):
        for graph in all_dags(4):
            c = PagedIndex('chain',len(graph),16)
            for pr in graph:
                c.append(pr)
            first = c._read_page(('manifest',0),0,'metadata')
            count = int.from_bytes(first[4:8],'little')
            self.assertTrue(1 <= count <= len(graph))

    def test_actual_page_and_wire_exactness(self):
        graph = ((),(0,),(0,),(1,2))
        for kind in ('bitmap','chain'):
            idx=PagedIndex(kind,4,8)
            for pr in graph:
                idx.append(pr)
            counter=idx.counters()
            self.assertEqual(counter.parent_bits,6)
            self.assertEqual(counter.metadata_pages, 1 if kind=='bitmap' else 2)
            self.assertEqual(counter.update_write_bytes,counter.update_writes*8)
            self.assertEqual(counter.update_read_bytes,counter.update_reads*8)
            calls=counter.update_reads+counter.update_writes+counter.metadata_reads+counter.metadata_writes+1
            self.assertEqual(counter.address_bytes,calls*3)
            prev=counter.query_reads
            self.assertTrue(idx.query(0,3))
            self.assertEqual(idx.counters().query_reads-prev,1 if kind=='bitmap' else 3)
            self.assertEqual(idx.counters().address_bytes-counter.address_bytes,
                             (1 if kind=='bitmap' else 3)*3)

    def test_family_crossover_is_not_universal_dominance(self):
        short_chain=((),)+tuple((v-1,) for v in range(1,24))
        wide_antichain=tuple(() for _ in range(24))
        b=PagedIndex('bitmap',24,16)
        c=PagedIndex('chain',24,16)
        for pr in wide_antichain:
            b.append(pr); c.append(pr)
        self.assertLess(b.counters().metadata_reads+b.counters().metadata_writes,
                        c.counters().metadata_reads+c.counters().metadata_writes)
        b2=PagedIndex('bitmap',24,16)
        c2=PagedIndex('chain',24,16)
        for pr in short_chain:
            b2.append(pr);c2.append(pr)
        self.assertEqual(b2.counters().metadata_reads+b2.counters().metadata_writes,
                         c2.counters().metadata_reads+c2.counters().metadata_writes)
        for u,v in ((0,23),(4,19),(22,23)):
            self.assertEqual(b2.query(u,v),c2.query(u,v))
        self.assertGreater(c2.counters().query_reads,b2.counters().query_reads)
        b3=PagedIndex('bitmap',160,16)
        c3=PagedIndex('chain',160,16)
        for v in range(160):
            pr=(() if v==0 else (v-1,))
            b3.append(pr);c3.append(pr)
        self.assertLess(c3.counters().label_pages,b3.counters().label_pages)
        self.assertGreater(c3.counters().metadata_writes,0)

    def test_ram_cap_is_checked_before_write(self):
        with self.assertRaises(MemoryError):
            PagedIndex('bitmap',4,16,ram_limit=31).append(())
        small=PagedIndex('chain',4,16,ram_limit=32)
        old=dict(small.pages)
        with self.assertRaises(MemoryError):
            small.append(())
        self.assertEqual(old,small.pages)
        self.assertEqual(small.parents,[])

    def test_parent_incidence_paid_even_when_empty(self):
        for kind in ('bitmap','chain'):
            idx=PagedIndex(kind,9,16)
            for _ in range(9):
                idx.append(())
            self.assertEqual(idx.counters().parent_bits,36)

    def test_parent_order_canonical_and_incorrect_inputs(self):
        for kind in ('bitmap','chain'):
            a=PagedIndex(kind,4,16)
            b=PagedIndex(kind,4,16)
            for p in ((),(),(),(2,0)):
                a.append(p)
            for p in ((),(),(),(0,2)):
                b.append(p)
            self.assertEqual(a.pages,b.pages)
            with self.assertRaises(ValueError):
                a.append(())
            for bad in ((0,0),(4,),(-1,),(True,)):
                other=PagedIndex(kind,4,16)
                other.append(())
                with self.assertRaises(ValueError):
                    other.append(bad)

    def test_query_corruption_is_not_authenticated(self):
        for kind in ('bitmap','chain'):
            idx=PagedIndex(kind,3,16)
            for pr in ((),(0,),(1,)):
                idx.append(pr)
            self.assertTrue(idx.query(0,2))
            idx.pages[('label',2,0)] = b'\0'*16
            if kind=='bitmap':
                self.assertFalse(idx.query(0,2))
            else:
                self.assertNotEqual(idx.query(0,2),True)

    def test_invalid_config(self):
        for args in (('other',5,16,99),('bitmap',0,16,99),
                     ('bitmap',4,7,99),('chain',4,16,-1)):
            with self.assertRaises(ValueError):
                PagedIndex(*args)
        self.assertEqual(pages_for_bytes(0,16),0)
        self.assertEqual(pages_for_bytes(17,16),2)
        with self.assertRaises(ValueError):
            pages_for_bytes(-1,16)
        with self.assertRaises(ValueError):
            pages_for_bytes(5,4)


if __name__=='__main__':
    unittest.main()
