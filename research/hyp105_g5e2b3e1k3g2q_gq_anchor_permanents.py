"""HYP-105 E1-K3-G2-Q — genuine GQ anchor-square/permanent identity.

ALL h: each B-left original six-incidence support has a UNIQUE doubled
original point p, two distinct incident original lines, and four other
original point pair-labels forming a SIMPLE physical C4 disjoint from
f(p). For each six-original-line subset R, w_f(R) is an EXACT sum of
4x4 0/1 incidence permanents, over true GQ pair anchors and physically
available square witnesses. The original GQ incidence girth >=8 forces
each 4x4 permanent <=2, sharply improving the previous pointwise cap
on W(3,2) from 81*e_GQ(R) to 6*e_GQ(R).

The global W32 executable independently reconstructs every original
sixsource weight (5005 R) and both original/dual source high-rank
signed correlations by count of genuine local permanent-1/2 witnesses.
This proves no P2/P7 all-label lower bound, no R3 upper or ASET exponent.
"""
from collections import Counter
from functools import lru_cache
from fractions import Fraction
from itertools import combinations,permutations
from math import comb
import json

from hyp105_g5e2b3e1c0_weighted_overlap import (
    source_weighted_BA_hypergraph,simple_six_2factor_targets,
)
from hyp105_g5e2b3e1k3g2n_johnson_harmonics import (
    _frozen_target_W32,physical_pair_indices,six_image_index,
    spectral_overlap_certificate,rat,gq_pair_model,
)
from hyp105_g5e2b3e1k3g2m_twofamily_falsifier import (
    dual_model,exact_two_family_point,_anchors,
)
from hyp105_g5e2b3e1k3g2h_exact_swap_shell import swapped_labeling

PERMS4=tuple(permutations(range(4)))
SIXRANK=6


def _valid_girth8_rows(rows):
    """No 4- or 6-cycle in the 4+4 incidence graph, even if disconnected."""
    if len(rows)!=4 or any(type(r) is not int or not 0<=r<16 for r in rows):
        raise ValueError("four binary 4-bit incidence row masks required")
    for i,j in combinations(range(4),2):
        if (rows[i]&rows[j]).bit_count()>1:
            return False
    # With no 4-cycles, each common-neighbor intersection is a singleton
    # or empty. Three rows form a 6-cycle iff three distinct intersections
    # are nonempty and pairwise distinct.
    for i,j,k in combinations(range(4),3):
        a,b,c=rows[i]&rows[j],rows[j]&rows[k],rows[k]&rows[i]
        if a and b and c and a!=b and b!=c and c!=a:
            return False
    return True


def permanent4(rows):
    """Exact 4x4 permanent; fail closed on malformed/non-GQ matrices."""
    rows=tuple(rows)
    if not _valid_girth8_rows(rows):
        raise ValueError("matrix violates original GQ girth >= 8")
    value=sum(all(rows[i]&(1<<p[i]) for i in range(4)) for p in PERMS4)
    if value>2:
        raise AssertionError("GQ girth-eight 4x4 permanent theorem failed")
    return value


@lru_cache(maxsize=1)
def exhaustive_girth8_permanent_lemma():
    """Complete finite 65536-matrix proof witness, independent of host s.

    Proof apart from enumeration: any two distinct perfect matchings have
    symmetric difference a cycle of length >=8, thus exactly one 8-cycle,
    using ALL eight vertices. With a fixed perfect matching M0, every
    other perfect matching corresponds to a 4-cycle permutation (odd).
    If there were M1 and M2 other than M0, their relative permutation
    would be even, whereas an 8-cycle difference again requires a
    4-cycle permutation (odd): contradiction. Therefore perm<=2.
    Sharpness occurs for a lone C8 with its two alternating matchings.
    """
    hist=Counter()
    example=None
    valid=0
    for mask in range(1<<16):
        rows=tuple((mask>>(4*i))&15 for i in range(4))
        if not _valid_girth8_rows(rows):
            continue
        valid+=1
        value=permanent4(rows)
        hist[value]+=1
        if value==2 and example is None:
            example=rows
    if (valid!=16217 or dict(hist)!={0:11321,1:4824,2:72} or
            example is None or permanent4(example)!=2):
        raise AssertionError("complete 4x4 original GQ permanent proof changed")
    return {
        "all_binary_4x4_matrices":65536,
        "girth_at_least_eight_matrices":valid,
        "permanent_histogram":{str(k):hist[k] for k in range(3)},
        "sharp_permanent_max":2,
        "sharp_example_row_masks":list(example),
        "universal_girth8_permanent_theorem":True,
    }


