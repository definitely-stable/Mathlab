"""AA4-DH: sharp CONSTANT independent-of-s reuse cap for original A-side Q.

Fix six distinct TRUE original point-line SOURCE incidence IDs in
W(3,s), accepted by the historical seven-GF5 all-a classifier, and
ONE pair of frozen globally injected complete correlated typed
point/line factor-to-physical K_a edge maps f,g.

For the AA4-DG 2-external A-reservoir C4-pair scheme:
 SOURCE A side admits <=24 physically valid (doubled,base,C4 triple)
 representations of this same Q: its physical 2factor must be one
 connected C6; for EACH of 6 possible doubled original SOURCE
 edges the only disjoint 3-edge path is the antipodal C6 path;
 the closing chord is uniquely determined; base is one of 4 cycle edges.
 SOURCE B side admits <=4; SOURCE C side admits <=24.
Therefore one accepted ORIGINAL six-ID Q may occur in the complete
AA4-DG source P3 × paired-C4 bridge multiset <=:
 D6 (A/A): 24*24=576
 A/B (either orientation):24*4=96
 C/A (either orientation):24*24=576.

Every inverted witness is filtered through the ACTUAL original
W(3,s) unique nonincident three-incidence path p--l0--q--l,
and AA4-DG true source physical A catalogue; NO original
incidence is conjured from physical pair-image occupancy.

Consequently M_D6 <=576 U_D6, M_A/B<=96 U_A/B and
M_C/A<=576 U_C/A for completion-weighted historical A-side Q,
where U is the number of DISTINCT SIX ORIGINAL source incidence IDs
in that class (same frozen f,g). The root S>=c s^6 still needs a
positive universal LOWER bound on M, which is NOT proved here.
"""
from collections import Counter
from itertools import combinations

from hyp105_issue230_d6aa4cq_original_macro_path_cut_gate import _validated_original
from hyp105_issue230_d6aa4cr_exact_BBo_three_matching_transfer import (
    original_nonincident_threepath,
)
from hyp105_issue230_d6aa4cg_four_shared_edge_two_completion import (
    classify_seven_all_a_original_Q,
)
from hyp105_issue230_d6aa4dg_two_external_A_bridge import (
    original_two_external_A_completion_catalogue,
)

UPPER_SIDE={"A":24,"B":4,"C":24}
ORIGINAL_HISTORICAL_A_CLASS_CAPS={
    "D6":576,
    "A-left/B-right":96,
    "B-left/A-right":96,
    "C/A":576,
}


def _edge_degree_two_regular(physical):
    degree=Counter(v for pair in physical for v in pair)
    return len(physical)==6 and len(degree)==6 and set(degree.values())=={2}


