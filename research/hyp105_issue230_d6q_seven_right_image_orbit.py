"""HYP-105 #230 D6-Q: all-seven exact right-IMAGE permutation-orbit transfer.

THEOREM (all finite h, genuine ORIGINAL W(3,s), any complete f,g):
Fix f and the IMAGE E={g(l) : l ORIGINAL right line} ⊆ E(K_a)
of a complete injective right pair-labeling. Draw a uniform bijection
from the V ORIGINAL right lines to the V physical pair edges of E.
This is the permutation orbit of g, NOT uniform all injections unless
E=E(K_a). For a right ORIGINAL six-incidence multiplicity profile
A=(1^6), B=(2,1^4), C=(2^3), the exact probability of right physical
six-coordinate 2-regularity, respectively, is
  p_A(E) = 6! * F_A(E) / (V)_6,
  p_B(E) = 4! * F_B(E) / (V)_5,
  p_C(E) = 3! * F_C(E) / (V)_3,
where F_A counts six-EDGE 2-factors, F_B counts one physical repeated
edge plus a vertex-disjoint C4 (5 distinct physical edges), and F_C
counts three vertex-disjoint physical pair edges. For left connected
A/A column-dual C6 alignment D6, separately:
  p_D(E) = 12 * F_C6(E) / (V)_6,
where F_C6 counts undirected physical six-cycles of E. A disconnected
left A-column-dual NEVER contributes to D6.

Consequently the expected positive counts of EACH of all seven
GF5-certified ORIGINAL sixset classes are explicit linear functionals
of the ORIGINAL incidence-cylinder weights from D6-P. The expected
selected necessary GF5 R3 floor numerator is their frozen-weighted sum.
No independence, random right IMAGE, full R3 upper, or all-g minimum.

ROBUSTNESS THEOREM for ANY E of size V=binom(a,2)-m:
  F_X(E) >= F_X(K_a) - m * (e_X F_X(K_a)/binom(a,2)),
  e_A=6,e_B=5,e_C=3,e_C6=6.
This is exact union-bound deletion counting, the per-edge template
incidence being integral by K_a symmetry. Complete counts are
  F_A(K_a)=70*C(a,6); F_B(K_a)=45*C(a,6);
  F_C(K_a)=15*C(a,6); F_C6(K_a)=60*C(a,6).
For minimal a and s=2^h, h>=1, 6m/K<1 (s=2: m=0;
s>=4: a>=14 and m<=a-2). Thus EACH physical right template family
survives every admissible right image E. In particular p_A(E)>0.

For any fixed f,E, since (K)_6/(V)_6>=1,
p_A(E) >= (1-6m/K)*p_A(K_a).
Coupled to the previously accepted D6-M uniform all-f lower for
B-left/A-right plus C-left/A-right, this gives the exact image-robust
conditional right-orbit EXPECTATION lower
  E_{g' with im(g')=E} S_seven(f,g')
    >= (1-6m/K) * L_BC(s),
where L_BC(s) is the accepted full-completion uniform first-moment
bound ~ (455/3)s^6. It is NOT a bound on any specific right g.

The executable original sixset census is limited to true W(3,2).
An optional right-physical IMAGE template census supports modest a;
never fabricate W(3,4)/W(3,8) seven-class ORIGINAL S.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import comb, factorial
import json

from hyp105_issue230_d6p_seven_cylinder_swap_audit import (
    compile_original_W32_cylinders, cylinder_census, SEVEN_CLASSES,
)
from hyp105_issue230_d6m_gq_collinearity_ca_transfer import (
    universal_fixed_left_CA_expectation,
)
from hyp105_g5e2b3e1b0_seven_signature import (
    R3_CERTIFIED_FLOORS, seven_census,
)
from hyp105_issue230_projection import fixture


KINDS=("A","B","C")
RIGHT_PROFILE={
    (1,1,1,1,1,1):"A",
    (2,1,1,1,1):"B",
    (2,2,2):"C",
}
TEMPLATE_EDGES={"A":6,"B":5,"C":3,"D6":6}
TEMPLATE_COMPLETE_FACTORS={"A":70,"B":45,"C":15,"D6":60}
ORBIT_ASSIGNMENTS={"A":factorial(6),"B":factorial(4),
                   "C":factorial(3),"D6":12}
ORBIT_DISTINCT_RIGHT_LINES={"A":6,"B":5,"C":3,"D6":6}


def falling(n,k):
    if type(n) is not int or type(k) is not int or not 0<=k<=n:
        raise ValueError("invalid falling factorial")
    value=1
    for i in range(k):
        value*=n-i
    return value


def original_w3_parameters(s):
    if type(s) is not int or s<2 or s&(s-1):
        raise ValueError("requires original GQ s=2^h, h>=1")
    V=(s+1)*(s*s+1)
    a=6
    while comb(a,2)<V:
        a+=1
    K=comb(a,2)
    m=K-V
    if not (V>=15 and 0<=m<a-1):
        raise AssertionError("minimal physical pair alphabet inconsistent")
    return {"s":s,"V":V,"a":a,"K":K,"missing_pair_edges":m}


def complete_physical_template_counts(a):
    if type(a) is not int or a<6:
        raise ValueError("physical alphabet a>=6 required")
    six=comb(a,6)
    return {kind:multiplicity*six for kind,multiplicity
            in TEMPLATE_COMPLETE_FACTORS.items()}


@lru_cache(maxsize=1)
def _local_template_edge_masks():
    """Independent unweighted physical right graph shapes on canonical K6."""
    coords=tuple(range(6))
    pairs=tuple(combinations(coords,2))
    A=[]
    D=[]
    for ix in combinations(range(15),6):
        edges=tuple(pairs[i] for i in ix)
        deg=Counter(v for edge in edges for v in edge)
        if len(deg)!=6 or set(deg.values())!={2}:
            continue
        mask=sum(1<<i for i in ix)
        A.append(mask)
        adj={v:set() for v in coords}
        for u,v in edges:
            adj[u].add(v);adj[v].add(u)
        visited={0}
        stack=[0]
        while stack:
            for v in adj[stack.pop()]:
                if v not in visited:
                    visited.add(v);stack.append(v)
        if len(visited)==6:
            D.append(mask)
    B=[]
    for rep_idx,repeated in enumerate(pairs):
        rest=tuple(v for v in coords if v not in repeated)
        other=tuple(i for i,pair in enumerate(pairs)
                    if pair[0] in rest and pair[1] in rest)
        for selected in combinations(other,4):
            deg=Counter(v for i in selected for v in pairs[i])
            if len(deg)==4 and all(deg[v]==2 for v in rest):
                B.append((1<<rep_idx)|sum(1<<i for i in selected))
    C=[]
    for selected in combinations(range(15),3):
        deg=Counter(v for i in selected for v in pairs[i])
        if len(deg)==6 and set(deg.values())=={1}:
            C.append(sum(1<<i for i in selected))
    result={"A":tuple(A),"B":tuple(B),"C":tuple(C),"D6":tuple(D)}
    if (any(len(set(masks))!=len(masks) for masks in result.values()) or
            {k:len(v) for k,v in result.items()}!=
            {"A":70,"B":45,"C":15,"D6":60}):
        raise AssertionError("canonical six-coordinate physical templates invalid")
    return result


def image_physical_template_census(a, physical_edges, *, max_six_coordinate_sets=5000):
    """Exact physical-mask template counts for a moderate fixed IMAGE E.

    This counts shapes in E; it never enumerates original GQ sixsets.
    More than max_six_coordinate_sets rejects rather than fakes high h.
    """
    if type(a) is not int or a<6:
        raise ValueError("a>=6 required")
    pairs={tuple(edge) for edge in physical_edges}
    legal=set(combinations(range(a),2))
    if any(edge not in legal for edge in pairs):
        raise ValueError("original right IMAGE requires canonical physical pairs")
    if len(pairs)<6:
        raise ValueError("at least six physical pair edges required")
    if comb(a,6)>max_six_coordinate_sets:
        raise ValueError("large image physical census exceeds explicit budget")
    masks=_local_template_edge_masks()
    counts=Counter()
    for six in combinations(range(a),6):
        local_pairs=tuple(combinations(six,2))
        available_mask=sum(1<<j for j,e in enumerate(local_pairs) if e in pairs)
        for kind,patterns in masks.items():
            counts[kind]+=sum(
                (available_mask & mask)==mask for mask in patterns)
    return {kind:counts[kind] for kind in TEMPLATE_EDGES}


def deletion_template_bounds(a,V):
    """Sharp per-missing-edge union bound on every physical template shape."""
    K=comb(a,2)
    if type(V) is not int or V<6 or V>K:
        raise ValueError("right IMAGE size must satisfy 6<=V<=K")
    m=K-V
    full=complete_physical_template_counts(a)
    per_edge={}
    lower={}
    for kind,count in full.items():
        edges=TEMPLATE_EDGES[kind]
        incidences=edges*count
        if incidences%K:
            raise AssertionError("K_a edge symmetry template incidence not integral")
        per_edge[kind]=incidences//K
        lower[kind]=max(0,count-m*per_edge[kind])
    return {
        "a":a,"K":K,"V_image_edges":V,"missing_pair_edges":m,
        "complete_templates":full,
        "per_single_missing_edge_templates":per_edge,
        "guaranteed_surviving_templates":lower,
    }


def right_image_orbit_probabilities(a,V,template_counts):
    """Exact orbit of all V! label bijections on a FIXED physical image E."""
    K=comb(a,2)
    if type(V) is not int or not 6<=V<=K:
        raise ValueError("right image must be a legal V-edge injection")
    full=complete_physical_template_counts(a)
    if set(template_counts)!=set(full):
        raise ValueError("exact four physical template families required")
    out={}
    for kind in TEMPLATE_EDGES:
        n=template_counts[kind]
        if type(n) is not int or not 0<=n<=full[kind]:
            raise ValueError("invalid physical template count")
        p=Fraction(ORBIT_ASSIGNMENTS[kind]*n,
                   falling(V,ORBIT_DISTINCT_RIGHT_LINES[kind]))
        if not 0<=p<=1:
            raise AssertionError("physical probability outside [0,1]")
        out[kind]=p
    if out["D6"]>out["A"]:
        raise AssertionError("aligned D6 event must be subset of right A")
    return out


def _original_profile_for_cylinder(signature):
    left,lines,left_dual,repeated_left=signature
    if left not in KINDS or len(lines)!=6:
        raise ValueError("invalid original incidence right cylinder")
    right=RIGHT_PROFILE.get(tuple(sorted(Counter(lines).values(),reverse=True)))
    if right is None:
        return None
    if (left,right)==("B","A"):
        return "B-left/A-right","A"
    if (left,right)==("A","B"):
        return "A-left/B-right","B"
    if {left,right}=={"A","C"}:
        return "C/A",right
    if {left,right}=={"B","C"}:
        return "C/B",right
    if (left,right)==("B","B"):
        repeated=[l for l,v in Counter(lines).items() if v==2]
        if len(repeated)!=1 or len(repeated_left)!=2:
            raise AssertionError("repeated original incidence position malformed")
        rr={i for i,l in enumerate(lines) if l==repeated[0]}
        hit=len(rr.intersection(repeated_left))
        if hit not in (0,1):
            raise AssertionError("original simple GQ forbids BB repeated double incidence")
        return ("B/B-overlap" if hit else "B/B-disjoint"),"B"
    if (left,right)==("A","A") and left_dual:
        return "D6","D6"
    return None


def fixed_f_right_image_exact_expectation(compiled,probabilities,
                                          right_labels):
    """Exact 7-class conditional E over permutations of one complete g IMAGE."""
    for kind in TEMPLATE_EDGES:
        if kind not in probabilities or not isinstance(probabilities[kind],Fraction):
            raise ValueError("missing exact rational shape probabilities")
    V=compiled["original_lines"]
    labels=tuple(tuple(e) for e in right_labels)
    if (len(labels)!=V or len(set(labels))!=V or
            any(e not in set(combinations(range(compiled["a"]),2))
                for e in labels)):
        raise ValueError("must provide globally injective canonical right labels")
    source=compiled["cylinders"]
    accepted_profile_original=Counter()
    rejected_original=0
    for sig,multiplicity in source.items():
        if type(multiplicity) is not int or multiplicity<=0:
            raise ValueError("original cylinders require positive integer weights")
        profile=_original_profile_for_cylinder(sig)
        if profile is None:
            rejected_original+=multiplicity
        else:
            accepted_profile_original[profile]+=multiplicity
    if rejected_original+sum(accepted_profile_original.values())!=compiled[
            "original_left_sixsets"]:
        raise AssertionError("original sixset profile partition lost mass")
    mean={t:Fraction() for t in SEVEN_CLASSES}
    for (klass,right_pattern),n in accepted_profile_original.items():
        mean[klass]+=n*probabilities[right_pattern]
    expected_total=sum(mean.values(),Fraction())
    expected_weighted=sum(
        mean[t]*R3_CERTIFIED_FLOORS[t] for t in SEVEN_CLASSES)
    actual=cylinder_census(compiled,labels)
    actual_counts=actual["seven_class_motif_counts"]
    discrepancy={t:Fraction(actual_counts[t])-mean[t] for t in SEVEN_CLASSES}
    if (sum(discrepancy.values(),Fraction())!=
            Fraction(actual["S_seven"])-expected_total or
            sum(R3_CERTIFIED_FLOORS[t]*discrepancy[t]
                for t in SEVEN_CLASSES)!=
            Fraction(actual["GF5_seven_lower_numerator"])-expected_weighted):
        raise AssertionError("seven-class exact right-orbit deficit mismatch")
    return {
        "a":compiled["a"],"V":V,
        "original_left_candidates":compiled["original_left_sixsets"],
        "profile_eligible_original_sixsets":sum(accepted_profile_original.values()),
        "profile_ineligible_original_sixsets":rejected_original,
        "profile_counts_by_GF5_class_and_original_right_type":{
            k[0]+"/R"+k[1]:v
            for k,v in sorted(accepted_profile_original.items())
        },
        "exact_right_image_orbit_shape_probabilities":{
            k:str(v) for k,v in probabilities.items()},
        "expected_seven_class_counts":{t:str(mean[t]) for t in SEVEN_CLASSES},
        "expected_all_seven_S":str(expected_total),
        "expected_GF5_seven_selected_lower_numerator":str(expected_weighted),
        "expected_GF5_seven_selected_R3_lower":str(
            expected_weighted/(51**6)),
        "fixed_actual_seven_class_counts":actual_counts,
        "fixed_actual_S_seven":actual["S_seven"],
        "fixed_actual_GF5_seven_selected_lower_numerator":
            actual["GF5_seven_lower_numerator"],
        "actual_minus_image_orbit_mean_by_class":{
            t:str(discrepancy[t]) for t in SEVEN_CLASSES},
        "actual_minus_image_orbit_mean_S":str(
            Fraction(actual["S_seven"])-expected_total),
        "actual_minus_image_orbit_mean_GF5_lower_numerator":str(
            Fraction(actual["GF5_seven_lower_numerator"])-expected_weighted),
        "right_orbit_fixed_IMAGE_not_unconditional_completion":True,
        "conditional_expectation_not_all_g_lower":True,
        "Branch_A":"OPEN","Branch_B":"OPEN",
    }


def original_all_h_image_robust_certificate(s):
    """All-h UNIFORM fixed-right-IMAGE conditional MEAN floor, not inf_g."""
    params=original_w3_parameters(s)
    bounds=deletion_template_bounds(params["a"],params["V"])
    K,V,m=params["K"],params["V"],params["missing_pair_edges"]
    frac=Fraction(6*m,K)
    if not frac<1:
        raise AssertionError("minimal a original W3s should keep all shapes robust")
    shape_lower=right_image_orbit_probabilities(
        params["a"],V,bounds["guaranteed_surviving_templates"])
    shape_complete=right_image_orbit_probabilities(
        params["a"],K,bounds["complete_templates"])
    if any(p<=0 for p in shape_lower.values()):
        raise AssertionError("every exact physical template shape survives deletions")
    robust_A=(1-frac)*shape_complete["A"]
    if shape_lower["A"]<robust_A:
        raise AssertionError("fixed IMAGE right-A orbit probability lower violated")
    old=universal_fixed_left_CA_expectation(s)
    old_BC=Fraction(old["new_joint_disjoint_BA_plus_CA_expected_lower"])
    lower=old_BC*(1-frac)
    return {
        "s":s,"a":params["a"],"V":V,"K":K,"missing_pair_edges":m,
        "six_edge_template_deletion_fraction":str(frac),
        "all_admissible_right_images_have_all_four_template_families":True,
        "physical_template_deletion_lower_counts":
            bounds["guaranteed_surviving_templates"],
        "fixed_IMAGE_orbit_probability_lower":{
            k:str(p) for k,p in shape_lower.items()},
        "unconditional_injection_probability":{
            k:str(p) for k,p in shape_complete.items()},
        "prior_all_left_full_completion_BA_CA_mean_floor":str(old_BC),
        "new_all_f_all_IMAGE_permutation_orbit_S_mean_floor":str(lower),
        "new_mean_floor_over_s6":str(lower/Fraction(s**6)),
        "limit_asymptotic_mean_floor_coefficient":"455/3",
        "uniform_for_every_right_IMAGE_of_size_V":True,
        "NOT_a_bound_on_each_fixed_right_injection":True,
        "NOT_complete_W34_W38_original_seven_S":True,
        "Branch_A":"OPEN","Branch_B":"OPEN",
    }


def real_original_W32_full_seven_orbit_report():
    records=[]
    s=2
    params=original_w3_parameters(s)
    if (params["a"],params["V"],params["K"],params["missing_pair_edges"])!=(
            6,15,15,0):
        raise AssertionError("true W32 physical complete pair bijection changed")
    probs=right_image_orbit_probabilities(
        6,15,complete_physical_template_counts(6))
    for scheme in ("lex","reverse","S68","S72"):
        model=fixture(1,scheme)
        compiled=compile_original_W32_cylinders(model)
        physical=image_physical_template_census(6,model["right_labels"])
        if physical!=complete_physical_template_counts(6):
            raise AssertionError("W32 right physical edge IMAGE is complete K6")
        row=fixed_f_right_image_exact_expectation(
            compiled,probs,model["right_labels"])
        independent=seven_census(model,independent_checks=False)
        if (row["fixed_actual_seven_class_counts"] !=
                independent["seven_class_motif_counts"] or
                row["fixed_actual_S_seven"]!=independent["S_seven"] or
                row["fixed_actual_GF5_seven_selected_lower_numerator"]!=
                independent["GF5_seven_lower_numerator"]):
            raise AssertionError("true original W32 seven-GF5 oracle discrepancy")
        row["scheme"]=scheme
        records.append(row)
    if not (records[0]["expected_seven_class_counts"]==
            records[1]["expected_seven_class_counts"] and
            records[2]["expected_seven_class_counts"]==
            records[3]["expected_seven_class_counts"]):
        raise AssertionError("same fixed left f must have same random right mean")
    return {
        "slice":"HYP105-ISSUE230-D6Q-EXACT-ALL-SEVEN-FIXED-IMAGE-ORBIT",
        "theorem":"EXACT-ALL-H-FIXED-RIGHT-IMAGE-ORBIT-SEVEN-CLASS-FIRST-MOMENT",
        "right_IMAGE_fixed_not_uniformly_resampled":True,
        "all_h_nontrivial_uniform_IMAGE_robust_MEAN_floor":True,
        "complete_W34_W38_ORIGINAL_seven_S":"NOT-CLAIMED",
        "Branch_A":"OPEN","Branch_B":"OPEN",
        "original_W32_rows":records,
        "all_h_uniform_right_IMAGE_bounds":[
            original_all_h_image_robust_certificate(s)
            for s in (2,4,8)
        ]
    }


if __name__=="__main__":
    print(json.dumps(real_original_W32_full_seven_orbit_report(),
                     indent=2,sort_keys=True))