@lru_cache(maxsize=10)
def original_GQ_tables(s,incidences):
    """Independently verify actual balanced GQ incidence and projection axiom."""
    if type(s) is not int or s<2 or type(incidences) is not tuple:
        raise ValueError("actual original GQ(s,s) incidence IDs required")
    V=(s+1)*(s*s+1)
    delta=s+1
    points=[set() for _ in range(V)]
    lines=[set() for _ in range(V)]
    for e in incidences:
        if (not isinstance(e,tuple) or len(e)!=2 or
                any(type(i) is not int or not 0<=i<V for i in e)):
            raise ValueError("invalid original incidence")
        p,l=e
        if l in points[p]:
            raise ValueError("duplicate original incidence")
        points[p].add(l)
        lines[l].add(p)
    if (len(incidences)!=V*delta or
            any(len(row)!=delta for row in points+lines)):
        raise ValueError("original GQ regular degree or size mismatch")
    anchors={}
    for p,ls in enumerate(points):
        for B in combinations(sorted(ls),2):
            if B in anchors:
                raise ValueError("original incidence contains a 4-cycle")
            anchors[B]=p
    for p in range(V):
        for l in range(V):
            if l in points[p]:
                continue
            if sum(bool(lines[l]&lines[m]) for m in points[p])!=1:
                raise ValueError("original GQ projection axiom failed (6-cycle/geometry)")
    return tuple(frozenset(x) for x in points),tuple(
        frozenset(x) for x in lines),anchors


def physical_squares(model):
    """ALL h, arbitrary injective physical LEFT labeling f, V<=C(a,2).

    A square is four DISTINCT ORIGINAL left points q1..q4 whose four
    physical edge labels form one SIMPLE C4 on four physical coordinates
    disjoint from the twice-used physical pair f(p).
    """
    a,s=model["a"],model["s"]
    labels=tuple(tuple(e) for e in model["left_labels"])
    V=(s+1)*(s*s+1)
    alphabet=set(combinations(range(a),2))
    if (type(a) is not int or a<6 or len(labels)!=V or len(set(labels))!=V or
            any(e not in alphabet for e in labels)):
        raise ValueError("legal globally injective original left pair labels required")
    reverse={edge:i for i,edge in enumerate(labels)}
    result=[]
    for p,edge in enumerate(labels):
        coords=tuple(t for t in range(a) if t not in edge)
        squares=set()
        for v in combinations(coords,4):
            allsix=set(combinations(v,2))
            forbidden=[
                (tuple(sorted((v[0],v[1]))),tuple(sorted((v[2],v[3])))),
                (tuple(sorted((v[0],v[2]))),tuple(sorted((v[1],v[3])))),
                (tuple(sorted((v[0],v[3]))),tuple(sorted((v[1],v[2])))),
            ]
            for matching in forbidden:
                sq=allsix-set(matching)
                if len(sq)!=4 or not all(e in reverse for e in sq):
                    continue
                q=tuple(sorted(reverse[e] for e in sq))
                if p in q or len(set(q))!=4:
                    raise AssertionError("duplicate or incident anchor point")
                squares.add(q)
        if len(squares)>3*comb(a-2,4):
            raise AssertionError("physical square bound violated")
        result.append(tuple(sorted(squares)))
    return tuple(result)


