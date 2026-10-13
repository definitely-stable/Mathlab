"""HYP-105 issue #230 D5: all-h RETENTION-ROBUST original endpoint energy.

Given the D4 genuine symplectic spread globally injective point map f, for
ANY globally injective ORIGINAL line pair map g and ANY simple physical
subgraph H <= G:
   W_H = sum_z deg_Bbad(z)*deg_H(z)
       >= s*sum_(i,x) T_H(i,x)^2
       >= s/(g0*a)*max(0,2*g0*k*s-R)^2
where k=t(s+1), g0=floor(a/4), t=floor((a-g0)/(2(s+1))),
R=#physical edges deleted from G to H, and T_H counts retained physical
edges from original point--line incidences p--r with p on a selected
spread line in physical anchor group i and r not the selected line.

If R=o(s4), this is >=(9/32+o(1))*s6. In particular unconditional
all-map W_H=o(s5.9) is FALSE for ANY 1-o(1)-edge-retaining pruning
including the type asserted in PR #394.

This refutes ONLY a sufficient AUXILIARY lemma, not the original
S_s(f,g)=Omega(s6), not any S-conditioned charging, and not Branch B.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
import json

from hyp105_issue230_proof_audit import _model
from hyp105_issue230_projection import ProjectionClosure
from hyp105_issue230_d4_spread_pencil_falsifier import (
    actual_original_symplectic_spread,balanced_right_labels,plan,
)
from hyp105_issue230_endpoint_mixedbook_d2 import _chord_ledger


def true_spread_global_model(power, right_mode="balanced"):
    """Independent reconstruction of D4's FULL ORIGINAL f and a free g."""
    if power not in (2,3) or right_mode not in ("balanced","reverse"):
        raise ValueError("real true original finite instances GF4/GF8; g balanced or reverse")
    (field,points,lines,incidences),spread,_=actual_original_symplectic_spread(power)
    s=field.q
    spec=plan(s)
    a=spec["a"]; V=spec["V"]
    g0=spec["anchor_coordinates"]
    t=spec["spread_lines_per_anchor"]
    selected=spread[:g0*t]
    left=[None]*V
    group_for_point={}
    for i in range(g0):
        lineids=selected[i*t:(i+1)*t]
        original_group_points=[p for l in lineids for p in lines[l]]
        if len(set(original_group_points))!=t*(s+1):
            raise AssertionError("not a genuine original disjoint spread")
        for j,p in enumerate(original_group_points):
            if left[p] is not None:
                raise AssertionError("two spread point groups overlap")
            left[p]=(i,g0+j)
            group_for_point[p]=(i,lineids[j//(s+1)])
    used=set(e for e in left if e is not None)
    if len(used)!=g0*t*(s+1):
        raise AssertionError("original selected global labels not injective")
    remaining=iter(e for e in combinations(range(a),2) if e not in used)
    for p in range(V):
        if left[p] is None:
            left[p]=next(remaining)
    if len(set(left))!=V:
        raise AssertionError("complete original f not globally injective")
    right=balanced_right_labels(s,a)
    if right_mode=="reverse":
        right=right[::-1]
    model=_model(s,points,lines,incidences,left,right)
    return model,selected,group_for_point,spec


def _edge_tuple(x,y):
    return (x,y) if x<y else (y,x)


def selected_anchor_edge_oracle(core,selected,group_for_point,spec):
    """Identify TRUE physical edges for each ORIGINAL selected p--r, r != L_p.

    For f(p)=(i,j), g(r)=(x,y) an actual original incidence contributes
    two real physical edges (i,x)--(j,y), (i,y)--(j,x).
    Exactly ONE endpoint of each is an anchor-i grid vertex.
    """
    a=core.a
    full_edges={_edge_tuple(v,w) for v,neighbors in enumerate(core.adj)
                for w,_ in neighbors}
    selected_edges={}
    for p,(i,original_spread_line) in group_for_point.items():
        if core.f[p][0]!=i or core.f[p][1]<spec["anchor_coordinates"]:
            raise AssertionError("selected ORIGINAL physical f-label malformed")
        j=core.f[p][1]
        for r in core.point_lines[p]:
            if r==original_spread_line:
                continue
            x,y=core.g[r]
            for first,other in ((x,y),(y,x)):
                v0=i*a+first
                v1=j*a+other
                edge=_edge_tuple(v0,v1)
                if edge not in full_edges:
                    raise AssertionError("selected original p--r diagonal missing from G")
                if edge in selected_edges:
                    raise AssertionError("distinct ORIGINAL incidences collided as physical edges")
                selected_edges[edge]=(i,first,p,r,original_spread_line)
    expected=2*spec["anchor_coordinates"]*spec["spread_lines_per_anchor"]*(core.s+1)*core.s
    if len(selected_edges)!=expected:
        raise AssertionError("original selected nonspread incidence edge identity")
    if len(full_edges)!=2*core.v*core.delta:
        raise AssertionError("the complete original physical graph has m=2VDelta edges")
    return full_edges,selected_edges


def retained_original_energy(model,selected,group_for_point,spec,
                             *,deleted_edges=(),assert_new_oracle=True):
    """Exact bad-chord energy and independently double-counted lower witness."""
    core=ProjectionClosure(model)
    full,selected_edges=selected_anchor_edge_oracle(
        core,selected,group_for_point,spec)
    removed=set(_edge_tuple(u,v) for u,v in deleted_edges)
    if len(removed)!=len(tuple(deleted_edges)) or not removed<=full:
        raise ValueError("deleted edges must be distinct TRUE ORIGINAL physical edges")
    adj=[set(v for v,_ in nbrs) for nbrs in core.adj]
    for u,v in removed:
        adj[u].remove(v)
        adj[v].remove(u)
    # Build sparse retained selected incidences from ORIGINAL p--r, and
    # their full-graph counterparts independently of D2's bad-chord code.
    g0,a=spec["anchor_coordinates"],core.a
    Tfull=[[0]*a for _ in range(g0)]
    Tkept=[[0]*a for _ in range(g0)]
    for edge,(i,x,_,_,_) in selected_edges.items():
        Tfull[i][x]+=1
        if edge not in removed:
            Tkept[i][x]+=1
    total_full=sum(map(sum,Tfull))
    total_ret=sum(map(sum,Tkept))
    if total_full!=len(selected_edges) or total_ret!=total_full-len(removed&set(selected_edges)):
        raise AssertionError("selected original half-edge mass not preserved")
    if total_ret<total_full-len(removed):
        raise AssertionError("all deleted G edges may remove at most one selected witness edge")
    # Each selected spread q on L excluding p yields one ORIGINAL
    # GQ nonincident q--L--p--r. For every x in g(r), Bbad(i,x)
    # includes at least s such q, hence Bbad(i,x)>=s*Tfull(i,x).
    led=_chord_ledger(core,adj)
    D=led["Hdeg"]
    B=led["Bdeg"]
    for i in range(g0):
        for x in range(a):
            z=i*a+x
            if B[z]<core.s*Tfull[i][x]:
                raise AssertionError("genuine ORIGINAL nonincident projection bad-chord lower fails")
            if D[z]<Tkept[i][x]:
                raise AssertionError("retained selected ORIGINAL physical incidences not present in H")
    quadratic=sum(k*k for row in Tkept for k in row)
    actual_W=led["W"]
    first=core.s*quadratic
    if actual_W<first:
        raise AssertionError("direct original bad-chord weighted energy below selected T² lower")
    if g0*a*quadratic<total_ret**2:
        raise AssertionError("finite integer Cauchy on rectangular witness T")
    if not (total_full>=len(removed)):
        guaranteed_mass=0
    else:
        guaranteed_mass=total_full-len(removed)
    robust=Fraction(core.s*guaranteed_mass**2,g0*a)
    refined=Fraction(core.s*total_ret**2,g0*a)
    if actual_W<refined or refined<robust:
        raise AssertionError("arbitrary-retention robust original endpoint-energy theorem falsified")
    full_floor=Fraction(core.s*total_full**2,g0*a)
    if len(removed)==0 and robust!=full_floor:
        raise AssertionError("full original G bound not exact symbolic value")
    if assert_new_oracle and len(removed)==0:
        # Independently enumerate original bad endpoint energies via D3
        # for the exact SAME global true original f,g.
        from hyp105_issue230_d3_double_centered_energy import double_centered_energy
        d3=double_centered_energy(model)
        if d3["physical_full_G_endpoint_energy_W"]!=actual_W:
            raise AssertionError("independent FULL G original D3 signed energy disagrees")
    return {
        "s":core.s,"a":a,
        "same_global_original_pair_injections":True,
        "selected_original_spread_lines":len(selected),
        "selected_original_points":len(group_for_point),
        "selected_nonspread_TRUE_physical_edges":total_full,
        "selected_kept_TRUE_physical_edges":total_ret,
        "all_original_G_physical_edges":len(full),
        "arbitrarily_deleted_TRUE_physical_edges":len(removed),
        "removed_selected_true_physical_edges":total_full-total_ret,
        "selected_original_anchor_cells":g0*a,
        "T_squared_original_selected_retained":quadratic,
        "exact_original_bad_chord_energy_W_H":actual_W,
        "first_true_original_projection_lower_s_times_Tsq":first,
        "refined_retained_lower_num":refined.numerator,
        "refined_retained_lower_den":refined.denominator,
        "robust_removed_edges_lower_num":robust.numerator,
        "robust_removed_edges_lower_den":robust.denominator,
        "full_graph_retention_free_lower_num":full_floor.numerator,
        "full_graph_retention_free_lower_den":full_floor.denominator,
        "all_original_graph_and_GQ_projections_verified":True,
        "universal_all_h_WH_little_o_s59over10":"FALSE for (1-o(1)) edge-retaining H",
        "universal_S_six_positive_lower_proved":False,
        "infinite_small_S_Branch_B_proved":False,
    }


def finite_fixture(power,mode="balanced",delete_every=None,adversarial=False):
    model,selected,group,spec=true_spread_global_model(power,mode)
    core=ProjectionClosure(model)
    full,select_edges=selected_anchor_edge_oracle(core,selected,group,spec)
    if delete_every is not None and adversarial:
        raise ValueError("select at most one deletion policy")
    if delete_every is not None:
        if not isinstance(delete_every,int) or delete_every<2:
            raise ValueError("deletion period integer >=2")
        deleted=tuple(edge for j,edge in enumerate(sorted(full))
                      if j%delete_every==0)
    elif adversarial:
        # Target selected anchor edges FIRST; finite destructive stress.
        # Even this cannot break the robust inequality.
        deleted=tuple(sorted(select_edges)[:max(1,len(select_edges)//5)])
    else:
        deleted=()
    x=retained_original_energy(model,selected,group,spec,
                               deleted_edges=deleted,
                               assert_new_oracle=not deleted)
    x["right_global_original_label_mode"]=mode
    x["physical_edge_removal_scheme"]=(
        "adversarial-original-selected" if adversarial else
        ("every-"+str(delete_every) if delete_every else "none"))
    return x


def report():
    instances=[
        finite_fixture(2,"balanced"),
        finite_fixture(2,"reverse"),
        finite_fixture(2,"balanced",delete_every=19),
        finite_fixture(2,"balanced",adversarial=True),
        finite_fixture(3,"balanced"),
        finite_fixture(3,"reverse"),
        finite_fixture(3,"balanced",delete_every=19),
        finite_fixture(3,"balanced",adversarial=True),
    ]
    symbolic=[plan(2**h) for h in range(4,11)]
    return {
        "slice":"HYP105-ISSUE230-D5-RETENTION-ROBUST-ORIGINAL-ENDPOINT-ENERGY",
        "all_h_exact_theorem":"WH>=s/(g0*a)*max(0,2*g0*t*(s+1)*s-R)^2",
        "all_h_asymptotic_retained_fraction":"R=o(s4) implies WH>=(9/32+o(1))*s6",
        "all_h_unconditional_D2_D3_WH_little_o_s59over10":"FALSE",
        "all_h_original_seven_family_S_lower":"OPEN",
        "all_h_small_S_branch_B":"OPEN",
        "adversarial_all_maps_counterexample_to_original_root":False,
        "real_true_original_witnesses":instances,
        "all_h_arithmetic_only":symbolic,
    }


if __name__=="__main__":
    print(json.dumps(report(),sort_keys=True,indent=2))
