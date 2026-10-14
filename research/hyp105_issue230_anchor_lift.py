"""EICE-003 exact ORIGINAL GQ-anchor lifted nonbacktracking collision energy.

A1 (necessary, all-h): theta_I**2 <= 16*N*s**2*(A_f+A_g).
This code is a finite falsifier, NOT a universal energy upper or Branch A.
Inputs are complete globally injective true ORIGINAL GQ maps; optionally
retain only complete pairs of physical Kikuchi diagonals by source ID.
"""
from collections import defaultdict
from fractions import Fraction
import json

from hyp105_issue230_endpoint_energy import EndpointEnergy


class AnchorLiftedEnergy:
    def __init__(self, model, selected=None):
        self.ctx = EndpointEnergy(model, selected=selected)

    def census(self, *, max_paths=500_000, require_proper=False,
               require_stationary=False, independent_collision=False):
        ctx = self.ctx
        if type(max_paths) is not int or max_paths <= 0:
            raise ValueError('positive integer path budget required')
        if require_stationary and (not ctx.m or
                                   any(0 < d < 2 for d in ctx.degree)):
            raise ValueError('stationary NB law requires active min-degree >=2')
        # raw subprobability matrices indexed by (ORIGINAL q, ORIGINAL r,
        # FIRST INTERNAL physical coordinate); not arbitrary physical paths
        # which may have an absent/incident endpoint or bad anchor.
        raw_f, raw_g = defaultdict(Fraction), defaultdict(Fraction)
        pair_f, pair_g = defaultdict(Fraction), defaultdict(Fraction)
        endpoint_mass = defaultdict(Fraction)
        collision_f = collision_g = Fraction()
        total = eligible = internal = left_hit = right_hit = Fraction()
        double_left = double_right = joint_lr = double_both = Fraction()
        improper = 0
        path_count = 0
        for (u, v, w, z), weight in ctx._iter_nb(max_paths):
            path_count += 1
            total += weight
            x0,y0 = divmod(u,ctx.a)
            x1,y1 = divmod(v,ctx.a)
            x2,y2 = divmod(w,ctx.a)
            x3,y3 = divmod(z,ctx.a)
            proper = len({x0,x1,x2,x3})==4 and len({y0,y1,y2,y3})==4
            if not proper:
                improper += 1
                if require_proper:
                    raise ValueError('improper NB path in alleged G*')
                continue
            q = ctx.fi.get(tuple(sorted((x0,x3))))
            r = ctx.gi.get(tuple(sorted((y0,y3))))
            if q is None or r is None or (q,r) not in ctx.anchor:
                continue
            p, ell = ctx.anchor[q,r]
            if not (set(ctx.f[p]).isdisjoint(ctx.f[q]) and
                    set(ctx.g[ell]).isdisjoint(ctx.g[r])):
                continue
            eligible += weight
            endpoint_mass[q,r] += weight
            kf=(q,r,x1)
            kg=(q,r,y1)
            if independent_collision:
                collision_f += weight*weight + 2*weight*pair_f[kf]
                collision_g += weight*weight + 2*weight*pair_g[kg]
                pair_f[kf] += weight
                pair_g[kg] += weight
            raw_f[kf] += weight
            raw_g[kg] += weight
            fl = x1 in ctx.f[p] or x2 in ctx.f[p]
            gr = y1 in ctx.g[ell] or y2 in ctx.g[ell]
            if fl or gr:
                internal += weight
            if fl:
                left_hit += weight
            if gr:
                right_hit += weight
            if fl and gr:
                joint_lr += weight
            dl = x1 in ctx.f[p] and x2 in ctx.f[p]
            dr = y1 in ctx.g[ell] and y2 in ctx.g[ell]
            if dl or dr:
                source_id = ctx.provenance[tuple(sorted((v,w)))]
                source_point,source_line = ctx.inc[source_id]
                if dl:
                    if source_point != p:
                        raise AssertionError('both-left anchor match must be true original middle point')
                    double_left += weight
                if dr:
                    if source_line != ell:
                        raise AssertionError('both-right anchor match must be true original middle line')
                    double_right += weight
                if dl and dr:
                    if (source_point,source_line)!=(p,ell):
                        raise AssertionError('double original anchor middle incidence mismatch')
                    double_both += weight
        if not total:
            raise ValueError('no nonbacktracking paths exist in selected graph')
        if require_stationary and total != 2*ctx.m:
            raise AssertionError('stationary NB law mass != 2m')
        # Reversal-preserving subprobabilities; validate independent path-pair
        # ordered collision summation, normalized by total raw path mass.
        Af = sum(x*x for x in raw_f.values())/total**2
        Ag = sum(x*x for x in raw_g.values())/total**2
        if independent_collision and (Af,Ag)!=(collision_f/total**2,
                                              collision_g/total**2):
            raise AssertionError('independent pair collision recurrence mismatch')

        clean_pairs = {
            (q,r) for (q,r),(p,ell) in ctx.anchor.items()
            if set(ctx.f[p]).isdisjoint(ctx.f[q]) and
               set(ctx.g[ell]).isdisjoint(ctx.g[r])
        }
        clean_carrier_size = 2*len(clean_pairs)
        carrier_size = 2*len(ctx.anchor)
        if carrier_size != 2*ctx.N*ctx.s**2:
            raise AssertionError('ORIGINAL GQ anchor fiber support identity false')
        # An anchor's p lies on r and ell passes through q. Each original
        # nonincident q,r has precisely two f(p) and two g(ell) coordinates.
        carrier_f=sum(m for (q,r,x),m in raw_f.items()
                      if x in ctx.f[ctx.anchor[q,r][0]])
        carrier_g=sum(m for (q,r,y),m in raw_g.items()
                      if y in ctx.g[ctx.anchor[q,r][1]])
        theta=internal/total
        theta_left=left_hit/total
        theta_right=right_hit/total
        Cf=carrier_f/total
        Cg=carrier_g/total
        if not (theta <= theta_left+theta_right and
                theta_left <= 2*Cf and theta_right <= 2*Cg):
            raise AssertionError('anchor event to reversible first-inner-event failed')
        if not (Cf*Cf <= clean_carrier_size*Af and
                Cg*Cg <= clean_carrier_size*Ag):
            raise AssertionError('GQ anchor support Cauchy bound failed')
        gap=16*ctx.N*ctx.s**2*(Af+Ag)-theta**2
        clean_gap=16*len(clean_pairs)*(Af+Ag)-theta**2
        if clean_gap < 0 or gap < clean_gap:
            raise AssertionError('A1-CLEAN all-h anchor-lifted inequality failed')
        # More discriminating but still only a necessary obstruction.
        # Compare with energies after forgetting one original endpoint:
        marginal_f=defaultdict(Fraction)
        marginal_g=defaultdict(Fraction)
        for (q,r,x),mass in raw_f.items():
            marginal_f[r,x] += mass
        for (q,r,y),mass in raw_g.items():
            marginal_g[q,y] += mass
        unlifted_f=sum(m*m for m in marginal_f.values())/total**2
        unlifted_g=sum(m*m for m in marginal_g.values())/total**2
        if Af>unlifted_f or Ag>unlifted_g:
            raise AssertionError('lifting original endpoint unexpectedly increased L2')
        # A3: exact orthogonal/Parseval decomposition relative to each
        # ORIGINAL q,r endpoint fiber. The common endpoint marginal t(q,r)
        # is shared by both coordinate sides.
        end_from_f = defaultdict(Fraction)
        end_from_g = defaultdict(Fraction)
        for (q,r,x), v in raw_f.items():
            end_from_f[q,r] += v
        for (q,r,y), v in raw_g.items():
            end_from_g[q,r] += v
        if dict(end_from_f) != dict(endpoint_mass) or dict(end_from_g) != dict(endpoint_mass):
            raise AssertionError('original endpoint marginal mismatch')
        T2 = sum(t*t for t in endpoint_mass.values()) / total**2
        residual_f = Af - T2/ctx.a
        residual_g = Ag - T2/ctx.a
        if residual_f < 0 or residual_g < 0:
            raise AssertionError('A3 nonnegative conditional-coordinate residual violated')
        if clean_pairs and T2 < (eligible/total)**2/len(clean_pairs):
            raise AssertionError('original end-clean marginal CS lower violated')
        # B1/B2: CENTERED source-anchor covariance. End-clean proper paths
        # have x1 outside f(q), y1 outside g(r): use n=a-2, NOT a.
        # The following quantities are EXACT rationals, no sqrt/roundoff.
        P = eligible/total
        n = ctx.a-2
        if n < 2:
            raise AssertionError('proper endpoint coordinate alphabet too small')
        delta_f = Cf - Fraction(2,n)*P
        delta_g = Cg - Fraction(2,n)*P
        reduced_residual_f = Af - T2/n
        reduced_residual_g = Ag - T2/n
        if reduced_residual_f < 0 or reduced_residual_g < 0:
            raise AssertionError('reduced-support source-coordinate Parseval invalid')
        reduced_R = reduced_residual_f + reduced_residual_g
        uncentered_baseline = Fraction(8,n)*P
        centered_excess = max(Fraction(), theta-uncentered_baseline)
        centered_covariance = delta_f+delta_g
        if theta > uncentered_baseline+2*centered_covariance:
            raise AssertionError('reversal-invariant anchor union versus signed covariance')
        # B3 EXACT ORIGINAL middle-incidence accounting, not just union bound.
        # For the left event: P[x1 or x2 in f(p)] = 2*Gamma_f - P[both].
        # Same on right; subtract the joint left/right union intersection.
        D_left = double_left/total
        D_right = double_right/total
        D_overlap = joint_lr/total
        D_total = D_left+D_right+D_overlap
        if theta != 2*(Cf+Cg)-D_total:
            raise AssertionError('B3 exact original anchor inclusion-exclusion failed')
        if theta != uncentered_baseline+2*centered_covariance-D_total:
            raise AssertionError('B3 centered source-anchor exact identity failed')
        if double_both > min(double_left,double_right):
            raise AssertionError('source middle intersection tally impossible')
        # Delta_f + Delta_g is the EXACT projection against the centered
        # 2-coordinate ORIGINAL GQ anchor indicator on the a-2 legal labels.
        # Its Gram norm squared is 2*C_clean*(2-4/n)*reduced_R.
        covariance_budget = 2*len(clean_pairs)*(2-Fraction(4,n))*reduced_R
        if centered_covariance**2 > covariance_budget:
            raise AssertionError('B1 centered anchor covariance CS violation')
        excess_budget = 16*len(clean_pairs)*(1-Fraction(2,n))*reduced_R
        if centered_excess**2 > excess_budget:
            raise AssertionError('B1 centered anchor energy obstruction violated')
        # B2: a weighted conditional chi-square residual. Handles
        # concentration of endpoint masses without multiplying by C_clean.
        raw_squares_f = defaultdict(Fraction)
        raw_squares_g = defaultdict(Fraction)
        for (q,r,x),mass in raw_f.items():
            raw_squares_f[q,r] += mass*mass
        for (q,r,y),mass in raw_g.items():
            raw_squares_g[q,r] += mass*mass
        Qf = (sum(raw_squares_f[key]/t for key,t in endpoint_mass.items())
              / total - P/n)
        Qg = (sum(raw_squares_g[key]/t for key,t in endpoint_mass.items())
              / total - P/n)
        if Qf < 0 or Qg < 0:
            raise AssertionError('B2 negative conditional chi-square residual')
        q_excess_budget = 16*P*(1-Fraction(2,n))*(Qf+Qg)
        if centered_excess**2 > q_excess_budget:
            raise AssertionError('B2 weighted conditional chi-square CS violated')
        if not (reduced_R <= residual_f+residual_g):
            raise AssertionError('reduced-support residual must improve A3')
        # Full-a version follows as a consequence from reduced-support
        # centered inequality and can also be checked independently.
        excess_a = max(Fraction(),theta-Fraction(8,ctx.a)*P)
        a_budget = 16*len(clean_pairs)*(1-Fraction(2,ctx.a))*(residual_f+residual_g)
        if excess_a**2 > a_budget:
            raise AssertionError('A4 full-alphabet centered energy violated')
        return {
            's':ctx.s, 'N':ctx.N,
            'original_incidences_selected':len(ctx.selected),
            'physical_edges':ctx.m,
            'oriented_nb_walks':path_count,
            'improper_nb_paths':improper,
            'conditional_on_survival':total != 2*ctx.m,
            'raw_nb_mass':str(total),
            'eligible_end_clean_mass':str(eligible/total),
            'theta_internal_only':str(theta),
            'theta_left':str(theta_left),'theta_right':str(theta_right),
            'anchor_carrier_size_each':carrier_size,
            'clean_original_endpoint_pairs':len(clean_pairs),
            'clean_carrier_size_each':clean_carrier_size,
            'anchor_first_left_mass':str(Cf),
            'anchor_first_right_mass':str(Cg),
            'A_f':str(Af),'A_g':str(Ag),
            'original_endpoint_collision_T2':str(T2),
            'endpoint_uniform_baseline_2T2_over_a':str(2*T2/ctx.a),
            'left_coordinate_residual':str(residual_f),
            'right_coordinate_residual':str(residual_g),
            'A3_parseval_validated':True,
            'B1_B2_centered_validated':True,
            'B3_exact_inclusion_exclusion':True,
            'middle_source_double_left':str(D_left),
            'middle_source_double_right':str(D_right),
            'simultaneous_left_right_internal':str(D_overlap),
            'middle_source_both_double':str(double_both/total),
            'B3_total_nonnegative_correction':str(D_total),
            'B3_union_identity_rhs':str(uncentered_baseline+2*centered_covariance-D_total),
            'proper_internal_alphabet_n':n,
            'proper_endpoint_uniform_baseline_2T2_over_n':str(Fraction(2,n)*T2),
            'proper_left_coordinate_residual':str(reduced_residual_f),
            'proper_right_coordinate_residual':str(reduced_residual_g),
            'anchor_covariance_left':str(delta_f),
            'anchor_covariance_right':str(delta_g),
            'anchor_covariance_total':str(centered_covariance),
            'proper_uniform_union_baseline':str(uncentered_baseline),
            'centered_excess':str(centered_excess),
            'B1_excess_budget':str(excess_budget),
            'B1_slack':str(excess_budget-centered_excess**2),
            'conditional_chisquare_Q_f':str(Qf),
            'conditional_chisquare_Q_g':str(Qg),
            'B2_excess_budget':str(q_excess_budget),
            'B2_slack':str(q_excess_budget-centered_excess**2),
            'A4_full_a_slack':str(a_budget-excess_a**2),
            'N_s2_times_anchor_energy':str(ctx.N*ctx.s**2*(Af+Ag)),
            'unlifted_same_restricted_f':str(unlifted_f),
            'unlifted_same_restricted_g':str(unlifted_g),
            'A1_slack':str(gap),
            'A1_clean_slack':str(clean_gap),
            'A1_clean_bound': 'theta_I^2 <= 16*C_clean*(A_f+A_g)',
            'root_Branch_A_proved':False,
        }


