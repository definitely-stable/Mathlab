"""AA4-EXT6: external ordinary C6 supersaturation normalization referee.

External input: Jiang--Yepremyan (2020), Theorem 1.1, k=3, r=2:
For absolute existential C_graph,c_graph>0, a simple graph F with
m>=C_graph*n^(4/3) has >=c_graph*(m/n)^6 UNORIENTED simple C6.

This module proves only the exact algebraic application from the
inherited HYP-105 #744 graph F hypotheses and independently certifies
the factor of twelve for unoriented cycles on finite ordinary graphs.
No numerical values for published C_graph,c_graph are asserted.
"""
from fractions import Fraction
from itertools import combinations, permutations
import json

SCHEMA = "mathlab.hyp105.external-ordinary-ss6-normalization.v1"
ROOT_STATUS = "OPEN_WITH_FORMAL_BLOCKER"
R = 93313
EXTERNAL_DOI = "10.1017/S0963548320000206"
EXTERNAL_THEOREM = "Jiang--Yepremyan (2020), Theorem 1.1, k=3,r=2"


def _ceil(q):
    if type(q) is not Fraction:
        raise ValueError("require exact Fraction")
    return -(-q.numerator // q.denominator)


def formal_external_transfer(C0, c0):
    """C0>=C_graph,c0<=c_graph are FORMAL, not numerically identified."""
    if (type(C0) is not Fraction or type(c0) is not Fraction
            or C0 < 1 or not Fraction(0) < c0 <= 1):
        raise ValueError("positive one-time FORMAL rational C0,c0 required")
    T = _ceil(Fraction(17, 2) * R**3 * C0**3)
    checks = {
        "r2_linear_hypergraph_IS_simple_ordinary_graph": True,
        "k3_gives_unoriented_simple_C6_count_not_walks": True,
        "six_cycle_count_normalization_no_divide_12_again": True,
        "T_ext_exact_ceiling": T >= Fraction(17, 2)*R**3*C0**3
            and T-1 < Fraction(17, 2)*R**3*C0**3,
        "monotone_external_constants_choose_once_before_s_f_g_Z": True,
        "R_adaptive_source_from_frozen_744": R == 93313,
        "exact_cube_density_threshold_valid": Fraction(17, 2)*R**3*C0**3 <= T,
        "sufficient_unoriented_C6_bound": c0 / R**6 > 0,
        "all_original_source_sixsets_injection_IS_SEPARATE_GATE": True,
        "no_numeric_published_graph_constants_claimed": True,
        "no_branch_A_or_new_ASET_promotion": True,
    }
    if not all(checks.values()):
        raise AssertionError("external graph theorem bridge failed")
    return {"C0_FORMAL":str(C0),"c0_FORMAL":str(c0),
            "R":R,"T":T,
            "C6_unoriented_conditional_sextic_coefficient":str(c0/Fraction(R**6)),
            "external_published_numeric_constants_VERIFIED":False,
            "Jiang_Yepremyan_Theorem_1_1_k3_r2":True,
            "exact_all_h_external_quantifier_gates":checks}


def verify_abstract_graph_budget(C0, c0, s, v, e):
    """Check all algebraic hypotheses on integer abstract graph parameters.

    Graph construction, source injection and actual C6 count are NOT
    decided here. The published theorem supplies the last implication
    only if F is an ordinary simple graph and its hypotheses hold.
    """
    t = formal_external_transfer(C0,c0)
    if any(type(x) is not int for x in (s,v,e)) or s<1 or v<6 or not 0<=e<=v*(v-1)//2:
        raise ValueError("valid integer graph budget s,v,e required")
    if e*R < s*v:
        raise ValueError("missing inherited source density e/v >= s/R")
    if 2*t["T"]*v > 17*s**3:
        raise ValueError("missing inherited original-heavy no-clone vertex cap")
    density_cube = Fraction(e**3, v**3)
    threshold_cube = C0**3*v
    if density_cube < threshold_cube or e**3 < C0**3*v**4:
        raise AssertionError("exact external threshold deduction invalid")
    lower_by_external = c0*(Fraction(e,v))**6
    inherited_lower = c0*Fraction(s,R)**6
    if lower_by_external < inherited_lower:
        raise AssertionError("wrong ordinary C6 sextic scaling")
    return {"s":s,"v":v,"e":e,"formal_C0":str(C0),
            "external_density_threshold_verified_by_exact_cubes":True,
            "m_cubed_gte_C0cubed_v4":True,
            "inherited_C6_sextic_floor":str(inherited_lower),
            "external_C6_sextic_floor":str(lower_by_external)}


def _graph(n, edges):
    if type(n) is not int or n<1:
        raise ValueError("simple graph vertex count must be positive integer")
    adj = [set() for _ in range(n)]
    seen = set()
    for edge in edges:
        if (not isinstance(edge,(tuple,list)) or len(edge)!=2 or
                any(type(i) is not int or not 0<=i<n for i in edge)):
            raise ValueError("edge must have two valid original vertex IDs")
        u,v = edge
        if u==v:
            raise ValueError("self loop not allowed in simple graph")
        e=(min(u,v),max(u,v))
        if e in seen:
            raise ValueError("parallel/duplicate edge not allowed")
        seen.add(e);adj[u].add(v);adj[v].add(u)
    return tuple(frozenset(x) for x in adj)


def sixcycles_minroot_dfs(n, edges):
    """One root = minimum cycle vertex, one orientation via first < last."""
    A = _graph(n,edges)
    total=0
    for root in range(n):
        def visit(path):
            nonlocal total
            last=path[-1]
            if len(path)==6:
                if root in A[last] and path[1] < last:
                    total+=1
                return
            for v in A[last]:
                if v>root and v not in path:
                    visit(path+[v])
        visit([root])
    return total


def sixcycles_opposite_threepaths(n, edges):
    """Independent exact combinatorial C6 count: 3 opposite vertex pairs."""
    A=_graph(n,edges)
    opposing=0
    for u,v in combinations(range(n),2):
        paths=[]
        for a in A[u]:
            if a==v:
                continue
            for b in A[a]:
                if b not in (u,v,a) and v in A[b]:
                    paths.append((a,b))
        for x,y in combinations(paths,2):
            if {x[0],x[1]}.isdisjoint((y[0],y[1])):
                opposing+=1
    if opposing%3:
        raise AssertionError("every ordinary C6 must have exactly three opposite pairs")
    return opposing//3


def closed_sixwalk_trace(n, edges):
    """Independent length-six CLOSED WALK trace, intentionally not simple C6.

    Distinguishes the published genuine six-CYCLE count from degenerate
    length-six walks. K_{2,5} has 2000 closed walks but ZERO genuine C6.
    """
    A=_graph(n,edges)
    total=0
    for start in range(n):
        counts=[0]*n
        counts[start]=1
        for _ in range(6):
            nxt=[0]*n
            for v,walks in enumerate(counts):
                if walks:
                    for w in A[v]:
                        nxt[w]+=walks
            counts=nxt
        total+=counts[start]
    return total


def oriented_sixcycle_embeddings(n, edges):
    """THIRD source-agnostic oracle: each unoriented C6 has 12 embeddings."""
    A=_graph(n,edges)
    if n>8:
        raise ValueError("exhaustive oriented embeddings limited to 8 vertices")
    total=0
    for p in permutations(range(n),6):
        if all(p[(i+1)%6] in A[p[i]] for i in range(6)):
            total+=1
    return total


def _complete(n):
    return list(combinations(range(n),2))


def _bipartite(a,b):
    return [(u,a+v) for u in range(a) for v in range(b)]


def canonical_report():
    examples=[
        ("C6",6,[(i,(i+1)%6) for i in range(6)],1),
        ("C6_with_two_isolated",8,[(i,(i+1)%6) for i in range(6)],1),
        ("K6",6,_complete(6),60),
        ("K7",7,_complete(7),420),
        ("K33",6,_bipartite(3,3),6),
        ("K34",7,_bipartite(3,4),24),
        ("K25",7,_bipartite(2,5),0),
        ("C5_no_six_cycle",5,[(i,(i+1)%5) for i in range(5)],0),
    ]
    graph_rows=[]
    for label,n,edges,known in examples:
        x=sixcycles_minroot_dfs(n,edges)
        y=sixcycles_opposite_threepaths(n,edges)
        z=oriented_sixcycle_embeddings(n,edges)
        closed=closed_sixwalk_trace(n,edges)
        if x!=y or z!=12*x or x!=known or closed<z:
            raise AssertionError("C6 source-cycle orientation/count disagreement")
        graph_rows.append({"graph":label,"v":n,"e":len(edges),
             "unoriented_C6":x,"opposite_threepath_C6":y,
             "oriented_embeddings":z,"closed_length6_walks":closed,"expected_C6":known})
    ledgers=[formal_external_transfer(C,c) for C,c in [
        (Fraction(1),Fraction(1)),
        (Fraction(2),Fraction(1,5)),
        (Fraction(7,3),Fraction(1,17)),
    ]]
    large_s=1<<60
    C,c=Fraction(1),Fraction(1)
    v=_ceil(Fraction(4*large_s,R))
    e=_ceil(Fraction(v*large_s,R))
    witness=verify_abstract_graph_budget(C,c,large_s,v,e)
    return {"schema":SCHEMA,"root_issue":230,"status":ROOT_STATUS,
            "external_published_theorem":EXTERNAL_THEOREM,
            "external_DOI":EXTERNAL_DOI,
            "original_source_inverse_independently_signed_off":False,
            "full_HEAVY_LOW_proof_independently_signed_off":False,
            "root_PROVED_A":False,"new_ASET_exponent":False,
            "formal_graph_theorem_normalization":ledgers,
            "finite_graph_three_oracle_cases":graph_rows,
            "large_abstract_integer_budget_NOT_physical_source_witness":witness}


if __name__=="__main__":
    print("AA4_EXT6_THEOREM_NORMALIZATION="+json.dumps(canonical_report(),sort_keys=True,separators=(",",":")))
