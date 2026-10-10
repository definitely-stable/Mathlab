"""INDEX-001 C5-A independent fixed-page, pin, crash-prefix and allocator tests."""
import io
import itertools
import struct
import unittest
import zlib

from index001_page_epochs import Arena, Epoch, ROOT, DATA, FREE, END
from index001_hybrid_streaming import (
    from_bits,update,read_all,check,view_image,
)


def standalone_root(raw,B):
    if len(raw)!=B or raw[:4]!=ROOT:
        raise ValueError("root magic")
    got=int.from_bytes(raw[24:28],"little")
    if got!=zlib.crc32(raw[:24]) or any(raw[28:]):
        raise ValueError("root checksum")
    return struct.unpack("<4sIIIII",raw[:24])


def independent_chain(image,B):
    """No import of Arena readers, decoder, graph walk or CRC functions."""
    if len(image)%B or len(image)<B:
        raise ValueError("geometry")
    header=standalone_root(image[:B],B)
    epoch,head,count,length,checksum=header[1:]
    out=bytearray()
    ptr=head
    for i in range(count):
        if not 1<=ptr<len(image)//B:
            raise ValueError("pointer")
        block=image[ptr*B:(ptr+1)*B]
        tag,nxt,used=struct.unpack("<4sIH",block[:10])
        if tag!=DATA or used<1 or used>B-14 or any(block[10+used:-4]):
            raise ValueError("frame")
        if zlib.crc32(block[:-4])!=int.from_bytes(block[-4:],"little"):
            raise ValueError("page checksum")
        if i+1==count and nxt!=END:
            raise ValueError("unterminated")
        out.extend(block[10:10+used])
        ptr=nxt
    if len(out)!=length or zlib.crc32(out)!=checksum:
        raise ValueError("image checksum")
    return epoch,bytes(out)


def fresh_blob(bits,B,mode="B"):
    f=from_bits(bits,B,mode)
    result=view_image(f)
    f.close()
    return result