def inverse_original_typed_ABC_C4_representations(labels,multiset_source_ids):
    """INVERSE exact ORIGINAL physical source factor C4 reservoir reps.

    Multiset of 6 ORIGINAL typed source factor IDs from the SAME 6
    immutable original SOURCE incidence flags; each returned tuple is
    (doubled-original-source-ID, base-original-source-ID,
     sorted(3 actually occupied ORIGINAL C4 factor IDs)).

    An A representation MUST be EXACTLY the AA4-DG two-external
    source bridge form; B/C are the local forms from AA4-DF.
    This routine does NOT read the original incidence M, only the
    fixed truly injected original typed physical pair images.
    """
    labels=tuple(tuple(e) for e in labels)
    if len(set(labels))!=len(labels) or any(
        len(e)!=2 or tuple(sorted(e))!=e or any(
            type(v) is not int or v<0 for v in e) for e in labels):
        raise ValueError("complete injective typed ORIGINAL simple canonical physical pair image labels required")
    src=tuple(multiset_source_ids)
    if len(src)!=6 or any(type(i) is not int or not 0<=i<len(labels) for i in src):
        raise ValueError("six original SOURCE factor appearances required")
    mult=Counter(src)
    profile={tuple([1]*6):"A",(1,1,1,1,2):"B",(2,2,2):"C"}.get(
        tuple(sorted(mult.values())))
    if profile is None:
        raise ValueError("original six-source-ID endpoint multiplicity must be A/B/C")
    inverse={e:i for i,e in enumerate(labels)}
    src_support=frozenset(mult)
    result=set()
    if profile=="A":
        physical=tuple(labels[i] for i in src_support)
        if not _edge_degree_two_regular(physical):
            return {"profile":profile,"representations":(),
                    "physical_A_cycle_structure":"not_two_regular",
                    "maximum":24}
        # A six-edge 2factor is exactly C6 or C3+C3.
        # For each doubled edge q, the 3 OTHER edges disjoint from
        # BOTH its endpoints either form a unique 3edge antipodal
        # PATH (C6), or a TRIANGLE (C3+C3). No choice of 3 among 5.
        valid_doubled=0
        for q in sorted(src_support):
            doubled=set(labels[q])
            path=tuple(i for i in sorted(src_support-{q})
                       if set(labels[i]).isdisjoint(doubled))
            if len(path)!=3:continue
            deg=Counter(v for i in path for v in labels[i])
            if len(deg)!=4 or sorted(deg.values())!=[1,1,2,2]:
                continue
            terminals=tuple(sorted(v for v,n in deg.items() if n==1))
            chord=tuple(sorted(terminals))
            missing=inverse.get(chord)
            if missing is None or missing in src_support:
                continue
            cycle=(missing,*path)
            vertices={v for i in cycle for v in labels[i]}
            if len(vertices)!=4 or len(set(cycle))!=4:
                raise AssertionError("physical A six-cycle inverse antipodal original source C4 malformed")
            valid_doubled+=1
            for base in cycle:
                triple=tuple(sorted(t for t in cycle if t!=base))
                result.add((q,base,triple))
        structure="one_C6" if valid_doubled else "no_A_bridge"
    elif profile=="B":
        doubled=next(i for i,n in mult.items() if n==2)
        cycle=tuple(sorted(src_support-{doubled}))
        deg=Counter(v for i in cycle for v in labels[i])
        if (len(deg)==4 and set(deg.values())=={2}
            and all(set(labels[i]).isdisjoint(labels[doubled]) for i in cycle)):
            for base in cycle:
                triple=tuple(sorted(t for t in cycle if t!=base))
                result.add((doubled,base,triple))
        structure="physical_B_4cycle_or_invalid"
    else:
        for doubled in sorted(src_support):
            others=tuple(sorted(src_support-{doubled}))
            if any(set(labels[i])&set(labels[doubled]) for i in others):
                continue
            i,j=others
            x,y=labels[i];u,v=labels[j]
            if {x,y}&{u,v}:continue
            for bridges in (((x,u),(y,v)),((x,v),(y,u))):
                mids=tuple(inverse.get(tuple(sorted(e))) for e in bridges)
                if any(z is None or z in src_support for z in mids):
                    continue
                cycle=(i,j,*mids)
                deg=Counter(t for k in cycle for t in labels[k])
                if len(deg)!=4 or set(deg.values())!={2}:
                    raise AssertionError("physical original C profile bridge cycle broken")
                for base in cycle:
                    triple=tuple(sorted(t for t in cycle if t!=base))
                    result.add((doubled,base,triple))
        structure="two_opposite_physical_C4_matchings"
    representations=tuple(sorted(result))
    if len(representations)>UPPER_SIDE[profile]:
        raise AssertionError("original sixflag typed source inverse CONSTANT-C4 multiplicity bound")
    return {
        "profile":profile,
        "representations":representations,
        "physical_A_cycle_structure":structure,
        "maximum":UPPER_SIDE[profile],
    }


