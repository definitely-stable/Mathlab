"""HYP-105 #230 EICE-003-J: TRUE GQ anchor-filtered source-codegrees.

J1 exact all-h row-pair/column-codegree formula for each original
middle incidence e and opposite physical quadrant pair. Reconstructs
actual four GQ anchors on the SAME globally injected source f,g.
J2 five monotone simultaneous four-corner status counts:
true physical I1 source template -> all original endpoints decoded ->
all source endpoints nonincident -> all GQ anchors end-clean ->
all four anchors internally source-blocked.
J3 independently count both same-side and checkerboard masks on genuine
four-blocked source quadruples; verify original GQ 4x4 girth.
J4 all-h conditional heavy-middle anchor-filtered codegree obstruction.

NO universal upper H_e=o(s^4), no original six-incidence GF5
compensation, no Branch A/B, no ASET exponent.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
import json

from hyp105_issue230_endpoint_energy import EndpointEnergy
from hyp105_issue230_quadrant_matching_capacity import (
    OPPOSITE, original_midpoint_quadrants,
    valid_original_two_arm_pairs, exact_local_middle_capacity,
)
from hyp105_issue230_five_source_blocked_search import FiveSourceSearch
from hyp105_issue230_four_anchor_capacity import blocked_checkerboard_or_adjacent
from hyp105_issue230_source_plaquettes import (
    source_girth_four_by_four, status_of_cell,
)

STAGES=("I1_physical_original_five_source_template",
        "J_all_four_original_endpoints_decoded",
        "J_all_four_original_endpoints_nonincident",
        "J_all_four_true_GQ_anchors_end_clean",
        "J_all_four_true_GQ_anchors_internally_blocked")
FILTERS=(
    frozenset(range(5)),
    frozenset((1,2,3,4)),
    frozenset((2,3,4)),
    frozenset((3,4)),
    frozenset((3,)),
)


def independent_original_anchor_status(ctx,e,w,z):
    """Independent direct ORIGINAL source point/line/original-anchor logic.

    Never use the earlier status_of_cell here: intended as a true second
    original-point-line path oracle, not an unsupported GF5 classifier.
    """
    xw,yw=divmod(w,ctx.a)
    xz,yz=divmod(z,ctx.a)
    if xw==xz or yw==yz:
        raise AssertionError("J physical source template not coordinate-proper")
    q=ctx.fi.get((min(xw,xz),max(xw,xz)))
    r=ctx.gi.get((min(yw,yz),max(yw,yz)))
    if q is None or r is None:
        return 0,q,r
    if r in ctx.point_lines[q]:
        return 1,q,r
    if (q,r) not in ctx.anchor:
        raise AssertionError("J true ORIGINAL GQ anchor projection missing")
    ap,al=ctx.anchor[q,r]
    if (set(ctx.f[ap]).intersection(ctx.f[q]) or
            set(ctx.g[al]).intersection(ctx.g[r])):
        return 2,q,r
    mp,ml=ctx.inc[e]
    return (3 if (set(ctx.f[ap]).intersection(ctx.f[mp]) or
                  set(ctx.g[al]).intersection(ctx.g[ml])) else 4),q,r


def two_arm_matching_count(records):
    """Exact number of two-arm pairs with distinct OUTSIDE x and y."""
    if len({r[0] for r in records})!=len(records):
        raise ValueError("distinct true ORIGINAL arm source IDs required")
    if len({(r[1],r[2]) for r in records})!=len(records):
        raise ValueError("distinct original arm physical outer coordinate pairs required")
    n=len(records)
    x=Counter(a[1] for a in records)
    y=Counter(a[2] for a in records)
    return n*(n-1)//2-sum(v*(v-1)//2 for v in x.values())-sum(
        v*(v-1)//2 for v in y.values())


def exact_original_anchor_middle_census(ctx,e, *, max_source_pair_checks=3_000_000,
                                        independent_oracle=True,
                                        max_blocked_expansions=60_000,
                                        retain_allblocked_source_sets=False):
    """All-h exact ORIGINAL five-source template-to-four-anchor cascade.

    A genuine true original source middle e has up to two opposite
    quadrant arm-pair combinations. For each compatible row two-arm
    pair, keep each opposite outer arm with:
      - distinct outside x/y from BOTH rows;
      - both true ORIGINAL cell statuses in a chosen acceptance set.
    The number of valid COLUMN two-arm pairs is the exact typed
    codegree C(k,2)-sum_x C(d_x,2)-sum_y C(d_y,2).

    No physical path is promoted to a positive GF5 original sixset.
    """
    if (type(max_source_pair_checks) is not int or max_source_pair_checks<0
            or type(max_blocked_expansions) is not int or max_blocked_expansions<0):
        raise ValueError("nonnegative exact original source audit budgets required")
    groups=original_midpoint_quadrants(ctx,e)
    stages=[0]*len(STAGES)
    channels=Counter()
    sigs=Counter()
    cross=Counter()
    source_sets=[] if retain_allblocked_source_sets else None
    inspected=0
    allblocked_examined=0
    status_checks=0
    for q0,q1 in OPPOSITE:
        rows=groups[q0]
        cols=groups[q1]
        # Pair count independent of source-specific blocker status.
        row_pairs=valid_original_two_arm_pairs(rows)
        pre=(two_arm_matching_count(rows)*
             two_arm_matching_count(cols))
        if len(row_pairs)!=two_arm_matching_count(rows):
            raise AssertionError("J row-pair exact matching formula inconsistent")
        sum_physical_before=stages[0]
        cache={}
        for pair in row_pairs:
            # pair stores (two ORIGINAL source IDs, two partner x, two partner y)
            rowids,rx,ry=pair
            actual_rows=[next(a for a in rows if a[0]==sid) for sid in rowids]
            eligible_columns=[]
            for arm in cols:
                inspected+=1
                if inspected>max_source_pair_checks:
                    raise ValueError("J exact original source pair-candidate budget exceeded")
                if arm[1] in rx or arm[2] in ry:
                    continue
                # Real physical endpoint of each true original diagonal,
                # at opposite physical corners of the central middle.
                end_col=arm[1]*ctx.a+arm[2]
                entry=[]
                for row in actual_rows:
                    key=(row[0],arm[0])
                    if key not in cache:
                        start_row=row[1]*ctx.a+row[2]
                        original=status_of_cell(ctx,e,start_row,end_col)
                        status_checks+=1
                        if independent_oracle and original!=independent_original_anchor_status(
                                ctx,e,start_row,end_col):
                            raise AssertionError("J independent TRUE original anchor status mismatch")
                        cache[key]=original
                    entry.append(cache[key])
                eligible_columns.append((arm,tuple(entry)))
            # For each progressively stronger 4-corner true source condition
            # filter opposite arm records whose BOTH corners satisfy it.
            for k,accepted in enumerate(FILTERS):
                eligible=[arm for arm,s in eligible_columns
                          if s[0][0] in accepted and s[1][0] in accepted]
                got=two_arm_matching_count(eligible)
                stages[k]+=got
            # Only here enumerate actual all-four-true-internal blocker
            # SOURCE templates to audit 3^4 typed masks/GQ girth.
            blocked=[(arm,ss) for arm,ss in eligible_columns
                     if ss[0][0]==3 and ss[1][0]==3]
            for (a,sta),(b,stb) in combinations(blocked,2):
                if a[1]==b[1] or a[2]==b[2]:
                    continue
                allblocked_examined+=1
                if allblocked_examined>max_blocked_expansions:
                    raise ValueError("J complete true four-anchor expansion budget exceeded")
                original_ids=tuple(sorted((e,rowids[0],rowids[1],a[0],b[0])))
                if len(set(original_ids))!=5:
                    raise AssertionError("J true original 5-ID distinctness failed")
                # Direct actual source q/r projections, one for each of
                # the four ORIGINAL physical path endpoint corners.
                xpoints=(sta[0][1],stb[0][1],sta[1][1],stb[1][1])
                rlines=(sta[0][2],stb[0][2],sta[1][2],stb[1][2])
                source_girth_four_by_four(xpoints,rlines,ctx.edge_id)
                cross[sum((q,r) in ctx.edge_id for q in xpoints
                           for r in rlines)]+=1
                mp,ml=ctx.inc[e]
                mask=[]
                for q,r in zip(xpoints,rlines):
                    ap,al=ctx.anchor[q,r]
                    mask.append(int(bool(set(ctx.f[ap])&set(ctx.f[mp])))+
                                2*int(bool(set(ctx.g[al])&set(ctx.g[ml]))))
                cls=blocked_checkerboard_or_adjacent(tuple(mask))
                channels["strict_checkerboard" if cls["strict_checkerboard"]
                         else "adjacent_common_side"]+=1
                sigs[cls["signature"]]+=1
                if source_sets is not None:
                    source_sets.append(original_ids)
        if stages[0]-sum_physical_before>pre:
            raise AssertionError("J physical status stage exceeds I2 pre-cross source capacity")
    if not all(stages[i]>=stages[i+1] for i in range(len(stages)-1)):
        raise AssertionError("J true original source anchor filtering is nonmonotone")
    if stages[-1]!=sum(channels.values()) or stages[-1]!=allblocked_examined:
        raise AssertionError("J allblocked direct true GQ expansion != pair-codegree count")
    if source_sets is not None and len(set(source_sets))!=len(source_sets):
        raise AssertionError("J I3 unique original middle source template failed")
    return {
        "true_original_middle_source":e,
        "stage_names":STAGES,
        "cumulative_all_four_corner_source_counts":tuple(stages),
        "first_failed_source_filter_counts":tuple(
            stages[i]-stages[i+1] for i in range(len(stages)-1)),
        "true_original_4x4_cross_incidence_histogram_allblocked":
            dict(sorted(cross.items())),
        "all_four_blocker_L_R_B_signature_counts":dict(sorted(sigs.items())),
        "all_four_blocker_channels":dict(sorted(channels.items())),
        "source_pair_arm_checks":inspected,
        "true_original_endpoint_anchor_status_oracle_checks":status_checks,
        "I2_source_template_equivalence_checked":True,
        "J_true_source_codegree_formula_exact":True,
        "allblocked_true_original_five_source_ids":tuple(source_sets) if source_sets is not None else None,
        "positive_GF5_accepted_seven_family_transfer_proved":False,
        "uniform_o_s4_four_anchor_capacity_proved":False,
        "root_Branch_A_proved":False,
    }


def finite_original_anchor_cascade_report(model, *,
                                          max_pairs=3_000_000,
                                          full_independent_global=True):
    """Exhaustive source middle census; optional second full physical oracle."""
    ctx=EndpointEnergy(model)
    stage=[0]*len(STAGES)
    max_stages=[0]*len(STAGES)
    channels=Counter()
    sigs=Counter()
    cross=Counter()
    checksum=Counter()
    mask_usable=0
    total_status_oracle=0
    budget=0
    all_sets=set()
    for e in range(ctx.N):
        report=exact_original_anchor_middle_census(
            ctx,e,max_source_pair_checks=max_pairs,
            independent_oracle=True,retain_allblocked_source_sets=True)
        counts=report["cumulative_all_four_corner_source_counts"]
        for i,v in enumerate(counts):
            stage[i]+=v
            max_stages[i]=max(max_stages[i],v)
        channels.update(report["all_four_blocker_channels"])
        sigs.update(report["all_four_blocker_L_R_B_signature_counts"])
        cross.update(report["true_original_4x4_cross_incidence_histogram_allblocked"])
        checksum[e]=counts[-1]
        budget+=report["source_pair_arm_checks"]
        total_status_oracle+=report["true_original_endpoint_anchor_status_oracle_checks"]
        for ids in report["allblocked_true_original_five_source_ids"]:
            if ids in all_sets:
                raise AssertionError("J duplicate original blocked five-family among middle sources")
            all_sets.add(ids)
    if len(all_sets)!=stage[-1]:
        raise AssertionError("J allblocked original five-source families lost")
    physical_comparison=None
    if full_independent_global:
        physical=FiveSourceSearch(model).census(
            export_true_five_source_families=True)
        if physical["locally_coherent_allfour_original_plaquettes"]!=2*stage[-1]:
            raise AssertionError("J original 5-source blocker count != physical paired directed G search")
        if physical["distinct_original_five_incidence_blocked_source_families"]!=stage[-1]:
            raise AssertionError("J exact true blocker family cardinality != independent original G search")
        if (physical["locally_coherent_blocking_channels"].get("checkerboard",0)
                !=2*channels["strict_checkerboard"] or
            physical["locally_coherent_blocking_channels"].get("adjacent_common_side",0)
                !=2*channels["adjacent_common_side"]):
            raise AssertionError("J true original blocker-mask categories != independent G search")
        physical_comparison="independent complete ORIGINAL G full physical NB3 oracle verified"
    return {
        "status":"RESTRICTED_THEOREM_J",
        "s":ctx.s,"a":ctx.a,"N":ctx.N,
        "true_original_middle_source_ids_exhausted":ctx.N,
        "stage_names":STAGES,
        "all_original_source_stage_totals":dict(zip(STAGES,stage)),
        "largest_true_middle_stage_counts":dict(zip(STAGES,max_stages)),
        "first_failed_source_filter_counts":dict(zip(STAGES[:-1],
                 (stage[i]-stage[i+1] for i in range(len(stage)-1)))),
        "original_allblocked_five_source_family_count":stage[-1],
        "allblocked_original_GQ_4x4_cross_histogram":dict(sorted(cross.items())),
        "original_blocker_mask_channels":dict(sorted(channels.items())),
        "original_blocker_mask_signatures":dict(sorted(sigs.items())),
        "top_10_original_middle_source_blocker_load":checksum.most_common(10),
        "total_true_original_source_pair_arm_checks":budget,
        "independent_true_original_anchor_status_checks":total_status_oracle,
        "full_independent_G_source_crosscheck":physical_comparison,
        "o_s4_real_source_capacity_proved":False,
        "original_GF5_positive_sixset_transfer_proved":False,
        "root_Branch_A_proved":False,
    }


def report():
    from hyp105_issue230_projection import fixture
    out=[]
    for scheme in ("lex","reverse","S68","S72"):
        data=finite_original_anchor_cascade_report(fixture(1,scheme))
        data["scheme"]=scheme
        out.append(data)
    for scheme in ("lex","random"):
        data=finite_original_anchor_cascade_report(fixture(2,scheme))
        data["scheme"]=scheme
        out.append(data)
    return {"status":"RESTRICTED_THEOREM_J","root_A":"OPEN","maps":out}


if __name__=="__main__":
    print(json.dumps(report(),indent=2,sort_keys=True))
