"""EICE-003-C: exact ORIGINAL middle-incidence transport kernel.

Research only. C1-C4 all-h identities and source-overlap spectral factorization.
No universal theta_I < 1-eta, no Branch A or ASET exponent.
"""
from collections import Counter, defaultdict
from fractions import Fraction
import json
from math import log

from hyp105_issue230_endpoint_energy import EndpointEnergy


def original_overlap(left, right):
    """TRUE 0/1 original-factor intersection for distinct injective pair maps."""
    return int(left[0] in right or left[1] in right)


def original_overlap_gram(left, right, same_factor):
    """H H^T - I exact source intersection identity (including diagonal)."""
    return sum(int(x in right) for x in left) - int(same_factor)



def list_information_lower_bound(theta, midpoint_sources, max_block_list):
    """C6: Shannon list-decoding obstruction in nats, NOT a spectral bound.

    Requires uniform true middle-original-source marginal. theta is the
    full-law probability of being in the actual blocker list of the
    eligible ORIGINAL endpoint row, with ineligible paths assigned ⊥.
    """
    if not (0 <= theta <= 1) or midpoint_sources < 1 or not (
            1 <= max_block_list <= midpoint_sources):
        raise ValueError('invalid source list information parameters')
    if theta == 0 or theta == 1:
        binary=0.0
    else:
        binary=-theta*log(theta)-(1-theta)*log(1-theta)
    return theta*log(midpoint_sources/max_block_list)-binary



def binary_relative_entropy(p,q):
    """Bernoulli KL in nats, with continuous endpoint conventions."""
    if not (0 <= p <= 1 and 0 <= q <= 1):
        raise ValueError('invalid Bernoulli probabilities')
    if p==q:
        return 0.0
    if q==0 or q==1:
        return float('inf')
    value=0.0
    if p:
        value+=p*log(p/q)
    if p<1:
        value+=(1-p)*log((1-p)/(1-q))
    return value


