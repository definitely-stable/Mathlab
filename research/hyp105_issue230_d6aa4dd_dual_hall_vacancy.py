"""AA4-DD: dual-symmetric zero-row/zero-column original Hall deficit witness energy.

Every marked ORIGINAL point-spoke->line-spoke incidence of an ACTUAL
physically occupied C4×C4 triple pair has cofactor per2 in {0,1}.
When cofactor=0 the residual ORIGINAL source incidence 2x2 matrix
has a ZERO ROW or ZERO COLUMN (2x2 Hall). Split each rejected mark
equally among ALL zero residual rows and columns, labelled by the
genuine original source factor's physical role P_spoke, P_center,
L_spoke, or L_center. A denominator of 12 is exact (LCM(1,2,3,4)).
Every source W(3,s) matrix is immutable, no source incidence is guessed.

The exact deficit D= (P_spoke+P_center+L_spoke+L_center)/12
is invariant under swapping the ORIGINAL POINT/LINE typed roles.
Combining with AA4-DC: for h>=96, ALL globally complete correlated
original physical pair maps, every halfcut, either
  U_BBo >=s^7/2^17
or one of four fractional original typed source Hall-vacancy classes
  >=s^7/2^18.
This is a scoped PARTIAL obstruction classification: root #230 OPEN.
"""
from collections import Counter
from itertools import combinations

from hyp105_issue230_d6aa4cq_original_macro_path_cut_gate import _validated_original
from hyp105_issue230_d6aa4cr_exact_BBo_three_matching_transfer import (
    c4_completions_from_single_and_doubled,
    original_nonincident_threepath,
    original_dual_model_immutable_source_Q,
)
from hyp105_issue230_d6aa4dc_marked_cofactor_hall_deficit import (
    original_three_by_three_cofactor_certificate,
    allh_original_marked_cofactor_dichotomy_arithmetic,
)

SOURCE_VACANCY_CLASSES = (
    "POINT_other_spoke", "POINT_center", "LINE_other_spoke", "LINE_center"
)
DENOMINATOR = 12


