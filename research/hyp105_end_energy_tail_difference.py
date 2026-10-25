"""Exact finite end-posting energy through nonincident-tail differences.

Independent of the SFC path/orbit enumeration. It counts each posting's
proper common-neighbor pairs, keeping original occupied endpoint labels.
The accompanying infinite packed-subfield proof concerns C1_end only.
"""
from collections import defaultdict

from hyp105_b1_symplectic import symplectic_gq
from hyp105_physical_degree_energy import minimal_alphabet, _verify_typed_injections


def end_energy_tail_difference(power, f, g):
    """Return the exact SFC C1_end for true W32/W34 full typed injections."""
    if type(power) is not int or power not in (1,2):
        raise ValueError("finite end-energy oracle supports only h=1,2")
    s = 1 << power
    V = (s+1)*(s*s+1)
    a = minimal_alphabet(V)
    f,g = tuple(map(tuple,f)),tuple(map(tuple,g))
    _verify_typed_injections(a,V,f,g)
    _,_,_,flags = symplectic_gq(power)
    original = set(flags)
    fi = {pair:p for p,pair in enumerate(f)}
    gi = {pair:l for l,pair in enumerate(g)}
    adjacent = defaultdict(set)
    for p,l in flags:
        u,v = f[p]
        x,y = g[l]
        for start,end in (((u,x),(v,y)),((u,y),(v,x))):
            adjacent[start].add(end)
            adjacent[end].add(start)
    vertices = tuple(adjacent)
    energy = envelope = eligible_tails = max_occupancy = 0
    for u in vertices:
        for v in vertices:
            common = adjacent[u].intersection(adjacent[v])
            k = len(common)
            if k < 2:
                continue
            tails = adjacent[u].difference(adjacent[v])
            envelope += len(tails)*k*(k-1)//2
            if u[0] == v[0] or u[1] == v[1]:
                continue
            for x in tails:
                if len({x[0],u[0],v[0]}) != 3 or len({x[1],u[1],v[1]}) != 3:
                    continue
                q = fi.get(tuple(sorted((x[0],v[0]))))
                r = gi.get(tuple(sorted((x[1],v[1]))))
                if q is None or r is None:
                    continue
                if (q,r) in original:
                    raise AssertionError("tail difference must imply source nonincidence")
                proper = sum(
                    len({x[0],u[0],z[0],v[0]}) == 4 and
                    len({x[1],u[1],z[1],v[1]}) == 4
                    for z in common
                )
                # x fixes the shared end flag and original endpoints;
                # each unordered free-corner pair is one C1_end collision.
                energy += proper*(proper-1)//2
                eligible_tails += 1
                max_occupancy = max(max_occupancy,proper)
    if energy > envelope:
        raise AssertionError("unmasked tail-difference envelope failed")
    return {
        "s":s,"C1_end":energy,"unmasked_envelope":envelope,
        "eligible_tail_postings_with_codegree_at_least_two":eligible_tails,
        "max_end_occupancy":max_occupancy,
        "root_sevenclass_proved":False,
    }
