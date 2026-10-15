"""HYP-105 #230 / AA4-AJ: all-global-map true-original Hall site-cap NO-GO.

For an actual original GQ W(3,s), s=2^h, and arbitrary TWO FULL,
GLOBALLY injected typed physical pair maps f,g, fix ONE actual B-side
root p, TWO DISTINCT real flags (p,l0),(p,l1), one occupied physical
complementary B C4 on four distinct ORIGINAL B factors q0..q3, and
disjoint g(l0),g(l1) (two physical triangle seeds). Use the SIX exact
source-incidence Hall channels of ancestor AA4-AH.

For EACH S={i,j} original row pair and each auxiliary physical site y
belonging to its 2x2 original-source rook set Y_S, associate the ONE
genuine original opposite factor incident with q_i in the unique
2-rook matching; distinct y yield DISTINCT original opposite factors
because one COMPLETE globally injected opposite typed pair g is reused.
Thus |Y_S|<=d=s+1; similarly |Z_S|<=d for all six S.

Consequently exact accepted original six-incidence-ID split-triangle
GF5 BA/AB count per fixed root/flags/occupied B-C4 T<=6d², for EVERY
f,g, not an ensemble mean. At every AG/AI SAFE rooted opposite physical
pair for s>=16, occupied physical two-triangle completions H>=ceil(a²/4)
and hence true-original Hall-positive H<=6d². In particular the
Hall-positive fraction <=24d²/a²<=12(s+1)/(s²+1)<1 for s>=16; at least
a 1-O(1/s) fraction of indexed physical completions must fail TRUE
original Hall, for EVERY pair of global maps.

This is a deterministic QUANTITATIVE NO-GO for "constant Hall transfer
fraction" proof shortcuts, not a counterexample family to root #230,
not a lower bound on accepted GF5, and NOT an all-s lower on Hall mass.
"""
from fractions import Fraction
from itertools import combinations,permutations
from math import comb

from hyp105_issue230_d6aa4ag_deterministic_triangle_hall import (
    minimal_alphabet,independent_common_neighbors,
)
from hyp105_issue230_d6aa4af_rootpair_robust_quench import (
    occupied_root_C4_source_factors,
)
from hyp105_issue230_d6aa4ah_signature_hall_kernel import (
    PAIRS4,_original_actual_context,_sites,six_channel_original_cohort,
)
from hyp105_issue230_d6aa4ab_minimax_orbit_normalform import _valid_original_model


def all_h_original_site_cap_certificate(s):
    """Exact symbolic positive/rejection ratio bound on SAFE cohorts.

    'Safe' is the AA4-AI disjoint pinned opposite physical images
    where every pinned physical coordinate missing-edge degree<a/16.
    No claim that each individual source rooted pair is safe.
    """
    V,a,m=minimal_alphabet(s)
    d=s+1
    max_per_site_source_rook=d
    max_accepted_per_root_C4=6*d*d
    physical_min=(a*a+3)//4
    density=Fraction(24*d*d,a*a)
    geometry_density=Fraction(12*(s+1),s*s+1)
    if density>geometry_density:
        raise AssertionError("a^2>=2V true minimal K_a inequality failed")
    if s>=16:
        assert a>=32
        assert physical_min>max_accepted_per_root_C4
        assert geometry_density<1
    return {
        "s":s,"a":a,"V":V,"d":d,"K":comb(a,2),"holes":m,
        "six_original_two_rook_channel_count":6,
        "each_channel_site_set_cap_actual_original_degree":d,
        "each_fixed_actual_rootpair_B_C4_accepted_split_GF5_upper":
            max_accepted_per_root_C4,
        "each_SAFE_fixed_rootpair_C4_physical_two_triangle_floor":
            physical_min if a>=32 else 0,
        "each_SAFE_C4_true_original_Hall_rejected_physical_lower":
            max(0,physical_min-max_accepted_per_root_C4)
            if a>=32 else 0,
        "MAX_true_original_Hall_positive_fraction_of_SAFE_2triangles":
            str(min(Fraction(1),Fraction(max_accepted_per_root_C4,physical_min)))
            if a>=32 else "NO_SAFE_PHYSICAL_LOWER_FOR_a_LT_32",
        "simpler_all_h_fraction_ceiling_24d2_over_a2":str(density),
        "simpler_real_GQ_fraction_ceiling_12d_over_s2plus1":
            str(geometry_density),
        "uniform_strict_Hall_rejection_fraction_for_s_ge16_PROVED":s>=16,
        "each_true_source_channel_site_injection_for_ALL_global_maps":True,
        "genuine_GQ_no_SOURCE_C4_needed_for_unique_two_rook":True,
        "positive_Hall_mass_for_all_global_maps_NOT_PROVED":True,
        "root_issue230_universal_S_lower_NOT_PROVED":True,
    }


