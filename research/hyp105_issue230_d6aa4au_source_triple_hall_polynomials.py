"""HYP-105 / #230 AA4-AU: exact ORIGINAL 3x3 source Hall polynomials & motifs.

Genuine original symplectic W(3,s), s=2^h, fixed complete original
global point/line physical factor maps f,g. A residual 3-point-slot /
3-line-slot source Hall degree problem has only four multiplicity types:
 A/A, A/B, B/A, B/B. Under the TRUE GQ girth-eight property each
explicit incidence polynomial is Boolean (0 or 1). This is a
factor-multiplicity refinement of AA4-AT's forest leaf uniqueness,
not a new generic permanent theorem and not a positive GF5 lower.

Independently, all unordered triples of distinct original flags split
EXACTLY into six source factor types. In particular, the authentic
original source B/B three-edge P4 population = N*s^2 >= s^6.
These triples have NOT been proved physically eligible or GF5 selected
under arbitrary adversarial correlated global f/g.
"""
from collections import Counter
from itertools import combinations,permutations
from math import comb

from hyp105_issue230_d6aa4al_global_original_coordinate_transport import (
    _parameters,_actual_strict_original_transport)


def _residual_source_slots(residual):
    if (not isinstance(residual,(tuple,list)) or len(residual)<2):
        raise ValueError("AA4-AS typed original (tag, factor slots, physical images) required")
    try:
        vals=tuple(residual[1])
    except TypeError as exc:
        raise ValueError("original residual source factor slots required") from exc
    if (len(vals)!=3 or any(type(z)!=int or z<0 for z in vals)
            or max(Counter(vals).values())>2):
        raise ValueError("three genuine source residual factor slots, multiplicities <=2")
    return vals


def _candidate_source_incidence_edge_sets(point_slots,line_slots):
    """INDEPENDENT closed-form four-case SOURCE Hall candidate edge triples."""
    pc,lc=Counter(point_slots),Counter(line_slots)
    pt="A" if len(pc)==3 else "B"
    lt="A" if len(lc)==3 else "B"
    pp=tuple(sorted(pc))
    ll=tuple(sorted(lc))
    if pt=="A" and lt=="A":
        for lperm in permutations(ll):
            yield "A/A",tuple((p,l) for p,l in zip(pp,lperm))
    elif pt=="A" and lt=="B":
        repeated=next(l for l,k in lc.items() if k==2)
        single=next(l for l,k in lc.items() if k==1)
        for p in pp:
            yield "A/B",tuple(sorted(
                ((p,single),)+tuple((q,repeated) for q in pp if q!=p)))
    elif pt=="B" and lt=="A":
        repeated=next(p for p,k in pc.items() if k==2)
        single=next(p for p,k in pc.items() if k==1)
        for l in ll:
            yield "B/A",tuple(sorted(
                ((single,l),)+tuple((repeated,m) for m in ll if m!=l)))
    else:
        p2=next(p for p,k in pc.items() if k==2)
        p1=next(p for p,k in pc.items() if k==1)
        l2=next(l for l,k in lc.items() if k==2)
        l1=next(l for l,k in lc.items() if k==1)
        yield "B/B",tuple(sorted(((p2,l2),(p2,l1),(p1,l2))))


def exact_original_threeflag_Hall_incidence_polynomial(
        original_source_flag_index,pinned_original_flag_ids,
        point_residual,line_residual,*,with_witness=True):
    """Explicit original 3x3 Boolean incidence polynomial (independent of leaf solver).

    A/A: 3x3 permanent sum of six products of 0/1 GQ incidences.
    A/B: choose the point paired to SINGLE line, the other two
         incident with the repeated line.
    B/A: dual of A/B.
    B/B: a forced three-edge point-line SOURCE P4 product.

    If >1 on forged source graphs, RAISE; real symplectic GQ with
    girth>=8 cannot realize >1 distinct residual source b-matchings.
    The map index is obtained from actual globally fixed ORIGINAL
    source incidence IDs; no fake physical re-sampling occurs.
    """
    p=_residual_source_slots(point_residual)
    l=_residual_source_slots(line_residual)
    pinned=tuple(pinned_original_flag_ids)
    if (len(pinned)!=3 or len(set(pinned))!=3
            or any(type(i)!=int or i<0 for i in pinned)):
        raise ValueError("three different original pinned source flag IDs required")
    if not isinstance(original_source_flag_index,dict):
        raise ValueError("actual original source flag index dictionary required")
    terms=0
    selected=[]
    shape=None
    for typ,edges in _candidate_source_incidence_edge_sets(p,l):
        if shape is None:shape=typ
        if typ!=shape:raise AssertionError("one original source residual type only")
        ids=[original_source_flag_index.get(edge) for edge in edges]
        if (all(type(i)==int and i>=0 and i not in pinned for i in ids)
                and len(set(ids))==3):
            terms+=1
            selected.append(tuple(sorted(pinned+tuple(ids))))
    if terms>1:
        raise ValueError("not a genuine W(3,s) girth-eight original source residual: multiple Hall matchings")
    if shape is None:raise AssertionError("no original source factors")
    if with_witness:
        return dict(
            original_source_residual_pattern=shape,
            exact_source_incidence_polynomial_value=terms,
            exact_original_six_DISTINCT_flag_ID_Q=selected[0] if terms else None,
            original_forest_boolean_per_template_predicate_proved=True,
            original_source_Hall_positive_density_not_proved=True,
            selected_seven_GF5_positive_not_proved=True)
    return terms


