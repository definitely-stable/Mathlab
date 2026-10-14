"""EICE-003-D: exact TRUE ORIGINAL GQ endpoint decoder from NB3 rectangles.

D1-D4 are structural identities/necessary entropy upper bounds for a coherent,
coordinate-bichromatic paired-diagonal G*. No universal gap on theta_I, no
Branch A/B, no ASET exponent. Full-G with cherries is fail-closed.
"""
from collections import defaultdict
from fractions import Fraction
from math import log
import json

from hyp105_issue230_endpoint_energy import EndpointEnergy
from hyp105_issue230_middle_transport import original_overlap


def binary_entropy(prob):
    if not 0 <= prob <= 1:
        raise ValueError("probability outside [0,1]")
    if prob == 0 or prob == 1:
        return 0.0
    return -prob*log(prob)-(1-prob)*log(1-prob)


def rectangle_entropy_ceiling(eligible_mass, clean_pairs, min_degree):
    """D4 Shannon upper for I(original endpoints or bottom; source midpoint).

    Requires a *stationary* edge-rooted NB law and a source-coherent
    bichromatic rectangle graph. NOT applicable to survival-conditioned NB.
    """
    if not 0 <= eligible_mass <= 1 or clean_pairs < 0 or min_degree < 2:
        raise ValueError("invalid stationary rectangle-entropy parameters")
    if eligible_mass == 0:
        return 0.0
    if clean_pairs == 0:
        raise ValueError("positive eligible mass with no end-clean endpoints")
    return (binary_entropy(eligible_mass) + eligible_mass*log(clean_pairs)
            - 2*eligible_mass*log(min_degree-1))


