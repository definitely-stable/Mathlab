"""AA4-TAILFRONTIER: exact ORIGINAL source path bad-neighbor tail layer cake.

All-h genuine fixed-correlated ORIGINAL model:
   r_gamma=b_gamma(w)/W_uv in [0,1],
   mu(gamma)=W_uv*w_gamma/M, sum mu=1,
   P_t=sum_{r_gamma>t}mu(gamma).
Then B/M = integral_0^1 P_t dt exactly. For any mesh
0=t0<...<tm=1:
   sum_i delta_i*P_(t_{i+1}) <= B/M <=
   sum_i delta_i*P_(t_i)
and gap <=max delta_i. A single P_(2/3)<1/4 is merely a
SUFFICIENT B75 test and does not logically follow from B75.

This module then ADVERSARIALLY searches full ORIGINAL symplectic W32
pair-injection assignments: all 15 point labels and all 15 line labels
are independent full permutations of the true 6-choose-2 pairs.
Float degree-product proxy ranks candidates ONLY, never certifies.
Every selected candidate is re-evaluated from true original GQ
first/middle/last physical ports, one common exact Fraction source
priority selector and a completely independent original physical
adjacency P3 walker. The source exact per-P3 bad row is independently
checked against the ORIGINAL sparse middle moment.

No finite counterexample to auxiliary P_(2/3)<1/4 implies an
infinite counterexample to ROOT seven-family Omega(s^6); no claims
of unproved universal all-h risk.
"""
from collections import defaultdict
from fractions import Fraction
import json,random

from hyp105_original_adversarial_B75_referee import (
    genuine_source_for_assignment,all_genuine_proper_p3,
    _initial_labelings,_mutate_labels,FLAGS,IDENTITY,
)
from hyp105_original_three_owner_joint_ports_referee import (
    _joint_original_three_owner_ports,_true_original_joint_middle_moment,
)
from hyp105_original_pathwise_corner_charge_referee import (
    _physical_original_pathwise_charges,
)
from hyp105_original_signed_physical_pair_charge_referee import (
    _original_independent_physical_pair_good,
)

SCHEMA="mathlab.hyp105.original-heavy-tail-adversarial-frontier.v1"
STATUS="OPEN_WITH_FORMAL_BLOCKER"
ROOT=230
SEED=230768
TRIALS=180
SHORTLIST=4
T=Fraction(2,3)
THRESHOLDS=(Fraction(1,2),T,Fraction(3,4))
MESH=32
B75=Fraction(3,4)


def _genuine_original_complete_W32(fperm,gperm):
    """Actual 45-flag symplectic source, no fake owners or pair clones."""
    raw=genuine_source_for_assignment(fperm,gperm)
    c=dict(raw)
    c.update(flags=FLAGS,owner=raw["edges"],s=2,a=6,V=15)
    assert len(c["ids"])==45 and len(c["owner"])==90
    assert len(set(c["f"]))==15 and len(set(c["g"]))==15
    assert c["source_max_J"]<=64
    return c


def _fast_original_degree_proxy_tail(fperm,gperm):
    """NONPROOF float scout; full actual original physical path population.

    The proxy source-priority weight is the artificial product of
    three singleton minima, deliberately NOT used in the exact gate.
    Bad/good pair supports use original physical point/line middle
    flags and actual first/last corner correction, never projected
    x/y endpoint shadows.
    """
    c=_genuine_original_complete_W32(fperm,gperm)
    sourcepaths=all_genuine_proper_p3(c)
    bins=defaultdict(list)
    ds=[len(js) for js in c["J"]]
    for path,owners in sourcepaths:
        w=1.
        for i in owners:
            w/=1+ds[i]
        bins[(path[0],path[-1])].append((path,owners,w))
    M=B=E0=Ehalf=Etwo=Ethree=0.
    for group in bins.values():
        W=sum(z[2] for z in group)
        M+=W*W
        for row in group:
            b=sum(other[2] for other in group
                  if not _original_independent_physical_pair_good(row,other,c))
            if not (0<=b<=W):
                raise AssertionError("nonproof ORIGINAL physical pair indicator invalid")
            B+=row[2]*b
            if b>0:E0+=W*row[2]
            if b>W/2:Ehalf+=W*row[2]
            if b>2*W/3:Etwo+=W*row[2]
            if b>3*W/4:Ethree+=W*row[2]
    if not M>0:
        raise AssertionError("empty TRUE ORIGINAL W32 physical source")
    return {
        "nonproof_float_proxy_P_2_over_3":Etwo/M,
        "nonproof_float_proxy_P_1_over_2":Ehalf/M,
        "nonproof_float_proxy_P_3_over_4":Ethree/M,
        "nonproof_float_proxy_B_over_M":B/M,
        "actual_original_P3_count":len(sourcepaths),
        "actual_original_endpoint_bins":len(bins),
    }


