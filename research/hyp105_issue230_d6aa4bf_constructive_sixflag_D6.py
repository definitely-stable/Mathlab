"""AA4-BF: constructive accepted GF(5) TRUE ORIGINAL sixflag D6 completion.

Strict child of AA4-BE #568. All given W(3,s) original factor IDs,
original incidence flags, occupied typed physical pair supports and
initially pinned original LINE->edge images are preserved. ONE globally
coherent whole LINE assignment is constructed via exact conditional
expectations; NO independent source-sixset redraw.

The all-h lower floor derives ONLY from #568. This code materializes
actual genuine W32 incidence data for finite independent falsification;
it does not silently materialize fictitious high-order GQ geometries.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import permutations, product

from hyp105_issue230_d6aa4ay_quenched_allD_opposite_mean import _params
from hyp105_issue230_d6aa4be_original_D6_pins import (
    falling, original_D6_sixflag_pinned_envelope,
)


def sixcycle_vertex_orders(edges, a):
    """Canonical undirected physical C6 vertices, one per edge-cycle.

    Intended for concrete finite original W32/W34 falsifiers, not
    a polynomial-time routine in the big combinatorial incidence size.
    """
    support={tuple(sorted(e)) for e in edges}
    if len(support)!=len(tuple(edges)) or any(
        len(e)!=2 or e[0]==e[1] or min(e)<0 or max(e)>=a for e in support
    ):
        raise ValueError("distinct valid physical edge image support required")
    for v in permutations(range(a),6):
        if v[0]!=min(v) or v[1]>v[5]:
            continue
        row=tuple(tuple(sorted((v[i],v[(i+1)%6]))) for i in range(6))
        if all(edge in support for edge in row):
            yield v


def oriented_right_sixcycles(edges,a):
    """Exact 12 positional original D6 line-image alignments per physical C6."""
    out=[]
    for v in sixcycle_vertex_orders(tuple(edges),a):
        base=tuple(tuple(sorted((v[i],v[(i+1)%6]))) for i in range(6))
        for j in range(6):
            out.append(tuple(base[(j+i)%6] for i in range(6)))
            out.append(tuple(base[(j-i)%6] for i in range(6)))
    if len(set(out))!=len(out):
        raise AssertionError("canonical one-right-image D6 orientations repeated")
    return tuple(out)


def true_W32_original_D6_sixline_weights(model,initially_pinned_lines=()):
    """Independent real symplectic W32 six distinct flags as ordered line IDs.

    An ordered physical point C6 is CANONICALLY rooted and oriented
    before 3^6 actual original incident line assignments are selected.
    We do NOT count six duplicate rotations as different source Q.
    """
    s=model["s"]
    if s!=2:
        raise ValueError("this independent full-incidence materializer is W32 only")
    V,a,_,_=_params(s)
    f=tuple(tuple(sorted(e)) for e in model["left_labels"])
    inc=set(map(tuple,model["incidences"]))
    if len(f)!=V or len(set(f))!=V or len(inc)!=V*(s+1):
        raise ValueError("source factors not complete actual W32")
    frozen=set(initially_pinned_lines)
    if any(type(j) is not int or j<0 or j>=V for j in frozen):
        raise ValueError("original pinned LINE factor outside true GQ")
    original_point_for_edge={e:i for i,e in enumerate(f)}
    nbr=[[] for _ in range(V)]
    for p,l in inc:
        if not(0<=p<V and 0<=l<V):
            raise ValueError("invalid original incidence ID")
        nbr[p].append(l)
    if any(len(x)!=s+1 for x in nbr) or any(
        sum(l in ns for ns in nbr)!=s+1 for l in range(V)
    ):
        raise ValueError("not a regular true original source flag model")
    weights=Counter()
    for vertices in sixcycle_vertex_orders(f,a):
        point_edges=[tuple(sorted((vertices[i],vertices[(i+1)%6]))) for i in range(6)]
        point_ids=[original_point_for_edge[e] for e in point_edges]
        if len(set(point_ids))!=6:
            raise AssertionError("physical point injection violated")
        for lines in product(*(nbr[p] for p in point_ids)):
            if len(set(lines))==6 and not frozen.intersection(lines):
                weights[tuple(lines)]+=1
    return dict(weights)


def _validate_source_weights(weights, V):
    if not isinstance(weights,dict) or not weights:
        raise ValueError("positive true-original 6line source candidate weights needed")
    if any(not isinstance(q,tuple) or len(q)!=6 or len(set(q))!=6 or
           any(type(j) is not int or j<0 or j>=V for j in q) or
           type(w) is not int or w<=0 for q,w in weights.items()):
        raise ValueError("six different ACTUAL source LINE factors, positive integer weights")
    return sum(weights.values())


def _check_pins(pins, V, physical_support):
    if not isinstance(pins,dict) or any(type(j) is not int or not 0<=j<V
                                        for j in pins):
        raise ValueError("all locks on distinct real original line IDs")
    mapped=tuple(tuple(sorted(edge)) for edge in pins.values())
    if len(set(mapped))!=len(mapped) or any(e not in physical_support for e in mapped):
        raise ValueError("every locked original line edge must be occupied and distinct")
    return {j:tuple(sorted(e)) for j,e in pins.items()}


class ExactOriginalD6ConditionalPotential:
    """Exact whole-global-map potential over original 6-ID D6, with global pins.

    Weighted Q in source event family must have been screened to AVOID all
    initially pinned original source LINE IDs. This ensures the all-h
    parent #568 expected mean quantitative floor can be applied directly.
    """

    def __init__(self, V, right_edges, a, source_weights):
        self.V=V
        self.a=a
        self.edges=tuple(tuple(sorted(e)) for e in right_edges)
        if len(self.edges)!=V or len(set(self.edges))!=V:
            raise ValueError("a complete globally injected right support is required")
        if any(len(e)!=2 or e[0]==e[1] or min(e)<0 or max(e)>=a for e in self.edges):
            raise ValueError("physical pair labels must be distinct valid K_a edges")
        self.support=frozenset(self.edges)
        self.weights=dict(source_weights)
        self.B=_validate_source_weights(self.weights,V)
        self.targets=oriented_right_sixcycles(self.edges,a)
        self.by_pos_edge=defaultdict(list)
        for row in self.targets:
            for pos,e in enumerate(row):
                self.by_pos_edge[pos,e].append(row)
        self._all_targets=len(self.targets)

    def potential(self,pins):
        """Sum of exact conditional probabilities for ONE SHARED completion.

        For each original source Q, known positions are fixed globally;
        the other 6-c positions are sampled without replacement from
        the globally remaining edge set. No assumption of independence
        among Q events is made.
        """
        psi=_check_pins(pins,self.V,self.support)
        n=self.V-len(psi)
        used=frozenset(psi.values())
        free=self.support-used
        allfree=None
        answer=Fraction()
        for lines,w in self.weights.items():
            fixed=tuple((pos,psi[j]) for pos,j in enumerate(lines) if j in psi)
            c=len(fixed)
            if 6-c>n:
                continue
            if not fixed:
                if allfree is None:
                    allfree=sum(all(e in free for e in row) for row in self.targets)
                favorable=allfree
            else:
                candidates=min((self.by_pos_edge[key] for key in fixed),key=len,
                               default=())
                favorable=sum(
                    all(row[pos]==edge for pos,edge in fixed) and
                    all(row[pos] in free for pos,j in enumerate(lines) if j not in psi)
                    for row in candidates
                )
            if favorable:
                answer+=Fraction(w*favorable,falling(n,6-c))
        return answer

    def literal_full_D6_count(self,complete):
        """Original six-source-ID selected D6 direct physical C6 test."""
        psi=_check_pins(complete,self.V,self.support)
        if len(psi)!=self.V:
            raise ValueError("must give ONE whole legal global LINE map")
        value=0
        for q,w in self.weights.items():
            edges=tuple(psi[j] for j in q)
            same=set()
            good=True
            for i in range(6):
                intersection=set(edges[i])&set(edges[(i+1)%6])
                if len(intersection)!=1:
                    good=False
                    break
                same.update(intersection)
            if good and len(same)==6:
                value+=w
        return value

    def maximize_one_source_line(self,pins,line):
        psi=_check_pins(pins,self.V,self.support)
        if type(line) is not int or line<0 or line>=self.V or line in psi:
            raise ValueError("choose exactly one unassigned original LINE factor")
        base=self.potential(psi)
        free=sorted(self.support-set(psi.values()))
        values=[(self.potential(dict(psi,**{} ) | {line:e}),e) for e in free]
        avg=sum((value for value,e in values),Fraction())/len(values)
        if avg!=base:
            raise AssertionError("exact one-WHOLE-global-permutation tower identity failed")
        best=max(value for value,e in values)
        picked=min(e for value,e in values if value==best)
        if best<base:
            raise AssertionError("conditional expectation greedy potential decreased")
        return {"source_line":line,"physical_edge":picked,
                "old_potential":base,"mean_of_all_next_potentials":avg,
                "next_potential":best,"available_edges_examined":len(free)}

    def greedy_complete(self,initial_pins, choose_next=None, max_steps=None):
        """Deterministically extend ALL actual source LINE IDs, adaptable order.

        choose_next accepts current immutable copy of partial map and its
        remaining source IDs, and returns ONE next original source LINE ID.
        An adversary may adaptively choose the ID, not the physical edge.
        """
        pins=_check_pins(initial_pins,self.V,self.support)
        if any(any(j in pins for j in q) for q in self.weights):
            raise ValueError("R_free source Q must avoid ALL initial pinned source LINE IDs")
        initial=self.potential(pins)
        transcript=[]
        while len(pins)<self.V:
            if max_steps is not None and len(transcript)>=max_steps:
                break
            remain=tuple(j for j in range(self.V) if j not in pins)
            line=(choose_next(dict(pins),remain) if choose_next else remain[0])
            step=self.maximize_one_source_line(pins,line)
            pins[line]=step["physical_edge"]
            transcript.append(step)
        final_potential=self.potential(pins)
        if final_potential<initial:
            raise AssertionError("conditional D6 potential did not increase")
        actual=None
        if len(pins)==self.V:
            actual=self.literal_full_D6_count(pins)
            if actual!=final_potential or final_potential.denominator!=1:
                raise AssertionError("full original selected D6 potential not literal count")
        return {"initial_conditional_original_D6_mean":initial,
                "current_conditional_original_D6_potential":final_potential,
                "final_literal_original_D6_count":actual,
                "complete_original_global_line_map":len(pins)==self.V,
                "line_image_mapping":pins,
                "trace":transcript,
                "all_initial_actual_LINE_pins_preserved":all(
                    pins[j]==tuple(sorted(e)) for j,e in initial_pins.items()),
                "no_per_source_Q_resampling":True,
                "fixed_arbitrary_f_g_root_230_NOT_PROVED":True,
                "root_230":"OPEN_WITH_FORMAL_BLOCKER"}


def all_h_original_D6_constructive_guarantee(s,k):
    """Do not materialize high-h genuine GQ; transfer accepted parent #568."""
    x=original_D6_sixflag_pinned_envelope(s,k)
    return {
        "s":s,"k":k,"V":x["V"],
        "any_adaptive_order_of_unassigned_original_LINE_IDs":True,
        "parent_verified_expected_original_D6_floor":
            x["one_global_conditional_original_sixID_D6_expected_count_lower"],
        "algorithmically_exists_one_complete_legal_g_extending_ALL_pins":True,
        "constructed_selected_original_GF5_D6_floor":s**6,
        "all_given_fully_fixed_original_f_g_lower_NOT_PROVED":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER"}
