"""EICE-003-E: exact ORIGINAL GQ plaquettes inside true NB3 rectangles.

E1: true physical 2x2 four-corner sources have double K_{2,2} labels.
E2: actual ORIGINAL 4-point/4-line incidence cap <=8 (girth 8).
E3: exact row-pair co-degree count and robust full-endpoint density.
E4: four-corner mass amplification with stationary squareable middle edges.
Research only; neither physical squares nor cross anchors imply GF5 positivity.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
import json

from hyp105_issue230_nb_rectangles import OriginalNBRectangle
from hyp105_issue230_middle_transport import original_overlap


STATUS = ('missing_original_endpoint', 'original_endpoint_incident',
          'original_anchor_end_dirty', 'original_anchor_internal_blocked',
          'original_anchor_unblocked')


def source_girth_four_by_four(point_ids, line_ids, incidence_ids):
    """Original GQ 4x4 bipartite girth-8 certificate (NOT a physical cycle)."""
    pp=tuple(point_ids)
    ll=tuple(line_ids)
    if len(pp)!=4 or len(ll)!=4 or len(set(pp))!=4 or len(set(ll))!=4:
        raise ValueError('four DISTINCT ORIGINAL point and line IDs required')
    edges={(i,j) for i,p in enumerate(pp) for j,r in enumerate(ll)
           if (p,r) in incidence_ids}
    # Two source points sharing two true source lines creates a forbidden C4.
    for i,k in combinations(range(4),2):
        if sum((i,j) in edges and (k,j) in edges for j in range(4))>1:
            raise AssertionError('SOURCE ORIGINAL GQ forbidden four-cycle')
    # A length-six cycle necessarily uses three distinct points and lines.
    for p0,p1,p2 in combinations(range(4),3):
        for l0,l1,l2 in __import__('itertools').permutations(range(4),3):
            if (all(e in edges for e in
                    ((p0,l0),(p0,l1),(p1,l1),(p1,l2),(p2,l2),(p2,l0)))):
                raise AssertionError('SOURCE ORIGINAL GQ forbidden six-cycle')
    if len(edges)>8:
        raise AssertionError('SOURCE ORIGINAL 4x4 girth-8 incidence cap')
    return {'original_cross_incidence_count':len(edges),
            'original_cross_nonincidence_count':16-len(edges)}


def all_four_count(rows, acceptable):
    """Exact number of 2x2 minors with all four entries in a set of statuses."""
    if not rows:
        return 0
    ncol=len(rows[0])
    if any(len(r)!=ncol for r in rows):
        raise ValueError('nonrectangular status grid')
    count=0
    for i,j in combinations(range(len(rows)),2):
        common=sum(rows[i][k] in acceptable and rows[j][k] in acceptable
                   for k in range(ncol))
        count+=common*(common-1)//2
    return count


def status_of_cell(ctx, middle_source, w, z):
    """True ORIGINAL q,r decode, actual unique projection and source block."""
    a=ctx.a
    x0,y0=divmod(w,a)
    x3,y3=divmod(z,a)
    q=ctx.fi.get(tuple(sorted((x0,x3))))
    r=ctx.gi.get(tuple(sorted((y0,y3))))
    if q is None or r is None:
        return 0,q,r
    if (q,r) in ctx.edge_id:
        return 1,q,r
    if (q,r) not in ctx.anchor:
        raise AssertionError('original GQ projection missing')
    p,ell=ctx.anchor[q,r]
    if set(ctx.f[p]) & set(ctx.f[q]) or set(ctx.g[ell]) & set(ctx.g[r]):
        return 2,q,r
    p2,ell2=ctx.inc[middle_source]
    blocked=(original_overlap(ctx.f[p],ctx.f[p2])
             or original_overlap(ctx.g[ell],ctx.g[ell2]))
    return (3 if blocked else 4),q,r


class OriginalPlaquette:
    """Whole-diagonal paired G* source plaquette oracle with exact fractions."""

    def __init__(self, model, selected, colors_left, colors_right):
        self.base=OriginalNBRectangle(model,selected,colors_left,colors_right)
        self.ctx=self.base.ctx

    def census(self, *, max_paths=500_000, max_plaquettes=150_000,
               independent_paths=True, independent_plaquettes=True):
        if (type(max_paths) is not int or max_paths<1 or
                type(max_plaquettes) is not int or max_plaquettes<0):
            raise ValueError('positive path budget and nonnegative plaquette budget required')
        ctx=self.ctx
        if not ctx.selected:
            raise ValueError('source selection must be nonempty')
        a=ctx.a
        unused=a*(a-1)//2-ctx.v
        Z=Fraction()
        category=Counter()
        plaquettes=complete=eligible=blocked_squares=unblocked_squares=0
        four_corner_missing=0
        weighted_squareable=Fraction()
        squareable_missing=Fraction()
        squareable_blocked=Fraction()
        squareable_eligible=Fraction()
        cross_hist=Counter()
        oriented_middle_rectangles=0
        squareable_orientations=0
        actual_paths=0
        for u,adj in enumerate(ctx.adj):
            for v in sorted(adj):
                oriented_middle_rectangles+=1
                e=ctx.provenance[tuple(sorted((u,v)))]
                A=sorted(adj-{v})
                B=sorted(ctx.adj[v]-{u})
                nr,nc=len(A),len(B)
                if not nr or not nc:
                    continue
                actual_paths+=nr*nc
                if actual_paths>max_paths:
                    raise ValueError('complete ORIGINAL NB path budget exceeded')
                weight=Fraction(1,nr*nc)
                row_status=[]
                row_points=[]
                row_lines=[]
                for w in A:
                    statuses=[]
                    points=[]
                    lines=[]
                    for z in B:
                        x0,y0=divmod(w,a)
                        x1,y1=divmod(u,a)
                        x2,y2=divmod(v,a)
                        x3,y3=divmod(z,a)
                        if (len({x0,x1,x2,x3})!=4 or
                                len({y0,y1,y2,y3})!=4):
                            raise AssertionError('improper physical NB3 survived G*')
                        st,q,r=status_of_cell(ctx,e,w,z)
                        statuses.append(st)
                        points.append(q)
                        lines.append(r)
                        category[st]+=weight
                        Z+=weight
                    row_status.append(statuses)
                    row_points.append(points)
                    row_lines.append(lines)
                missing=sum(st==0 for row in row_status for st in row)
                if missing>2*unused:
                    raise AssertionError('original endpoint missing-pair capacity exceeded')
                if nr<2 or nc<2:
                    continue
                squareable_orientations+=1
                weighted_squareable+=1
                squareable_missing+=Fraction(missing,nr*nc)
                squareable_blocked+=Fraction(
                    sum(st==3 for row in row_status for st in row),nr*nc)
                squareable_eligible+=Fraction(
                    sum(st in (3,4) for row in row_status for st in row),nr*nc)
                count=(nr*(nr-1)//2)*(nc*(nc-1)//2)
                if plaquettes+count>max_plaquettes:
                    raise ValueError('exact ORIGINAL 2x2 plaquette budget exceeded')
                plaquettes+=count
                got_complete=all_four_count(row_status,{1,2,3,4})
                got_eligible=all_four_count(row_status,{3,4})
                got_blocked=all_four_count(row_status,{3})
                got_unblocked=all_four_count(row_status,{4})
                complete+=got_complete
                eligible+=got_eligible
                blocked_squares+=got_blocked
                unblocked_squares+=got_unblocked
                if got_complete < count - missing*(nr-1)*(nc-1):
                    raise AssertionError('E3 near-complete original plaquette union bound violated')
                if independent_plaquettes:
                    # Independent brute-force incidence/coordinate provenance
                    # on each ORIGINAL endpoint-defined 2x2 cell quartet.
                    brute_complete=brute_eligible=brute_blocked=brute_unblocked=0
                    for i,k in combinations(range(nr),2):
                        for j,l in combinations(range(nc),2):
                            cells=((i,j),(i,l),(k,j),(k,l))
                            ss=[row_status[ii][jj] for ii,jj in cells]
                            if any(x==0 for x in ss):
                                four_corner_missing+=1
                                continue
                            brute_complete+=1
                            pts=[row_points[ii][jj] for ii,jj in cells]
                            lns=[row_lines[ii][jj] for ii,jj in cells]
                            if len(set(pts))!=4 or len(set(lns))!=4:
                                raise AssertionError('E1 ORIGINAL plaquette four factors not distinct')
                            # Physical ORIGINAL point pairs form exactly K2,2
                            # between two first-outside x and two final-outside x;
                            # same for line pairs with right physical coordinates.
                            expected_left={tuple(sorted((A[ii]//a,B[jj]//a)))
                                           for ii,jj in cells}
                            expected_right={tuple(sorted((A[ii]%a,B[jj]%a)))
                                            for ii,jj in cells}
                            if ({ctx.f[q] for q in pts} != expected_left or
                                    {ctx.g[r] for r in lns} != expected_right):
                                raise AssertionError('E1 genuine double-K22 source labels failed')
                            geometry=source_girth_four_by_four(
                                pts,lns,ctx.edge_id)
                            cross_hist[geometry['original_cross_incidence_count']]+=1
                            if all(x in (3,4) for x in ss):
                                brute_eligible+=1
                            if all(x==3 for x in ss):
                                brute_blocked+=1
                            if all(x==4 for x in ss):
                                brute_unblocked+=1
                    if (brute_complete,brute_eligible,brute_blocked,brute_unblocked)!=(
                            got_complete,got_eligible,got_blocked,got_unblocked):
                        raise AssertionError('E3 independent direct plaquette count disagreed')
                else:
                    four_corner_missing+=count-got_complete

        if not Z:
            raise ValueError('no valid physical NB3 paths in selected source graph')
        if sum(category.values(),Fraction())!=Z:
            raise AssertionError('source path status decomposition lost mass')
        if sum(category[st] for st in range(5))!=Z:
            raise AssertionError('disjoint original GQ path status partition invalid')
        if complete+four_corner_missing!=plaquettes:
            raise AssertionError('source plaquette completeness partition invalid')
        if independent_paths:
            direct=Counter()
            z_direct=Fraction()
            for (w,u,v,z),weight in ctx._iter_nb(max_paths):
                source=ctx.provenance[tuple(sorted((u,v)))]
                st,_,_=status_of_cell(ctx,source,w,z)
                direct[st]+=weight
                z_direct+=weight
            if direct!=category or z_direct!=Z:
                raise AssertionError('independent true ORIGINAL direct NB path statuses disagree')
        if weighted_squareable:
            denominator=weighted_squareable
            miss=Fraction(squareable_missing,denominator)
            blocked_ratio=Fraction(squareable_blocked,denominator)
            eligible_ratio=Fraction(squareable_eligible,denominator)
            complete_prob=Fraction(complete,plaquettes)
            blocked_prob=Fraction(blocked_squares,plaquettes)
            eligible_prob=Fraction(eligible,plaquettes)
            if complete_prob < 1-4*miss:
                raise AssertionError('E4 global sampled-plaquette missing union bound')
            if blocked_prob < 4*blocked_ratio-3:
                raise AssertionError('E4 global all-blocked amplification failed')
            if eligible_prob < 4*eligible_ratio-3:
                raise AssertionError('E4 global all-eligible amplification failed')
        else:
            miss=blocked_ratio=eligible_ratio=None
        dmin=min((d for d in ctx.degree if d),default=0)
        stationary=dmin>=2
        all_squareable=dmin>=3
        if all_squareable:
            if squareable_orientations!=2*ctx.m:
                raise AssertionError('stationary source every middle rectangle squareable failed')
            if Z!=2*ctx.m:
                raise AssertionError('full stationary edge-rooted NB3 normalization failed')
            if Fraction(category[0],Z)>Fraction(2*unused,(dmin-1)**2):
                raise AssertionError('E4 stationary original endpoint missing asymptotic bound')
            if plaquettes:
                if Fraction(complete,plaquettes)<1-Fraction(8*unused,(dmin-1)**2):
                    raise AssertionError('E4 stationary quartet label completeness violated')
        return {
            's':ctx.s,'a':ctx.a,'N':ctx.N,
            'original_middle_source_count':len(ctx.selected),
            'physical_edges':ctx.m,
            'stationary':stationary,
            'all_middle_rectangles_squareable':all_squareable,
            'oriented_middle_rectangles':oriented_middle_rectangles,
            'squareable_middle_orientations':squareable_orientations,
            'raw_nb_weight':str(Z),
            'original_nb_path_status_weight':{
                name:str(category[i]/Z) for i,name in enumerate(STATUS)},
            'missing_original_endpoint_weight':str(category[0]/Z),
            'internally_blocked_end_clean_weight':str(category[3]/Z),
            'fully_good_unblocked_original_weight':str(category[4]/Z),
            'total_2x2_plaquettes':plaquettes,
            'original_endpoint_complete_plaquettes':complete,
            'eligible_end_clean_plaquettes':eligible,
            'all_four_internally_blocked_plaquettes':blocked_squares,
            'all_four_unblocked_plaquettes':unblocked_squares,
            'squareable_mean_missing_cell_fraction':str(miss) if miss is not None else None,
            'squareable_mean_blocked_cell_fraction':str(blocked_ratio) if blocked_ratio is not None else None,
            'squareable_mean_eligible_cell_fraction':str(eligible_ratio) if eligible_ratio is not None else None,
            'E4_global_complete_fraction':str(Fraction(complete,plaquettes)) if plaquettes else None,
            'E4_global_allblocked_fraction':str(Fraction(blocked_squares,plaquettes)) if plaquettes else None,
            'original_cross_incidence_histogram':dict(sorted(cross_hist.items())),
            'original_cross_girth8_cap':8,
            'source_gf5_sixset_from_cross_pairs_proved':False,
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
            result=OriginalPlaquette(model,reg['original_incidence_ids'],
                                    reg['colors_left'],reg['colors_right']).census()
            result['scheme']=scheme
            rows.append(result)
        except ValueError as exc:
            if 'no valid physical NB3' not in str(exc):
                raise
            rows.append({'scheme':scheme,'scope':'finite G* has no NB3'})
    return {'status':'RESTRICTED_THEOREM_C',
            'scope':'TRUE original W32 paired G* source plaquette tests, no asymptotic extrapolation',
            'root_A':'OPEN','rows':rows}


if __name__=='__main__':
    print(json.dumps(report(),indent=2,sort_keys=True))
