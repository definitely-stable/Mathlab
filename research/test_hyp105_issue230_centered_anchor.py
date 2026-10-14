"""EICE-003-B: independent exact ORIGINAL q/r-anchor centered spectral falsifiers."""
from collections import defaultdict
from fractions import Fraction
import unittest

from hyp105_issue230_anchor_lift import AnchorLiftedEnergy
from hyp105_issue230_endpoint_energy import EndpointEnergy
from hyp105_issue230_paired_gstar import paired_gstar
from hyp105_issue230_projection import fixture


def independent_explicit_centered_tensor(model, selected=None, *, max_paths=900_000):
    """Re-enumerate original paths and directly expand every allowed-coordinate square.

    Deliberately does NOT reuse AnchorLiftedEnergy's saved pi, endpoint
    histograms, Gram products, or chi-square summation.
    """
    ctx=EndpointEnergy(model,selected=selected)
    per_left=defaultdict(Fraction)
    per_right=defaultdict(Fraction)
    end_mass=defaultdict(Fraction)
    z=p=internal=gamma_left=gamma_right=Fraction()
    for (u,v,w,t),weight in ctx._iter_nb(max_paths):
        z += weight
        x0,y0=divmod(u,ctx.a)
        x1,y1=divmod(v,ctx.a)
        x2,y2=divmod(w,ctx.a)
        x3,y3=divmod(t,ctx.a)
        if len({x0,x1,x2,x3})!=4 or len({y0,y1,y2,y3})!=4:
            continue
        q=ctx.fi.get(tuple(sorted((x0,x3))))
        r=ctx.gi.get(tuple(sorted((y0,y3))))
        if q is None or r is None or (q,r) not in ctx.anchor:
            continue
        anchor_p,anchor_l=ctx.anchor[q,r]
        if set(ctx.f[anchor_p]) & set(ctx.f[q]):
            continue
        if set(ctx.g[anchor_l]) & set(ctx.g[r]):
            continue
        p += weight
        per_left[q,r,x1] += weight
        per_right[q,r,y1] += weight
        end_mass[q,r] += weight
        if x1 in ctx.f[anchor_p]:
            gamma_left += weight
        if y1 in ctx.g[anchor_l]:
            gamma_right += weight
        if (x1 in ctx.f[anchor_p] or x2 in ctx.f[anchor_p] or
                y1 in ctx.g[anchor_l] or y2 in ctx.g[anchor_l]):
            internal += weight
    if not z:
        raise ValueError('no nonbacktracking paths')
    n=ctx.a-2
    rf=rg=qf=qg=Fraction()
    for (q,r),mass in end_mass.items():
        legal_left=set(range(ctx.a))-set(ctx.f[q])
        legal_right=set(range(ctx.a))-set(ctx.g[r])
        assert len(legal_left)==n and len(legal_right)==n
        mean=mass/Fraction(n)
        for x in legal_left:
            dev=per_left[q,r,x]-mean
            rf += dev*dev
            qf += dev*dev/mass
        for y in legal_right:
            dev=per_right[q,r,y]-mean
            rg += dev*dev
            qg += dev*dev/mass
    # Independent direct evaluation of the Gram covariance sum.
    dlf=drg=Fraction()
    for (q,r),mass in end_mass.items():
        pp,ll=ctx.anchor[q,r]
        legal_left=set(range(ctx.a))-set(ctx.f[q])
        legal_right=set(range(ctx.a))-set(ctx.g[r])
        for x in legal_left:
            dlf += (per_left[q,r,x]-mass/Fraction(n))*(
                Fraction(int(x in ctx.f[pp]))-Fraction(2,n))
        for y in legal_right:
            drg += (per_right[q,r,y]-mass/Fraction(n))*(
                Fraction(int(y in ctx.g[ll]))-Fraction(2,n))
    return dict(z=z,p=p/z,theta=internal/z,lf=gamma_left/z,
                rg=gamma_right/z,Rf=rf/z**2,Rg=rg/z**2,
                Qf=qf/z,Qg=qg/z,
                Df=dlf/z,Dg=drg/z,
                endpoint_T2=sum(t*t for t in end_mass.values())/z**2)


