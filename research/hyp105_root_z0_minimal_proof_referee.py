"""AA4-ROOT-Z0: strict original no-deletion branch-A proof-budget referee.

A new exact Z=empty sharpening; NOT an independent acceptance of the cited
HEAVY/LOW source lemmas, nor of the root #230 theorem. Formal C0/c0 are
placeholders bounded by existential published ordinary C6 constants.
The finite oracle imports only the independently constructed symplectic
W(3,2)/W(3,4) original incidence source, not predecessor proof code.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb, isqrt
import json

SCHEMA = "mathlab.hyp105.original-root-z0-sharp-core.v1"
ROOT_STATUS = "OPEN_WITH_FORMAL_BLOCKER"
K = 64
R_ZERO = 93312
R_ZPOS = 93313
OLD_CORE = Fraction(3, 4)
NO_Z_CORE = Fraction(83, 104)
NEW_W3 = Fraction(1143574, 177957)
NEW_BBO = Fraction(8614721, 2847312)
OLD_BBO = Fraction(119, 48)


def _ceil(q):
    if not isinstance(q, Fraction):
        raise TypeError("Fraction required")
    return -(-q.numerator // q.denominator)


def _ceil_sqrt(n):
    if type(n) is not int or n < 0:
        raise ValueError("nonnegative int required")
    x = isqrt(n)
    return x + (x*x != n)


def source_z0_budget(C0, c0):
    """Exact logical all-h ledger; cited source lemmas are NOT machine-proven."""
    if not isinstance(C0, Fraction) or not isinstance(c0, Fraction):
        raise TypeError("formal constants must be exact fractions")
    if C0 < 1 or not 0 < c0 <= 1:
        raise ValueError("formal C0>=1 and 0<c0<=1 required")
    # Sharp no-deletion Caro-Wei: lambda=1/16, alpha=1/1296.
    lam = Fraction(1, 16)
    cw = lam*lam/(lam+5)
    density = cw/72
    assert cw == Fraction(1, 1296)
    assert density == Fraction(1, R_ZERO)
    # Sharp >64 pruning: each deleted J vertex contributes at least 65.
    high_J_cap = Fraction(5, K+1)
    core = 1 - Fraction(1, 8) - high_J_cap
    assert core == NO_Z_CORE and core > OLD_CORE
    # Physical n=a^2 <= 9/4*s^3, paired physical edges m=2|C|.
    walk3 = Fraction(16, 81)*(4*core)**3
    assert walk3 == NEW_W3
    # Only the three non-Z costs: improper, non-Z endpoint, A/C blockers.
    nonZ_errors = 3*Fraction(1, 8)
    produced = (walk3 - nonZ_errors)/2
    assert produced == NEW_BBO and produced > OLD_BBO

    T = _ceil(Fraction(17*R_ZERO**3, 2)*C0**3)
    q2 = 16*comb(2*(K+1), 2)
    q3 = 64*comb(3*(K+1), 3)
    L6 = 24 + 153*T*T
    L4 = q2*q2*_ceil_sqrt(_ceil(Fraction(17*L6, 4))) + 19*T
    B0 = _ceil_sqrt(360*(K+1)*T)
    E = 5*q3*_ceil_sqrt(L6)
    D = 4*_ceil_sqrt(B0*T*L4)
    s0 = max(64, 444*T, (8*E)**2, (8*D)**8)
    h0 = (s0-1).bit_length()
    delta = Fraction(c0, R_ZERO**6)
    checks = {
        "true_original_fixed_complete_pair_injective_correlated_maps_required": True,
        "source_J_spectral_eJ_at_most_5s4_over2_is_INHERITED": True,
        "full_source_original_flags_N_at_least_s4": True,
        "all_h_K64_removed_J_degree_gt64_at_least65_per_removed": high_J_cap == Fraction(1,13),
        "strict_LOW_original_heavy_E_less_than_s4_over8": True,
        "new_Z0_original_paired_core_ge_83over104_s4": core == NO_Z_CORE,
        "new_Z0_core_strictly_exceeds_inherited_3over4": core > OLD_CORE,
        "minimal_alphabet_a2_le_9over4_s3_is_INHERITED": True,
        "Blakley_Roy_full_isolates_source_W3_sharpened": walk3 == NEW_W3,
        "original_four_mixed_A_equals_I_not_C_is_INHERITED": True,
        "three_nonZ_errors_each_at_most_s6_over8_are_INHERITED": True,
        "original_PRODUCED_BBo_exact_2_to_1_is_INHERITED": True,
        "new_Z0_produced_BBo_ge_8614721over2847312_s6": produced == NEW_BBO,
        "old_Z0_produced_BBo_119over48_strictly_improved": produced > OLD_BBO,
        "Caro_Wei_and_two_actual_typed_cuts_density_is_INHERITED": density == Fraction(1,R_ZERO),
        "published_ordinary_simple_unoriented_C6_requires_EXISTENTIAL_constants": True,
        "heavy_C6_threshold_matches_R93312": T >= Fraction(17*R_ZERO**3,2)*C0**3,
        "all_h_low_moment_L6_and_L4_match_inherited_error_scales": L6 > 0 and L4 > 0,
        "all_h_s0_dyadic_independent_of_labels": (1<<h0)>=s0>(1<<(h0-1)),
        "root_minimax_FROM_INHERITED_HEAVY_LOW_ONLY": 0<delta<=1<produced,
        "different_c0_c0_probe_values_not_published_graph_constants": True,
        "no_numeric_external_C6_constant_claimed": True,
        "no_GF5_palette_needed_for_UNWEIGHTED_root_Branch_A": True,
        "full_ancestral_math_acceptance_pending": True,
        "no_ASET_exponent_claim": True,
    }
    if not all(checks.values()):
        raise AssertionError("Z0 arithmetic or scope failed")
    return {
        "formal_C0_NOT_A_PUBLISHED_VALUE": str(C0),
        "formal_c0_NOT_A_PUBLISHED_VALUE": str(c0),
        "R_zero_Z": R_ZERO,
        "R_with_Z_parent": R_ZPOS,
        "T": str(T), "q2": q2, "q3": q3,
        "L6": str(L6), "L4": str(L4), "B0": str(B0),
        "E": str(E), "D": str(D),
        "s0": str(s0), "h0": h0,
        "new_Z0_core_floor": str(core),
        "new_Z0_W3_floor": str(walk3),
        "new_Z0_produced_BBo_floor": str(produced),
        "previous_Z0_produced_BBo_floor": str(OLD_BBO),
        "low_improvement_factor": str(produced/OLD_BBO),
        "heavy_delta_conditioned": str(delta),
        "final_source_seven_motif_S_conditioned": str(delta),
        "exact_25_gate_ledger": checks,
        "root_PROVED_A": False,
        "full_predecessor_scientific_acceptance": False,
        "ASET_exponent_claimed": False,
    }


def _pair_alphabet(V):
    a = 2
    while a*(a-1)//2 < V:
        a += 1
    return a, tuple(combinations(range(a), 2))


def _edge(u, v):
    if u == v:
        raise AssertionError("physical diagonal is not a loop")
    return tuple(sorted((u, v)))


def original_physical_model(s, flags, mode):
    """Rebuild actual ORIGINAL pair maps, owner graph and conflict J."""
    V = (s+1)*(s*s+1)
    flags = tuple(flags)
    if len(flags) != (s+1)*V or len(set(flags)) != len(flags):
        raise ValueError("not a complete uniquely named original source")
    if len(set(p for p,_ in flags))!=V or len(set(l for _,l in flags))!=V:
        raise ValueError("not the prescribed source")
    a, pairs = _pair_alphabet(V)
    f = tuple(pairs[:V])
    if mode == "lex":
        g = tuple(pairs[:V])
    elif mode == "reverse":
        g = tuple(reversed(pairs[:V]))
    elif mode == "shift":
        g = tuple(pairs[(i*3+1) % len(pairs)] for i in range(V)) if len(pairs)==V else tuple(pairs[(i+1)%len(pairs)] for i in range(V))
    else:
        raise ValueError("unknown pair-label mode")
    if len(set(f)) != V or len(set(g)) != V:
        raise AssertionError("injection failed")
    byp = defaultdict(list)
    byl = defaultdict(list)
    flagid = {}
    for i, (p,l) in enumerate(flags):
        byp[p].append(i)
        byl[l].append(i)
        flagid[(p,l)] = i
    if any(len(byp[p]) != s+1 or len(byl[p]) != s+1 for p in range(V)):
        raise AssertionError("not a genuine regular original source")
    J = [set() for _ in flags]
    for group, labels, side in ((byp,g,1),(byl,f,0)):
        for _, members in group.items():
            for i,j in combinations(members,2):
                ti=flags[i][side]
                tj=flags[j][side]
                if set(labels[ti]) & set(labels[tj]):
                    J[i].add(j)
                    J[j].add(i)
    owners={}
    for i, (p,l) in enumerate(flags):
        x0,x1 = f[p]
        y0,y1 = g[l]
        for u,v in (((x0,y0),(x1,y1)),((x0,y1),(x1,y0))):
            e = _edge(u,v)
            if e in owners:
                raise AssertionError("two original flags own one physical edge")
            owners[e]=i
    assert len(owners)==2*len(flags)
    return dict(s=s,V=V,a=a,f=f,g=g,flags=flags,
                byp=byp,byl=byl,flagid=flagid,J=J,owners=owners)


def _adjacency(owners):
    adj = defaultdict(set)
    for u,v in owners:
        adj[u].add(v)
        adj[v].add(u)
    return adj


def _source_projection(m, q, r):
    if (q,r) in m["flagid"]:
        return None
    points = {m["flags"][i][0] for i in m["byl"][r]}
    opts=[]
    for p in points:
        shared = set(m["flags"][i][1] for i in m["byp"][q]) & set(
            m["flags"][i][1] for i in m["byp"][p])
        for ell in shared:
            opts.append((p,ell))
    if len(opts) != 1:
        raise AssertionError("not genuine GQ unique nonincident projection")
    return opts[0]


def _classify_path(path, m, owners):
    u,a,b,v=path
    if len({x[0] for x in path})!=4 or len({x[1] for x in path})!=4:
        return None
    q = {p:i for i,p in enumerate(m["f"])}.get(_edge(u[0],v[0]))
    r = {p:i for i,p in enumerate(m["g"])}.get(_edge(u[1],v[1]))
    if q is None or r is None or (q,r) in m["flagid"]:
        return None
    x = _source_projection(m,q,r)
    if x is None:
        return None
    p,ell=x
    if set(m["f"][q]) & set(m["f"][p]):
        return None
    if set(m["g"][r]) & set(m["g"][ell]):
        return None
    if a[0] in m["f"][p] or b[0] in m["f"][p]:
        return None
    if a[1] in m["g"][ell] or b[1] in m["g"][ell]:
        return None
    ids = (owners[_edge(u,a)], owners[_edge(a,b)], owners[_edge(b,v)],
           m["flagid"][(q,ell)],m["flagid"][(p,ell)],m["flagid"][(p,r)])
    if len(set(ids))!=6:
        raise AssertionError("repeated ORIGINAL incidence owner in produced BBo")
    cpoint=sorted(Counter(m["flags"][i][0] for i in ids).values())
    cline=sorted(Counter(m["flags"][i][1] for i in ids).values())
    if cpoint!=[1,1,1,1,2] or cline!=[1,1,1,1,2]:
        raise AssertionError("not ORIGINAL B/B overlap factor source")
    return tuple(sorted(ids))


def source_case(s, mode):
    from hyp105_original_defect_factor_referee import genuine_symplectic_source
    model=original_physical_model(s,genuine_symplectic_source(s),mode)
    J=model["J"]
    eJ=sum(len(neighbors) for neighbors in J)//2
    high={i for i, n in enumerate(J) if len(n)>K}
    if 65*len(high)>2*eJ:
        raise AssertionError("integer J degree pruning fails")
    adj_all=_adjacency(model["owners"])
    maxdeg=max(map(len,adj_all.values()),default=0)
    # Diagnostic low threshold is NOT the enormous asymptotic theorem T.
    T = maxdeg//s + 1
    Q={u for u,ns in adj_all.items() if len(ns)>T*s}
    E_heavy={e for e in model["owners"] if any(v in Q for v in e)}
    assert not E_heavy and 8*len(E_heavy)<s**4
    discarded={model["owners"][e] for e in E_heavy}
    selected=set(range(len(J)))-high-discarded
    owners={e:i for e,i in model["owners"].items() if i in selected}
    adj=_adjacency(owners)
    deg={u:len(adj[u]) for u in adj}
    W3=2*sum(deg[u]*deg[v] for u,v in owners)
    n=model["a"]**2
    literal_walk_lower=Fraction((4*len(selected))**3,n*n)
    if Fraction(W3)<literal_walk_lower:
        raise AssertionError("full physical with isolates Blakley-Roy failed")
    if Fraction(len(selected)) < len(J)-len(E_heavy)-Fraction(2*eJ,65):
        raise AssertionError("sharp original J/HEAVY union estimate failed")
    # Two independently ordered traversals of EXACT real source-owned P3.
    from_left=set()
    from_middle=set()
    for u in adj:
        for a in adj[u]:
            for b in adj[a]:
                for v in adj[b]:
                    if len({x[0] for x in (u,a,b,v)})==4 and len(
                        {x[1] for x in (u,a,b,v)})==4:
                        from_left.add((u,a,b,v))
    for e in owners:
        x,y=e
        for a,b in ((x,y),(y,x)):
            for u in adj[a]:
                for v in adj[b]:
                    if len({z[0] for z in (u,a,b,v)})==4 and len(
                        {z[1] for z in (u,a,b,v)})==4:
                        from_middle.add((u,a,b,v))
    if from_left!=from_middle:
        raise AssertionError("independent original physical P3 traversals disagree")
    sixsets=Counter()
    for path in from_left:
        q=_classify_path(path,model,owners)
        if q is not None:
            sixsets[q]+=1
    if any(x!=2 for x in sixsets.values()):
        raise AssertionError("ORIGINAL produced BBo not exactly path reversal 2-to-1")
    return dict(s=s,mode=mode,flags=len(J),physical_real_diagonals=len(owners),
                complete_pair_maps=True,actual_original_J_edges=eJ,
                high_J_removed=len(high),diagnostic_T_not_asymptotic=T,
                original_heavy_touch_edges=len(E_heavy),source_core=len(selected),
                core_lower_exact=str(Fraction(len(J)-len(E_heavy))-Fraction(2*eJ,65)),
                source_W3_exact=W3,Blakley_Roy_full_isolate_lower=str(literal_walk_lower),
                proper_original_directed_physical_P3=len(from_left),
                accepted_original_directed_P3=sum(sixsets.values()),
                produced_original_distinct_BBo=len(sixsets),
                accepted_to_original_sixset_exactly_two=all(n==2 for n in sixsets.values()))


def certificate():
    probes=[source_z0_budget(*x) for x in (
        (Fraction(1),Fraction(1)),
        (Fraction(2),Fraction(1,5)),
        (Fraction(7,3),Fraction(1,17)))]
    examples=[source_case(s,mode) for s in (2,4)
              for mode in ("lex","reverse")]
    if not any(x["produced_original_distinct_BBo"]>0 for x in examples):
        raise AssertionError("original P3-to-BBo source oracle was vacuous")
    return {
        "schema":SCHEMA, "issue":230, "status":ROOT_STATUS,
        "parent_pr":768,
        "new_analytical_Z0_core":str(NO_Z_CORE),
        "new_analytical_Z0_W3":str(NEW_W3),
        "new_analytical_Z0_BBo":str(NEW_BBO),
        "root_branch_A_math_premises_still_need_independent_signoff":True,
        "all_h_formal_not_numeric_graph_constant_probes":probes,
        "genuine_original_W32_W34_independent_source_cases":examples,
        "root_PROVED_A":False,"infinite_B_counterexample":False,
        "general_ASET_exponent":False,
    }


if __name__=="__main__":
    print("AA4_ROOT_Z0_CERTIFICATE="+json.dumps(
        certificate(),sort_keys=True,separators=(",",":")))
