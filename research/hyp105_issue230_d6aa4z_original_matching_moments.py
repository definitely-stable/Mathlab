"""HYP-105 / issue #230 AA4-Z-SRC — original GQ six-matching source A/A
and one-P2-plus-four-independent-edge source A/B,B/A, ALL h=1,2,...

The mathematical moments of the matching polynomial via Godsil's
self-avoiding-walk path tree are PRIOR ART, not claimed new. This slice
applies that identity to true original source flag forests of W(3,2^h)
and tests independently on actual globally validated ORIGINAL GQs.

No physical projections are used to count source Q. The separately
established AA4-W probability transfer is used only AFTER source
counting, with one complete uniformly global f and independent g.
Actual arbitrary globally injected pair f,g may have fewer positives!
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import comb

from hyp105_issue230_projection import fixture, ProjectionClosure
from hyp105_issue230_d6aa4w_full_seven_quenched_kernel import (
    all_h_full_seven_one_global_map_transfer_probabilities,
)
from hyp105_issue230_d6aa4x_exact_source_forest_capacities import (
    checked_gq_parameters, all_h_two_closed_source_forest_expectations,
)
from hyp105_issue230_d6aa4y_original_triple_pencil_overlaps import (
    full_global_uniform_AC_CA_selected_GF5,
)


def regular_tree_matching_root_even_moment(d, k):
    """Independent finite length-2k rooted walk count of the d-regular tree.

    Upward choices from root d; upward from positive depth d-1; down 1.
    The first k matching root moments of a d-regular girth>=8 graph,
    k<=6, equal these values by the self-avoiding path tree identity.
    """
    if type(d) is not int or d<2 or type(k) is not int or k<0:
        raise ValueError("valid regular-tree degree and nonnegative integer k")
    frontier={0:1}
    for _ in range(2*k):
        nxt=Counter()
        for h,v in frontier.items():
            nxt[h+1]+=v*(d if h==0 else d-1)
            if h:nxt[h-1]+=v
        frontier=dict(nxt)
    return frontier.get(0,0)


def matching_polynomial_from_root_power_sums(power_sums):
    """Exact Newton identities, no floating point and no spectral guesses.

    If p_j=sum_(matching-roots lambda) lambda^(2j), then
       2k m_k = sum_(j=1..k) (-1)^(j+1) p_j m_(k-j).
    p_j may be arbitrary actual-graph Godsil SAW-path-tree moments.
    """
    ms=[1]
    for k in range(1,len(power_sums)+1):
        num=sum(((-1)**(j+1)*power_sums[j-1]*ms[k-j])
                for j in range(1,k+1))
        if num%(2*k):
            raise AssertionError("matching polynomial moment Newton integrality failed")
        m=num//(2*k)
        if m<0:
            raise AssertionError("actual matching polynomial coefficient cannot be negative")
        ms.append(m)
    return tuple(ms)


def all_h_original_matching_source_AA(s):
    """EXACT ALL-h true ORIGINAL source A/A = six-edge matching in GQ.

    G has 2V vertices, degree d, girth 8. Matching polynomial root
    moments up to 2*6 equal d-regular universal-tree closed-walk moments
    since a SAW path of <=6 edges cannot self-close into a <=6-cycle.
    """
    V,d,N=checked_gq_parameters(s)
    moments=[regular_tree_matching_root_even_moment(d,k) for k in range(1,7)]
    matchings=matching_polynomial_from_root_power_sums(
        tuple(2*V*t for t in moments))
    if matchings[1]!=N or matchings[6]<=0:
        raise AssertionError("original A/A six-match count or N flags invalid")
    return {
        "s":s,"V":V,"d":d,"N_actual_original_flag_IDs":N,
        "regular_original_source_root_closed_walk_moments_2k":moments,
        "original_source_matching_numbers_m0_to_m6":list(matchings),
        "source_original_A/A_six_distinct_point_line_flags":matchings[6],
        "exact_original_GQ_all_h_AA_source_matchings_PROVED":True,
        "Godsil_1981_preexisting_path_tree_method_not_claimed_new":True,
        "all_h_physical_global_maps_NOT_used":True,
    }


def formal_cavity_monomer_star_ratio(d,k=4):
    """Exact formal series R_{P2}(z) = x(z)^2*y(z) modulo z^(k+1).

    x=1/(1+(d-1) z x) is the rooted regular-tree cavity monomer
    probability; y=1/(1+d z x) is ordinary root monomer probability.

    For a deleted REAL ORIGINAL source line-centered P2 (point-line-
    point), P2 monomer event is y*x^2. Since source girth >=8, a
    non-tree loop or alternative path between its endpoints cannot
    alter its formal z^0..z^4 coefficients. A direct actual finite
    original-graph SAW path-tree oracle checks the identity separately.
    """
    if type(d) is not int or d<3 or type(k) is not int or k<0:
        raise ValueError("original regular degree and truncation invalid")
    x=[((-1)**j*(d-1)**j*comb(2*j,j))//(j+1) for j in range(k+1)]
    # Alternative exact recurrence verifies the Catalan-coefficient form
    for n in range(1,k+1):
        if x[n]!=-(d-1)*sum(x[i]*x[n-1-i] for i in range(n)):
            raise AssertionError("exact cavity x fixed point expansion disagree")
    y=[1]
    for n in range(1,k+1):
        y.append(-d*sum(x[j]*y[n-j-1] for j in range(n)))
    def product(a,b):
        return [sum(a[j]*b[n-j] for j in range(n+1))
                for n in range(k+1)]
    mono=product(product(x,x),y)
    return {
        "d":d,"up_to_k":k,
        "cavity_x_coefficients":x,
        "root_monomer_y_coefficients":y,
        "original_P2_three_vertex_joint_monomer_ratio":mono,
        "formal_tree_cavity_only_through_order_four":True,
        "tree_method_original_prior_art":True,
    }


def all_h_original_one_P2_plus_four_matching_AB(s):
    """EXACT ALL-h A/B and B/A = centered genuine ORIGINAL P2 + m4(G-S).

    Fixed one genuine ORIGINAL line-centered P2 source path P-L-P:
    its two selected original flags share ONE original line and have
    distinct original points. Four isolated original flags must have
    distinct original endpoints and avoid all three P2 source vertices.
    Exactly m4(G - {P,L,P}) such four-matchings; all rooted P2
    path configurations have the same m4 by all-h source-girth cutoff.
    """
    V,d,N=checked_gq_parameters(s)
    base=all_h_original_matching_source_AA(s)
    cav=formal_cavity_monomer_star_ratio(d)
    mm=base["original_source_matching_numbers_m0_to_m6"]
    residual_m4=sum(mm[i]*cav["original_P2_three_vertex_joint_monomer_ratio"][4-i]
                    for i in range(5))
    roots=V*comb(d,2)
    if residual_m4<=0 or roots*residual_m4<=0:
        raise AssertionError("nonempty actual 4matching after original P2 deletion expected")
    return {
        "s":s,"V":V,"d":d,
        "original_LINE_centered_P2_source_roots":roots,
        "original_true_P2_deleted_residual_4matching_count":residual_m4,
        "source_original_A/B_one_P2_plus_4_disjoint_flags":roots*residual_m4,
        "source_original_B/A_by_true_GQ_duality":roots*residual_m4,
        "original_P2_formal_cavity_monomer_ratio":cav[
            "original_P2_three_vertex_joint_monomer_ratio"],
        "source_original_AA_six_matching":base[
            "source_original_A/A_six_distinct_point_line_flags"],
        "actual_original_six_distinct_incidence_IDs":True,
        "all_h_girth_eight_rooted_P2_cavity_PROVED":True,
        "adversarial_joint_physical_acceptance_NOT_PROVED":True,
    }


def all_h_two_new_selected_GF5_ensemble_sectors(s):
    """Full GLOBAL-UNIFORM maps separately on point and line originals.

    All-h source A/A and A/B/B/A are now EXACT, so add exact selected
    D6 and the two historical separate B/A and A/B full GF5 tags.
    Also preserve AA4-X/Y exactly three previously closed tags.
    Unclosed original B/B-disjoint stays explicitly UNDETERMINED.
    """
    aa=all_h_original_matching_source_AA(s)
    ab=all_h_original_one_P2_plus_four_matching_AB(s)
    p=all_h_full_seven_one_global_map_transfer_probabilities(s)
    ph=p["D6_position_matched_connected_H"]
    pa=p["A_any_connected_or_disconnected_physical_2factor"]
    pb=p["B_same_source_repeated_plus_physical_C4"]
    Ed6=60*aa["source_original_A/A_six_distinct_point_line_flags"]*ph**2
    Eab=2*ab["source_original_A/B_one_P2_plus_4_disjoint_flags"]*pa*pb
    older=full_global_uniform_AC_CA_selected_GF5(s)
    three=older["three_positive_original_selected_tags_expected"]
    five=three+Ed6+Eab
    if min(Ed6,Eab,three,five)<=0:
        raise AssertionError("positive exact uniform full-global selected five-tag expectations")
    return {
        "s":s,"V":aa["V"],"d":aa["d"],"a":p["a"],
        "exact_TRUE_SOURCE_U_AA":aa["source_original_A/A_six_distinct_point_line_flags"],
        "exact_TRUE_SOURCE_U_AB_and_BA":ab["source_original_A/B_one_P2_plus_4_disjoint_flags"],
        "exact_both_complete_global_uniform_selected_D6":Ed6,
        "exact_both_complete_global_uniform_selected_AB_plus_BA":Eab,
        "prior_X_Y_three_selected_tag_expectation":three,
        "five_distinct_selected_GF5_tag_expectation":five,
        "source_original_BB_disjoint_still_UNCLOSED":True,
        "leading_AA_source_over_s24":Fraction(1,720),
        "leading_AB_BA_source_each_over_s21":Fraction(1,48),
        "leading_selected_D6_over_s6":Fraction(16,3),
        "leading_selected_AB_plus_BA_over_s6":280,
        "leading_three_previous_tags_over_s6":Fraction(160,3),
        "leading_five_selected_tags_over_s6":Fraction(1016,3),
        "ensemble_not_adversarial_minimum":True,
    }


def strict_actual_source_GQ_adjacency(model):
    """Actual genuine ORIGINAL geometry; no fake regular sixcycle source."""
    checked=ProjectionClosure(model)
    adj=[set() for _ in range(2*checked.v)]
    for p,l in checked.edges:
        adj[p].add(checked.v+l)
        adj[checked.v+l].add(p)
    if any(len(x)!=checked.delta for x in adj):
        raise AssertionError("original incidence graph not degree d")
    return checked,tuple(frozenset(x) for x in adj)


def _series_inverse_one_minus_z_sum(series,k):
    """Compute H=1/(1-z A) coefficientwise with exact integers."""
    h=[1]
    for j in range(1,k+1):
        h.append(sum(series[t]*h[j-1-t] for t in range(j)))
    return tuple(h)


def independent_actual_source_SAW_matching_polynomial(adj,k):
    """INDEPENDENT exact Godsil SAW path-tree matching root moments.

    Unlike the ALL-h shortcut, this explores actual finite TRUE source
    adjacency with vertex exclusions and does NOT assume d-regularity,
    no short cycles, universal moments, or the cavity formula.
    Works on deleted nonregular actual ORIGINAL source GQ.
    """
    if not 0<=k<=6 or type(k) is not int:
        raise ValueError("actual source SAW matching polynomial order<=6")
    n=len(adj)
    p_sums=[0]*k
    for root in range(n):
        @lru_cache(None)
        def H(path,remaining):
            if remaining==0:return (1,)
            tail=path[-1]
            seen=set(path)
            kids=[H(path+(t,),remaining-1) for t in adj[tail]
                  if t not in seen]
            sums=[sum(kd[j] for kd in kids) for j in range(remaining)]
            return _series_inverse_one_minus_z_sum(sums,remaining)
        vals=H((root,),k)
        for j in range(k):
            p_sums[j]+=vals[j+1]
    matched=matching_polynomial_from_root_power_sums(tuple(p_sums))
    return {
        "actual_source_vertices":n,
        "actual_graph_root_matching_power_sums":p_sums,
        "actual_matchings_m0_to_mk":list(matched),
        "actual_original_graph_agnostic_Godsil_SAW_independent":True,
    }


def independent_actual_true_GQ_six_matching_and_P2_4matching(model,
                                                               *,
                                                               max_P2_samples=6,
                                                               check_whole_graph=True):
    """Check actual W32/W34 GQ source graph without independent sixset cells.

    The SAW oracle counts all matching k<=6 in the actual graph; source
    A/B residual m4 is independently computed after deleting actual
    original line-centered P2 source vertices. All P2 samples use
    original actual distinct incidences. Source geometry is validated
    BEFORE traversing the graph. Do not transfer physically sampled labels.
    """
    checked,adj=strict_actual_source_GQ_adjacency(model)
    s=checked.s
    aa=all_h_original_matching_source_AA(s)
    ab=all_h_original_one_P2_plus_four_matching_AB(s)
    whole=(independent_actual_source_SAW_matching_polynomial(adj,6)
           if check_whole_graph else None)
    if whole is not None and whole["actual_matchings_m0_to_mk"]!=aa[
            "original_source_matching_numbers_m0_to_m6"]:
        raise AssertionError("INDEPENDENT actual SOURCE full m0..m6 differs all-h tree theorem")
    V=checked.v
    witnesses=[]
    # Choose 2 ORIGINAL POINT neighbors of a genuine ORIGINAL LINE.
    for l in range(V):
        nbr=tuple(sorted(t for t in adj[V+l] if t<V))
        for p1,p2 in combinations(nbr,2):
            deleted={p1,p2,V+l}
            remaining=[frozenset(v for v in adj[u] if v not in deleted)
                       if u not in deleted else frozenset()
                       for u in range(2*V)]
            rec=independent_actual_source_SAW_matching_polynomial(
                tuple(remaining),4)
            actual=rec["actual_matchings_m0_to_mk"][4]
            if actual!=ab["original_true_P2_deleted_residual_4matching_count"]:
                raise AssertionError("genuine ORIGINAL P2-local residual m4 not invariant")
            witnesses.append({"actual_original_line":l,
                              "actual_original_points":(p1,p2),
                              "actual_source_residual_m4":actual})
            if len(witnesses)>=max_P2_samples:
                return {
                    "s":s,"V":V,"d":checked.delta,
                    "all_original_full_source_matchings":whole,
                    "exact_original_source_U_AA":aa[
                        "source_original_A/A_six_distinct_point_line_flags"],
                    "exact_original_source_U_AB":ab[
                        "source_original_A/B_one_P2_plus_4_disjoint_flags"],
                    "independently_checked_actual_P2_roots":witnesses,
                    "true_original_GQ_projection_unique_anchor_VALIDATED":True,
                    "does_NOT_prove_every_physical_f_g_joint_GF5":True,
                }
    raise AssertionError("insufficient true-original P2 centers for source check")


def report(s_values=(2,4,8,16)):
    out={}
    for s in s_values:
        row=all_h_two_new_selected_GF5_ensemble_sectors(s)
        out[str(s)]={
            "source_AA_six_matching":row["exact_TRUE_SOURCE_U_AA"],
            "source_AB_each_P2_plus_four_matching":row["exact_TRUE_SOURCE_U_AB_and_BA"],
            "exact_selected_D6_EXPECTATION":str(row["exact_both_complete_global_uniform_selected_D6"]),
            "exact_selected_AB_BA_EXPECTATION":str(row["exact_both_complete_global_uniform_selected_AB_plus_BA"]),
            "exact_five_GF5_EXPECTATION":str(row["five_distinct_selected_GF5_tag_expectation"]),
        }
    return {"slice":"HYP105-ISSUE230-D6-AA4-Z-SRC-SIX-MATCHING-MOMENTS",
            "rows":out,"root_A":"OPEN","root_B":"OPEN","five_tags_ensemble_only":True}


if __name__=="__main__":
    import argparse,json
    cli=argparse.ArgumentParser()
    cli.add_argument("--verify-real",action="store_true")
    args=cli.parse_args()
    data=report()
    if args.verify_real:
        data["independent_true_original_GQ"]={
            str(1<<h):independent_actual_true_GQ_six_matching_and_P2_4matching(
                fixture(h,"lex"),max_P2_samples=3)
            for h in (1,2)}
    print(json.dumps(data,indent=2,sort_keys=True,default=str))
