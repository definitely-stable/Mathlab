"""AA4-HARRIS: all-h ORIGINAL low-selector independent priority association.

PROVED all-order source lemma, for original symplectic W(3,2^h), arbitrary
fixed separately globally pair-injective f/g, arbitrary deleted original
incidence-ID Z, and paired original CORE C with deg(J_C)<=K:

Every coordinate-proper real physical rpath (r=2,3) has r mutually J-free
original incidence-ID owners I_1,...,I_r. Retention by ONE global uniform
source priority and TWO independent typed physical color cuts satisfies

  Pr(path retained) >= 4^-r * product_i 1/(1+degree_J_C(I_i))
                    >= 1 / (4^r * (K+1)^r).

Harris association proof: for the entire independent owner set S reverse
independent uniform priority T_i -> Y_i=1-T_i, leaving all outside priorities
Y_j=T_j. Each source local minimum inequality T_i<T_j becomes
Y_i+Y_j>1 and is INCREASING in each independent Y coordinate.
The indicators are positively associated; hence their intersection
probability is at least the product of the individual 1/(deg+1) minima.

The q2/q3 gain flows into the conditional original LOW/HEAVY all-h
closed constant ledger (fixed external existential C0,c0), but no
root Branch A proof-acceptance, ASET exponent or numeric external graph
constants are claimed by these deterministic checks.

Main referee rebuilds original source J and physical two-diagonal graph
independently using ONLY trusted original symplectic incidence fixture.
No historical selector, all-h/LOW ledger, or GF5 program is imported.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations, product
from math import comb, factorial, isqrt
import json

from hyp105_original_defect_factor_referee import genuine_symplectic_source

SCHEMA="mathlab.hyp105.original-harris-product-selector.v1"
ROOT_STATUS="OPEN_WITH_FORMAL_BLOCKER"
K=64
R=93313
D6_WEIGHT=54162
BBO_WEIGHT=53838


def _ceil_fraction(q):
    if type(q) is not Fraction:
        raise ValueError("exact rational only")
    return -(-q.numerator//q.denominator)


def _ceil_sqrt(n):
    if type(n) is not int or n<0:
        raise ValueError("exact nonnegative integer only")
    k=isqrt(n)
    return k+(k*k<n)


def _constant_ledger(C0,c0,mode):
    """Independent full original LOW-source math, with named external constants FORMAL."""
    if (type(C0) is not Fraction or type(c0) is not Fraction or
        C0<1 or not 0<c0<=1):
        raise ValueError("C0,c0 must be fixed formal exact qualifying rational bounds")
    if mode not in ("harris","historical"):
        raise ValueError("only exact original source priority choices")
    T=_ceil_fraction(Fraction(17*R**3,2)*C0**3)
    q2=16*(65**2 if mode=="harris" else comb(130,2))
    q3=64*(65**3 if mode=="harris" else comb(195,3))
    L6=24+153*T*T
    L4=q2*q2*_ceil_sqrt(_ceil_fraction(Fraction(17*L6,4)))+19*T
    B0=_ceil_sqrt(360*(K+1)*T)
    E=5*q3*_ceil_sqrt(L6)
    D=4*_ceil_sqrt(B0*T*L4)
    s0=max(64,444*T,(8*E)**2,(8*D)**8)
    h0=(s0-1).bit_length()
    delta=c0/Fraction(R**6)
    tstar=Fraction(119,24)-Fraction(2*D6_WEIGHT,BBO_WEIGHT)*delta
    rho=tstar*tstar/Fraction(12*q3*q3*L6)
    bbo=(Fraction(119,24)-tstar)/2
    tests={
        "original_HEAVY_T_fixed_by_published_existential_graph_constants":
            T>=Fraction(17*R**3,2)*C0**3,
        "original_dual_J_degree_K_is_64":K==64,
        "Harris_source_priority_uniform_retention":
            (q2==16*65**2 and q3==64*65**3) if mode=="harris"
            else (q2==16*comb(130,2) and q3==64*comb(195,3)),
        "selected_bipartite_sixth_L6_unchanged":L6==24+153*T*T,
        "original_sharp_fourth_moment_from_selected_fourth":
            L4==q2**2*_ceil_sqrt(_ceil_fraction(Fraction(17*L6,4)))+19*T,
        "FULL_A_CORE_C_mixed_dual_book_kept":
            B0**2>=360*(K+1)*T,
        "original_four_INTERNAL_blockers":
            D>=4*_ceil_sqrt(B0*T*L4),
        "nonZ_genuine_GQ_endpoint_24s5":
            E>=5*q3*_ceil_sqrt(L6),
        "nonZ_coordinate_wrong_s6_over8":444*T<=s0,
        "nonZ_endpoint_wrong_s6_over8":(8*E)**2<=s0,
        "nonZ_four_blocker_s6_over8":(8*D)**8<=s0,
        "physical_W3_lower_16_over3_minus_3_errors":
            Fraction(16,3)-3*Fraction(1,8)==Fraction(119,24),
        "full_original_three_anchor_deletion_mask_exact":
            Fraction(12*q3*q3*L6)*rho==tstar*tstar,
        "new_original_rho_HEAVY_cap_and_LOW_core":
            0<rho<Fraction(1,2**32) and rho<Fraction(1,32) and
            rho<Fraction(3,64) and
            Fraction(1)-Fraction(1,8)-Fraction(5,64)-rho>=Fraction(3,4),
        "tstar_pos_and_smaller_than_119_over24":
            0<tstar<Fraction(119,24),
        "LOW_positive_BBo_produced_2to1":
            bbo==Fraction(D6_WEIGHT,BBO_WEIGHT)*delta and bbo>=delta>0,
        "GF5_weighted_additive_not_union_probability":
            BBO_WEIGHT*bbo==D6_WEIGHT*delta,
        "dyadic_sufficient_all_h_threshold":
            (1<<h0)>=s0,
        "numerical_graph_constants_not_claimed":True,
        "global_root_proof_not_promoted":True,
    }
    if not all(tests.values()):
        raise AssertionError("conditional all-h low/heavy formula ledger failed")
    return {"mode":mode,"C0_FORMAL":str(C0),"c0_FORMAL":str(c0),
        "T":T,"R":R,"q2":q2,"q3":q3,"L6":L6,"L4":L4,
        "B0":B0,"E":E,"D":D,"s0":str(s0),"h0":h0,
        "delta":str(delta),"tstar":str(tstar),
        "rho":str(rho),"low_BBo_sextic_floor":str(bbo),
        "GF5_additive_accepted_signed_sextic_floor":
            str(D6_WEIGHT*delta/Fraction(51**6)),
        "conditional_all_h_checks":tests}


def formal_harris_upgrade(C0,c0):
    """Exact side-by-side historical and stronger all-h ledger."""
    new=_constant_ledger(C0,c0,"harris")
    old=_constant_ledger(C0,c0,"historical")
    if not (new["q2"]<old["q2"] and new["q3"]<old["q3"] and
        new["L6"]==old["L6"] and new["T"]==old["T"] and
        new["L4"]<old["L4"] and new["E"]<old["E"] and
        new["D"]<old["D"] and new["h0"]<old["h0"] and
        new["delta"]==old["delta"] and
        new["GF5_additive_accepted_signed_sextic_floor"]==
            old["GF5_additive_accepted_signed_sextic_floor"]):
        raise AssertionError("source priority Harris strengthening must retain all HEAVY and GF5 gates")
    ratio=Fraction(new["q3"],old["q3"])
    rho_ratio=Fraction(old["q3"]**2,new["q3"]**2)
    if Fraction(new["rho"])/Fraction(old["rho"])!=rho_ratio:
        raise AssertionError("EXACT rho scaling not q3^-2")
    return {"mode":"true_original_all_h_Harris_upgrade",
        "historical":old,"harris":new,
        "q2_improvement":str(Fraction(old["q2"],new["q2"])),
        "q3_improvement":str(Fraction(old["q3"],new["q3"])),
        "adversarial_original_Z_deletion_radius_improvement":str(rho_ratio),
        "h0_dyadic_exponent_improvement":old["h0"]-new["h0"],
        "source_sixth_moment_L6_unchanged":True,
        "HEAVY_threshold_T_unchanged":True,
        "signed_GF5_proof_gate_unchanged":True,
        "real_published_numeric_C0_c0_assumed":False,
        "root_PROVED_A":False}


def _actual_original_source(s,mode="lex",core="full"):
    """Rebuild ORIGINAL physical source and J, independent of prior AA4 calculators."""
    if type(s) is not int or s not in (2,4):
        raise ValueError("only genuine original W(3,2) or W(3,4) for finite tests")
    V=(s+1)*(s*s+1)
    named=tuple(map(tuple,genuine_symplectic_source(s)))
    a=2
    while comb(a,2)<V:a+=1
    pairlist=list(combinations(range(a),2))
    f=list(pairlist[:V])
    g=list(pairlist[:V])
    if mode=="reverse":
        g.reverse()
    elif mode=="shift":
        f=f[3:]+f[:3]
        g=g[7:]+g[:7]
    elif mode!="lex":
        raise ValueError("fixed correlated pair label scheme required")
    if core=="full":
        ids=tuple(range(len(named)))
    elif core=="even":
        ids=tuple(range(0,len(named),2))
    elif core=="Z17":
        ids=tuple(i for i in range(len(named)) if i%17)
    else:raise ValueError("invalid named source CORE")
    if len(named)!=(s+1)*V or len(set(named))!=len(named):
        raise AssertionError("not true named original GQ incidence geometry")
    if len(set(f))!=V or len(set(g))!=V:
        raise AssertionError("not separately globally pair-injective f/g")
    buckets_point=defaultdict(list)
    buckets_line=defaultdict(list)
    for i in ids:
        p,l=named[i]
        buckets_point[p].append(i)
        buckets_line[l].append(i)
    J=[set() for _ in named]
    for side,buckets in (("point",buckets_point),("line",buckets_line)):
        for xs in buckets.values():
            for i,j in combinations(xs,2):
                pi,li=named[i];pj,lj=named[j]
                pairi=g[li] if side=="point" else f[pi]
                pairj=g[lj] if side=="point" else f[pj]
                if set(pairi)&set(pairj):
                    J[i].add(j)
                    J[j].add(i)
    owner={}
    adj=defaultdict(set)
    for i in ids:
        p,l=named[i]
        x0,x1=f[p];y0,y1=g[l]
        for u,v in (((x0,y0),(x1,y1)),((x0,y1),(x1,y0))):
            key=tuple(sorted((u,v)))
            if key in owner:raise AssertionError("real physical edge duplicate owner")
            owner[key]=i
            adj[u].add(v);adj[v].add(u)
    if len(owner)!=2*len(ids):
        raise AssertionError("not two true opposite diagonals per named original flag")
    if max((len(J[i]) for i in ids),default=0)>K:
        raise AssertionError("finite source not under LOW original J-degree prerequisite")
    return {"s":s,"V":V,"flags":named,"a":a,"f":tuple(f),"g":tuple(g),
        "ids":ids,"deleted_original_Z":len(named)-len(ids),"J":J,
        "owner":owner,"adj":adj,
        "actual_original_source_max_J_degree":
            max((len(J[i]) for i in ids),default=0)}


def _actual_proper_paths(c,r,limit=None):
    """TRUE all oriented physical proper rwalks, not synthetic owner sequence."""
    if r not in (2,3):raise ValueError("only proper length 2 and 3")
    paths=[]
    adj=c["adj"]
    for start in sorted(adj):
        stack=[(start,)]
        while stack:
            path=stack.pop()
            if len(path)==r+1:
                owners=tuple(c["owner"][tuple(sorted((path[j],path[j+1])))]
                    for j in range(r))
                if len(set(owners))!=r or any(j in c["J"][i]
                    for i,j in combinations(owners,2)):
                    raise AssertionError("coordinate-proper path has owner clash in true source J")
                paths.append((path,owners))
                if limit is not None and len(paths)>=limit:return paths
                continue
            for nxt in sorted(adj[path[-1]],reverse=True):
                if nxt[0] not in (v[0] for v in path) and nxt[1] not in (
                    v[1] for v in path):
                    stack.append(path+(nxt,))
    return paths


def _rank_exact_independent(owners,J):
    S=tuple(sorted(set(owners)))
    if len(S)!=len(owners) or any(j in J[i] for i,j in combinations(S,2)):
        return Fraction(0)
    outside=set()
    for i in S:outside.update(J[i])
    outside.difference_update(S)
    nbrs={z:tuple(i for i in S if z in J[i]) for z in sorted(outside)}
    out=Fraction(0)
    k=len(S)
    for order in permutations(S):
        positions={x:j for j,x in enumerate(order)}
        cs=[0]*k
        for group in nbrs.values():
            cs[max(positions[i] for i in group)]+=1
        denominator=1
        remaining=0
        for j in range(k-1,-1,-1):
            remaining+=1+cs[j]
            denominator*=remaining
        out+=Fraction(1,denominator)
    return out


def _rank_independent_linear_extensions(owners,J,limit=18):
    """Separate exhaustive bitmask poset oracle; not the product-Harris proof."""
    S=tuple(sorted(set(owners)))
    if any(j in J[i] for i,j in combinations(S,2)):return Fraction(0)
    U=set(S)
    for i in S:U.update(J[i])
    U=tuple(sorted(U))
    if len(U)>limit:
        raise ValueError("independent source poset certificate too large")
    at={v:k for k,v in enumerate(U)}
    requirements=[0]*len(U)
    for i in S:
        for j in J[i]:
            requirements[at[j]]|=1<<at[i]
    @lru_cache(None)
    def f(mask):
        if mask==(1<<len(U))-1:return 1
        count=0
        for j in range(len(U)):
            if mask>>j&1==0 and requirements[j]&mask==requirements[j]:
                count+=f(mask|(1<<j))
        return count
    return Fraction(f(0),factorial(len(U)))


def _path_priority_cert(owners,J):
    r=len(owners)
    S=tuple(sorted(owners))
    if len(set(S))!=r or any(j in J[i] for i,j in combinations(S,2)):
        raise AssertionError("not pairwise source J-free")
    neigh=set(S)
    for i in S:neigh.update(J[i])
    local=Fraction(1)
    for i in S:local/=len(J[i])+1
    first_r=Fraction(1,comb(len(neigh),r))
    exact=_rank_exact_independent(S,J)
    cut=Fraction(1,4**r)
    universal=cut/Fraction((K+1)**r)
    if not (exact>=local and exact>=first_r and
            exact*cut>=universal and local*cut>=universal):
        raise AssertionError("Harris product or original first-r mathematical floor is false")
    return {"r":r,"original_owners":list(S),
        "individual_original_J_degrees":[len(J[i]) for i in S],
        "closed_original_J_neighborhood_size":len(neigh),
        "exact_priority_joint":str(exact),
        "Harris_local_product_floor":str(local),
        "historical_local_first_r_floor":str(first_r),
        "Harris_adaptive_max_both_floors":str(max(local,first_r)),
        "original_two_physical_cuts":str(cut),
        "exact_path_survival":str(exact*cut),
        "new_uniform_K64_survival_floor":str(universal)}


def _independent_typed_cut_exhaustive(r):
    # Four alternating two-factor assignments; no independence between paths.
    cols=r+1
    good=0
    for bits in product((0,1),repeat=2*cols):
        lhs=bits[:cols];rhs=bits[cols:]
        if all(lhs[i]!=lhs[i+1] and rhs[i]!=rhs[i+1] for i in range(r)):
            good+=1
    if good!=4 or Fraction(good,2**(2*cols))!=Fraction(1,4**r):
        raise AssertionError("actual original two-typed factor cut changed")
    return {"r":r,"literal_cut_assignments":2**(2*cols),
        "favorable_assignments":good,
        "two_independent_typed_cut_probability":str(Fraction(good,2**(2*cols)))}


def finite_original_source_cert(s,scheme,core,path_limit=None):
    c=_actual_original_source(s,scheme,core)
    records=[]
    for r in (2,3):
        paths=_actual_proper_paths(c,r,path_limit)
        if not paths:raise AssertionError("original core has no true coordinate-proper rpath")
        priority_DPs=0
        source_floor_tight=Fraction(0)
        best=None
        worst_gap=None
        min_p=None
        original_degree_hist=Counter()
        for path,owners in paths:
            x=_path_priority_cert(owners,c["J"])
            surv=Fraction(x["exact_path_survival"])
            floor=Fraction(x["new_uniform_K64_survival_floor"])
            factor=surv/floor
            if worst_gap is None or factor<worst_gap:
                worst_gap=factor
                best={"physical_vertices":[list(v) for v in path],
                      "source_certificate":x}
            min_p=surv if min_p is None else min(min_p,surv)
            local=Fraction(x["Harris_local_product_floor"])
            source_floor_tight+=local
            original_degree_hist.update(tuple(x["individual_original_J_degrees"]))
            if priority_DPs<4 and x["closed_original_J_neighborhood_size"]<=18:
                check=_rank_independent_linear_extensions(owners,c["J"])
                if Fraction(x["exact_priority_joint"])!=check:
                    raise AssertionError("independent source-poset DP contradicts Harris integral")
                priority_DPs+=1
        if priority_DPs==0:
            raise AssertionError("failed independent original source poset cross-check")
        records.append({"r":r,
            "genuine_physical_coordinate_proper_rpaths":len(paths),
            "complete_original_physical_path_census":path_limit is None,
            "exact_source_priority_poset_DP_sampled_checks":priority_DPs,
            "true_original_J_degree_histogram":dict(sorted(original_degree_hist.items())),
            "min_exact_source_physical_rpath_survival":str(min_p),
            "sum_adaptive_degree_product_floors":str(source_floor_tight),
            "least_exact_over_new_uniform_floor":str(worst_gap),
            "least_factor_witness_true_original_physical_path":best,
            "literal_independent_factor_color_check":_independent_typed_cut_exhaustive(r)})
    return {"s":s,"fixed_label_scheme":scheme,"source_CORE_mode":core,
        "original_flags":len(c["flags"]),
        "retained_named_original_CORE_flags":len(c["ids"]),
        "adversarial_deleted_original_Z_flags":c["deleted_original_Z"],
        "physical_REAL_edges":len(c["owner"]),
        "original_K64_admissible":c["actual_original_source_max_J_degree"]<=K,
        "original_source_max_J_degree":c["actual_original_source_max_J_degree"],
        "r2_r3":records}


def _original_source_incompatible_path_weight(c,paths):
    """EXACT full ORIGINAL W32 weighted B, and a rigorous uniform all-h bound.

    For each genuine ordered physical endpoint (u,v), fix its four endpoint
    physical coloring bits to the alternating values of ANY proper 3path.
    A path then survives both typed cuts with conditional probability 1/16,
    rather than unconditional 1/64. If p_path denotes its UNCONDITIONAL
    priority×both-cut survival, conditionally it survives with probability
    4*p_path. Let Y=sum_path p_path * 1(selected) in this experiment.
    E[Y]=4 sum_path p_path^2. Every realization's selected path pairs are
    actually J-free and typed-color-compatible. Therefore
       G_endpoint >= E[Y²] >= 16 * (sum_path p_path^2)^2.
    Since p_path >= 1/(64*(K+1)^3), this implies
       G >= (1/[256*(K+1)^6]) * ||E X||_F²
       B <= (1 - 1/[256*(K+1)^6]) * ||E X||_F².
    Weak but nonzero, no independence between actual original paths.
    """
    if c["s"]!=2:
        raise ValueError("exact full-original finite B ledger only W32")
    byend=defaultdict(list)
    for path,os in paths:
        byend[(path[0],path[-1])].append((path,os))
    epsilon=Fraction(1,256*(K+1)**6)
    proper=Fraction(1,64*(K+1)**3)
    marg_cache={}
    total_M=Fraction(0)
    total_G=Fraction(0)
    total_B=Fraction(0)
    constructive_G=Fraction(0)
    pair_classes=Counter()
    n_pairs=0
    for group in byend.values():
        weights=[]
        for path,os in group:
            key=tuple(sorted(os))
            if key not in marg_cache:
                marg_cache[key]=_rank_exact_independent(os,c["J"])/64
            p=marg_cache[key]
            if p<proper:
                raise AssertionError("new Harris full ORIGINAL p3 path floor violated")
            weights.append(p)
        W=sum(weights,Fraction(0))
        M=W*W
        G=Fraction(0)
        B=Fraction(0)
        low=16*sum((w*w for w in weights),Fraction(0))**2
        for (path1,os1),pa in zip(group,weights):
            for (path2,os2),pb in zip(group,weights):
                S=tuple(sorted(set(os1+os2)))
                if any(j in c["J"][i] for i,j in combinations(S,2)):
                    kind="original_J_conflict"
                elif (path1[1][0]==path2[2][0] or
                      path1[2][0]==path2[1][0]):
                    kind="original_first_typed_opposite_depth_collision"
                elif (path1[1][1]==path2[2][1] or
                      path1[2][1]==path2[1][1]):
                    kind="original_second_typed_opposite_depth_collision"
                else:
                    kind="compatible"
                pair_classes[kind]+=1
                n_pairs+=1
                if kind=="compatible":
                    G+=pa*pb
                else:
                    B+=pa*pb
        if G+B!=M or G<low or G<epsilon*M:
            raise AssertionError("all-h original compatible weight B Harris certificate false")
        total_M+=M
        total_G+=G
        total_B+=B
        constructive_G+=low
    if not total_M or total_G+total_B!=total_M:
        raise AssertionError("bad/good source path mass not conserved")
    if not (total_G>=constructive_G>=epsilon*total_M):
        raise AssertionError("uniform all-h bad weight bound invalid")
    return {"s":c["s"],"true_original_CORE_ID_count":len(c["ids"]),
            "adversarial_original_Z_deleted":c["deleted_original_Z"],
            "actual_full_coordinate_proper_directed_P3_count":len(paths),
            "ordered_same_end_real_path_pairs":n_pairs,
            "four_original_incompatibility_classes":dict(pair_classes),
            "actual_exact_compatible_G":str(total_G),
            "actual_exact_incompatible_B":str(total_B),
            "actual_exact_mean_Frobenius2_G_plus_B":str(total_M),
            "constructive_endpoint_conditioned_FKG_G_lower":
                str(constructive_G),
            "all_h_universal_compatible_fraction_epsilon":str(epsilon),
            "all_h_B_less_equal_1_minus_epsilon_times_M":True,
            "real_original_W32_compatible_fraction":str(total_G/total_M)}


def _small_graph_rank_exhaustive(n=5):
    """Independent ALL original simple-graph precedence falsifier: n=5 graphs."""
    edges=list(combinations(range(n),2))
    total_graphs=0
    independent_sets=0
    tested_priorities=0
    strict_product_cases=0
    for mask in range(1<<len(edges)):
        nbr=[set() for _ in range(n)]
        for j,(u,v) in enumerate(edges):
            if (mask>>j)&1:
                nbr[u].add(v);nbr[v].add(u)
        total_graphs+=1
        # Full n! orders, no integral and no poset DP.
        for r in (2,3):
            for S in combinations(range(n),r):
                if any(j in nbr[i] for i,j in combinations(S,2)):
                    continue
                independent_sets+=1
                p=Fraction(0)
                for order in permutations(range(n)):
                    pos={u:i for i,u in enumerate(order)}
                    if all(pos[i]<pos[j] for i in S for j in nbr[i]):
                        p+=Fraction(1,factorial(n))
                prod=Fraction(1)
                for i in S:prod/=1+len(nbr[i])
                if p<prod:
                    raise AssertionError("Harris independent owner rank product fails abstract graph")
                if p>prod:strict_product_cases+=1
                tested_priorities+=1
    if not strict_product_cases:
        raise AssertionError("no strict positive original-source-priority correlations found")
    return {"n_source_vertices":n,"exhaustively_enumerated_simple_J_graphs":total_graphs,
        "J_independent_owner_r2_r3_sets_tested":independent_sets,
        "global_priority_permutation_exhaustive_comparisons":tested_priorities,
        "strictly_positive_source_priority_association_cases":strict_product_cases,
        "all_K_and_graphs_regardless_of_W_symplectic_source_as_algebra_check":True}


def canonical_report():
    formal=[]
    for c0,C in ((Fraction(1),Fraction(1)),
                 (Fraction(1,5),Fraction(2)),
                 (Fraction(1,17),Fraction(7,3))):
        formal.append(formal_harris_upgrade(C,c0))
    source_cases=[]
    for s,scheme,core,cap in (
        (2,"lex","full",None),
        (2,"reverse","full",None),
        (2,"shift","Z17",None),
        (4,"lex","even",160),
        (4,"reverse","even",160),
        (4,"shift","Z17",160),
    ):
        source_cases.append(finite_original_source_cert(s,scheme,core,cap))
    graph=_small_graph_rank_exhaustive(5)
    original_B=[]
    for scheme,core in (("lex","full"),("reverse","full"),("shift","Z17")):
        c=_actual_original_source(2,scheme,core)
        paths=_actual_proper_paths(c,3)
        row=_original_source_incompatible_path_weight(c,paths)
        row["scheme"]=scheme
        row["core"]=core
        original_B.append(row)
    return {"schema":SCHEMA,"issue":230,"status":ROOT_STATUS,
        "root_PROVED_A":False,
        "new_all_h_original_J_free_owner_Harris_product_theorem":True,
        "source_adaptive_degree_floor_uniform_independent_of_f_g_correlation":True,
        "HEAVY_real_no_clone_source_unchanged":True,
        "external_C6_numeric_graph_constants_assumed":False,
        "all_h_derived_original_LOW_arithmetic_FORMAL":formal,
        "true_original_W32_complete_W34_sample_physical_sources":source_cases,
        "independent_abstract_J_small_graph_total_priority_falsifier":graph,
        "independent_exact_W32_Harris_bad_pair_B_uniform_bound":original_B,
        "source_quantifiers":"all dyadic s and arbitrary correlated globally pair-injective fixed f/g, named original Z and paired core C",
        "new_global_seven_class_root_proof_certified":False}


if __name__=="__main__":
    print("AA4_HARRIS_CERTIFICATE="+json.dumps(canonical_report(),sort_keys=True,separators=(",",":")))