def inverse_true_original_historical_A_Q_bridge_certificate(model,original_Q):
    """All ORIGINAL SOURCE-P3/C4 representations for ONE accepted A-side Q.

    Complete inverse, not a sampled source-anchor scan. The genuine
    original P3 path and matching between stored source factor IDs
    are independently checked. Counts do not scale with s.
    """
    s,V,a,f,g,pl,lp=_validated_original(model)
    inc=tuple(model["incidences"])
    Q=tuple(sorted(original_Q))
    if len(Q)!=6 or len(set(Q))!=6 or any(
        type(z) is not int or not 0<=z<len(inc) for z in Q):
        raise ValueError("six distinct genuine original incidence IDs needed")
    kind=classify_seven_all_a_original_Q(Q,f,g,inc)
    if kind not in ORIGINAL_HISTORICAL_A_CLASS_CAPS:
        raise ValueError("an accepted historical ORIGINAL GF5 A-side sixflag Q is required")
    P=tuple(inc[z][0] for z in Q)
    L=tuple(inc[z][1] for z in Q)
    IP=inverse_original_typed_ABC_C4_representations(f,P)
    IL=inverse_original_typed_ABC_C4_representations(g,L)
    profile_P=IP["profile"];profile_L=IL["profile"]
    if "A" not in (profile_P,profile_L):
        raise AssertionError("A-side accepted original GF5 Q has no A factor profile")
    possible=tuple((pt,lt) for pt in IP["representations"]
                   for lt in IL["representations"])
    result=[]
    flag_id={(p,l):z for z,(p,l) in enumerate(inc)}
    for (q,p,pt),(l0,l,lt) in possible:
        if l in pl[p] or set(f[p])&set(f[q]) or set(g[l])&set(g[l0]):
            continue
        three=original_nonincident_threepath(p,l,pl,lp)
        if three[1][0]!=q or three[0][1]!=l0:
            continue
        # Exact historical sixflag Q already immutable and positive,
        # but explicitly validate the A-side uses an ACTUALLY
        # occupied paired C4 of AA4-DG's strict 2-external set.
        if profile_P=="A":
            if tuple(sorted(set(P))) not in original_two_external_A_completion_catalogue(
                    f,p,q,pt):
                raise AssertionError("inverse actual original POINT A candidate not in forward 8-template list")
        if profile_L=="A":
            if tuple(sorted(set(L))) not in original_two_external_A_completion_catalogue(
                    g,l,l0,lt):
                raise AssertionError("inverse actual original LINE A candidate not in forward 8-template list")
        if any((i,j) not in flag_id for i,j in (inc[z] for z in Q)):
            raise AssertionError("fake original W3 incidence in six-ID Q")
        result.append((p,l,pt,lt))
    result=tuple(sorted(set(result)))
    cap=ORIGINAL_HISTORICAL_A_CLASS_CAPS[kind]
    if len(result)>cap:
        raise AssertionError("source original historical A positive Q reused > all-h 576")
    return {
        "s":s,"a":a,"historical_true_original_GF5_label":kind,
        "immutable_six_original_incidence_ID_Q":Q,
        "original_POINT_side_profile":profile_P,
        "original_LINE_side_profile":profile_L,
        "POINT_inverse_occupied_original_C4_representation_count":
            len(IP["representations"]),
        "LINE_inverse_occupied_original_C4_representation_count":
            len(IL["representations"]),
        "original_source_possible_C4_pair_representations_before_P3_filter":
            len(possible),
        "original_source_ACTUAL_nonincident_P3_paired_C4_reuse_count":
            len(result),
        "actual_true_original_source_P3_C4_representations":result,
        "allh_uniform_independent_of_s_multiplicity_bound":cap,
        "GF5_root_S_omega_s6_NOT_proven":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def allh_original_A_bridge_reuse_caps():
    """Constant exact all-h bounds on original sixflag C4-pair multiplicity."""
    return {
        "per_A_original_sixflag_source_C4_representations":24,
        "per_B_original_sixflag_source_C4_representations":4,
        "per_C_original_sixflag_source_C4_representations":24,
        "D6":576,
        "A-left/B-right":96,
        "B-left/A-right":96,
        "C/A":576,
        "equivalent_mass_transfer":
            "M_D6 <= 576 U_D6; M_A/B <= 96 U_A/B; M_C/A <= 576 U_C/A",
        "holds_every_dyadic_h_and_every_complete_correlated_global_original_map":True,
        "requires_SEPARATE_uniform_lower_bound_on_M":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }
