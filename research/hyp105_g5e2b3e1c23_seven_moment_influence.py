"""HYP-105 C23: exact all-h seven-class common-right means and swap influence.

All-h two structural theorems, with actual W(3,2) and W(3,4) physical
target finite enumerators. NO adversarial all-g S lower / ASET theorem.

(1) For ANY original six-incidence source J whose ORIGINAL right line
multiplicities are A=(1^6), B=(2,1^4), or C=(2^3), and ONE COMMON
uniformly random bijection g from all V original lines onto occupied F_R:
  * A-right physical simple six-edge 2factor probability:
      6! T_A(F_R) / (V)_6;
  * B-right physical doubled-edge-plus-C4:
      4! T_B(F_R) / (V)_5;
  * C-right physical three doubled matching edges:
      3! T_C(F_R) / (V)_3;
  * Strict D6 left C6, original right A:
      12 C6(F_R) / (V)_6.
T_A,T_B,T_C count different physical six-coordinate 2factor
MULTISETS (A simple / B one doubled edge / C three doubled edges).
For C/A and C/B accepted classes use each original right profile's
correct probability. A common g is shared for every J; expectation
uses LINEARITY and NOT independence.
Weighted original sixsets are counted exactly once.

(2) All-h one GLOBAL right line transposition changes S_seven only
on original sixsets touching either line. A FULL physical K_a has 130
physical six-edge 2factor multisets per six-coordinate subset:
  A:70, B:45, C:15.
Each fixed physical pair edge occurs once in 40 of these multisets
and twice in six: 28 simple+12 B-square =40; 3 B-double+3 C=6.
For each fixed original incidence (p,l), max selected original sixsets
= C(a-2,4)*(40*Delta^5 + 6*(Delta-1)*Delta^4).
A right GQ line touches Delta original incidences; union over two:
   abs(delta S_seven) <=
      2*C(a-2,4)*(46*Delta^6 - 6*Delta^5).
This is O(s^12), far too weak for any positive all-g Omega(s^6).
The exact same support bound times the maximum class weight bounds
absolute change in the accepted GF5 NECESSARY numerator, not R3 total.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb, factorial, perm

from hyp105_g5e2b3e1a_fixed_leading import PAIRS
from hyp105_g5e2b3e1b0_seven_signature import R3_CERTIFIED_FLOORS
from hyp105_g5e2b3e1c20_global_left_c6 import (
    all_h_global_left_c6_lower)
from hyp105_g5e2b3e1c22_joint_seven_tensor import (
    compile_original_W32_joint_source)

TAGS=tuple(R3_CERTIFIED_FLOORS)
PROFILES=("A","B","C")


def six_coordinate_multifactor_templates():
    """Independent exact 130 unlabeled K6 edge-multiset physical shapes."""
    physical=tuple(combinations(range(6),2))
    simple=[]
    for choices in combinations(physical,6):
        degrees=Counter(u for e in choices for u in e)
        if len(degrees)==6 and set(degrees.values())=={2}:
            simple.append(tuple(choices))
    square=[]
    for doubled in physical:
        rest=tuple(i for i in range(6) if i not in doubled)
        for cycle in combinations(tuple(combinations(rest,2)),4):
            d=Counter(u for e in cycle for u in e)
            if len(d)==4 and set(d.values())=={2}:
                square.append((doubled,doubled,*cycle))
    matching=[]
    for triplet in combinations(physical,3):
        if len(set(x for e in triplet for x in e))==6:
            matching.append(tuple(e for edge in triplet for e in (edge,edge)))
    if tuple(map(len,(simple,square,matching)))!=(70,45,15):
        raise AssertionError("K6 130 2factor multigraphs not decomposed")
    def canonical(es):
        return tuple(sorted(es))
    classes={"A":tuple(canonical(es) for es in simple),
             "B":tuple(canonical(es) for es in square),
             "C":tuple(canonical(es) for es in matching)}
    for x in classes.values():
        if len(set(x))!=len(x):
            raise AssertionError("physically distinct multiset source duplicated")
    return classes


def local_pair_template_incidence_census():
    """Independent per-pair exact singleton/double counts in all K6 130."""
    templates=six_coordinate_multifactor_templates()
    counts=Counter()
    for pair in PAIRS:
        for kind,tups in templates.items():
            for edges in tups:
                mult=edges.count(pair)
                if mult:
                    counts[(kind,mult)]+=1
    # Each value counts 15 possible physical pair positions across K6.
    expected={("A",1):15*28,("B",1):15*12,
              ("B",2):15*3,("C",2):15*3}
    if counts!=expected:
        raise AssertionError("40 singleton/6 double 2factor edge incidences changed")
    return {"total_K6_physical_twofactor_multisets":130,
            "A_simple":70,"B_one_doubled_plus_C4":45,
            "C_three_doubled_matching":15,
            "per_fixed_physical_pair_singleton":40,
            "per_fixed_physical_pair_doubled":6,
            "all_h_constant_by_embedding_in_each_six_coordinate_subset":True}


def all_h_seven_global_right_swap_influence_upper(s):
    """Safe all-h S and accepted GF5 NECESSARY numerator Lipschitz bounds."""
    info=all_h_global_left_c6_lower(s)
    a=info["minimal_physical_coordinates"]
    d=s+1
    # Count left candidate upper over complete physical palette.
    all_left=comb(a,6)*(70*d**6 +
        45*comb(d,2)*d**4 + 15*comb(d,2)**3)
    # Fixed original edge (p,l) occupies physical f(p); the two
    # multiplicity cases may involve additional ORIGINAL incidences
    # at p but never independent physical labels for them.
    one_incidence=comb(a-2,4)*(40*d**5+6*(d-1)*d**4)
    one_line=d*one_incidence
    two_line=2*one_line
    upper=min(two_line,all_left)
    return {
        "s":s, "Delta":d, "a":a,
        "complete_physical_alphabet_all_left_source_upper":all_left,
        "one_fixed_original_incidence_source_touched_upper":one_incidence,
        "one_original_right_line_source_touched_upper":one_line,
        "two_swapped_original_right_lines_source_touched_upper":two_line,
        "abs_global_right_swap_S_seven_delta_upper":upper,
        "max_accepted_GF5_seven_necessary_numerator_weight":
            max(R3_CERTIFIED_FLOORS.values()),
        "abs_global_right_swap_GF5_seven_necessary_numerator_delta_upper":
            upper*max(R3_CERTIFIED_FLOORS.values()),
        "upper_growth_not_asymptotic_positive_lower":"O(s^12)",
        "not_all_g_seven_lower":True,
    }


def physical_right_shape_counts(physical_coordinates, occupied_edges,
                                *,max_six_coordinate_subsets=3003):
    """Exact K_a occupied physical 2factor target census; capped oracle.

    Works for s2 complete K6 or s4 85/91 physical occupancy, and
    arbitrary missing-edge selections. ALL-h formulas do not rely
    on doing an exponential large-s source enumeration.
    """
    a=physical_coordinates
    if type(a) is not int or a<6:
        raise ValueError("physical alphabet coordinate count must be >=6")
    if (type(max_six_coordinate_subsets) is not int
            or max_six_coordinate_subsets<1
            or comb(a,6)>max_six_coordinate_subsets):
        raise ValueError("exact occupied physical target census exceeds host cap")
    edges=tuple(tuple(e) for e in occupied_edges)
    if (len(set(edges))!=len(edges) or
            any(len(e)!=2 or type(e[0]) is not int or
                type(e[1]) is not int or not 0<=e[0]<e[1]<a for e in edges)):
        raise ValueError("physical occupied edges must be distinct canonical pairs")
    occupied=set(edges)
    templates=six_coordinate_multifactor_templates()
    per_profile=Counter()
    c6=0
    for six in combinations(range(a),6):
        for kind,tups in templates.items():
            for template in tups:
                if not all((six[u],six[v]) in occupied for u,v in template):
                    continue
                per_profile[kind]+=1
                if kind=="A":
                    # A simple 6-edge 2factor: six-cycle iff 6 vertex
                    # physical graph is connected, else two C3.
                    adj=[set() for _ in six]
                    for u,v in template:
                        adj[u].add(v)
                        adj[v].add(u)
                    seen={0}
                    stack=[0]
                    while stack:
                        for v in adj[stack.pop()]:
                            if v not in seen:
                                seen.add(v)
                                stack.append(v)
                    if len(seen)==6:
                        c6+=1
    if c6>per_profile["A"]:
        raise AssertionError("strict C6 count exceeds simple physical 2factors")
    return {"a":a,"occupied_physical_pair_labels":len(occupied),
            "T_A_simple":per_profile["A"],
            "T_B_one_double_C4":per_profile["B"],
            "T_C_three_doubled_matching":per_profile["C"],
            "C6_simple":c6,
            "physical_templates_each_6set":(70,45,15),
            "capped_finite_oracle_not_needed_for_all_h_identity":True}


def exact_original_W32_static_seven_source():
    """One 62370 ORIGINAL six-incidence GQ census, static in global f."""
    data=compile_original_W32_joint_source()
    counts=Counter()
    for tag,lines,dual,mult in data["records"]:
        x=Counter(lines)
        profile=tuple(sorted(x.values(),reverse=True))
        kind=({(1,1,1,1,1,1):"A",(2,1,1,1,1):"B",
               (2,2,2):"C"}).get(profile)
        if kind is None or tag not in TAGS or mult<=0:
            raise AssertionError("invalid true original right multiplicity source")
        if tag=="D6" and kind!="A":
            raise AssertionError("strict D6 must have six original right lines")
        counts[(tag,kind)]+=mult
    if sum(counts.values())!=data["eligible_original_sixsets"]:
        raise AssertionError("GQ source category/original multiplicity dropped")
    return {"original_six_incidence_source":data["full_actual_original_sixsets"],
            "eligible_six_incidence_source":data["eligible_original_sixsets"],
            "source_by_seven_class_and_original_right_multiplicity":dict(counts)}


def expected_common_global_right_seven_from_source(
        V, source_by_tag_rightkind, physical_target):
    """EXACT seven-class mean for EVERY f and ONE SHARED uniform global g.

    All-h identity, for arbitrary legal physical occupied right pair
    alphabet F_R and correct static original incidence source counts.
    Caller must supply source counts from true ORIGINAL GQ J, not
    independence-generated labels or signed flow samples.
    """
    if type(V) is not int or V<6:
        raise ValueError("V must be >=6 original right factor lines")
    if physical_target["occupied_physical_pair_labels"] != V:
        raise ValueError("right occupied physical alphabet size must equal V")
    a=physical_target["T_A_simple"]
    b=physical_target["T_B_one_double_C4"]
    c=physical_target["T_C_three_doubled_matching"]
    n6=physical_target["C6_simple"]
    if any(type(x) is not int or x<0 for x in (a,b,c,n6)):
        raise ValueError("nonnegative integer physical target counts required")
    if 12*n6>perm(V,6):
        raise AssertionError("strict D6 probability exceeds one")
    p={
        "A":Fraction(factorial(6)*a,perm(V,6)),
        "B":Fraction(factorial(4)*b,perm(V,5)),
        "C":Fraction(factorial(3)*c,perm(V,3)),
        "D6":Fraction(12*n6,perm(V,6)),
    }
    if any(x>1 for x in p.values()):
        raise AssertionError("physical target profile probability >1")
    counts={t:Fraction(0) for t in TAGS}
    for (tag,right_kind),source in source_by_tag_rightkind.items():
        if tag not in TAGS or right_kind not in PROFILES or (
                type(source) is not int or source<0):
            raise ValueError("invalid ORIGINAL six-incidence source profile")
        if tag=="D6" and right_kind!="A":
            raise ValueError("D6 requires six distinct original right lines")
        prob=p["D6"] if tag=="D6" else p[right_kind]
        counts[tag]+=source*prob
    expected_S=sum(counts.values(),Fraction(0))
    gf5_num=sum((counts[tag]*weight for tag,weight
                 in R3_CERTIFIED_FLOORS.items()),Fraction(0))
    return {
        "V":V,
        "probabilities_by_original_right_profile":
            {k:str(v) for k,v in p.items()},
        "expected_seven_by_class":{k:str(counts[k]) for k in TAGS},
        "one_common_uniform_global_right_expected_seven_S":str(expected_S),
        "one_common_uniform_global_right_GF5_necessary_numerator_mean":
            str(gf5_num),
        "one_common_global_g_linearity_not_witness_independence":True,
        "not_adversarial_seven_minimum":True,
        "not_full_GF5_R3":True,
    }


def genuine_W32_C23_report():
    static=exact_original_W32_static_seven_source()
    targets=physical_right_shape_counts(6,PAIRS)
    result=expected_common_global_right_seven_from_source(
        15,static["source_by_seven_class_and_original_right_multiplicity"],
        targets)
    from hyp105_g5e2b3e1c21_global_right_transfer import (
        all_h_joint_uniform_right_seven_mean_lower)
    previous=all_h_joint_uniform_right_seven_mean_lower(2)
    if (Fraction(result["one_common_uniform_global_right_expected_seven_S"]) <
            Fraction(previous["same_global_random_g_disjoint_seven_classes_mean_lower"])):
        raise AssertionError("full seven exact mean below accepted C21 subclass floor")
    return {
        "scope":"TRUE_ORIGINAL_W32_S2_FULL_SEVEN_SHARED_UNIFORM_GLOBAL_RIGHT",
        "source":{k:({str(pair):val for pair,val in v.items()}
                     if isinstance(v,dict) else v) for k,v in static.items()},
        "physical_target":targets,
        "exact_mean":result,
        "C21_BA_plus_D6_uniform_lower":
            previous["same_global_random_g_disjoint_seven_classes_mean_lower"],
        "all_h_swap_influence":
            [all_h_seven_global_right_swap_influence_upper(s)
             for s in (2,4,8,16,32,64,128)],
        "not_all_g_positive_lower":True,
    }


if __name__=="__main__":
    import json
    print(json.dumps(genuine_W32_C23_report(),sort_keys=True,indent=2))