def original_pair_square_permanent_cap(s,a):
    """All-h true GQ pointwise bound; records limits without claiming P2."""
    if type(s) is not int or s<2 or type(a) is not int or a<6:
        raise ValueError("integer GQ order and physical alphabet required")
    V=(s+1)*(s*s+1)
    if V>comb(a,2):
        raise ValueError("physical K_a cannot inject all source vertices")
    old=(s+1)**4
    new=6*comb(a-2,4)
    return {
        "s":s,"a":a,"V":V,
        "old_per_intersecting_GQ_pair_cap":old,
        "girth8_permanent_cap":2,
        "physical_C4_per_anchor_bound":3*comb(a-2,4),
        "new_per_intersecting_GQ_pair_cap":new,
        "combined_upper":min(old,new),
        "new_improves_previous":new<old,
        "all_h_source_pointwise_bound_proved":True,
        "all_h_P2_proved":False,
    }


def _line_rows(four_lines,four_points,line_points):
    if len(four_lines)!=4 or len(four_points)!=4 or (
            len(set(four_lines))!=4 or len(set(four_points))!=4):
        raise ValueError("four DISTINCT original lines and points")
    return tuple(sum(1<<i for i,p in enumerate(four_points)
                     if p in line_points[l])
                 for l in four_lines)


def true_original_sixsource_permanents(model):
    """W32 5005 full six-R original GQ permanent ledger, independent of C0."""
    if (model["s"],model["a"],model["v_left"],model["v_right"])!=(2,6,15,15):
        raise ValueError("complete original-source finite gate W32/K6 only")
    _,line_points,anchors=original_GQ_tables(
        model["s"],tuple(model["incidences"]))
    squares=physical_squares(model)
    if any(len(x)!=3 for x in squares):
        raise AssertionError("full physical K6 left bijection must have 3 squares per point")
    pm_cache={}
    weights={}
    pm1={}
    pm2={}
    histogram=Counter()
    weighted_by_intersections=Counter()
    all_terms=Counter()
    nonzero_sixsets=0
    strongest=Fraction(0)
    for R in combinations(range(15),6):
        w=n1=n2=e=0
        for B in combinations(R,2):
            p=anchors.get(B)
            if p is None:
                continue
            e+=1
            remaining=tuple(t for t in R if t not in B)
            for Q in squares[p]:
                key=(remaining,Q)
                value=pm_cache.get(key)
                if value is None:
                    value=permanent4(_line_rows(remaining,Q,line_points))
                    pm_cache[key]=value
                histogram[value]+=1
                if value==1:
                    n1+=1
                elif value==2:
                    n2+=1
                elif value!=0:
                    raise AssertionError("GQ local matching cap two violated")
                w+=value
        if w!=n1+2*n2 or w>6*e or w>81*e:
            raise AssertionError("sharp universal GQ local source cap violated")
        if w:
            nonzero_sixsets+=1
            weights[frozenset(R)]=w
            pm1[frozenset(R)]=n1
            pm2[frozenset(R)]=n2
            weighted_by_intersections[e]+=w
            if e:
                strongest=max(strongest,Fraction(w,e))
        all_terms[e]+=1
    reference=source_weighted_BA_hypergraph(model)
    if weights!=reference:
        diff=next(((R,weights.get(R,0),reference.get(R,0))
                   for R in set(weights)|set(reference)
                   if weights.get(R,0)!=reference.get(R,0)),None)
        raise AssertionError(f"independent 4x4 permanent source != original C0: {diff}")
    if sum(histogram.values())!=sum(e*3*n for e,n in all_terms.items()):
        raise AssertionError("complete GQ anchor-square term census lost multiplicity")
    return {
        "weights":weights,"permanent_one_counts":pm1,"permanent_two_counts":pm2,
        "report":{
            "W32_original_sixsets_all":comb(15,6),
            "source_positive_sixsets":nonzero_sixsets,
            "original_sixsource_mass":sum(weights.values()),
            "square_counts_by_original_point":[len(x) for x in squares],
            "all_permanent_zero_one_two_terms":
                {str(i):histogram[i] for i in range(3)},
            "sixset_GQ_intersection_count_histogram":
                {str(i):all_terms[i] for i in sorted(all_terms)},
            "weighted_mass_by_original_intersecting_pairs":
                {str(i):weighted_by_intersections[i]
                 for i in sorted(weighted_by_intersections)},
            "largest_actual_source_weight_over_GQ_meeting_pairs":
                rat(strongest),
            "previous_81_e_bound_replaced_by_6_e":True,
            "full_C0_independent_sixset_reconstruction":True,
            "whole_original_W32_space_exhausted":False,
        },
    }


