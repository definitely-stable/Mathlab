"""HYP-105 #230 / D6-AA4-S: all-h ORIGINAL-root conditioned Frechet NO-GO.

For every TRUE original W(3,s), s=2^h, and every complete global point/line
pair-label injection, the Fréchet lower floor for the original B(point)/A(line)
six-incidence intersection is ZERO, even after independently conditioning on
EACH repeated original point source root. Same for A(point)/B(line) by duality.

This is a theorem about what one-sided root marginals CANNOT certify.
It neither says genuine intersections vanish nor settles the all-h S minimax.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations
from math import comb, prod

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4q_two_sided_seven_join import (
    exact_ONE_side_original_projection_index,
)
from hyp105_issue230_d6aa4r_original_joint_swap_certificate import (
    strict_true_W32_gq_model,
)


def minimal_physical_a(s):
    if type(s) is not int or s < 2 or s & (s - 1):
        raise ValueError("genuine W(3,s), s=2^h with h>=1 only")
    V = (s + 1) * (s*s + 1)
    a = 2
    while comb(a, 2) < V:
        a += 1
    return a


def all_h_root_conditional_frechet_no_go(s):
    """Exact integer all-h B/A root envelope; dual A/B is symmetric.

    Universe lower bound: choose a repeated original point p and two
    genuine original incident lines, then four further actual source
    incidences on fresh point AND line factors. Up to (3+2j)*d flags
    forbidden at step j, no independence or fabricated per-Q maps.

    Left B-root and right A half projection upper bounds use the full
    physical K_a edge set; actual globally injected partial occupancy
    can only reduce candidate counts. The two roots are conditioned on
    the SAME actual original source p and its six original flag IDs.
    """
    a = minimal_physical_a(s)
    d = s + 1
    V = (s + 1) * (s*s + 1)
    N = V * d
    # Ordered fresh original incidence choices / 4!:
    ordered = comb(d,2) * prod(d * (V - 3 - 2*j) for j in range(4))
    if ordered % 24:
        raise AssertionError("root source counting lower must be an integer")
    universe_floor = ordered // 24
    left_B_root_cap = 3 * comb(a-2,4) * comb(d,2) * d**4
    right_A_global_cap = 70 * comb(a,6) * d**6
    slack = universe_floor-left_B_root_cap-right_A_global_cap
    if slack <= 0:
        raise AssertionError("all-h root-conditioned Frechet gap did not close")
    # Prove large orders without numerical fitting:
    #   a <= 2*s^(3/2), d<=5s/4, V-9>=s^3/2 (s>=4),
    #   M_p>=s^18/768,
    #   L_p+R_p <=(5/4)^6 * [s^12 +(56/9)s^15]
    #            <=(65/9)(5/4)^6*s^15 < s^18/768 (s>=32).
    # A power-of-two integer bound a^2<=4s^3 avoids floats.
    large_proof = (
        s >= 32 and
        a*a <= 4*s**3 and
        4*d <= 5*s and
        2*(V-9) >= s**3 and
        s**3*48 > 1015625
    )
    if s>=32 and not large_proof:
        raise AssertionError("analytic all-h bound failed")
    return {
        "s":s, "V":V, "N":N, "d":d, "a":a,
        "minimum_true_original_B_A_source_universe_per_root":universe_floor,
        "maximum_left_physical_B_original_root_half":left_B_root_cap,
        "maximum_right_physical_A_global_half":right_A_global_cap,
        "strict_universe_minus_both_marginal_caps":slack,
        "best_possible_root_conditional_Frechet_lower":0,
        "dual_A_left_B_right_same_no_go":True,
        "proof_mode":"symbolic_uniform_s_ge_32" if s>=32 else "finite_integer_small_h_1_to_4",
        "independence_or_local_pseudolabeling_used":False,
        "all_h_seven_S_omega_s6_PROVED":False,
    }


def original_B_A_point_root(Q, incidences):
    """One repeated TRUE source point and six distinct TRUE source lines."""
    ps = Counter(incidences[i][0] for i in Q)
    ls = {incidences[i][1] for i in Q}
    if len(ls) != 6 or sorted(ps.values(),reverse=True) != [2,1,1,1,1]:
        return None
    return next(p for p, count in ps.items() if count==2)


@lru_cache(maxsize=3)
def exact_true_W32_B_A_source_universe_by_root(incidences):
    """Source-only enumeration, independent of any physical f or g.

    For every original repeated point p, enumerate all EXACT source
    six-flag B(point)/A(line) candidates; no artificial per-Q labels.
    """
    inc = tuple(incidences)
    if len(inc)!=45 or len(set(inc))!=45:
        raise ValueError("exact source host needs 45 distinct ORIGINAL flags")
    rootcols=[[] for _ in range(15)]
    for j,(p,l) in enumerate(inc):
        rootcols[p].append(j)
    counts=[]
    for p in range(15):
        n=0
        for i,j in combinations(rootcols[p],2):
            usedlines={inc[i][1],inc[j][1]}
            others=[k for k,(q,l) in enumerate(inc)
                    if q!=p and l not in usedlines]
            for Q in combinations(others,4):
                pts={inc[k][0] for k in Q}
                if len(pts)!=4:
                    continue
                lines={inc[k][1] for k in Q}
                if len(lines)!=4:
                    continue
                n+=1
        counts.append(n)
    return tuple(counts)


def real_W32_root_marginal_and_joint_audit(model,*,exact_universe=True):
    """Real all-seven-related B/A sector, independent two-half source indexes.

    The returned true joint root counts are *not* the hypothetical Frechet
    model: they retain true original incidence intersection coherence.
    """
    inc,f,g = strict_true_W32_gq_model(model)
    P=exact_ONE_side_original_projection_index(model,0)["candidate_sixset_map"]
    L=exact_ONE_side_original_projection_index(model,1)["candidate_sixset_map"]
    LP=[set() for _ in range(15)]
    RA=[set() for _ in range(15)]
    for Q,kind in P.items():
        if kind=="B":
            p=original_B_A_point_root(Q,inc)
            if p is not None:
                LP[p].add(Q)
    for Q,kind in L.items():
        if kind=="A":
            p=original_B_A_point_root(Q,inc)
            if p is not None:
                RA[p].add(Q)
    bound=all_h_root_conditional_frechet_no_go(2)
    if exact_universe:
        universe=exact_true_W32_B_A_source_universe_by_root(inc)
    else:
        universe=(bound["minimum_true_original_B_A_source_universe_per_root"],)*15
    results={}
    for p in range(15):
        actual_joint=len(LP[p] & RA[p])
        left=len(LP[p]);right=len(RA[p]);n=universe[p]
        if not (left<=bound["maximum_left_physical_B_original_root_half"] and
                right<=bound["maximum_right_physical_A_global_half"] and
                n >= bound["minimum_true_original_B_A_source_universe_per_root"]):
            raise AssertionError("true source and physical capacity envelope failed")
        if n<=left+right:
            raise AssertionError("root conditional Fréchet unexpectedly nonzero")
        if actual_joint>min(left,right):
            raise AssertionError("actual B/A joint exceeds marginal")
        results[str(p)]={
            "true_source_universe_BA_root":n,
            "actual_left_B_source_root_margin":left,
            "actual_right_A_source_B_root_margin":right,
            "root_conditional_Frechet_lower":max(0,left+right-n),
            "real_coupled_B_left_A_right_joint":actual_joint,
        }
    return {
        "scope":"genuine ORIGINAL W32 source-point-root B/A with two GLOBAL physical injections",
        "per_true_original_root":results,
        "actual_total_B_left_A_right":sum(x["real_coupled_B_left_A_right_joint"] for x in results.values()),
        "all_15_root_frechet_floors_zero":all(x["root_conditional_Frechet_lower"]==0
                                              for x in results.values()),
        "source_universe_exactly_enumerated":exact_universe,
        "root_conditioned_half_marginal_no_go_all_h":True,
        "all_h_S_positive_minimum_proved":False,
    }


def report(scheme="S68",*,exact_universe=True):
    return {
        "slice":"HYP105-ISSUE230-D6-AA4-S-ROOT-CONDITIONAL-FRECHET-NOGO",
        "small_orders":[all_h_root_conditional_frechet_no_go(1<<h)
                        for h in range(1,6)],
        "actual":real_W32_root_marginal_and_joint_audit(
            fixture(1,scheme),exact_universe=exact_universe)
    }


if __name__=="__main__":
    import argparse,json
    p=argparse.ArgumentParser()
    p.add_argument("--scheme",choices=("S68","S72","lex","reverse"),default="S68")
    p.add_argument("--no-exact-universe",action="store_true")
    args=p.parse_args()
    print(json.dumps(report(args.scheme,exact_universe=not args.no_exact_universe),
                     sort_keys=True,indent=2))