class OriginalMiddleTransport:
    """Joint endpoint/source-midpoint weighted NB3 tensor with typed provenance."""

    def __init__(self, model, selected=None):
        self.ctx = EndpointEnergy(model, selected=selected)

    def census(self, *, max_paths=1_000_000, require_proper=False,
               require_stationary=False, independent_oracle=False):
        ctx=self.ctx
        if type(max_paths) is not int or max_paths < 1:
            raise ValueError('positive integer walk budget required')
        if require_stationary and (not ctx.m or
                                   any(0 < d < 2 for d in ctx.degree)):
            raise ValueError('stationary middle-source law requires active min-degree >=2')
        a=ctx.a
        E=set(ctx.selected)
        M=len(E)
        if M != ctx.m//2:
            raise AssertionError('source pair coherence violated')
        source_middle=defaultdict(Fraction)
        joint=defaultdict(Fraction)
        Z=elig=left=right=left_right=theta=Fraction()
        gram_f=gram_g=diag_p=diag_l=Fraction()
        proper_paths=bad_paths=0
        for (z0,z1,z2,z3),w in ctx._iter_nb(max_paths):
            Z += w
            key=tuple(sorted((z1,z2)))
            source_id=ctx.provenance[key]
            if source_id not in E:
                raise AssertionError('physical middle edge lacks ORIGINAL incidence ID')
            source_middle[source_id] += w
            x0,y0=divmod(z0,a)
            x1,y1=divmod(z1,a)
            x2,y2=divmod(z2,a)
            x3,y3=divmod(z3,a)
            if len({x0,x1,x2,x3})!=4 or len({y0,y1,y2,y3})!=4:
                bad_paths += 1
                if require_proper:
                    raise ValueError('improper original physical NB3 path in alleged G*')
                continue
            proper_paths += 1
            q=ctx.fi.get(tuple(sorted((x0,x3))))
            r=ctx.gi.get(tuple(sorted((y0,y3))))
            if q is None or r is None or (q,r) not in ctx.anchor:
                continue
            p,l=ctx.anchor[q,r]
            if set(ctx.f[p]) & set(ctx.f[q]) or set(ctx.g[l]) & set(ctx.g[r]):
                continue
            elig += w
            p2,l2=ctx.inc[source_id]
            joint[q,r,source_id]+=w
            overlap_f=original_overlap(ctx.f[p],ctx.f[p2])
            overlap_g=original_overlap(ctx.g[l],ctx.g[l2])
            gf=original_overlap_gram(ctx.f[p],ctx.f[p2],p==p2)
            gg=original_overlap_gram(ctx.g[l],ctx.g[l2],l==l2)
            if gf!=overlap_f or gg!=overlap_g:
                raise AssertionError('true source Gram H H^T-I intersection failed')
            lf=bool(overlap_f)
            rg=bool(overlap_g)
            # Physically x1,x2 are exactly the two coords of ORIGINAL f(p2).
            if (lf != bool(set(ctx.f[p]) & {x1,x2}) or
                    rg != bool(set(ctx.g[l]) & {y1,y2})):
                raise AssertionError('midpoint provenance overlap disagrees with physical mask')
            gram_f += w*(overlap_f+int(p==p2))
            gram_g += w*(overlap_g+int(l==l2))
            diag_p += w*int(p==p2)
            diag_l += w*int(l==l2)
            if lf:
                left += w
            if rg:
                right += w
            if lf and rg:
                left_right += w
            if lf or rg:
                theta += w

        if not Z:
            raise ValueError('no nonbacktracking length-three paths')
        if require_stationary and Z!=2*ctx.m:
            raise AssertionError('stationary source midpoint normalization !=2m')
        is_stationary=(Z==2*ctx.m)
        if is_stationary:
            if any(source_middle[e]!=Z/M for e in E):
                raise AssertionError('ALL-h uniform original middle-source marginal failed')
        if theta!=left+right-left_right:
            raise AssertionError('C1 original source union failed')
        if theta!=gram_f+gram_g-diag_p-diag_l-left_right:
            raise AssertionError('C2 original Gram plus diagonal corrections failed')

        # An independent oracle uses the aggregated REAL ORIGINAL
        # (original endpoint point q, original endpoint line r, middle
        # original incidence ID) transport, not the physical-path masks.
        if independent_oracle:
            alt_l=alt_r=alt_both=Fraction()
            for (q,r,e),wt in joint.items():
                p,l=ctx.anchor[q,r]
                p2,l2=ctx.inc[e]
                f=bool(set(ctx.f[p]).intersection(ctx.f[p2]))
                g=bool(set(ctx.g[l]).intersection(ctx.g[l2]))
                if f:
                    alt_l+=wt
                if g:
                    alt_r+=wt
                if f and g:
                    alt_both+=wt
            if (alt_l,alt_r,alt_both)!=(left,right,left_right):
                raise AssertionError('independent ORIGINAL joint transport oracle disagreed')

        # C3 source row sparsity on true globally injective physical pair
        # maps.  Each fixed physical pair f(p) meets at most 2a-3 other
        # original point labels INCLUDING itself.
        for labels in (ctx.f,ctx.g):
            for p in range(ctx.v):
                degree=sum(original_overlap(labels[p],other) for other in labels)
                if degree>2*a-3:
                    raise AssertionError('physical K_a line-graph source capacity violated')
        source_row_bound = min(M, 2*(2*a-3)*(ctx.s+1))
        seen_endpoints=sorted({(q,r) for q,r,e in joint})
        end_t=defaultdict(Fraction)
        for (q,r,e),wt in joint.items():
            end_t[q,r] += wt
        # Precompute sparse ORIGINAL middle incidence masks per source
        # anchor factor; many distinct (q,r) endpoint fibers share one
        # projected original anchor (p,ell). The mask is built from the
        # original source IDs, never from fictitious physical adjacency.
        anchor_points={ctx.anchor[q,r][0] for q,r in seen_endpoints}
        anchor_lines={ctx.anchor[q,r][1] for q,r in seen_endpoints}
        left_source_masks={
            p:{e for e in E if original_overlap(ctx.f[p],ctx.f[ctx.inc[e][0]])}
            for p in anchor_points
        }
        right_source_masks={
            l:{e for e in E if original_overlap(ctx.g[l],ctx.g[ctx.inc[e][1]])}
            for l in anchor_lines
        }
        full_anchor_masks={}
        row_counts=[]
        beta_weight=Fraction()
        for q,r in seen_endpoints:
            p,l=ctx.anchor[q,r]
            if (p,l) not in full_anchor_masks:
                full_anchor_masks[p,l]=left_source_masks[p] | right_source_masks[l]
            blocked=len(full_anchor_masks[p,l])
            if blocked>source_row_bound:
                raise AssertionError('original source overlap sparsity row bound failed')
            row_counts.append(blocked)
            beta_weight+=end_t[q,r]*Fraction(blocked,M)

        # C4: exact centered original source-incidence transport. The
        # uniformly averaged kernel B row is computed ONCE per true anchor,
        # not for every observed middle source cell.
        signed_raw=Fraction()
        for (q,r,e),wt in joint.items():
            p,l=ctx.anchor[q,r]
            blocked_mask=full_anchor_masks[p,l]
            signed_raw+=wt*(int(e in blocked_mask)-Fraction(len(blocked_mask),M))
        if theta!=signed_raw+beta_weight:
            raise AssertionError('C4 exact centered source-middle identity invalid')

        # C6: exact ORIGINAL endpoint-symbol/middle-source joint law.
        # Every ineligible physical path is grouped into a special ⊥ row.
        # For *stationary* G* the column marginal is uniformly 1/M; apply
        # Shannon's list bound, with float logs used ONLY for diagnostics
        # (the all-h inequality is proved analytically in the document).
        info_nats=None
        info_lower_nats=None
        info_binary_kl_nats=None
        if is_stationary:
            row_source_eligible=defaultdict(Fraction)
            for (q,r,e),wt in joint.items():
                row_source_eligible[e] += wt
            bottom={e:source_middle[e]-row_source_eligible[e] for e in E}
            if any(w<0 for w in bottom.values()):
                raise AssertionError('eligible ORIGINAL midpoint mass > all NB midpoint mass')
            bottom_mass=Z-elig
            if bottom_mass != sum(bottom.values(),Fraction()):
                raise AssertionError('ineligible endpoint ⊥ row marginal wrong')
            info_nats=0.0
            for (q,r,e),wt in joint.items():
                if wt:
                    m_row=end_t[q,r]
                    info_nats += float(wt/Z)*log(float(Fraction(wt*M,m_row)))
            if bottom_mass:
                for e,w in bottom.items():
                    if w:
                        info_nats += float(w/Z)*log(float(Fraction(w*M,bottom_mass)))
            info_lower_nats=list_information_lower_bound(
                float(theta/Z),M,source_row_bound)
            info_binary_kl_nats=binary_relative_entropy(
                float(theta/Z),float(beta_weight/Z))
            if info_nats+1e-10 < info_binary_kl_nats:
                raise AssertionError('C7 true ORIGINAL Bernoulli data-processing KL invalid')
            if info_nats+1e-10 < info_lower_nats:
                raise AssertionError('C6 original midpoint Shannon list bound invalid')

        # A stationary full-graph midpoint marginal is exactly 1/M, but
        # the TRUE conditional endpoint/source transport can be correlated.
        # No theorem bounds its signed covariance on valid G*.
        return {
            's':ctx.s,'a':a,'original_incidence_total':ctx.N,
            'original_midpoint_source_count':M,
            'physical_edges':ctx.m,
            'oriented_nb_walks':proper_paths+bad_paths,
            'coordinate_proper_walks':proper_paths,'improper_nb_walks':bad_paths,
            'raw_nb_weight':str(Z),'stationary_midpoint':is_stationary,
            'conditioned_survival':not is_stationary,
            'eligible_end_clean_mass':str(elig/Z),
            'theta_internal_only':str(theta/Z),
            'true_left_overlap_mass':str(left/Z),
            'true_right_overlap_mass':str(right/Z),
            'true_double_lr_mass':str(left_right/Z),
            'gram_f_mass':str(gram_f/Z),
            'gram_g_mass':str(gram_g/Z),
            'original_middle_equals_anchor_point':str(diag_p/Z),
            'original_middle_equals_anchor_line':str(diag_l/Z),
            'C2_exact_identity_rhs':str((gram_f+gram_g-diag_p-diag_l-left_right)/Z),
            'max_original_source_blocked_row':max(row_counts,default=0),
            'original_source_row_bound':source_row_bound,
            'eligible_original_endpoint_rows':len(seen_endpoints),
            'C4_source_uniform_baseline':str(beta_weight/Z),
            'C4_signed_original_transport':str(signed_raw/Z),
            'C4_exact_total':str((beta_weight+signed_raw)/Z),
            'all_h_source_gram_rank_upper':a,
            'source_gram_shift_eigenvalue':'-1 on kernel(H^T), multiplicity >= V-a',
            'middle_uniform_alone_proves_gap':False,
            'C6_info_nats_diagnostic':info_nats,
            'C6_list_lower_nats_diagnostic':info_lower_nats,
            'C7_binary_data_processing_kl_nats':info_binary_kl_nats,
            'C6_log_base':'natural',
            'C6_info_theorem_requires_unconditional_stationary':True,
            'root_Branch_A_proved':False,
        }