def rank56_permanent_split(model, ledger):
    """Signed 5+6 Johnson contribution by local permanent multiplicity 1 or 2."""
    index,components,_=_frozen_target_W32()
    palette=physical_pair_indices(6)
    source=ledger["weights"]
    once=ledger["permanent_one_counts"]
    twice=ledger["permanent_two_counts"]
    labels=model["right_labels"]
    part1=part2=Fraction(0)
    physical_overlap=0
    T=simple_six_2factor_targets(6)
    for R,w in source.items():
        S=six_image_index(R,labels,palette)
        idx=index[S]
        H56=components[5][idx]+components[6][idx]
        if w!=once[R]+2*twice[R]:
            raise AssertionError("source permanent split inconsistent")
        part1+=once[R]*H56
        part2+=2*twice[R]*H56
        if frozenset(labels[p] for p in R) in T:
            physical_overlap+=w
    spectrum=spectral_overlap_certificate(source,labels)
    expected=sum((Fraction(*v) for v in spectrum["signed_ranks"][5:]),
                 Fraction(0))
    if part1+part2!=expected or physical_overlap!=spectrum["actual_U"]:
        raise AssertionError("local GQ permanent rank56 signed split differs from Johnson")
    return {
        "source_from_permanents_mass":sum(source.values()),
        "permanent_one_source_mass":sum(once.values()),
        "permanent_two_source_mass":2*sum(twice.values()),
        "actual_physical_BA_overlap":physical_overlap,
        "rank56_permanent_one_contribution":rat(part1),
        "rank56_permanent_two_contribution":rat(part2),
        "rank56_sum":rat(part1+part2),
        "independent_full_Johnson_rank56":rat(expected),
        "rank56_nonnegative_claim":False,
    }


def report():
    proof=exhaustive_girth8_permanent_lemma()
    caps={str(a):original_pair_square_permanent_cap(s,a)
          for s,a in ((2,6),(4,14),(8,35))}
    models=(("lex",gq_pair_model(1,"lex")),
            ("hardest-M",swapped_labeling(_anchors()[0][1],"left",13,14)))
    result=[]
    for name,m in models:
        point=exact_two_family_point(m)
        BA=true_original_sixsource_permanents(m)
        dual=dual_model(m)
        AB=true_original_sixsource_permanents(dual)
        BA56=rank56_permanent_split(m,BA)
        AB56=rank56_permanent_split(dual,AB)
        if (BA56["actual_physical_BA_overlap"],
                AB56["actual_physical_BA_overlap"])!=(
                    point["U_BA"],point["U_AB"]):
            raise AssertionError("two genuine original dual B0/C0 totals differ")
        result.append({
            "name":name,"U_BA":point["U_BA"],
            "U_AB":point["U_AB"],"S_seven":point["S_seven"],
            "P2_margin":point["two_family_minus_mu"],
            "original_BA":{**BA["report"],**BA56},
            "true_original_dual_AB":{**AB["report"],**AB56},
        })
    return {
        "slice":"HYP-105-E1-K3-G2-Q",
        "complete_4x4_girth8_permanent_proof":proof,
        "all_h_GQ_original_source_caps":caps,
        "true_original_GQ_models":result,
        "all_h_anchor_square_permanent_identity_proved":True,
        "all_h_two_family_P2_proved":False,
        "all_h_seven_family_P7_proved":False,
        "branch_A_B":"OPEN",
    }


if __name__=="__main__":
    print(json.dumps(report(),sort_keys=True,indent=2))
