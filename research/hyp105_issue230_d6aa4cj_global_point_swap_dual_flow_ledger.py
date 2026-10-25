"""HYP-105 #230 AA4-CJ: one GLOBAL original POINT swap all-seven signed migration.

ALL h>=1 genuine original W(3,2^h), arbitrary complete correlated typed
injections f,g, original six DISTINCT incidence IDs Q. Swap whole physical
POINT-factor images f(p)<->f(q), with original LINE map g UNCHANGED.

If Q has six DISTINCT original POINT factors (POINT-source A):
 * neither p nor q occurs -> SAME seven-GF5 class and eligibility;
 * exactly one occurs -> before/after POINT physical sixvertex-2factor
   eligibility are MUTUALLY EXCLUSIVE (five-common-edge uniqueness);
 * both occur ONCE -> same physical point edge multiset/eligibility;
   right source B/C accepted GF5 tags stay exactly invariant;
   right source A/D6 acceptance BEFORE and AFTER is disjoint, because
   transposing two ORIGINAL incidence-column positions of an aligned
   labeled sixcycle is never an automorphism of that 6cycle.
Consequently exact all-h signed POINT-A original class transfer is
  Delta_A = Delta_exactly_one_all7 + W_D6*(D6_both_gain-D6_both_loss).
No positivity direction is guaranteed.

For ALL original Q (POINT-source A/B/C), if multiplicity of p equals
multiplicity of q, the point physical SIX-edge multiset and eligibility
are invariant, all historical seven accepted class labels except D6
are invariant. Unequal multiplicity is the only remaining general
physical-side change sector. Thus the complete original weighted
seven-GF5 delta has an exact conditional class/sector ledger.

Finite W32 exhaustively enumerates the UNION of all 62370 genuine
original LEFT physically eligible six-ID Q before and after, counts
each unique ORIGINAL six-ID Q once, and tests independent all-seven
historical class transitions. Genuine W34/W38 samples falsify the
all-h POINT-A transition scopes. Not root A/B/C.
"""
from collections import Counter,defaultdict
from itertools import combinations

from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4cg_four_shared_edge_two_completion import (
    classify_seven_all_a_original_Q,
)
from hyp105_issue230_d6aa4ci_dual_cycle_orbit_fiber_invariant import (
    _six_position_dual_cycle, SIX_CYCLE,
)
from hyp105_g5e2b3e1a_fixed_leading import selected_left_six
from hyp105_g5e2b3e1b0_seven_signature import (
    R3_CERTIFIED_FLOORS, classify_seven_prechecked,
)
from hyp105_issue230_projection import fixture

GF5_WEIGHTS=R3_CERTIFIED_FLOORS
TAG_NONE="NONE"


def original_two_point_global_swap(f,p,q):
    """Swap two whole real original POINT physical edge images, never Q images."""
    f=tuple(tuple(sorted(e)) for e in f)
    if (type(p) is not int or type(q) is not int or p==q
            or not 0<=p<len(f) or not 0<=q<len(f)):
        raise ValueError("two different genuine original POINT factor IDs required")
    if any(len(e)!=2 or e[0]==e[1] or min(e)<0 for e in f):
        raise ValueError("simple physical POINT pair-edge images required")
    if len(set(f))!=len(f):
        raise ValueError("entire original POINT image map must be globally injected")
    changed=list(f);changed[p],changed[q]=changed[q],changed[p]
    if set(changed)!=set(f) or len(set(changed))!=len(changed):
        raise AssertionError("original whole POINT swap broke complete-image injection")
    return tuple(changed)


def literal_original_point_six_vertex_2factor(Q,inc,f):
    """An independent raw original-POINT physical degree oracle."""
    deg=Counter(v for j in Q for v in f[inc[j][0]])
    return len(Q)==6 and len(set(Q))==6 and len(deg)==6 and set(deg.values())=={2}


def original_point_source_kind(Q,inc):
    """TRUE original source POINT incidence ID multiplicities, not physical labels."""
    freq=Counter(inc[j][0] for j in Q)
    return {(1,1,1,1,1,1):"A",(1,1,1,1,2):"B",
            (2,2,2):"C"}.get(tuple(sorted(freq.values())))


def _source_sector(mp,mq):
    if mp==mq==0:return "none"
    if mp==mq:return "both_equal"
    return "unequal"


def _A_sector(mp,mq):
    if (mp,mq)==(0,0):return "A_neither"
    if (mp,mq) in ((1,0),(0,1)):return "A_exactly_one"
    if (mp,mq)==(1,1):return "A_both"
    raise AssertionError("POINT source A only permits 0/1 source multiplicities")