def midpoint_only_no_go(model):
    """A RELAXED transport, NOT a true path law: uniform source marginal,
    all source-middle points are their chosen endpoint's true GQ anchors.

    Crucially, end-clean + physical path realizability are NOT imposed.
    It falsifies arguments using ONLY midpoint uniformity and source Gram
    row sparsity to bound blocking. It does NOT falsify Branch A.
    """
    ctx=EndpointEnergy(model)
    witness=[]
    for e,(p,l) in enumerate(ctx.inc):
        q_candidates=sorted(q for (q,r),(anchor_p,ell) in ctx.anchor.items()
                            if r==l and anchor_p==p)
        if not q_candidates:
            raise AssertionError('true GQ axiom must supply projected end q')
        q=q_candidates[0]
        if (q,l) in ctx.edge_id or ctx.anchor[q,l][0]!=p:
            raise AssertionError('relaxed witness not a valid ORIGINAL projection')
        witness.append((e,q,l))
    return {
        'label':'RELAXED TRANSPORT ONLY: no end-clean or true physical NB3',
        'true_original_middle_sources':len(witness),
        'uniform_middle_marginal_each':str(Fraction(1,len(witness))),
        'every_middle_point_equals_true_anchor_point':True,
        'relaxed_internal_overlap_mass':'1',
        'actual_branch_A_counterexample':False,
    }


def report():
    from hyp105_issue230_projection import fixture
    from hyp105_issue230_paired_gstar import paired_gstar
    results=[]
    for scheme in ('lex','reverse','S68','S72'):
        model=fixture(1,scheme)
        full=OriginalMiddleTransport(model).census(independent_oracle=True)
        full['scheme']=scheme
        full['scope']='full ORIGINAL W32 G (not certified G*)'
        results.append(full)
        ids=paired_gstar(model)['original_incidence_ids']
        try:
            reg=OriginalMiddleTransport(model,selected=ids).census(
                require_proper=True,independent_oracle=True)
            reg['scheme']=scheme
            reg['scope']='finite coherent paired G*, conditional NB if leaves'
            results.append(reg)
        except ValueError as ex:
            if 'no nonbacktracking length-three paths' not in str(ex):
                raise
            results.append({'scheme':scheme,
                            'scope':'finite coherent paired G* without NB3'})
    return {'status':'RESTRICTED_THEOREM_C','root_A':'OPEN',
            'results':results,'marginal_only_relaxation':midpoint_only_no_go(fixture(1,'lex'))}


if __name__=='__main__':
    print(json.dumps(report(),indent=2,sort_keys=True))
