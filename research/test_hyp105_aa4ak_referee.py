"""AA4-AK review oracle: STANDALONE stdlib, intentionally imports no Draft PR code.

A separate true symplectic W(3,2) construction, literal six-physical-cycle/
24-original-rook enumeration vs source-neighbor anchor, and small K_a
cross-hole charging falsifiers. No all-h proof is claimed by finite tests.
"""
import unittest
from itertools import combinations, permutations
from math import comb, isqrt
from fractions import Fraction


def edge(x,y):
    return (x,y) if x<y else (y,x)


def symplectic(x,y):
    """Alternating nondegenerate form on F_2^4."""
    b=lambda z,i:(z>>i)&1
    return (b(x,0)*b(y,2)+b(x,2)*b(y,0)
            +b(x,1)*b(y,3)+b(x,3)*b(y,1))%2


def original_W32():
    points=tuple(range(1,16))
    lines=sorted({tuple(sorted((x,y,x^y)))
                  for x,y in combinations(points,2) if symplectic(x,y)==0})
    assert len(lines)==15
    neighborhood={p:set() for p in points}
    for j,L in enumerate(lines):
        assert len(L)==3
        for p in L: neighborhood[p].add(j)
    assert all(len(neighborhood[p])==3 for p in points)
    assert len(set((p,j) for p in points for j in neighborhood[p]))==45
    assert all(len(neighborhood[p]&neighborhood[q])<=1
               for p,q in combinations(points,2))
    return points,lines,neighborhood


def source_quartets(root,physical,points):
    blocked=set(physical[root])
    others=set(range(6))-blocked
    ans=[]
    for four in combinations((p for p in points if p!=root),4):
        E={physical[q] for q in four}
        vertices={v for e in E for v in e}
        deg={v:sum(v in e for e in E) for v in vertices}
        if vertices==others and set(deg.values())=={2}:
            ans.append(four)
    return ans


def all_physical_C6():
    H=set()
    for permutation in permutations(range(1,6)):
        cycle=(0,)+permutation
        H.add(frozenset(edge(cycle[i],cycle[(i+1)%6]) for i in range(6)))
    assert len(H)==60
    return H


def independent_true_original_13_W32():
    points,lines,N=original_W32()
    K=tuple(combinations(range(6),2))
    f={p:K[(7*i+4)%15] for i,p in enumerate(points)}
    g={i:K[(11*i+2)%15] for i in range(15)}
    assert set(f.values())==set(K)==set(g.values())
    ginverse={e:i for i,e in g.items()}
    all_cycles=all_physical_C6()
    direct=anchored=cohorts=nonzero=0
    for root in points:
        quartets=source_quartets(root,f,points)
        assert len(quartets)==3
        for l0,l1 in combinations(sorted(N[root]),2):
            e0,e1=g[l0],g[l1]
            fourpins=set(e0+e1)
            if len(fourpins)<4: continue
            for q in quartets:
                cohorts+=1
                # METHOD I: literal globally occupied connected H and 4! rook
                direct_cohort=0
                for H in all_cycles:
                    if e0 not in H or e1 not in H:continue
                    free=H-{e0,e1}
                    cross=[e for e in free if
                           len(set(e)&set(e0))==1 and
                           len(set(e)&set(e1))==1]
                    if len(cross)!=1:continue
                    opposite=[ginverse[e] for e in sorted(free)]
                    direct_cohort+=sum(
                        all(opposite[pi[i]] in N[q[i]] for i in range(4))
                        for pi in permutations(range(4)))
                # METHOD II: different SOURCE incidence anchored middle yz,
                # without iterating any physical Hamiltonian cycles
                anchor_cohort=0
                for x in e0:
                    for z in e1:
                        h=edge(x,z)
                        r0=next(a for a in e0 if a!=x)
                        r1=next(a for a in e1 if a!=z)
                        for k in range(4):
                            for middle in N[q[k]]:
                                yz=g[middle]
                                if set(yz)&fourpins:continue
                                for y,t in (yz,yz[::-1]):
                                    col=(ginverse[h],ginverse[edge(r0,y)],
                                         ginverse[edge(t,r1)])
                                    remaining=tuple(j for j in range(4) if j!=k)
                                    anchor_cohort+=sum(all(
                                        col[pi[v]] in N[q[remaining[v]]]
                                        for v in range(3))
                                        for pi in permutations(range(3)))
                assert direct_cohort==anchor_cohort, (
                    root,l0,l1,q,direct_cohort,anchor_cohort)
                assert direct_cohort<=192*3
                direct+=direct_cohort;anchored+=anchor_cohort
                nonzero+=int(direct_cohort>0)
    return dict(cohorts=cohorts,direct=direct,anchored=anchored,nonzero=nonzero)


