"""Independent graph/reference and every page-write crash-cut regression."""
import unittest
from dag002_g1c2d_atomic_pages import AtomicAppendPages, page_count


def all_dags(n):
    if n == 0:
        yield ()
        return
    for prefix in all_dags(n-1):
        for mask in range(1<<(n-1)):
            yield prefix+(tuple(i for i in range(n-1) if mask & (1<<i)),)


def dfs(parents,u,v):
    pending,seen=[v],set()
    while pending:
        x=pending.pop()
        if x==u:
            return True
        if x not in seen:
            seen.add(x)
            pending.extend(parents[x])
    return False


class G1C2DCrashTests(unittest.TestCase):
    def test_all_crash_prefixes_all_small_dags(self):
        for graph in all_dags(4):
            store=AtomicAppendPages(32,128)
            for v,parents in enumerate(graph):
                plan=store.prepare_append(parents)
                self.assertEqual(plan.parent_input_bits,v)
                self.assertEqual(plan.preparation_reads,2+
                    page_count(8+8*v,32)*(v>0)+
                    sum(page_count((p+7)//8,32) for p in parents))
                self.assertEqual(plan.writes[-1][0],(v+1)&1)
                self.assertEqual(len(plan.writes),
                    page_count((v+7)//8,32)+page_count(8+8*(v+1),32)+1)
                for cut in range(len(plan.writes)+1):
                    image=store.clone()
                    image.apply_prefix(plan,cut)
                    expected=plan.new if cut==len(plan.writes) else plan.previous
                    self.assertEqual(image.recover(),expected)
                    for u in range(expected.vertices):
                        for t in range(expected.vertices):
                            self.assertEqual(image.query(u,t),
                                             dfs(graph[:expected.vertices],u,t))
                self.assertEqual(store.append(parents),v)
                for u in range(v+1):
                    for t in range(v+1):
                        self.assertEqual(store.query(u,t),dfs(graph[:v+1],u,t))

    def test_every_five_vertex_dag(self):
        for graph in all_dags(5):
            store=AtomicAppendPages(32,128)
            for parents in graph:
                store.append(parents)
            for u in range(5):
                for t in range(5):
                    self.assertEqual(store.query(u,t),dfs(graph,u,t))

    def test_aborted_writes_reuse_tail_safely(self):
        store=AtomicAppendPages(32,48)
        store.append(())
        store.append((0,))
        old=store.recover()
        plan=store.prepare_append((0,1))
        crash=store.clone()
        crash.apply_prefix(plan,len(plan.writes)-1)
        self.assertEqual(crash.recover(),old)
        self.assertGreater(crash.ledger()['uncommitted_tail_pages'],0)
        crash.append(())
        self.assertEqual(crash.recover().generation,old.generation+1)
        self.assertFalse(crash.query(0,2))
        self.assertTrue(crash.query(2,2))

    def test_multiple_directory_pages_and_parent_transitivity(self):
        store=AtomicAppendPages(32,500)
        for v in range(45):
            store.append(() if v==0 else (v-1,))
        self.assertTrue(store.query(0,44))
        self.assertTrue(store.query(37,44))
        self.assertFalse(store.query(44,0))
        self.assertGreater(store.recover().directory_pages,1)

    def test_exact_full_page_io_address_and_incidence_accounting(self):
        store=AtomicAppendPages(32,40)
        for v in range(6):
            store.append(() if not v else (v-1,))
        values=store.ledger()
        self.assertEqual(values['root_page_writes'],6)
        self.assertEqual(values['data_page_writes'],sum(
            page_count((v+7)//8,32)+page_count(8+8*(v+1),32)
            for v in range(6)))
        self.assertEqual(values['write_bytes'],32*(
            values['root_page_writes']+values['data_page_writes']))
        self.assertEqual(values['read_bytes'],32*values['charged_page_reads'])
        self.assertEqual(values['initialization_pages'],2)
        self.assertEqual(values['parent_input_bits'],15)
        self.assertEqual(values['page_request_address_bytes'],4*(
            values['charged_page_reads']+values['data_page_writes']+
            values['root_page_writes']))

    def test_no_space_is_safe_stop_not_free_gc(self):
        store=AtomicAppendPages(32,2)
        frozen=dict(store.disk)
        with self.assertRaises(MemoryError):
            store.append(())
        self.assertEqual(store.disk,frozen)
        self.assertEqual(store.recover().vertices,0)

    def test_ram_cap_rejects_before_persistent_writes(self):
        store=AtomicAppendPages(32,64,ram_limit=31)
        frozen=dict(store.disk)
        with self.assertRaises(MemoryError):
            store.append(())
        self.assertEqual(store.disk,frozen)
        self.assertEqual(store.recover().vertices,0)

    def test_crc_is_not_rollback_authentication(self):
        store=AtomicAppendPages(32,64)
        store.append(())
        old=store.disk[1]
        store.append((0,))
        self.assertEqual(store.recover().vertices,2)
        # Restore a valid old root in the newest slot: no trusted clock.
        store.disk[0]=old
        self.assertEqual(store.recover().vertices,1)
        self.assertTrue(store.query(0,0))

    def test_invalid_models_and_commands(self):
        for params in (dict(page_bytes=16),dict(capacity=1),
                       dict(ram_limit=-1),dict(page_bytes=True),
                       dict(capacity=True)):
            with self.assertRaises(ValueError):
                AtomicAppendPages(**params)
        store=AtomicAppendPages()
        with self.assertRaises(ValueError):
            store.append((0,))
        store.append(())
        for parents in ((0,0),(1,),(-1,),(True,)):
            with self.assertRaises(ValueError):
                store.prepare_append(parents)
        with self.assertRaises(ValueError):
            store.query(0,1)
        with self.assertRaises(ValueError):
            store.apply_prefix(store.prepare_append(()),-1)
        with self.assertRaises(ValueError):
            page_count(5,16)


if __name__=="__main__":
    unittest.main()