def original_marked_true_source_vacancy_certificate(rows, i, j):
    """Exact four-role ORIGINAL cofactor-failure certificate of ONE marked flag.

    The 3x3 binary matrix rows 0,1=ORIGINAL point physical SPOKES,
    row2=point C4 center; columns analogous ORIGINAL LINE factors.
    """
    c=original_three_by_three_cofactor_certificate(rows)
    B=c["true_original_3x3_binary_rows"]
    if type(i) is not int or type(j) is not int or i not in (0,1) or j not in (0,1):
        raise ValueError("actual ORIGINAL marked incidence must join two physical source SPOKES")
    if B[i][j]!=1:
        raise ValueError("source marked crossing must be a real ORIGINAL incidence flag")
    pr,lc=1-i,1-j
    cofactor=B[pr][lc]*B[2][2]+B[pr][2]*B[2][lc]
    if cofactor>1:
        raise AssertionError("two original matching completions contradict GQ girth8")
    witnesses=()
    if cofactor==0:
        found=[]
        if B[pr][lc]==0 and B[pr][2]==0:found.append("POINT_other_spoke")
        if B[2][lc]==0 and B[2][2]==0:found.append("POINT_center")
        if B[pr][lc]==0 and B[2][lc]==0:found.append("LINE_other_spoke")
        if B[pr][2]==0 and B[2][2]==0:found.append("LINE_center")
        if not found:
            raise AssertionError("2x2 source cofactor zero without an ORIGINAL Hall-vacant row/col")
        witnesses=tuple(found)
    credits={name:(DENOMINATOR//len(witnesses) if name in witnesses else 0)
             for name in SOURCE_VACANCY_CLASSES} if witnesses else {
                 name:0 for name in SOURCE_VACANCY_CLASSES}
    if sum(credits.values())!=DENOMINATOR*(1-cofactor):
        raise AssertionError("original source Hall vacancy fractional partition mismatch")
    return {
        "marked_original_source_incidence":(i,j),
        "source_original_2x2_cofactor":cofactor,
        "original_SOURCE_zero_row_or_column_witnesses":witnesses,
        "dual_symmetric_vacancy_credits_in_twelfths":credits,
        "genuine_original_marked_unextendible":cofactor==0,
        "not_a_historical_original_sixflag_motif_without_matching":True,
    }


def allh_original_vacancy_dichotomy_arithmetic(h):
    """All-h quantitative forced four-way source Hall-vacancy alternative."""
    z=allh_original_marked_cofactor_dichotomy_arithmetic(h)
    s=z["s"]
    if h>=96:
        assert z["allh_gate_h_ge_96"]
        assert (1<<17)==4*(1<<15) and (1<<18)==8*(1<<15)
    return {
        "h":h,"s":s,"V":z["V"],"a":z["a"],"k":z["k"],
        "source_vacancy_class_count":4,
        "source_fractional_Hall_vacancy_common_denominator":DENOMINATOR,
        "allh_marked_original_source_crossflag_mass_floor_numerator":s**7,
        "allh_marked_original_source_crossflag_mass_floor_denominator":1<<15,
        "either_historical_original_BBo_lower_numerator":s**7,
        "either_historical_original_BBo_lower_denominator":1<<17,
        "or_ONE_true_original_vacancy_class_lower_numerator":s**7,
        "or_ONE_true_original_vacancy_class_lower_denominator":1<<18,
        "requires_nontrivial_same_global_map_crossclass_GF5_compensation":True,
        "does_NOT_resolve_root_230":True,
        "allh_gate_h_ge_96":h>=96,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def exact_original_C4_source_vacancy_energy(model, *, anchor_pairs,
                                            point_cut=None,line_cut=None,
                                            max_triples_per_side=None):
    """Finite genuine original C4×C4 marked Hall vacancy energy, fixed f/g.

    Explicit anchor_pairs required to avoid accidentally claiming an
    unbounded W38 ALL-original-BBo census. max_triples_per_side makes
    this only a PARTIAL sample, never a full historical original U.
    """
    s,V,a,f,g,pl,lp=_validated_original(model)
    if anchor_pairs is None:
        raise ValueError("explicit true ORIGINAL source anchor list required")
    def cut(c):
        if c is None:return None
        v=tuple(c)
        if len(set(v))!=len(v) or any(type(x)is not int or not 0<=x<a for x in v):
            raise ValueError("valid unique physical coordinate labels required")
        return frozenset(v)
    X,Y=cut(point_cut),cut(line_cut)
    if max_triples_per_side is not None and (
        type(max_triples_per_side)is not int or max_triples_per_side<1
    ):
        raise ValueError("positive partial source C4 cap required")
    anchors=tuple(tuple(t) for t in anchor_pairs)
    if len(anchors)!=len(set(anchors)):
        raise ValueError("duplicate original nonincident P3")
    for p,l in anchors:
        if (type(p)is not int or type(l)is not int or
            not 0<=p<V or not 0<=l<V or l in pl[p] or
            (X is not None and not set(f[p])<=X) or
            (Y is not None and not set(g[l])<=Y)):
            raise ValueError("genuine original nonincident P3 anchor outside source cut")
    invf={tuple(sorted(e)):i for i,e in enumerate(f)}
    invg={tuple(sorted(e)):i for i,e in enumerate(g)}
    totals=Counter()
    credits=Counter({name:0 for name in SOURCE_VACANCY_CLASSES})
    witness_example={}
    distinct_original_marked_sources=set()
    def order_triple(tr,labels,base):
        spokes=tuple(sorted(t for t in tr if len(set(labels[t])&set(base))==1))
        center=tuple(t for t in tr if not set(labels[t])&set(base))
        if len(spokes)!=2 or len(center)!=1:
            raise AssertionError("not a truly occupied point/line physical C4 original 3-source-factor triple")
        return spokes+center
    for p,l in anchors:
        path=original_nonincident_threepath(p,l,pl,lp)
        q,l0=path[1][0],path[0][1]
        if set(f[p])&set(f[q]) or set(g[l])&set(g[l0]):
            continue
        P=c4_completions_from_single_and_doubled(f[p],f[q],invf,a)
        L=c4_completions_from_single_and_doubled(g[l],g[l0],invg,a)
        if max_triples_per_side is not None:
            P=P[:max_triples_per_side];L=L[:max_triples_per_side]
        for pids in P:
            pp=order_triple(pids,f,f[p])
            for lids in L:
                ll=order_triple(lids,g,g[l])
                B=tuple(tuple(int(j in pl[i]) for j in ll) for i in pp)
                c=original_three_by_three_cofactor_certificate(B)
                totals["actual_occupied_physical_C4_pairs"]+=1
                totals["actual_source_original_3x3_perfect_matchings"]+=c["true_original_3x3_permanent"]
                nmarks=0
                for i in (0,1):
                    for j in (0,1):
                        if not B[i][j]:continue
                        nmarks+=1
                        x=original_marked_true_source_vacancy_certificate(B,i,j)
                        totals["actual_original_source_marked_spoke_crossflag_T"]+=1
                        totals["actual_original_source_extendible_marked_E"]+=x["source_original_2x2_cofactor"]
                        totals["actual_original_source_unextendible_marked_D"]+=(1-x["source_original_2x2_cofactor"])
                        if x["genuine_original_marked_unextendible"]:
                            for typ,value in x["dual_symmetric_vacancy_credits_in_twelfths"].items():
                                credits[typ]+=value
                                if value and typ not in witness_example:
                                    witness_example[typ]=(p,l,pp,ll,B,(i,j),x["original_SOURCE_zero_row_or_column_witnesses"])
                        distinct_original_marked_sources.add((p,l,pp[i],ll[j]))
                if nmarks and not c["true_original_3x3_permanent"]:
                    totals["actual_marked_positive_but_no_source_matching_C4_pairs"]+=1
    T=totals["actual_original_source_marked_spoke_crossflag_T"]
    D=totals["actual_original_source_unextendible_marked_D"]
    E=totals["actual_original_source_extendible_marked_E"]
    U=totals["actual_source_original_3x3_perfect_matchings"]
    if sum(credits.values())!=DENOMINATOR*D or T!=D+E or not U<=E<=2*U:
        raise AssertionError("true ORIGINAL marked SOURCE four-way dual Hall partition failed")
    return {
        "s":s,"V":V,"a":a,
        "actual_original_source_P3_anchors_requested":len(anchors),
        "actual_occupied_source_C4_pairs":totals["actual_occupied_physical_C4_pairs"],
        "actual_original_marked_spoke_incidence_T":T,
        "actual_original_extendible_marked_E":E,
        "actual_original_unextendible_source_cofactor_D":D,
        "actual_historical_original_BBo_sixflag_U":U,
        "actual_original_spoke_marks_without_3matching_pairs":
            totals["actual_marked_positive_but_no_source_matching_C4_pairs"],
        "source_Hall_fractional_vacancy_credits_in_twelfths":
            dict(credits),
        "source_Hall_vacancy_credit_denominator":DENOMINATOR,
        "first_true_original_vacancy_witness_by_type":witness_example,
        "distinct_original_anchored_marked_source_spoke_flags":
            len(distinct_original_marked_sources),
        "quantities_are_partial_if_capped":max_triples_per_side is not None,
        "original_point_LINE_dual_symmetric":True,
        "allh_root_A_B_C_NOT_proven":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }
