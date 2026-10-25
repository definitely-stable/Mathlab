"""Issue #230 D2: ORIGINAL GQ bad-endpoint relation and mixed-book energy.

Mathematically exact all-h identities for arbitrary globally coherent f,g
and any physical diagonal subgraph H:
  B_bad contains exactly TWO unordered grid-antipodal chords for each
  ORIGINAL nonincident projection pair (q,r) whose ORIGINAL completion
  anchor f(p) or g(l) meets an endpoint label.
  E_H = #proper oriented H-P3 ending at one of these B_bad chords.
  |B_bad| = 2 |bad original pairs|;
  W_H = sum_(grid vertex z) deg_Bbad(z) deg_H(z).
  W_H = sum_(q,r bad) sum_(u in f(q),x in g(r)) D_H[u,x].
The mixed-book inequality on G=H and B=B_bad gives
  E_H <= 24*t_H*W_H + sqrt(192*|B_bad|*D6(H)),
where t_H is the largest coordinate-neighbor block size in H. The bound
is generally VACUOUS on unpruned finite models and yields NO all-h upper
on C. For any spectrally pruned H_s with t<=s^alpha, alpha<1/2,
W_H=o(s^(6-alpha)) is SUFFICIENT, *conditional* on S=o(s6), to conclude
E_H=o(s6); the internal-only part remains entirely OPEN.
"""
from collections import Counter
from itertools import combinations
from math import isqrt
import json

from hyp105_issue230_projection import ProjectionClosure, fixture
from hyp105_issue230_anchor_blocking import (
    _original_endpoint_pair_census, anchor_ledger,
)


def original_pencil_bad_pairs(core):
    """Independently construct the entire TRUE ORIGINAL bad set, not just its count."""
    left=set()
    right=set()
    # q--l--p--r and f(q) intersects f(p).
    for l,points in enumerate(core.lines):
        for q in points:
            fq=set(core.f[q])
            for p in points-{q}:
                if fq.isdisjoint(core.f[p]):
                    continue
                for r in core.point_lines[p]-{l}:
                    left.add((q,r))
    # q--l--p--r and g(r) intersects g(l).
    for p,lines in enumerate(core.point_lines):
        for r in lines:
            gr=set(core.g[r])
            for l in lines-{r}:
                if gr.isdisjoint(core.g[l]):
                    continue
                for q in core.lines[l]-{p}:
                    right.add((q,r))
    if any(pair not in core.projection for pair in left|right):
        raise AssertionError("all pencil-derived bad pairs must be genuine ORIGINAL nonincidences")
    direct_left={pair for pair,(p,l) in core.projection.items()
                 if set(core.f[p]).intersection(core.f[pair[0]])}
    direct_right={pair for pair,(p,l) in core.projection.items()
                  if set(core.g[l]).intersection(core.g[pair[1]])}
    if (left,right)!=(direct_left,direct_right):
        raise AssertionError("ORIGINAL pencil generation disagrees with independent unique GQ projection")
    return left,right


def _typed_degrees(core):
    """Independent F*I*L^T integer product from ORIGINAL incidences."""
    degree=[0]*(core.a**2)
    for p,l in core.edges:
        for u in core.f[p]:
            for x in core.g[l]:
                degree[u*core.a+x]+=1
    if degree!=list(map(len,core.adj)):
        raise AssertionError("ORIGINAL typed matrix F*I*L^T != physical adjacency degrees")
    return degree