class OriginalNBRectangle:
    """Exact two-sided independent-neighbor transport of a true source edge."""

    def __init__(self, model, selected, colors_left, colors_right):
        self.ctx = EndpointEnergy(model, selected=selected)
        ctx = self.ctx
        if (len(colors_left) != ctx.a or len(colors_right) != ctx.a or
                any(type(c) is not int or c not in (0,1) for c in colors_left)
                or any(type(c) is not int or c not in (0,1) for c in colors_right)):
            raise ValueError("two complete fixed binary physical coordinate colors required")
        self.left_colors = tuple(colors_left)
        self.right_colors = tuple(colors_right)
        a = ctx.a
        for u, neigh in enumerate(ctx.adj):
            xs = [v//a for v in neigh]
            ys = [v%a for v in neigh]
            if len(xs) != len(set(xs)) or len(ys) != len(set(ys)):
                raise ValueError("non-coherent neighbor-coordinate cherry in source graph")
            for v in neigh:
                if (self.left_colors[u//a] == self.left_colors[v//a] or
                        self.right_colors[u%a] == self.right_colors[v%a]):
                    raise ValueError("physical edge violates two bichromatic cuts")
        if len(ctx.provenance) != 2*len(ctx.selected):
            raise AssertionError("source pair was split")

    def census(self, *, max_paths=500_000, independent_oracle=True):
        ctx=self.ctx
        if type(max_paths) is not int or max_paths < 1:
            raise ValueError("positive integer rectangle budget required")
        M=len(ctx.selected)
        if not M:
            raise ValueError("no selected original source incidences")
        npaths=rectangles=0
        Z=eligible=blocked=Fraction()
        missing_left_mass=missing_right_mass=missing_either_mass=Fraction()
        physical_unused_pairs=(a:=ctx.a)*(a-1)//2-ctx.v
        if not (0<=physical_unused_pairs<a-1):
            raise AssertionError("minimal physical alphabet or injection capacity invalid")
        raw_joint=defaultdict(Fraction)
        mid=defaultdict(Fraction)
        left_marg=defaultdict(Fraction)
        right_marg=defaultdict(Fraction)
        max_oriented_q=max_oriented_r=0
        source_q=defaultdict(set)
        source_r=defaultdict(set)
        source_row_support=defaultdict(set)
        max_rectangle_cell_weight=Fraction()
        for u, neigh in enumerate(ctx.adj):
            for v in neigh:
                source_id=ctx.provenance[tuple(sorted((u,v)))]
                first=sorted(neigh-{v})
                last=sorted(ctx.adj[v]-{u})
                rectangles+=1
                if not first or not last:
                    continue
                d1=len(first)
                d2=len(last)
                weight=Fraction(1,d1*d2)
                if weight > max_rectangle_cell_weight:
                    max_rectangle_cell_weight=weight
                qs=set()
                rs=set()
                physical_left_pairs=set()
                physical_right_pairs=set()
                missing_left_count=missing_right_count=missing_either_count=0
                for w in first:
                    for z in last:
                        npaths+=1
                        if npaths>max_paths:
                            raise ValueError("physical NB3 rectangle budget exceeded")
                        Z+=weight
                        mid[source_id]+=weight
                        x0,y0=divmod(w,ctx.a)
                        x1,y1=divmod(u,ctx.a)
                        x2,y2=divmod(v,ctx.a)
                        x3,y3=divmod(z,ctx.a)
                        if (len({x0,x1,x2,x3})!=4 or
                                len({y0,y1,y2,y3})!=4):
                            raise AssertionError("improper path survived paired G* certificate")
                        left_pair=tuple(sorted((x0,x3)))
                        right_pair=tuple(sorted((y0,y3)))
                        if (left_pair in physical_left_pairs or
                                right_pair in physical_right_pairs):
                            raise AssertionError("D5 physical K_a rectangle endpoint pair duplicated")
                        physical_left_pairs.add(left_pair)
                        physical_right_pairs.add(right_pair)
                        q=ctx.fi.get(left_pair)
                        r=ctx.gi.get(right_pair)
                        if q is None:
                            missing_left_count+=1
                            missing_left_mass+=weight
                        if r is None:
                            missing_right_count+=1
                            missing_right_mass+=weight
                        if q is None or r is None:
                            missing_either_count+=1
                            missing_either_mass+=weight
                        if q is not None:
                            if q in qs:
                                raise AssertionError("D2 left endpoint decoder not injective")
                            qs.add(q)
                        if r is not None:
                            if r in rs:
                                raise AssertionError("D2 right endpoint decoder not injective")
                            rs.add(r)
                        if q is None or r is None or (q,r) not in ctx.anchor:
                            continue
                        p,l=ctx.anchor[q,r]
                        if (set(ctx.f[p])&set(ctx.f[q]) or
                                set(ctx.g[l])&set(ctx.g[r])):
                            continue
                        eligible+=weight
                        raw_joint[q,r,source_id]+=weight
                        source_q[source_id,q].add(r)
                        source_r[source_id,r].add(q)
                        source_row_support[q,r].add(source_id)
                        left_marg[q,r]+=weight
                        right_marg[q,r]+=weight
                        p2,l2=ctx.inc[source_id]
                        if (original_overlap(ctx.f[p],ctx.f[p2]) or
                                original_overlap(ctx.g[l],ctx.g[l2])):
                            blocked+=weight
                if (len(physical_left_pairs)!=d1*d2 or
                        len(physical_right_pairs)!=d1*d2 or
                        missing_left_count>physical_unused_pairs or
                        missing_right_count>physical_unused_pairs or
                        missing_either_count>2*physical_unused_pairs):
                    raise AssertionError("D5 true physical near-complete decoder failed")
                max_oriented_q=max(max_oriented_q,len(qs))
                max_oriented_r=max(max_oriented_r,len(rs))

        if not Z:
            raise ValueError("no valid physical nonbacktracking rectangles")
        if rectangles != 2*ctx.m:
            raise AssertionError("oriented true source midpoint rectangles not 4M")
        if any(len(vals)>4 for vals in source_q.values()) or any(
                len(vals)>4 for vals in source_r.values()):
            raise AssertionError("D2 source-column endpoint support not four matchings")
        min_positive=min(d for d in ctx.degree if d)
        stationary=min_positive>=2
        if stationary:
            if Z!=2*ctx.m:
                raise AssertionError("stationary NB3 normalization failed")
            if any(mid.get(i,Fraction())!=4 for i in ctx.selected):
                raise AssertionError("D3 stationary original source midpoint not 4")
            atom_limit=Fraction(4,(min_positive-1)**2)
            if any(mass>atom_limit for mass in raw_joint.values()):
                raise AssertionError("D3 stationary endpoint-source atom cap violated")
        if missing_either_mass>missing_left_mass+missing_right_mass:
            raise AssertionError("D5 unassigned original endpoint union violated")
        if stationary:
            denominator=(min_positive-1)**2
            if missing_either_mass/Z>Fraction(2*physical_unused_pairs,denominator):
                raise AssertionError("D5 stationary missing ORIGINAL factor bound violated")
        if independent_oracle:
            direct=defaultdict(Fraction)
            raw_source=defaultdict(Fraction)
            independent_Z=independent_eligible=independent_block=Fraction()
            count=0
            for (w,u,v,z),weight in ctx._iter_nb(max_paths):
                count+=1
                independent_Z+=weight
                source_id=ctx.provenance[tuple(sorted((u,v)))]
                raw_source[source_id]+=weight
                x0,y0=divmod(w,ctx.a)
                x3,y3=divmod(z,ctx.a)
                q=ctx.fi.get(tuple(sorted((x0,x3))))
                r=ctx.gi.get(tuple(sorted((y0,y3))))
                if q is None or r is None or (q,r) not in ctx.anchor:
                    continue
                p,l=ctx.anchor[q,r]
                if (set(ctx.f[p])&set(ctx.f[q]) or
                        set(ctx.g[l])&set(ctx.g[r])):
                    continue
                independent_eligible+=weight
                direct[q,r,source_id]+=weight
                p2,l2=ctx.inc[source_id]
                if (original_overlap(ctx.f[p],ctx.f[p2]) or
                        original_overlap(ctx.g[l],ctx.g[l2])):
                    independent_block+=weight
            if (direct!=raw_joint or raw_source!=mid or
                    (independent_Z,independent_eligible,independent_block)!=
                    (Z,eligible,blocked) or count!=npaths):
                raise AssertionError("independent original NB3 edge-path oracle disagrees")

        end_mass=defaultdict(Fraction)
        for (q,r,e),mass in raw_joint.items():
            end_mass[q,r]+=mass
        end_clean_count=sum(1 for (q,r),(p,l) in ctx.anchor.items()
                            if (not set(ctx.f[p])&set(ctx.f[q]) and
                                not set(ctx.g[l])&set(ctx.g[r])))
        if end_clean_count<len(end_mass):
            raise AssertionError("nonincident original endpoint support mismatch")
        info=info_upper=None
        if stationary:
            # I(X;E), X=(true original q,r) when eligible and X=bottom otherwise.
            # The exact uniform E law is 1/M; logs are diagnostics, NOT proof.
            bottom=defaultdict(Fraction)
            source_eligible=defaultdict(Fraction)
            for (q,r,e),mass in raw_joint.items():
                source_eligible[e]+=mass
            botZ=Z-eligible
            for e in ctx.selected:
                bottom[e]=mid[e]-source_eligible[e]
                if bottom[e]<0:
                    raise AssertionError("negative ineligible midpoint weight")
            if sum(bottom.values(),Fraction())!=botZ:
                raise AssertionError("noneligible bottom midpoint mass lost")
            info=0.0
            for (q,r,e),mass in raw_joint.items():
                info+=float(mass/Z)*log(float(mass*M/end_mass[q,r]))
            if botZ:
                for e,mass in bottom.items():
                    if mass:
                        info+=float(mass/Z)*log(float(mass*M/botZ))
            info_upper=rectangle_entropy_ceiling(
                float(eligible/Z),end_clean_count,min_positive)
            if info>info_upper+1e-9:
                raise AssertionError("D4 original rectangle minentropy upper violated")

        return {
            's':ctx.s,'a':ctx.a,'N':ctx.N,
            'source_middle_ids':M,'physical_edges':ctx.m,
            'oriented_middle_rectangles':rectangles,
            'oriented_nonbacktracking_paths':npaths,
            'raw_rectangle_law_mass':str(Z),
            'stationary':stationary,
            'conditional_on_survival':not stationary,
            'minimum_positive_physical_degree':min_positive,
            'eligible_end_clean_mass':str(eligible/Z),
            'unused_physical_label_pairs_each_side':physical_unused_pairs,
            'D5_left_original_endpoint_absent_mass':str(missing_left_mass/Z),
            'D5_right_original_endpoint_absent_mass':str(missing_right_mass/Z),
            'D5_either_original_endpoint_absent_mass':str(missing_either_mass/Z),
            'D5_stationary_missing_upper':str(
                Fraction(2*physical_unused_pairs,(min_positive-1)**2)
            ) if stationary else None,
            'D5_near_complete_decoder_verified':True,
            'theta_internal_only':str(blocked/Z),
            'nonzero_true_transport_cells':len(raw_joint),
            'distinct_original_endpoint_pairs':len(end_mass),
            'max_original_q_per_oriented_middle_rectangle':max_oriented_q,
            'max_original_r_per_oriented_middle_rectangle':max_oriented_r,
            'max_original_r_per_middle_source_q':max((len(v) for v in source_q.values()),default=0),
            'max_original_q_per_middle_source_r':max((len(v) for v in source_r.values()),default=0),
            'four_partial_matchings_verified':True,
            'D3_stationary_atom_cap':str(Fraction(1,M*(min_positive-1)**2)) if stationary else None,
            'D4_info_nats_diagnostic':info,
            'D4_info_upper_nats_diagnostic':info_upper,
            'D4_upper_excludes_C6_counterexample':False,
            'universal_branch_A_proved':False,
        }


def report():
    from hyp105_issue230_projection import fixture
    from hyp105_issue230_paired_gstar import paired_gstar
    rows=[]
    for scheme in ('lex','reverse','S68','S72'):
        model=fixture(1,scheme)
        reg=paired_gstar(model)
        try:
            d=OriginalNBRectangle(model,reg['original_incidence_ids'],
                                  reg['colors_left'],reg['colors_right']).census()
        except ValueError as ex:
            if "no valid physical nonbacktracking rectangles" not in str(ex):
                raise
            rows.append({'scheme':scheme,'status':'no NB3; small-s finite only'})
            continue
        d['scheme']=scheme
        rows.append(d)
    return {'status':'RESTRICTED_THEOREM_C',
            'scope':'true ORIGINAL W32 coherent paired G*, not all-h energy upper',
            'root_A':'OPEN','rows':rows}


if __name__=='__main__':
    print(json.dumps(report(),indent=2,sort_keys=True))