def _exact_genuine_original_tail(fperm,gperm,strict_full_pair_crosscheck=True):
    """ALL true original W32 P3, exact Fraction priorities and tail CDF.

    This is a FINITE source certificate, not an all-h extrapolation.
    """
    c=_genuine_original_complete_W32(fperm,gperm)
    bins,rank_sets=_joint_original_three_owner_ports(c)
    if strict_full_pair_crosscheck:
        independently_walked=set(all_genuine_proper_p3(c))
        independently_joined={(path,owners) for group in bins.values()
                              for path,owners,*_ in group}
        if independently_joined!=independently_walked:
            raise AssertionError("true original physical port JOIN != independent walker")
    row_profiles=[]
    totals=defaultdict(Fraction)
    count=0
    original_five_witness=None
    for ends,group in bins.items():
        ch=_physical_original_pathwise_charges(group,c,2)
        other=_true_original_joint_middle_moment(group,c,2)
        if any(ch[k]!=other[k] for k in ("M","B","G")):
            raise AssertionError("exact ORIGINAL source sparse second-moment oracle mismatch")
        W=ch["W"]
        for row,(good,bad,Ni,Tail,Head) in zip(group,ch["rows"]):
            w=row[2]
            r=bad/W
            if not 0<=r<=1:
                raise AssertionError("invalid source bad physical path fraction")
            row_profiles.append((r,W*w))
            if r>T and original_five_witness is None:
                original_five_witness={
                    "true_physical_path_corners":[list(v) for v in row[0]],
                    "named_original_first_middle_last_owner_ids":list(row[1]),
                    "true_exact_path_selector_weight":str(w),
                    "true_exact_path_bad_neighbor_fraction":str(r),
                    "middle_original_bad_label_mass":str(Ni),
                    "physical_first_corner_compatible_mass":str(Tail),
                    "physical_last_corner_compatible_mass":str(Head),
                }
            count+=1
        for k in ("M","G","B"):
            totals[k]+=ch[k]
    M=totals["M"]
    B=totals["B"]
    if not (M>0 and B+totals["G"]==M):
        raise AssertionError("genuine ORIGINAL risk energy conservation failed")
    if sum((mass for _,mass in row_profiles),Fraction(0))!=M:
        raise AssertionError("endpoint size-biased physical path distribution not a probability")

    # Exact all-h layer cake applied to finite original ranks; independent
    # integral by weighted atom masses, exact Fraction not floating point.
    direct_integral=sum((r*mass for r,mass in row_profiles),Fraction(0))/M
    if direct_integral!=B/M:
        raise AssertionError("exact TRUE source bad fraction != full weighted tail layer cake")
    tail={}
    for t in (Fraction(0),)+THRESHOLDS+(Fraction(1),):
        n=sum((mass for r,mass in row_profiles if r>t),Fraction(0))
        tail[str(t)]=n/M
    if not (1>=tail["0"]>=tail["1/2"]>=tail["2/3"]>=tail["3/4"]>=tail["1"]==0):
        raise AssertionError("ORIGINAL weighted bad fraction tail not decreasing")
    # NEW universal 3-threshold coarse physical risk certificate.
    # On [0,1/2], [1/2,2/3], [2/3,3/4], [3/4,1],
    # bound each nonincreasing tail by its LEFT value. For the first
    # interval use P_0<=1, eliminating the need to compute P_0.
    composite=(Fraction(1,2)+tail["1/2"]/6+
               tail["2/3"]/12+tail["3/4"]/4)
    composite_mass=2*tail["1/2"]+tail["2/3"]+3*tail["3/4"]
    if not B/M<=composite<=1 or (composite<B75)!=(composite_mass<3):
        raise AssertionError("universal ORIGINAL three-tail combined B75 bound invalid")
    if B/M>B75 and not composite_mass>3:
        raise AssertionError("adversarial strict B75 source lacks joint heavy-tail obstruction")

    # An exact alternative computation via the STRICT survival-function
    # step intervals, independent of the original good/bad sparse moment.
    unique=sorted({Fraction(0),Fraction(1)}|{r for r,_ in row_profiles})
    rank_tail={t:sum((mass for r,mass in row_profiles if r>t),
                     Fraction(0))/M for t in unique[:-1]}
    integral=sum(((b-a)*rank_tail[a] for a,b in zip(unique,unique[1:])),
                 Fraction(0))
    if integral!=B/M:
        raise AssertionError("independently integrated exact ORIGINAL tail curve disagrees")

    grid=tuple(Fraction(k,MESH) for k in range(MESH+1))
    P={t:sum((mass for r,mass in row_profiles if r>t),
             Fraction(0))/M for t in grid}
    grid_L=sum((P[grid[k+1]] for k in range(MESH)),Fraction(0))/MESH
    grid_U=sum((P[grid[k]] for k in range(MESH)),Fraction(0))/MESH
    if not (0<=grid_L<=B/M<=grid_U<=1 and
            grid_U-grid_L<=Fraction(1,MESH)):
        raise AssertionError("valid all-h ORIGINAL mesh tail sandwich violated")
    out={
        "genuine_original_W32":True,
        "complete_true_original_source_not_sampling":True,
        "named_original_flags":len(c["ids"]),
        "owned_actual_physical_opposite_diagonals":len(c["owner"]),
        "true_original_coordinate_proper_P3s":count,
        "true_original_endpoint_bins":len(bins),
        "distinct_genuine_original_rank_triples":rank_sets,
        "exact_original_M":str(M),
        "exact_original_G":str(totals["G"]),
        "exact_original_B":str(B),
        "exact_original_B_over_M":str(B/M),
        "exact_original_weighted_tail_P_0":str(tail["0"]),
        "exact_original_weighted_tail_P_1_over_2":str(tail["1/2"]),
        "exact_original_weighted_tail_P_2_over_3":str(tail["2/3"]),
        "exact_original_weighted_tail_P_3_over_4":str(tail["3/4"]),
        "new_three_physical_tail_combined_B_over_M_upper":str(composite),
        "new_three_physical_tail_joint_halfspace_mass":str(composite_mass),
        "new_three_physical_tail_certifies_B75":composite<B75,
        "new_all_h_three_tail_B75_necessary_mass_above_three":True,
        "exact_original_tail_LayerCake_equals_B_over_M":str(integral),
        "exact_original_tail_mesh32_lower":str(grid_L),
        "exact_original_tail_mesh32_upper":str(grid_U),
        "original_heavy_three_owner_path_witness":original_five_witness,
        "fixed_source_violates_auxiliary_P_2_over_3_below_1_over_4":
            tail["2/3"]>=Fraction(1,4),
        "fixed_source_violates_global_B75": B/M>=B75,
        "root_PROVED_A":False,
        "f_pair_perm_indices":list(fperm),
        "g_pair_perm_indices":list(gperm),
    }
    return out