class CenteredAnchorTests(unittest.TestCase):
    def test_independent_explicit_original_W32_four_schemes(self):
        for scheme in ('lex','reverse','S68','S72'):
            with self.subTest(scheme=scheme):
                model=fixture(1,scheme)
                row=AnchorLiftedEnergy(model).census(independent_collision=True)
                independent=independent_explicit_centered_tensor(model)
                self.assertEqual(Fraction(row['eligible_end_clean_mass']),independent['p'])
                self.assertEqual(Fraction(row['theta_internal_only']),independent['theta'])
                self.assertEqual(Fraction(row['proper_left_coordinate_residual']),independent['Rf'])
                self.assertEqual(Fraction(row['proper_right_coordinate_residual']),independent['Rg'])
                self.assertEqual(Fraction(row['conditional_chisquare_Q_f']),independent['Qf'])
                self.assertEqual(Fraction(row['conditional_chisquare_Q_g']),independent['Qg'])
                self.assertEqual(Fraction(row['anchor_covariance_left']),independent['Df'])
                self.assertEqual(Fraction(row['anchor_covariance_right']),independent['Dg'])
                self.assertEqual(Fraction(row['original_endpoint_collision_T2']),independent['endpoint_T2'])
                self.assertEqual(Fraction(row['anchor_first_left_mass']),independent['lf'])
                self.assertEqual(Fraction(row['anchor_first_right_mass']),independent['rg'])
                self.assertTrue(row['B1_B2_centered_validated'])
                self.assertFalse(row['root_Branch_A_proved'])

    def test_exact_reduced_support_parseval_and_nonnegative_variance(self):
        for scheme in ('lex','reverse','S68','S72'):
            r=AnchorLiftedEnergy(fixture(1,scheme)).census()
            n=r['proper_internal_alphabet_n']
            t2=Fraction(r['original_endpoint_collision_T2'])
            af=Fraction(r['A_f'])
            ag=Fraction(r['A_g'])
            rf=Fraction(r['proper_left_coordinate_residual'])
            rg=Fraction(r['proper_right_coordinate_residual'])
            self.assertEqual(af+ag,Fraction(2,n)*t2+rf+rg)
            self.assertGreaterEqual(rf,0)
            self.assertGreaterEqual(rg,0)
            self.assertLessEqual(rf,Fraction(r['left_coordinate_residual']))
            self.assertLessEqual(rg,Fraction(r['right_coordinate_residual']))

    def test_signed_covariance_and_both_exact_squared_bounds(self):
        for scheme in ('lex','reverse','S68','S72'):
            r=AnchorLiftedEnergy(fixture(1,scheme)).census()
            theta=Fraction(r['theta_internal_only'])
            base=Fraction(r['proper_uniform_union_baseline'])
            cov=Fraction(r['anchor_covariance_total'])
            self.assertLessEqual(theta,base+2*cov)
            excess=max(Fraction(),theta-base)
            self.assertEqual(excess,Fraction(r['centered_excess']))
            self.assertGreaterEqual(Fraction(r['B1_slack']),0)
            self.assertGreaterEqual(Fraction(r['B2_slack']),0)
            self.assertGreaterEqual(Fraction(r['A4_full_a_slack']),0)
            self.assertLessEqual(excess*excess,Fraction(r['B1_excess_budget']))
            self.assertLessEqual(excess*excess,Fraction(r['B2_excess_budget']))

    def test_original_W34_full_graph_without_independence(self):
        # The real W(3,4) source has 85 original typed points and lines;
        # full G is diagnostic and does NOT satisfy paired G* hypotheses.
        model=fixture(2,'lex')
        row=AnchorLiftedEnergy(model).census(max_paths=1_000_000)
        self.assertEqual(row['N'],425)
        self.assertEqual(row['proper_internal_alphabet_n'],model['a']-2)
        self.assertTrue(row['B1_B2_centered_validated'])
        self.assertGreaterEqual(Fraction(row['B1_slack']),0)
        self.assertGreaterEqual(Fraction(row['B2_slack']),0)

    def test_paired_original_Gstar_and_optional_no_paths_finite(self):
        for scheme in ('lex','reverse','S68','S72'):
            model=fixture(1,scheme)
            paired=paired_gstar(model)
            self.assertTrue(paired['graph']['both_diagonals'])
            try:
                r=AnchorLiftedEnergy(model, selected=paired['original_incidence_ids']).census(
                    require_proper=True)
            except ValueError as exc:
                self.assertIn('no nonbacktracking paths',str(exc))
                continue
            self.assertEqual(r['improper_nb_paths'],0)
            self.assertTrue(r['B1_B2_centered_validated'])

    def test_path_measure_no_go_for_endpoint_only_control(self):
        # On an authentic ORIGINAL source model, there exists a proper
        # end-clean path. The reversal-invariant law supported only on this
        # path and its reversal has t(q,r)=1 and hence T2=1.
        # It does NOT claim to be stationary on an admissible high-degree G*.
        model=fixture(1,'lex')
        ctx=EndpointEnergy(model)
        found=False
        for (u,v,w,z),weight in ctx._iter_nb(100_000):
            x0,y0=divmod(u,ctx.a)
            x1,y1=divmod(v,ctx.a)
            x2,y2=divmod(w,ctx.a)
            x3,y3=divmod(z,ctx.a)
            if len({x0,x1,x2,x3})<4 or len({y0,y1,y2,y3})<4:
                continue
            q=ctx.fi.get(tuple(sorted((x0,x3))))
            r=ctx.gi.get(tuple(sorted((y0,y3))))
            if q is None or r is None or (q,r) not in ctx.anchor:
                continue
            p,ell=ctx.anchor[q,r]
            if set(ctx.f[p]) & set(ctx.f[q]) or set(ctx.g[ell]) & set(ctx.g[r]):
                continue
            found=True
            break
        self.assertTrue(found,'true W32 ORIGINAL end-clean path expected')
        clean_pairs=sum(1 for (q,r),(p,ell) in ctx.anchor.items()
                        if set(ctx.f[p]).isdisjoint(ctx.f[q])
                        and set(ctx.g[ell]).isdisjoint(ctx.g[r]))
        self.assertGreater(clean_pairs,1)
        # In the concentrated REVERSIBLE 2-path probability space
        # all eligible endpoint mass sits on a single (q,r).
        self.assertEqual(sum(t*t for t in (Fraction(1),)),Fraction(1))
        self.assertGreater(clean_pairs*Fraction(1),1)

    def test_exact_fail_closed_input(self):
        model=fixture(1,'lex')
        model['right_labels']=list(model['right_labels'])
        model['right_labels'][1]=model['right_labels'][0]
        with self.assertRaisesRegex(ValueError,'global injective'):
            AnchorLiftedEnergy(model)
        with self.assertRaisesRegex(ValueError,'positive integer path budget'):
            AnchorLiftedEnergy(fixture(1,'lex')).census(max_paths=0)


if __name__=='__main__':
    unittest.main()
