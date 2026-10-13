"""HYP-105 #230 D6-T: exact GLOBAL permutation-assignment projected-marginal dual.

ALL-h sound theorem, independent of permutation local-search stationarity.
Let all ORIGINAL W(3,s) six-incidence factors be F_Q(f,g)>=0 (seven
GF5-positive indicator or its certified necessary weighted numerator).
Treat each f and g as independent INJECTIVE assignments to the SAME
physical K_a alphabet (their injectivity constraints are per side).
Every factor depends on <=6 left ORIGINAL point vertices and <=6
right ORIGINAL line vertices, retaining original incidence positions.

For each local factor c on r<=12 factor vertices, construct its exact
truth table over ALL locally injective physical assignments on both
sides, with cost F_c. Let b_c=min F_c and
m_(c,i,e)=min{F_c(phi): phi_i=e}. Then FOR EVERY local assignment phi,

  F_c(phi)>=b_c+(1/r)*sum_{i in scope(c)}(m_(c,i,phi_i)-b_c).

Multiply by D=lcm(1..12)=27720. Sum inequalities over ALL actual
ORIGINAL incidence sixset factors. The global injectivity of f and g
implies the sum of sitewise coefficients is >= the minimum-cost
INJECTIVE assignment on each side (rectangular Hungarian):
  min_{f,g} sum_c F_c(f,g)
   >= [D*sum_c b_c + match_min(A_left) + match_min(A_right)]/D.

This is a fully checkable *sufficient* global lower certificate (dual
feasible solution), NOT a proof that it is positive: one-site marginals
can lose genuine higher-order correlated constraints. Truth tables for
the ALL-h original factor system are intentionally not fabricated.
The exact theorem also holds with one side frozen and arbitrary
physical IMAGE E subset on the other side.

FINITE IMPLEMENTATION on TRUE ORIGINAL W(3,2): freeze left f and all
right labels outside a 3-line set T, allow every bijection of the THREE
occupied physical pair labels on T, compile ALL 62370 original left
candidate sixsets into exact D6-P position-aware right cylinders, group
them by right original support intersect T, and build exhaustive
injection truth tables (0/1/2/3 right variables). Solve the exact
suborbit primal and obtain a VERIFIED projected-marginal dual floor,
separately for full seven-S and the certified GF5 necessary NUMERATOR.
This finite 3-line suborbit is NOT the global 15! right orbit and is
not Branch A/B. No W34/W38 complete seven-S is computed.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, permutations, product
from math import factorial, lcm
import json

from hyp105_issue230_d6p_seven_cylinder_swap_audit import (
    SEVEN_CLASSES, R3_CERTIFIED_FLOORS,
    compile_original_W32_cylinders, cylinder_seven_class, cylinder_census,
)
from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import seven_census

DUAL_SCALE=lcm(*range(1,13))
assert DUAL_SCALE==27720


def physical_non_two_regular_star_witness(original_factor_endpoints,a):
    """Construct physical injection forcing a six-incidence side to FAIL.

    Uniform ALL-h lemma: for ANY six ORIGINAL factor endpoint positions
    and a>=6, there exists a locally injective assignment of their
    distinct ORIGINAL factor vertices to physical K_a edges, such that
    the resulting six physical edges (with repeats by ORIGINAL factor
    incidence) do NOT occupy exactly six coordinates each twice.

    If any ORIGINAL factor repeats >=3 times, its edge already forces
    physical coordinate degree >=3 for EVERY injection. Otherwise
    at least three ORIGINAL factor vertices are distinct; assign the
    first three the edges (0,1),(0,2),(0,3), contributing degree>=3
    at coordinate 0, and extend injectively on the other vertices.

    Hence for a fixed SINGLE original vertex physical label on one
    side, the OPPOSITE side may always be chosen to fail. Every
    single-site projection min of each two-sided ORIGINAL GF5-positive
    sixset indicator, and likewise its certified nonnegative GF5
    coefficient, is zero. The unrestricted two-sided degree-one
    projected-marginal dual (as constructed here) is IDENTICALLY ZERO.
    This is an all-h NO-GO for that particular certificate family,
    NOT an all-h counterexample to actual S(f,g)>=c*s**6.
    """
    pts=tuple(original_factor_endpoints)
    if (len(pts)!=6 or type(a) is not int or a<6 or
            any(type(i) is not int or i<0 for i in pts)):
        raise ValueError("requires six ORIGINAL factor endpoints and a>=6")
    ordered=tuple(dict.fromkeys(pts))
    if len(ordered)>len(tuple(combinations(range(a),2))):
        raise AssertionError("original local injection physical K_a too small")
    pairs=tuple(combinations(range(a),2))
    counts=Counter(pts)
    selected={}
    if max(counts.values())<=2:
        if len(ordered)<3:
            raise AssertionError("six positions with multiplicity<=2 require >=3 factors")
        for v,pair in zip(ordered[:3],((0,1),(0,2),(0,3))):
            selected[v]=pair
    remaining=(p for p in pairs if p not in set(selected.values()))
    for orig in ordered:
        if orig not in selected:
            selected[orig]=next(remaining)
    physical=Counter(coord for orig in pts for coord in selected[orig])
    is_2regular=(len(physical)==6 and all(n==2 for n in physical.values()))
    if is_2regular or len(set(selected.values()))!=len(ordered):
        raise AssertionError("star-pattern local GF5 zero oracle failed")
    return {
        "original_distinct_factor_count":len(ordered),
        "physical_factor_pairs":{str(k):list(v) for k,v in selected.items()},
        "physical_degree_multiset":sorted(physical.values(),reverse=True),
        "all_seven_GF5_classes_on_this_side_impossible":True,
        "root_two_sided_single_site_projection_min":"ZERO",
    }


def integer_injective_assignment_min(cost):
    """Exact min-weight rectangular injection; pure integer Hungarian.

    Rows are ORIGINAL factor vertices; columns are available physical
    pairs. No outside optimizer, floating point, or approximation.
    """
    if not isinstance(cost,(list,tuple)):
        raise ValueError("integer rectangular cost matrix required")
    n=len(cost)
    if n==0:
        return 0,()
    if not isinstance(cost[0],(list,tuple)):
        raise ValueError("invalid injection cost row")
    m=len(cost[0])
    if m<n or m==0 or any(
            not isinstance(row,(list,tuple)) or len(row)!=m or
            any(type(v) is not int for v in row)
            for row in cost):
        raise ValueError("require n<=m and exact integer rectangular matrix")
    u=[0]*(n+1);v=[0]*(m+1)
    p=[0]*(m+1);way=[0]*(m+1)
    for i in range(1,n+1):
        p[0]=i
        j0=0
        minv=[None]*(m+1)
        used=[False]*(m+1)
        while True:
            used[j0]=True
            i0=p[j0]
            delta=None
            j1=0
            for j in range(1,m+1):
                if used[j]:
                    continue
                cur=cost[i0-1][j-1]-u[i0]-v[j]
                if minv[j] is None or cur<minv[j]:
                    minv[j]=cur;way[j]=j0
                if delta is None or minv[j]<delta:
                    delta=minv[j];j1=j
            if delta is None:
                raise AssertionError("rectangular assignment augmenting path absent")
            for j in range(m+1):
                if used[j]:
                    u[p[j]]+=delta;v[j]-=delta
                elif minv[j] is not None:
                    minv[j]-=delta
            j0=j1
            if p[j0]==0:
                break
        while True:
            j1=way[j0]
            p[j0]=p[j1]
            j0=j1
            if j0==0:
                break
    assignment=[None]*n
    for j in range(1,m+1):
        if p[j]:
            assignment[p[j]-1]=j-1
    if any(x is None for x in assignment) or len(set(assignment))!=n:
        raise AssertionError("Hungarian did not yield a complete injection")
    total=sum(cost[i][j] for i,j in enumerate(assignment))
    if total!=-v[0]:
        raise AssertionError("exact Hungarian primal/dual potential mismatch")
    return total,tuple(assignment)


def _validate_variables_and_images(variables,images,side):
    if not isinstance(variables,(tuple,list)) or len(set(variables))!=len(variables):
        raise ValueError(f"{side}: distinct ordered ORIGINAL factor variables required")
    if type(images) is not int or images<len(variables):
        raise ValueError(f"{side}: not enough physical images")
    if any(type(z) is not int or z<0 for z in variables):
        raise ValueError(f"{side}: ORIGINAL factor IDs must be nonnegative integers")


def _scope_assignments(images,scope):
    return tuple(permutations(range(images),len(scope)))


def verified_projected_marginal_dual(variables_left,images_left,
                                     variables_right,images_right,factors,
                                     *,max_local_truth_rows=150000):
    """EXACT all-h global assignment dual, if complete local tables supplied.

    factors: list of {'L': ordered tuple of original point IDs,
                     'R': ordered tuple of original line IDs,
                     'costs': {(tuple left_image_indices,
                                tuple right_image_indices): exact nonnegative int}}
    Tables MUST contain every independently locally injective
    assignment into the full domain for each side, no sparse defaults.
    A malicious/incorrect omitted row FAILS CLOSED. A true-original
    all-h proof witness needs additionally attest each cost matches the
    corresponding genuine ORIGINAL incidence sixset GF5-positive event.
    """
    left=tuple(variables_left);right=tuple(variables_right)
    _validate_variables_and_images(left,images_left,"left")
    _validate_variables_and_images(right,images_right,"right")
    if not isinstance(factors,(tuple,list)) or not factors:
        raise ValueError("at least one complete nonnegative local factor table required")
    row_L={a:i for i,a in enumerate(left)}
    row_R={a:i for i,a in enumerate(right)}
    AL=[[0]*images_left for _ in left]
    AR=[[0]*images_right for _ in right]
    intercept=0
    local_floor=0
    rows_verified=0
    local_potential_max=0
    for factor in factors:
        if not isinstance(factor,dict) or set(factor)!={"L","R","costs"}:
            raise ValueError("local factor requires exactly L/R/costs fields")
        L=tuple(factor["L"]);R=tuple(factor["R"])
        if (len(L)!=len(set(L)) or len(R)!=len(set(R)) or
                any(v not in row_L for v in L) or
                any(v not in row_R for v in R) or
                len(L)>6 or len(R)>6):
            raise ValueError("invalid ORIGINAL local scope, max six per side")
        r=len(L)+len(R)
        if r>12:
            raise AssertionError("original GF5 six-incidence factor scope exceeded")
        all_l=_scope_assignments(images_left,L)
        all_r=_scope_assignments(images_right,R)
        count=len(all_l)*len(all_r)
        if count>max_local_truth_rows or rows_verified+count>max_local_truth_rows:
            raise ValueError("local full oracle exceeds explicit computational budget")
        costs=factor["costs"]
        if not isinstance(costs,dict) or len(costs)!=count:
            raise ValueError("incomplete ORIGINAL local injection truth table")
        assignments=[]
        for la in all_l:
            for ra in all_r:
                key=(la,ra)
                if key not in costs or type(costs[key]) is not int or costs[key]<0:
                    raise ValueError("missing or nonintegral/nonpositive local objective cost")
                assignments.append((la,ra,costs[key]))
        if any(k not in {(a,b) for a in all_l for b in all_r}
               for k in costs):
            raise ValueError("local oracle contains illegal/noninjective image assignment")
        rows_verified+=count
        b=min(z for _,_,z in assignments)
        intercept+=DUAL_SCALE*b
        local_floor+=b
        if not r:
            continue
        c_L={v:[None]*images_left for v in L}
        c_R={v:[None]*images_right for v in R}
        for la,ra,z in assignments:
            for i,t in enumerate(L):
                k=la[i];old=c_L[t][k]
                if old is None or z<old:c_L[t][k]=z
            for i,t in enumerate(R):
                k=ra[i];old=c_R[t][k]
                if old is None or z<old:c_R[t][k]:c_R[t][k]=z
        local_coef_L={(t,e):DUAL_SCALE//r*(c_L[t][e]-b)
                      for t in L for e in range(images_left)}
        local_coef_R={(t,e):DUAL_SCALE//r*(c_R[t][e]-b)
                      for t in R for e in range(images_right)}
        if any(z<0 for z in (*local_coef_L.values(),*local_coef_R.values())):
            raise AssertionError("local projection minima below base cost")
        for la,ra,z in assignments:
            bound=DUAL_SCALE*b+sum(local_coef_L[L[i],e]
                       for i,e in enumerate(la))+sum(
                       local_coef_R[R[i],e] for i,e in enumerate(ra))
            if bound>DUAL_SCALE*z:
                raise AssertionError("locally verified projected marginal dual inequality false")
        for (t,e),coef in local_coef_L.items():
            AL[row_L[t]][e]+=coef
            local_potential_max=max(local_potential_max,coef)
        for (t,e),coef in local_coef_R.items():
            AR[row_R[t]][e]+=coef
            local_potential_max=max(local_potential_max,coef)
    hL,assign_L=integer_injective_assignment_min(AL)
    hR,assign_R=integer_injective_assignment_min(AR)
    numerator=intercept+hL+hR
    if numerator<0:
        raise AssertionError("nonnegative costs generated negative certified lower")
    bound=Fraction(numerator,DUAL_SCALE)
    return {
        "scale":DUAL_SCALE,
        "local_factors_verified":len(factors),
        "local_truth_rows_verified":rows_verified,
        "local_independent_minima_sum":local_floor,
        "local_intercept_scaled":intercept,
        "minimum_left_injective_assignment_potential_scaled":hL,
        "minimum_right_injective_assignment_potential_scaled":hR,
        "global_assignment_dual_numerator":numerator,
        "global_assignment_dual_lower":str(bound),
        "global_assignment_dual_integer_floor":(numerator+DUAL_SCALE-1)//DUAL_SCALE,
        "max_single_site_potential_scaled":local_potential_max,
        "minimum_cost_assignment_left":list(assign_L),
        "minimum_cost_assignment_right":list(assign_R),
        "globally_injective_both_factor_sides":"EXACTLY_ENFORCED_IN_ASSIGNMENT_MIN",
        "complete_local_truth_tables_required":True,
        "certificate_for_global_root_positive":"NOT-CLAIMED",
    }


def complete_true_original_W32_three_factor_tables(model,triple):
    """TRUE original 62,370-left-candidate GF5 full seven-S factor tables.

    Freeze f and all right labels OUTSIDE triple. THREE original right
    lines may bijectively reassign the THREE occupied physical pairs
    originally in triple. Every original right cylinder is included,
    including positional D6 and B/B. No other g is admitted; this is
    a finite subgroup orbit of six globally injective complete maps.
    """
    if (len(triple)!=3 or len(set(triple))!=3 or
            any(type(v) is not int or not 0<=v<15 for v in triple)):
        raise ValueError("exactly three distinct genuine W32 original line IDs")
    T=tuple(sorted(triple))
    labels=tuple(model["right_labels"])
    if len(labels)!=15 or len(set(labels))!=15:
        raise ValueError("require genuine W32 complete physical right pair bijection")
    compiled=compile_original_W32_cylinders(model)
    image=tuple(labels[t] for t in T)
    grouped=defaultdict(list)
    for sig,m in compiled["cylinders"].items():
        U=tuple(t for t in T if t in sig[1])
        grouped[U].append((sig,m))
    factors_S=[];factors_GF5=[]
    for U in sorted(grouped,key=lambda q:(len(q),q)):
        local_S={};local_GF5={}
        for assignment in permutations(range(3),len(U)):
            mutable=list(labels)
            for original_id,image_index in zip(U,assignment):
                mutable[original_id]=image[image_index]
            # Other currently duplicated T labels do NOT occur in these
            # cylinders; every injective U assignment extends to a
            # complete globally injective permutation of THREE labels.
            value_S=0
            value_GF5=0
            for sig,m in grouped[U]:
                klass=cylinder_seven_class(sig,mutable)
                if klass:
                    value_S+=m
                    value_GF5+=m*R3_CERTIFIED_FLOORS[klass]
            local_S[((),assignment)]=value_S
            local_GF5[((),assignment)]=value_GF5
        factors_S.append({"L":(),"R":U,"costs":local_S})
        factors_GF5.append({"L":(),"R":U,"costs":local_GF5})
    identity=tuple(range(3))
    baseline_S=sum(factor["costs"][((),tuple(identity[T.index(t)] for t in factor["R"]))]
                   for factor in factors_S)
    baseline_GF5=sum(factor["costs"][((),tuple(identity[T.index(t)] for t in factor["R"]))]
                     for factor in factors_GF5)
    independent=cylinder_census(compiled,labels)
    if (baseline_S!=independent["S_seven"] or
            baseline_GF5!=independent["GF5_seven_lower_numerator"]):
        raise AssertionError("true ORIGINAL W32 original cylinder partition failed")
    return T,labels,image,compiled,factors_S,factors_GF5


def local_factor_objective(factors,triple,assignment):
    mapping={v:assignment[i] for i,v in enumerate(triple)}
    return sum(f["costs"][((),tuple(mapping[v] for v in f["R"]))]
               for f in factors)


def frozen_W32_assignment_dual_report():
    rows=[]
    for scheme,T in (("S68",(3,11,12)),("S72",(1,7,9))):
        model=fixture(1,scheme)
        triple,labels,image,compiled,factors_S,factors_GF5=(
            complete_true_original_W32_three_factor_tables(model,T))
        dual_S=verified_projected_marginal_dual(
            (),0,triple,3,factors_S)
        dual_GF5=verified_projected_marginal_dual(
            (),0,triple,3,factors_GF5)
        permutations_six=list(permutations(range(3)))
        orbit=[]
        for phi in permutations_six:
            changed=list(labels)
            for t,physical_index in zip(triple,phi):
                changed[t]=image[physical_index]
            if len(set(changed))!=15:
                raise AssertionError("invalid genuine W32 complete right injection")
            S=local_factor_objective(factors_S,triple,phi)
            Y=local_factor_objective(factors_GF5,triple,phi)
            actual=cylinder_census(compiled,changed)
            if S!=actual["S_seven"] or Y!=actual["GF5_seven_lower_numerator"]:
                raise AssertionError("global all-seven true W32 local-factor objective false")
            orbit.append({"permutation_image_indices":list(phi),
                          "S_seven":S,
                          "GF5_selected_lower_numerator":Y})
        best=min(orbit,key=lambda row:(row["S_seven"],
            row["permutation_image_indices"]))
        weighted_best=min(orbit,key=lambda row:(
            row["GF5_selected_lower_numerator"],
            row["permutation_image_indices"]))
        primal_min_S=best["S_seven"]
        primal_min_GF5=weighted_best["GF5_selected_lower_numerator"]
        if (Fraction(dual_S["global_assignment_dual_lower"])>primal_min_S or
                Fraction(dual_GF5["global_assignment_dual_lower"])>primal_min_GF5):
            raise AssertionError("certified assignment dual exceeds exact primal")
        baseline=next(v for v in orbit if v["permutation_image_indices"]==[0,1,2])
        old=seven_census(model,independent_checks=False)
        if (baseline["S_seven"]!=old["S_seven"] or
                baseline["GF5_selected_lower_numerator"]!=
                old["GF5_seven_lower_numerator"]):
            raise AssertionError("independent ORIGINAL full-seven GF5 baseline mismatch")
        rows.append({
            "scheme":scheme,
            "original_right_factor_subset":list(triple),
            "true_ORIGINAL_left_sixsets_accounted":compiled["original_left_sixsets"],
            "independent_true_ORIGINAL_seven_GF5_baseline":baseline,
            "six_legal_fixed_IMAGE_three_line_assignments_exhaustively_checked":True,
            "right_suborbit":[*orbit],
            "exact_suborbit_min_S":primal_min_S,
            "exact_suborbit_min_GF5_selected_lower_numerator":primal_min_GF5,
            "exact_best_S_assignment":best,
            "exact_best_weighted_assignment":weighted_best,
            "projected_marginal_global_dual_S":dual_S,
            "projected_marginal_global_dual_GF5":dual_GF5,
            "number_ORIGINAL_right_support_groups":len(factors_S),
            "right_image_outside_three_original_factor_ids":"FROZEN",
            "global_15_factor_right_image_assignment_min":"NOT-COMPUTED",
            "Branch_A":"OPEN","Branch_B":"OPEN",
        })
    return {
        "slice":"HYP105-ISSUE230-D6T-GLOBAL-ASSIGNMENT-DUAL-CERTIFICATE",
        "theorem":"ALL-H-TWO-SIDED-GLOBAL-INJECTION-PROJECTED-MARGINAL-DUAL",
        "all_h_sound_sufficient_dual_for_original_S_and_selected_GF5":True,
        "all_h_full_original_12_local_factor_truth_tables":"NOT-ENUMERATED",
        "W32_only_three_factor_frozen_complement":"EXACT_FINITE_CONTROL",
        "global_all_f_g_theorem_PROVED_A":False,
        "infinite_correlated_counterexample_PROVED_B":False,
        "Branch_A":"OPEN","Branch_B":"OPEN",
        "rows":rows,
    }


if __name__=="__main__":
    print(json.dumps(frozen_W32_assignment_dual_report(),sort_keys=True,indent=2))