class PageEpochTests(unittest.TestCase):
    def test_initial_root_and_invalid_geometry(self):
        for B in (64,128):
            a=Arena(B)
            self.assertEqual(a.npages(),1)
            self.assertEqual(a.verify(),0)
            self.assertEqual(a.blob(),b"")
            self.assertEqual(a.root().epoch,0)
            self.assertEqual(standalone_root(a.snapshot(),B)[2],END)
            self.assertEqual(a.summary()["free_pages"],0)
            self.assertEqual(a.sweep(),0)
        for B in (0,16,63):
            with self.assertRaises(ValueError):
                Arena(B)

    def test_exhaustive_small_binary_hyb4_generations(self):
        # Source stream contains the real C4 HYB4 on-disk representation.
        for B in (64,128):
            for n in range(1,7):
                for state in itertools.product((0,1),repeat=n):
                    for mode in ("B","R","S0","S1"):
                        source=from_bits(state,B,mode)
                        a=Arena(B)
                        current=a.publish(source)
                        self.assertEqual(a.root(),current)
                        self.assertEqual(a.blob(),view_image(source))
                        self.assertEqual(independent_chain(a.snapshot(),B),
                                         (1,view_image(source)))
                        self.assertEqual(a.verify(),len(view_image(source)))
                        self.assertEqual(a.summary()["current_pages"],current.count)
                        source.close()

    def test_snapshot_pins_reclaim_and_exact_reuse(self):
        B=64;bits=tuple(i%2 for i in range(1024))
        a=Arena(B)
        f=from_bits(bits,B,"B")
        e1=a.publish(f)
        pin=a.pin()
        self.assertEqual(pin,e1)
        new,newledger=update(f,B,(0,len(bits),0),"U0")
        e2=a.publish(new)
        self.assertGreater(e2.epoch,e1.epoch)
        self.assertEqual(a.blob(pin),view_image(f))
        self.assertEqual(a.blob(),view_image(new))
        self.assertEqual(a.sweep(),0)
        before=a.summary()
        self.assertEqual(before["pinned_pages"],e1.count)
        self.assertEqual(before["current_pages"],e2.count)
        self.assertEqual(before["unreclaimed_dead_pages"],0)
        a.unpin(pin)
        self.assertEqual(a.sweep(),e1.count)
        freed=a.summary()
        self.assertEqual(freed["free_pages"],e1.count)
        expected_pages=freed["total_pages"]
        again=from_bits(bits,B,"B")
        last=a.publish(again)
        self.assertEqual(last.count,e1.count)
        self.assertEqual(a.npages(),expected_pages)
        self.assertEqual(a.blob(),view_image(again))
        self.assertGreater(a.io["reads"],0)
        self.assertGreater(a.io["writes"],0)
        self.assertEqual(a.io["gc_page_writes"],e1.count)
        f.close();new.close();again.close()

    def test_root_publish_crash_prefix_preserves_old_or_new(self):
        # hook receives every write/symbolic crash point; independent parser
        # verifies exact bytes, not just the same Arena code.
        B=64
        old=from_bits(tuple(i%2 for i in range(410)),B,"B")
        src=from_bits((0,)*410,B,"R")
        a=Arena(B)
        a.publish(old)
        original=a.snapshot()
        oldblob=view_image(old);newblob=view_image(src)
        samples=[("before",original)]
        a.publish(src,hook=lambda phase,sim: samples.append((phase,sim.snapshot())))
        self.assertGreater(len(samples),3)
        self.assertEqual(samples[-1][0],"publish")
        self.assertEqual(independent_chain(samples[-1][1],B)[1],newblob)
        for phase,image in samples:
            epoch,decoded=independent_chain(image,B)
            if phase=="publish":
                self.assertEqual((epoch,decoded),(2,newblob))
            else:
                self.assertEqual((epoch,decoded),(1,oldblob))
            recovered=Arena.recover(image,B)
            self.assertEqual(recovered.blob(),decoded)
            # On restart no pre-crash reader pins survive; partially prepared
            # unreachable DATA slots can be reclaimed safely.
            recovered.sweep()
            self.assertEqual(recovered.blob(),decoded)
            self.assertEqual(recovered.summary()["unreclaimed_dead_pages"],0)
        old.close();src.close()

    def test_pin_retention_defeats_small_page_cap_then_reclaims(self):
        B=64
        base=from_bits(tuple(i&1 for i in range(512)),B,"B")
        change=from_bits(tuple(0 for _ in range(512)),B,"U0")
        arena=Arena(B)
        old=arena.publish(base)
        pinned=arena.pin()
        # One shared persistent root and exactly old data page slots; cannot
        # stage a distinct immutable new generation while pinned.
        arena.max_pages=arena.npages()
        before=arena.blob()
        with self.assertRaises(MemoryError):
            arena.publish(change)
        self.assertEqual(arena.blob(),before)
        arena.unpin(pinned)
        self.assertEqual(arena.sweep(),0)  # current root retains old pages
        # Extra data slot required until root publication; page cap is a real
        # obstruction even after dropping the snapshot without in-place writes.
        with self.assertRaises(MemoryError):
            arena.publish(change)
        arena.max_pages=None
        arena.publish(change)
        self.assertEqual(arena.blob(),view_image(change))
        self.assertEqual(arena.sweep(),old.count)
        base.close();change.close()

    def test_corruption_root_and_page_detected_independently(self):
        B=64
        f=from_bits(tuple(i%2 for i in range(512)),B,"B")
        a=Arena(B)
        a.publish(f)
        good=a.snapshot()
        badpositions=[0,4,24,B+10,B+(B-4)]
        for pos in badpositions:
            changed=bytearray(good)
            changed[pos]^=1
            with self.assertRaises(ValueError):
                Arena.recover(bytes(changed),B)
            # Not every single byte should be caught by standalone root only;
            # entire chain CRC covers any in-page payload/footer mutation.
        with self.assertRaises(ValueError):
            Arena.recover(good[:-1],B)
        f.close()

    def test_invalid_hybrid_source_rejected_before_allocation(self):
        B=64
        src=from_bits((0,1,0,1),B,"B")
        a=Arena(B)
        first=a.publish(src)
        image=bytearray(view_image(src))
        image[7]^=1  # corrupt the opaque bitmap payload, not page root
        invalid=io.BytesIO(image)
        before=a.snapshot()
        with self.assertRaises(ValueError):
            a.publish(invalid)
        self.assertEqual(a.snapshot(),before)
        self.assertEqual(a.root(),first)
        self.assertEqual(a.blob(),view_image(src))
        self.assertGreater(a.io.get("source_preflight_pages",0),0)
        src.close()

    def test_invalid_pin_unpin_and_free_pages_protected(self):
        f=from_bits((0,1,1,0),64,"B")
        a=Arena(64)
        e=a.publish(f)
        with self.assertRaises(ValueError):
            a.unpin(e)
        token=a.pin()
        a.unpin(token)
        with self.assertRaises(ValueError):
            a.unpin(token)
        self.assertEqual(a.sweep(),0)
        f.close()

    def test_report_reproducible_scope(self):
        from index001_page_epochs import report
        z=report()
        self.assertEqual(z["schema"],"mathlab.index001.g2b4c5a.page-epoch.v1")
        self.assertEqual(z["freed_after_unpin"],z["first_pages"])
        self.assertEqual(z["after_reuse"]["free_pages"],0)
        self.assertFalse(z["os_fsync_or_torn_page_proved"])
        self.assertFalse(z["whole_program_ram_bounded"])
        self.assertFalse(z["fixed_update_working_page_buffers_claimed"])


if __name__=="__main__":
    unittest.main()