def original_true_Q_swap_transition(Q,inc,f,g,p,q):
    """All-h literal two-sided historical original GF5 tag/no-go constraints."""
    Q=tuple(sorted(Q))
    if len(Q)!=6 or len(set(Q))!=6 or any(type(j) is not int or not 0<=j<len(inc) for j in Q):
        raise ValueError("six distinct TRUE original incidence IDs required")
    changed=original_two_point_global_swap(f,p,q)
    freq=Counter(inc[j][0] for j in Q)
    mp,mq=freq[p],freq[q]
    kind=original_point_source_kind(Q,inc)
    old_phys=literal_original_point_six_vertex_2factor(Q,inc,f)
    new_phys=literal_original_point_six_vertex_2factor(Q,inc,changed)
    before=classify_seven_all_a_original_Q(Q,f,g,inc)
    after=classify_seven_all_a_original_Q(Q,changed,g,inc)
    if kind=="A":
        if mp==mq==0 and (old_phys!=new_phys or before!=after):
            raise AssertionError("unaffected original Q changed class")
        if mp+mq==1 and old_phys and new_phys:
            raise AssertionError("five common actual original physical POINT edges cannot have two different valid sixth edges")
        if mp==mq==1:
            if old_phys!=new_phys:
                raise AssertionError("two original POINT-edge swaps must preserve same six-edge physical multiset")
            if before=="D6" and after=="D6":
                raise AssertionError("single physical POINT source-position swap cannot preserve aligned labeled sixcycle D6")
            if before in ("A-left/B-right","C/A") and after!=before:
                raise AssertionError("POINT-A right-B/C historical positive must persist under two present source-factor permutations")
            if after in ("A-left/B-right","C/A") and before!=after:
                raise AssertionError("new POINT-A right-B/C historical positive impossible with identical left physical 2factor")
    if mp==mq:
        if old_phys!=new_phys:
            raise AssertionError("equal source multiplicities under whole-point swap must keep physical 2factor")
        if kind in ("A","B","C") and (before!=after) and (
                before!="D6" and after!="D6"):
            raise AssertionError("only original D6 can change historical class with equal original POINT multiplicities")
    return {"source_point_kind":kind,"source_p_count":mp,"source_q_count":mq,
            "sector":_source_sector(mp,mq),
            "A_sector":_A_sector(mp,mq) if kind=="A" else None,
            "left_physical_before":old_phys,"left_physical_after":new_phys,
            "historical_before":before,"historical_after":after,
            "weighted_before":GF5_WEIGHTS.get(before,0),
            "weighted_after":GF5_WEIGHTS.get(after,0),
            "weighted_delta":GF5_WEIGHTS.get(after,0)-GF5_WEIGHTS.get(before,0)}


def true_original_W32_sevenclass_global_point_swap_ledger(model,p,q):
    """Exhaustive UNIQUE original W32 six-incidence source Q migration.

    Enumerates BOTH actual left physically 2factor candidate domains,
    not just baseline Q (otherwise gains after the swap would be lost).
    The two domains consist of 62370 genuine original Q EACH.
    """
    s,V,a,inc,f,g,_,_=_original_source(model)
    if (s,V,a)!=(2,15,6):
        raise ValueError("full exhaustive original sevenclass oracle W32 only")
    moved=original_two_point_global_swap(f,p,q)
    other=dict(model,left_labels=moved)
    left_base={Q for Q,kind in selected_left_six(model)}
    left_moved={Q for Q,kind in selected_left_six(other)}
    if len(left_base)!=62370 or len(left_moved)!=62370:
        raise AssertionError("W32 original left full sixflag exact census drift")
    universe=left_base|left_moved
    by_sector=Counter()
    by_Asector=Counter()
    old_tags=Counter()
    new_tags=Counter()
    transitions=Counter()
    physical_changes=Counter()
    delta_sectors=Counter()
    delta_Asectors=Counter()
    gain_lost=Counter()
    source_A_count=0
    checked=0
    for Q in universe:
        freq=Counter(inc[j][0] for j in Q)
        mp,mq=freq[p],freq[q]
        sector=_source_sector(mp,mq)
        original_kind=original_point_source_kind(Q,inc)
        pre=classify_seven_prechecked(Q,f,g,inc) if Q in left_base else None
        post=classify_seven_prechecked(Q,moved,g,inc) if Q in left_moved else None
        # Independent generalized historical classifier must agree even
        # for Q with point physics invalid: no fabricated source-ID fixes.
        checked+=1
        actual_before=classify_seven_all_a_original_Q(Q,f,g,inc)
        actual_after=classify_seven_all_a_original_Q(Q,moved,g,inc)
        if (pre,post)!=(actual_before,actual_after):
            raise AssertionError("pinned W32 historical classifier disagrees with independent all-a source-Q oracle")
        if not (pre or post):continue
        source_A_count+=original_kind=="A"
        by_sector[(original_kind,sector)]+=1
        if original_kind=="A":by_Asector[_A_sector(mp,mq)]+=1
        old_tags[pre or TAG_NONE]+=1;new_tags[post or TAG_NONE]+=1
        transitions[(original_kind,sector,pre or TAG_NONE,post or TAG_NONE)]+=1
        physical_changes[(original_kind,sector,Q in left_base,Q in left_moved)]+=1
        delta=GF5_WEIGHTS.get(post,0)-GF5_WEIGHTS.get(pre,0)
        delta_sectors[(original_kind,sector)]+=delta
        if original_kind=="A":
            key=_A_sector(mp,mq)
            delta_Asectors[key]+=delta
            if key=="A_neither" and delta!=0:raise AssertionError("unaffected Q changed weighted")
            if key=="A_both":
                if (pre,post)==("D6","D6"):
                    raise AssertionError("D6 original POINT position transposition unexpectedly preserved right dual")
                if pre in ("A-left/B-right","C/A") and post!=pre or post in ("A-left/B-right","C/A") and pre!=post:
                    raise AssertionError("same source POINT A two-factor stable B/C tag must be invariant")
            if key=="A_exactly_one" and (Q in left_base and Q in left_moved):
                raise AssertionError("one original POINT factor five-common physical edges cannot both complete a 2factor")
        gain_lost[(pre or TAG_NONE,post or TAG_NONE)]+=1
    old_weight=sum(GF5_WEIGHTS.get(k,0)*n for k,n in old_tags.items())
    new_weight=sum(GF5_WEIGHTS.get(k,0)*n for k,n in new_tags.items())
    if new_weight-old_weight!=sum(delta_sectors.values()):
        raise AssertionError("literal all-seven original Q weighted global change != sector migration")
    if delta_Asectors["A_neither"]!=0:
        raise AssertionError("unchanged actual original POINT A source Q produced spurious migration")
    if delta_Asectors["A_both"]%GF5_WEIGHTS["D6"]:
        raise AssertionError("two POINT A factor D6 change not an integer D6 weight")
    return {"s":s,"original_full_left_Q_each":62370,
      "original_union_left_Q_candidates":len(universe),
      "all_seven_original_historical_class_before":dict(old_tags),
      "all_seven_original_historical_class_after":dict(new_tags),
      "global_weighted_all7_before":old_weight,
      "global_weighted_all7_after":new_weight,
      "global_weighted_all7_delta":new_weight-old_weight,
      "source_sector_positive_candidate_counts":dict(by_sector),
      "original_A_sector_positive_candidate_counts":dict(by_Asector),
      "original_A_sector_weighted_delta":dict(delta_Asectors),
      "all_source_sector_weighted_delta":dict(delta_sectors),
      "historical_GF5_migration_by_source_sector":dict(transitions),
      "independent_W32_vs_generalized_classifier_Q_count":checked,
      "physical_membership_ledger":dict(physical_changes),
      "complete_original_f_g_maps_preserved":True,
      "same_original_Q_six_distinct_IDs_on_both_sides":True,
      "root_230":"OPEN_WITH_FORMAL_BLOCKER"}


def original_swap_W34_point_A_fiber_falsifiers(model,points,p,q):
    """True h=2/3 arbitrary original f/g: both-present B/C persist and D6 switch."""
    s,V,a,inc,f,g,_,_=_original_source(model)
    if p not in points or q not in points or p==q:
        raise ValueError("two different POINTs must occur in same real source fiber")
    changed=original_two_point_global_swap(f,p,q)
    if set(f)!=set(changed):
        raise AssertionError("must preserve all complete original physical POINT edges")
    Qs=tuple()
    # source-left A original right-eligible Q independent of the original
    # selected six-point physical source image permutation.
    from hyp105_issue230_d6aa4ci_dual_cycle_orbit_fiber_invariant import original_point_A_fiber
    src=original_point_A_fiber(model,points)
    changes=Counter()
    for Q,typ,cyc in src["eligible_actual_original_Q"]:
        res=original_true_Q_swap_transition(Q,inc,f,g,p,q)
        changes[(res["historical_before"] or TAG_NONE,res["historical_after"] or TAG_NONE)]+=1
    return {"s":s,"right_eligible_original_POINT_A_Q":len(src["eligible_actual_original_Q"]),
            "genuine_original_full_f_swap_class_transitions":dict(changes),
            "right_source_B_C_unchanged":True,
            "full_original_S_s_not_computed":True}