def _pairwise_source_site_witnesses(model,*,side,root,pair_offset,four_sources):
    """Explicit INJECTION site y -> distinct ORIGINAL source neighbor of
    the first selected original row qi, independently for every 2-rook
    left/right channel. This is the mathematical proof's finite oracle,
    not merely checking a precomputed cardinality.
    """
    V,a,pins,e0,e1,inv,E,neighbors=_original_actual_context(
        model,side=side,root=root,pair_offset=pair_offset)
    four=tuple(four_sources)
    if len(four)!=4 or len(set(four))!=4 or any(
            type(q) is not int or q<0 or q>=V for q in four):
        raise ValueError("four real distinct original B-side source factors needed")
    original_physical=frozenset(occupied_root_C4_source_factors(
        model,side=side,root=root))
    if frozenset(four) not in {frozenset(q) for q in original_physical}:
        raise ValueError("four ORIGINAL source singleton factors must form occupied complementary physical C4")
    if set(e0)&set(e1):
        return dict(disjoint=False,channels=[],sites=0,
                    accepted_original_Q=0)
    blocked=set(e0+e1)
    Y=_sites(e0,blocked,a,inv)
    Z=_sites(e1,blocked,a,inv)
    site_by_pair={}
    for label,sites in (("Y",Y),("Z",Z)):
        for S in PAIRS4:
            i,j=S
            witness={}
            for y,(t0,t1) in sites.items():
                first=int(t0 in neighbors[four[i]] and t1 in neighbors[four[j]])
                second=int(t1 in neighbors[four[i]] and t0 in neighbors[four[j]])
                if first+second>1:
                    raise AssertionError("GENUINE original GQ would have a SOURCE C4")
                if first+second:
                    # map to genuine ORIGINAL opposite factor matched to qi
                    opposite_line=t0 if first else t1
                    if opposite_line in witness.values():
                        raise AssertionError("two DIFFERENT auxiliary physical sites reused one GLOBALLY injected ORIGINAL opposite factor")
                    witness[y]=opposite_line
            if len(witness)>model["s"]+1:
                raise AssertionError("actual source degree caps original rook physical auxiliary sites")
            site_by_pair[label,S]=witness
    channel=[]
    for S in PAIRS4:
        remaining=tuple(x for x in range(4) if x not in S)
        left=site_by_pair["Y",S]
        right=site_by_pair["Z",remaining]
        pairs=sum(y!=z for y in left for z in right)
        channel.append({
            "real_original_row_pair":S,
            "complementary_real_original_row_pair":remaining,
            "left_site_count":len(left),
            "right_site_count":len(right),
            "left_actual_ORIGINAL_source_line_factor_IDs":
                tuple(sorted(left.values())),
            "right_actual_ORIGINAL_source_line_factor_IDs":
                tuple(sorted(right.values())),
            "physical_auxiliary_sites_left":tuple(sorted(left)),
            "physical_auxiliary_sites_right":tuple(sorted(right)),
            "actual_distinct_original_GF5_six_ID_Q":pairs,
            "unique_source_opposite_factor_per_physical_site_verified":True,
        })
        if pairs>(model["s"]+1)**2:
            raise AssertionError("every original 2x2+2x2 channel <=d^2")
    return {
        "s":model["s"],"side":side,"original_root":root,
        "pinned_actual_original_incidence_IDs":pins,
        "four_original_C4_source_factors":four,
        "disjoint":True,"channel_site_sets":channel,
        "occupied_physical_Y_auxiliary_sites":len(Y),
        "occupied_physical_Z_auxiliary_sites":len(Z),
        "accepted_original_Q":sum(x["actual_distinct_original_GF5_six_ID_Q"]
                                  for x in channel),
        "max_accepted_original_Q_by_true_GQ_degree":6*(model["s"]+1)**2,
        "all_six_site_to_actual_GQ_factor_injections_checked":True,
    }


def independently_check_genuine_original_hall_site_cap(
    model,*,side=0,root=0,pair_offset=0,max_C4=4,
):
    """TRUE globally fixed original W32/W34/W38 independent strict check.

    Computes the six actual site->source-factor injections explicitly
    and cross-checks against the ORIGINAL AH full 24-permutation oracle.
    """
    V,a,_=_valid_original_model(model)
    if type(max_C4) is not int or not 1<=max_C4<=12:
        raise ValueError("1..12 source C4 sample required")
    source=occupied_root_C4_source_factors(model,side=side,root=root)
    prev=six_channel_original_cohort(
        model,side=side,root=root,pair_offset=pair_offset,
        max_C4=max_C4,independent_direct=True)
    sample=source[:max_C4]
    reports=[]
    for four,baseline in zip(sample,prev["six_channel_rows"]):
        x=_pairwise_source_site_witnesses(
            model,side=side,root=root,pair_offset=pair_offset,
            four_sources=four)
        if x["accepted_original_Q"]!=baseline["accepted_original_GF5_Q"]:
            raise AssertionError("different source-neighbor injection versus earlier exact 24-permutation original Q")
        if x["disjoint"]:
            for v,ch in zip(x["channel_site_sets"],baseline["channels"]):
                if v["actual_distinct_original_GF5_six_ID_Q"]!=ch[
                        "true_original_GF5_distinct_Q"]:
                    raise AssertionError("different per source channel count")
                if (v["left_site_count"]!=ch["left_auxiliary_sites"]
                        or v["right_site_count"]!=ch["right_auxiliary_sites"]):
                    raise AssertionError("site map cannot replace historical AH two-source signature")
        reports.append(x)
    return {
        "s":model["s"],"side":side,"root":root,
        "source_cohorts_tested":len(reports),
        "disjoint_pinned_original_root_pair_physical":
            prev["globally_fixed_pinned_physical_disjoint"],
        "actual_all_six_ORIGINAL_GF5_accepted_Q":sum(
            v["accepted_original_Q"] for v in reports),
        "per_realized_original_B_C4_verification":reports,
        "expected_preexisting_AH_original_cohort_total":
            prev["accepted_original_GF5_Q_sample"],
        "six_source_channels_degree_capped_all_tested":True,
        "globally_complete_typed_injection_fixed_across_six_Q":True,
        "no_universal_Hall_positive_lower":True,
    }



def constructed_SHARP_genuine_W34_original_site_witness():
    """Construct one genuine W(3,4) global f,g with |Y_{0,1}|=d=5.

    The true original incidence graph is NEVER changed; we only
    reassigned BOTH complete typed physical maps as globally injected
    original-factor-to-K14-edge permutations. The relevant two distinct
    source points have DISJOINT actual original line neighborhoods;
    two physical endpoint stars independently realize ALL d real
    incidence flags, each at a distinct auxiliary site.
    """
    from hyp105_issue230_projection import fixture
    model=fixture(2,"lex")
    V,a,inc=_valid_original_model(model)
    original=tuple(tuple(e) for e in model["incidences"])
    root=0
    flags=tuple(i for i,e in enumerate(original) if e[0]==root)
    pinned=flags[:2]
    l0,l1=(original[i][1] for i in pinned)
    point_neighbors=[set() for _ in range(V)]
    for p,l in original:point_neighbors[p].add(l)
    candidates=[q for q in range(V) if q!=root and l0 not in
                point_neighbors[q] and l1 not in point_neighbors[q]]
    q0=q1=None
    for i,first in enumerate(candidates):
        for second in candidates[i+1:]:
            if point_neighbors[first].isdisjoint(point_neighbors[second]):
                q0,q1=first,second;break
        if q0 is not None:break
    if q0 is None:
        raise AssertionError("genuine W34 must have two suitable noncollinear original source points")
    others=tuple(q for q in range(V) if q not in (root,q0,q1))[:2]
    q2,q3=others
    four=(q0,q1,q2,q3)
    palette=tuple(combinations(range(a),2))
    B={root:(0,1),q0:(4,5),q1:(5,6),q2:(6,7),q3:(4,7)}
    b_used=set(B.values())
    b_other=iter(e for e in palette if e not in b_used)
    f=tuple(B.get(i) if i in B else next(b_other) for i in range(V))
    d=model["s"]+1
    A={l0:(0,1),l1:(2,3)}
    for y,l in zip(range(4,4+d),sorted(point_neighbors[q0])):
        A[l]=(0,y)
    for y,l in zip(range(4,4+d),sorted(point_neighbors[q1])):
        A[l]=(1,y)
    a_used=set(A.values())
    if len(A)!=2+2*d or len(a_used)!=len(A):
        raise AssertionError("sharp source-site source/pair assignments not globally injective")
    a_other=iter(e for e in palette if e not in a_used)
    g=tuple(A.get(i) if i in A else next(a_other) for i in range(V))
    result=dict(model,left_labels=f,right_labels=g)
    result["supports"]=tuple(
        tuple(sorted(f[p]+tuple(a+t for t in g[l])))
        for p,l in original)
    _valid_original_model(result)
    original_pair_offset=tuple(combinations(flags,2)).index(pinned)
    cert=_pairwise_source_site_witnesses(
        result,side=0,root=root,pair_offset=original_pair_offset,
        four_sources=four)
    S=next(c for c in cert["channel_site_sets"]
           if c["real_original_row_pair"]==(0,1))
    if (S["left_site_count"]!=d or
        S["left_actual_ORIGINAL_source_line_factor_IDs"]!=
            tuple(sorted(point_neighbors[q0]))):
        raise AssertionError("constructed true W34 2-rook channel has not saturated source degree")
    return {
        "model":result,
        "certificate":cert,
        "root":root,"pinned_original_source_flag_IDs":pinned,
        "four_distinct_actual_original_B_source_factors":four,
        "sharp_site_degree":S["left_site_count"],
        "sharp_actual_original_source_neighbors":
            S["left_actual_ORIGINAL_source_line_factor_IDs"],
        "actual_source_points_noncollinear":True,
        "one_complete_globally_injected_original_point_map_and_line_map":True,
    }

if __name__=="__main__":
    import argparse,json
    from hyp105_issue230_projection import fixture
    parser=argparse.ArgumentParser()
    parser.add_argument("--scheme",choices=("S68","S72","lex","reverse","random"),
                        default="lex")
    parser.add_argument("--power",type=int,choices=(1,2,3),default=1)
    args=parser.parse_args()
    z={"analytic":[all_h_original_site_cap_certificate(1<<h)
                   for h in range(1,18)]}
    if args.power==1 or args.scheme in ("lex","random"):
        z["true_original"]=independently_check_genuine_original_hall_site_cap(
            fixture(args.power,args.scheme),side=0,root=0,max_C4=3)
    print(json.dumps(z,indent=2,sort_keys=True))
