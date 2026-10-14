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