def report():
    from hyp105_issue230_projection import fixture
    from hyp105_issue230_paired_gstar import paired_gstar
    rows=[]
    for scheme in ('lex','reverse','S68','S72'):
        model=fixture(1,scheme)
        full=AnchorLiftedEnergy(model).census(independent_collision=True)
        full['scheme']=scheme
        full['source_graph']='complete G (not G*)'
        rows.append(full)
        reg=paired_gstar(model)
        try:
            refined=AnchorLiftedEnergy(model, selected=reg['original_incidence_ids']).census(
                require_proper=True,independent_collision=True)
            refined['scheme']=scheme
            refined['source_graph']='paired G* (finite conditional NB)'
            rows.append(refined)
        except ValueError as exc:
            if 'no nonbacktracking paths' not in str(exc):
                raise
            rows.append({'scheme':scheme,'source_graph':'paired G*',
                         'nb_status':'no NB3; finite asymptotic theorem inapplicable',
                         'selected_source_ids':reg['final_original_count']})
    return {'status':'RESTRICTED_THEOREM_C',
            'scope':'exact W32 ORIGINAL anchor lifted finite energy; no asymptotic bound',
            'root_A': 'OPEN', 'rows':rows}


if __name__ == '__main__':
    print(json.dumps(report(),indent=2,sort_keys=True))