def independent_integer_gate(s):
    assert type(s) is int and s>=2 and s&(s-1)==0
    V=(s+1)*(s*s+1)
    a=(1+isqrt(1+8*V))//2
    if comb(a,2)<V:a+=1
    d=s+1;m=comb(a,2)-V;N=V*comb(d,2)
    safe=max(0,N-a*comb(a-1,2)
             -(32*m//a)*(a-1)*d*(d-1))
    dead=m*(a-2)*(a-3)//4
    active=max(0,safe-dead)
    C4=max(0,3*comb(a-2,4)-m*(a-4)*(a-5))
    phys=active*C4*((a*a+3)//4) if a>=32 else 0
    return dict(s=s,a=a,m=m,safe=safe,dead=dead,active=active,
                C4=C4,physical=phys,
                hall_positive_upper=Fraction(384,s*s+1))


class Hyp105AA4AKReferee(unittest.TestCase):
    def test_true_original_symplectic_W32_two_unrelated_algorithms(self):
        z=independent_true_original_13_W32()
        self.assertGreater(z["cohorts"],0)
        self.assertEqual(z["direct"],z["anchored"])
        self.assertGreater(z["nonzero"],0)

    def test_crosslink_charge_all_K6_K7_K8_four_missing_edges(self):
        # No source geometry is assumed here, so this is an adversarial
        # worst-case physical test stronger than checking random f/g.
        for a in (6,7,8):
            E=tuple(combinations(range(a),2))
            crosslinks=[
                frozenset(edge(x,y) for x in e for y in f)
                for e,f in combinations(E,2) if not set(e)&set(f)]
            for missing in combinations(E,4):
                M=set(missing)
                completely_dead=sum(c.issubset(M) for c in crosslinks)
                self.assertLessEqual(completely_dead,
                                     4*(a-2)*(a-3)//4)

    def test_reach_all_h_certificates_separate_integer_implementation(self):
        for h in range(1,61):
            s=1<<h;z=independent_integer_gate(s)
            if s>=16:self.assertGreaterEqual(z["physical"]*384,s**14)
            if s>=32:
                self.assertLess(z["hall_positive_upper"],1)
                self.assertLessEqual(
                    Fraction(192*(s+1),(z["a"]*z["a"]+3)//4),
                    z["hall_positive_upper"])
                self.assertGreaterEqual(
                    z["physical"]*(1-z["hall_positive_upper"]),
                    (1-z["hall_positive_upper"])*Fraction(s**14,384))
        self.assertEqual(
            [independent_integer_gate(s)["active"] for s in (16,32,64)],
            [187866,4022933,224930885])

    def test_physical_missing_middle_edge_exclusion(self):
        # Algebraic physical bridge lower under cold endpoints is NOT
        # a Hall acceptance claim.
        for a in (32,33,64,94,261):
            E=set(combinations(range(a),2))
            pinned=((0,1),(2,3))
            out=set(range(4,a))
            for m in (0,1,a//3,a-2):
                # deletions entirely on outside vertices, cold pins exactly
                M=set(list(combinations(range(4,a),2))[:m])
                occupied_edges=E-M  # Materialize once; do not rebuild per (y,z).
                Y={y for y in out if edge(1,y) in occupied_edges}
                Z={z for z in out if edge(3,z) in occupied_edges}
                occupied=sum(edge(y,z) in occupied_edges
                             for y in Y for z in Z if y!=z)
                self.assertGreaterEqual(occupied, (a*a+3)//4)
                self.assertGreaterEqual(
                    occupied, len(Y)*len(Z)-len(Y&Z)-2*len(M))


if __name__=="__main__":
    unittest.main()