def _chord_ledger(core,H_adj=None):
    """Explicit physical antipodal relation B_bad and exact energy."""
    left,right=original_pencil_bad_pairs(core)
    bad=left|right
    n=core.a**2
    if H_adj is None:
        H_adj=[set(v for v,_ in row) for row in core.adj]
    if len(H_adj)!=n:
        raise ValueError("physical graph must have a^2 vertices")
    full=[set(v for v,_ in row) for row in core.adj]
    # Allow retained coherent subgraphs only; no fabricated edges/chords.
    if any(not set(H_adj[u])<=full[u] for u in range(n)):
        raise ValueError("H is not a subgraph of ORIGINAL physical graph G")
    if any(u not in H_adj[v] for u in range(n) for v in H_adj[u]):
        raise ValueError("retained H must be undirected")
    if any(u in H_adj[u] for u in range(n)):
        raise ValueError("retained H must be loopless")
    Hdeg=[len(row) for row in H_adj]
    if H_adj==full:
        _typed_degrees(core)
    Bdeg=[0]*n
    chord_set=set()
    energy_by_pair={}
    for q,r in bad:
        (u,v)=core.f[q]
        (x,y)=core.g[r]
        c1=(u*core.a+x,v*core.a+y)
        c2=(u*core.a+y,v*core.a+x)
        for ab in (c1,c2):
            a,b=ab
            if b in full[a]:
                raise AssertionError("NONINCIDENT original endpoints cannot form a real physical edge")
            chord=tuple(sorted(ab))
            if chord in chord_set:
                raise AssertionError("distinct original bad pairs MUST have disjoint chords")
            chord_set.add(chord)
            Bdeg[a]+=1
            Bdeg[b]+=1
        energy_by_pair[q,r]=sum(Hdeg[uu*core.a+xx]
                                for uu in core.f[q] for xx in core.g[r])
    if len(chord_set)!=2*len(bad):
        raise AssertionError("exact original bad pair to TWO antipodal chords failed")
    energy=sum(Bdeg[v]*Hdeg[v] for v in range(n))
    if energy!=sum(energy_by_pair.values()):
        raise AssertionError("independent original endpoint and physical grid energies disagree")
    coordinate_block_max=0
    for u,neighbors in enumerate(H_adj):
        first=Counter(v//core.a for v in neighbors)
        second=Counter(v%core.a for v in neighbors)
        coordinate_block_max=max(coordinate_block_max,
                                 max(first.values(),default=0),
                                 max(second.values(),default=0))
    B2=sum(v*v for v in Bdeg)
    H2=sum(v*v for v in Hdeg)
    if energy**2>B2*H2:
        raise AssertionError("Cauchy certificate failed on independently reconstructed degree energies")
    return {
        "left":left,"right":right,"bad":bad,
        "chords":chord_set,"Bdeg":Bdeg,
        "H_adj":H_adj,"Hdeg":Hdeg,
        "W":energy,"B2":B2,"H2":H2,
        "max_block":coordinate_block_max,
        "pair_energy":energy_by_pair,
    }


def _independent_endpoint_threewalks(core,led):
    """Unrestricted A_H^3*B_bad with exact proper coordinate filtering.

    A completely independent ORIGINAL (q,r)-first enumeration,
    not imported from D1's 16-atom path scanner. Each two antipodal
    rectangle diagonals is enumerated in BOTH path orientations.
    """
    H=led["H_adj"]
    n=core.a**2
    a=core.a
    complete=0
    proper=0
    duplicate_same_vertex=0
    for v0,v3 in led["chords"]:
        for start,finish in ((v0,v3),(v3,v0)):
            x0,y0=divmod(start,a)
            x3,y3=divmod(finish,a)
            for v1 in H[start]:
                x1,y1=divmod(v1,a)
                for v2 in H[finish]:
                    if v2 not in H[v1]:
                        continue
                    complete+=1
                    if len({start,v1,v2,finish})<4:
                        duplicate_same_vertex+=1
                    x2,y2=divmod(v2,a)
                    if (len({x0,x1,x2,x3})==4 and
                            len({y0,y1,y2,y3})==4):
                        proper+=1
    if proper>complete:
        raise AssertionError("proper count exceeds unrestricted A^3 trace")
    return {
        "all_oriented_threewalks_bad_endpoint_chords":complete,
        "exact_proper_original_endpoint_bad_paths":proper,
        "improper_coincident_physical_vertex_walks":duplicate_same_vertex,
        "improper_coordinate_or_walk_slack":complete-proper,
    }



def _independent_sparse_square_trace(led):
    """Independent sparse A_H^2 then A_H^3 * A_Bbad, including W38.

    Different from the original endpoint-first two-middle-vertex scan:
    build the entire two-step adjacency tensor row by row, then contract
    selected antipodal chord endpoints. Retained undirected H only.
    """
    H=led["H_adj"]
    two=[]
    for u in range(len(H)):
        row=Counter()
        for v in H[u]:
            row.update(H[v])
        two.append(row)
    # Each ORIGINAL bad chord is unordered, trace visits both directions.
    total=0
    for a,b in led["chords"]:
        forward=sum(two[v][b] for v in H[a])
        reverse=sum(two[v][a] for v in H[b])
        if forward!=reverse:
            raise AssertionError("symmetric integer physical A^3 contraction failed")
        total+=forward+reverse
    return total


def mixedbook_gate(model,*,verify_proper=False,retained_adjacency=None):
    core=ProjectionClosure(model)
    led=_chord_ledger(core,retained_adjacency)
    B=len(led["chords"])
    t=led["max_block"]
    W=led["W"]
    trace=_independent_sparse_square_trace(led)
    # Exact integer upper, not an approximation or s^h extrapolation:
    # 24 t W is the small-book floor. Positive gap would force a D6
    # count by the already PROVED PR394 mixed-book inequality.
    floor=24*t*W
    result={
        "s":core.s,"a":core.a,
        "true_original_global_f_g":True,
        "original_nonincidence_pairs":len(core.projection),
        "left_bad_original_pairs":len(led["left"]),
        "right_bad_original_pairs":len(led["right"]),
        "bad_original_union_pairs":len(led["bad"]),
        "bad_original_intersection_pairs":len(led["left"]&led["right"]),
        "two_antipodal_chords_per_bad_original_pair":True,
        "actual_bad_physical_antipodal_chords":B,
        "H_is_valid_original_physical_subgraph":True,
        "chord_relation_disjoint_from_original_G_edges":True,
        "degree_energy_W":W,
        "original_qr_tensor_energy_W":sum(led["pair_energy"].values()),
        "physical_bad_chord_degree_square":led["B2"],
        "physical_H_degree_square":led["H2"],
        "max_bad_chord_degree":max(led["Bdeg"],default=0),
        "max_H_physical_degree":max(led["Hdeg"],default=0),
        "physical_coordinate_neighbor_block_cap":t,
        "mixedbook_small_book_allowance_24tW":floor,
        "independent_sparse_A2_A3_chord_trace":trace,
        "independent_sparse_square_trace_computed":True,
        "positive_mixedbook_D6_lower_proved":False,
        "all_h_weighted_energy_bound_proved":False,
        "all_h_endpoint_mass_o_s6_proved":False,
        "all_h_internal_only_upper_proved":False,
        "issue230_Branch_A":"OPEN",
        "issue230_Branch_B":"OPEN",
    }
    if verify_proper:
        x=_independent_endpoint_threewalks(core,led)
        if x["all_oriented_threewalks_bad_endpoint_chords"]!=trace:
            raise AssertionError("independent sparse A^2 tensor and endpoint-first full 3-walk census differ")
        result.update(x)
        result["mixedbook_certificate_nontrivial"]=x["exact_proper_original_endpoint_bad_paths"]>floor
        gap=max(0,x["exact_proper_original_endpoint_bad_paths"]-floor)
        # z>= gap^2/(192B), integer floor if needed. Avoid claiming
        # direct D6 positivity in empty/vacuous cases.
        result["mixedbook_D6_rational_lower_numerator"]=gap*gap
        result["mixedbook_D6_rational_lower_denominator"]=192*B if B else 1
        if not gap:
            result["mixedbook_D6_rational_lower_numerator"]=0
    else:
        result["independent_endpoint_first_threewalk_census_computed"]=False
    return result


def report():
    records=[]
    for power,schemes in ((1,("lex","reverse","S68","S72")),
                          (2,("lex","random")),
                          (3,("random",))):
        for scheme in schemes:
            state=fixture(power,scheme)
            obj=mixedbook_gate(state,verify_proper=(power<=2))
            if power<=2:
                d1=anchor_ledger(state)
                if (obj["exact_proper_original_endpoint_bad_paths"] !=
                        d1["endpoint_bad_pair_weight"]):
                    raise AssertionError("independent D2 endpoint threewalks != full D1 sixteen-atom scan")
            obj["scheme"]=scheme
            records.append(obj)
    return {
        "slice":"ISSUE230-PROJECTION-ENDPOINT-MIXEDBOOK-D2",
        "theorem":"all-h exact ORIGINAL bad-pair physical chord tensor W",
        "conditional_gate":"t*W=o(s^6) plus S=o(s^6) implies endpoint E=o(s^6)",
        "original_P2_P7_unit_mean":"FALSE (existing legal W32 S68)",
        "all_h_necessary_endpoint_energy_bound_proved":False,
        "all_h_seven_S_lower":"OPEN",
        "all_h_infinite_counterexample":"OPEN",
        "records":records,
    }


if __name__=="__main__":
    print(json.dumps(report(),sort_keys=True,indent=2))