def _deterministic_frontier(trials=TRIALS,seed=SEED,shortlist=SHORTLIST):
    if not 20<=trials<=500 or not 1<=shortlist<=8:
        raise ValueError("bounded finite genuine original W32 adversarial search required")
    rng=random.Random(seed)
    scores=[]
    seen=set()
    cur=(IDENTITY,IDENTITY)
    best=cur
    cur_s=-1.
    n_restarts=0
    def evaluate(f,g,kind):
        key=(tuple(f),tuple(g))
        if key in seen:
            return None
        seen.add(key)
        proxy=_fast_original_degree_proxy_tail(*key)
        score=proxy["nonproof_float_proxy_P_2_over_3"]
        scores.append((score,key[0],key[1],kind,proxy))
        return score
    for name,f,g in _initial_labelings():
        evaluate(f,g,"baseline:"+name)
    base_best=max(scores,key=lambda z:z[0])
    best=base_best[1:3]
    for k in range(trials):
        if k%29==0:
            f=list(IDENTITY);g=list(IDENTITY)
            rng.shuffle(f);rng.shuffle(g)
            f,g=tuple(f),tuple(g)
            kind="seeded-global-restart"
            n_restarts+=1
        elif k%13==0 and scores:
            s=rng.choice(sorted(scores,key=lambda x:x[0],reverse=True)[:6])
            f,g=_mutate_labels(rng,s[1],s[2])
            kind="seeded-elite-neighbor"
        elif k%4==0:
            f,g=_mutate_labels(rng,*best)
            kind="current-best-neighbor"
        else:
            f,g=_mutate_labels(rng,*cur)
            kind="seeded-local-neighbor"
        score=evaluate(f,g,kind)
        if score is None:
            continue
        if score>max(z[0] for z in scores[:-1]):
            best=(tuple(f),tuple(g))
        if score>=cur_s or rng.random()<(.07 if score>=cur_s-.05 else .005):
            cur=(tuple(f),tuple(g));cur_s=score
    scores.sort(key=lambda z:(-z[0],z[1],z[2]))
    # Exact-certify TOP K, plus the predeclared lex/reverse baseline.
    selected=scores[:shortlist]
    exact=[_exact_genuine_original_tail(f,g) for _,f,g,_,_ in selected]
    # Mandatory independently established original full W32 baseline
    # exact Fraction values from AA4-PATHCHARGE, not just optimizer picks.
    for label in ("baseline:lex-lex","baseline:lex-reverse"):
        baseline=next((z for z in scores if z[3]==label),None)
        if baseline is None:
            raise AssertionError("mandatory original W32 source baseline missing")
        known=(baseline[1],baseline[2])
        if not any(tuple(x["f_pair_perm_indices"])==known[0] and
                   tuple(x["g_pair_perm_indices"])==known[1] for x in exact):
            exact.append(_exact_genuine_original_tail(*known))
    by_scheme={
        "lex-lex":(Fraction(395498199363009600,1190067603581473393),
                   Fraction(203238170327875425,1190067603581473393)),
        "lex-reverse":(Fraction(2197221736032,6861627242215),
                       Fraction(816966722907,6861627242215)),
    }
    for label,permF,permG in ((name,f,g) for name,f,g in _initial_labelings()
                               if name in by_scheme):
        original=next(x for x in exact if tuple(x["f_pair_perm_indices"])==permF
                      and tuple(x["g_pair_perm_indices"])==permG)
        expected_risk,expected_P=by_scheme[label]
        if (Fraction(original["exact_original_B_over_M"])!=expected_risk or
            Fraction(original["exact_original_weighted_tail_P_2_over_3"])!=expected_P):
            raise AssertionError("adversarial exact ORIGINAL priority source fails frozen independent W32 baseline")
    if not exact:
        raise AssertionError("no exact genuine ORIGINAL adverse candidates audited")
    besttrue=max(exact,key=lambda x:Fraction(x["exact_original_weighted_tail_P_2_over_3"]))
    bestB=max(exact,key=lambda x:Fraction(x["exact_original_B_over_M"]))
    return {
        "schema":SCHEMA,"issue":ROOT,"status":STATUS,
        "all_h_exact_original_layer_cake_tail_identity_proved":True,
        "all_h_finite_mesh_original_tail_sandwich_proved":True,
        "all_h_original_three_tail_composite_B75_sufficient_inequality_proved":True,
        "all_h_universal_three_tail_composite_strict_B75_PROVED":False,
        "all_h_universal_P_2_over_3_below_quarter_PROVED":False,
        "all_h_original_B75_proved":False,
        "root_seven_six_motif_Omega_s6_PROVED":False,
        "ASET_exponent_claimed":False,
        "fixed_original_order":2,
        "full_original_GQ_flags":45,
        "pair_alphabet":6,
        "original_f_and_g_each_permute_all_15_pairs":True,
        "seed":seed,"trial_budget":trials,
        "finite_float_only_proposals":len(scores),
        "nonproof_proxy_top_P_2_over_3":str(scores[0][0]),
        "seeded_global_restarts":n_restarts,
        "exact_fraction_true_source_candidates":exact,
        "best_exact_original_P_2_over_3":besttrue,
        "best_exact_original_B_over_M":bestB,
        "at_least_one_exact_original_W32_violates_auxiliary_quarter_gate":
            any(x["fixed_source_violates_auxiliary_P_2_over_3_below_1_over_4"]
                for x in exact),
        "at_least_one_exact_original_W32_violates_auxiliary_half_gate":
            any(Fraction(x["exact_original_weighted_tail_P_1_over_2"])>=Fraction(1,2)
                for x in exact),
        "all_exact_candidates_three_tail_composite_certify_strict_B75":
            all(x["new_three_physical_tail_certifies_B75"] for x in exact),
        "at_least_one_exact_original_W32_violates_B75":
            any(x["fixed_source_violates_global_B75"] for x in exact),
        "finite_search_nonproof_for_all_h":True,
    }


def canonical_report():
    return _deterministic_frontier()


if __name__=="__main__":
    print("AA4_TAILFRONTIER_CERTIFICATE="+json.dumps(
        canonical_report(),sort_keys=True,separators=(",",":")))