def all_h_original_threeflag_source_motif_population(s):
    """Full EXACT ORIGINAL 3-distinct-incidence-FLAG source population, all h.

    N=V*(s+1) authentic original source flags, d=s+1.
    The six source point/line factor distinct-count profiles are:
      A/A 3+3: 3 edge matching;
      A/B 3+2: two flags share a line, third has NEW point and line;
      B/A 2+3: dual;
      B/B 2+2: a three-incidence edge source P4 path;
      A/C 3+1: three flags through one line;
      C/A 1+3: three flags through one point.
    There are no other types for three DISTINCT source flag IDs.
    """
    V,d,a=_parameters(s)
    N=V*d
    c3=lambda n:n*(n-1)*(n-2)//6
    CA=V*comb(d,3)
    AC=CA
    AB=V*comb(d,2)*(N-3*d+2)
    BA=AB
    BB=N*(d-1)**2
    AA=c3(N)-AC-CA-AB-BA-BB
    if min(AA,AB,BA,BB,AC,CA)<0:
        raise AssertionError("genuine original three-flag source-type census negative")
    counts={"A/A":AA,"A/B":AB,"B/A":BA,"B/B":BB,"A/C":AC,"C/A":CA}
    if sum(counts.values())!=c3(N):
        raise AssertionError("six genuine original source three-flag motif partition")
    assert BB>=s**6
    return dict(
        s=s,V=V,d=d,a=a,N_original_incidence_flags=N,
        three_DISTINCT_original_source_flag_ID_type_counts=counts,
        all_unordered_genuine_original_threeflag_subsets=c3(N),
        original_BB_threeflag_P4_source_count=N*s*s,
        original_BB_threeflag_P4_source_at_least_s6=True,
        original_source_motif_population_independent_of_global_f_g=True,
        original_BB_physically_two_typed_opposite_NOT_PROVED=True,
        original_BB_selected_seven_GF5_NOT_PROVED=True)


def literal_true_original_W32_source_threeflag_motif_census(model):
    """Independent exhaustive source flag-first combination checker, W32 only."""
    s,V,d,a,f,g,inc,np,nl=_actual_strict_original_transport(model)
    if (s,len(inc))!=(2,45):
        raise ValueError("full literal source triple census is restricted to TRUE W32")
    hist=Counter()
    for x,y,z in combinations(inc,3):
        np3=len({x[0],y[0],z[0]})
        nl3=len({x[1],y[1],z[1]})
        fmt={3:"A",2:"B",1:"C"}
        hist[fmt[np3]+"/"+fmt[nl3]]+=1
    exact=all_h_original_threeflag_source_motif_population(s)
    if dict(hist)!=exact["three_DISTINCT_original_source_flag_ID_type_counts"]:
        raise AssertionError("literal actual original W32 source factor type census disagrees with symbolic formula")
    return dict(s=s,full_true_original_triples=sum(hist.values()),
                direct_original_source_flag_triple_histogram=dict(hist),
                independent_from_formal_source_motif_count=True)


def literal_true_original_source_BB_P4_audit(model):
    """Genuine original W32/W34/source-local exact P4 center-edge audit.

    Count each three original incidences forming source P4 ONCE:
    central real incidence (p,l), one other point incident with l
    and one other line incident with p. They determine precisely
    three DISTINCT genuine original incidence flag IDs.
    """
    s,V,d,a,f,g,inc,np,nl=_actual_strict_original_transport(model)
    if len(inc)>500:
        raise ValueError("literal real source P4 audit only W32/W34")
    idx={edge:i for i,edge in enumerate(inc)}
    paths=set()
    for p,l in inc:
        for q in nl[l]:
            if q==p:continue
            for k in np[p]:
                if k==l:continue
                path=tuple(sorted((idx[(p,l)],idx[(q,l)],idx[(p,k)])))
                paths.add(path)
    truth=all_h_original_threeflag_source_motif_population(s)
    if len(paths)!=truth["three_DISTINCT_original_source_flag_ID_type_counts"]["B/B"]:
        raise AssertionError("actual original GQ B/B P4 source count differs from all-h formula")
    for triple in paths:
        fac=[inc[i] for i in triple]
        if len({p for p,l in fac})!=2 or len({l for p,l in fac})!=2:
            raise AssertionError("not a real original source B/B P4")
    return dict(s=s,true_original_BB_incidence_P4_count=len(paths),
                original_distinct_source_BB_flags=tuple(sorted(paths)) if s==2 else None,
                independently_source_center_edge_enumerated=True)


def literal_true_original_source_AB_audit(model):
    """Independent ORIGINAL source A/B count: pair of flags on repeated line,
    then third truly ORIGINAL flag on NEW point and NEW line. W32/W34 only.
    """
    s,V,d,a,f,g,inc,np,nl=_actual_strict_original_transport(model)
    if len(inc)>500:
        raise ValueError("source A/B count limited to W32/W34")
    total=0
    sample=[]
    for l,points in enumerate(nl):
        for p,q in combinations(points,2):
            for r,k in inc:
                if k!=l and r!=p and r!=q:
                    total+=1
                    if len(sample)<10:sample.append(((p,l),(q,l),(r,k)))
    truth=all_h_original_threeflag_source_motif_population(s)
    if total!=truth["three_DISTINCT_original_source_flag_ID_type_counts"]["A/B"]:
        raise AssertionError("actual original A/B line-double source triples disagree")
    return dict(s=s,true_original_AB_line_repeat_count=total,
                independently_incidence_enumerated_A_B=True,
                ten_actual_original_AB_examples=tuple(sample))
