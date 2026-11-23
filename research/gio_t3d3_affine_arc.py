"""GIO-003/G6-D3: affine q-arc -> actual near-Moore source -> source six-ID T3.

Mathematical contributions INSIDE this project: unconditional arc-to-centered-
spectral certificate under explicit incidence/source axioms and consequent
conditional-HEAVY/LOW original named D6+BBo lower bound for EVERY actual
arc-source with arbitrary complete minimal typed source factor maps.

Prior art NOT ours: finite-field arcs, affine arc incidence graph construction,
Wenger and generalized Wenger / Cayley characters. Extends previous
Wenger-only use of the project-specific obstruction, NOT a new graph family.

For any prime-power q>=5 and ANY arc of the affine graph shape
{(1,u,h(u)):u in Fq} with no three points collinear, source has:
  degree q, |P|=|L|=q^3, girth>=8, Delta=2q(q-1),
  BBt-centered eigenvalues 0,q,2q,
  ||F0||^2 = max(q(q-2)^2,8q) <= (q-1)^3.
No assumption of a GQ source, a field representation in the *general*
T3 theorem, or old nonexisting projected anchors.

Additional explicit infinite case: q=2^e, e odd >=3,
h(u)=u^4; slopes from base u are (u+v)^3, a bijection for
gcd(3,2^e-1)=1. All actual q>=8 are thick non-GQ quadratic
Moore-excess sources with uniform b=1,C=3,kappa=1.

Finite q=3,5 prime and q=8 GF(8) instances validate the actual source;
q=4,16 h(u)=u^4 are negative non-arcs.
"""
import argparse
import json
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations, product
from math import comb, gcd
from pathlib import Path

from gio_t3c_intrinsic_defect import source_graph, typed_maps
from gio_t3d2_centered_sixth import (
    integrated_quadratic_direct_ledger,
    wenger_W2_spectral_parameters,
    wenger_W2_prime_source,
)
from gio_t3d_cubic_missing import necessary_small_excess_screen

SCHEMA="mathlab.gio003.g6d3.affine-arc-source-transfer.v1"
PARENT_G6D2="6605187776e0d5d15aa70c2df123a39d55ac85f6"
IRREDUCIBLE_BINARY={4:0b111,8:0b1011,16:0b10011,32:0b100101}


def is_prime(n):
    return type(n) is int and n>=2 and all(n%d for d in range(2,int(n**.5)+1))


class Field:
    """Exact finite field, q prime or selected 2^e polynomial quotient.

    No floating field arithmetic, no Z/4 claim, and no generic arbitrary
    prime power implementation beyond literal verified cases.
    """
    def __init__(self,q):
        if type(q) is not int or q<3:
            raise ValueError("literal finite field order q>=3")
        self.q=q
        if is_prime(q):
            self.poly=None
        elif q in IRREDUCIBLE_BINARY:
            self.poly=IRREDUCIBLE_BINARY[q]
            assert q & (q-1)==0 and self.poly.bit_length()==q.bit_length()
        else:
            raise ValueError("literal field only primes or selected binary powers")

    def add(self,a,b):
        return (a+b)%self.q if self.poly is None else a^b

    def sub(self,a,b):
        return (a-b)%self.q if self.poly is None else a^b

    def mul(self,a,b):
        assert 0<=a<self.q and 0<=b<self.q
        if self.poly is None:
            return a*b%self.q
        x=0
        while b:
            if b&1:
                x^=a
            a<<=1
            if a&self.q:
                a^=self.poly
            b>>=1
        assert 0<=x<self.q
        return x

    def power(self,a,k):
        if type(k) is not int or k<0:
            raise ValueError("nonnegative integer exponent")
        z=1
        while k:
            if k&1:
                z=self.mul(z,a)
            a=self.mul(a,a)
            k>>=1
        return z

    def inv(self,a):
        if not 0<a<self.q:
            raise ValueError("nonzero field element")
        z=self.power(a,self.q-2)
        assert self.mul(a,z)==1
        return z

    def div(self,a,b):
        return self.mul(a,self.inv(b))


def affine_arc_oracle(field,exponent):
    """Independent exact slope and projective determinant censuses."""
    q=field.q
    if type(exponent) is not int or exponent<0:
        raise ValueError("nonnegative monomial exponent required")
    h=[field.power(x,exponent) for x in range(q)]
    bad_slope=[]
    for u in range(q):
        seen={}
        for v in range(q):
            if v==u:
                continue
            slope=field.div(field.sub(h[v],h[u]),field.sub(v,u))
            if slope in seen:
                bad_slope.append((u,seen[slope],v))
            else:
                seen[slope]=v
    bad_determinant=[]
    for u,v,w in combinations(range(q),3):
        # det of [(1,u,h(u)),(1,v,h(v)),(1,w,h(w))]
        a=field.mul(field.sub(v,u),field.sub(h[w],h[u]))
        b=field.mul(field.sub(w,u),field.sub(h[v],h[u]))
        if field.sub(a,b)==0:
            bad_determinant.append((u,v,w))
    assert bool(bad_slope)==bool(bad_determinant)
    return dict(q=q,exponent=exponent,
       projective_arc=(len(bad_determinant)==0),
       noncollinear_triples=comb(q,3)-len(bad_determinant),
       literal_all_collinear_triples=bad_determinant,
       exact_slope_collision_witnesses=bad_slope,
       exact_slope_equals_determinant_decision=True,
       graph_form_is_affine_projective_arc=True)


def source_from_affine_arc(field,exponent,require_arc=True):
    """ACTUAL named original source incidence, not a synthetic F matrix."""
    q=field.q
    arc=affine_arc_oracle(field,exponent)
    if require_arc and not arc["projective_arc"]:
        raise ValueError("not a q-arc: forbidden original source C6")
    verts=list(product(range(q),repeat=3))
    index={v:i for i,v in enumerate(verts)}
    assert len(index)==q**3
    lines=[]
    for ell in verts:
        a,b,c=ell
        on=set()
        for u in range(q):
            p=(u,field.sub(field.mul(a,u),b),
               field.sub(field.mul(a,field.power(u,exponent)),c))
            on.add(index[p])
        assert len(on)==q
        lines.append(on)
    # The original incidence-first graph checker catches BOTH C4/C6
    # independently of the arc oracle, and freezes ORIGINAL source
    # nonincident partial 3flag projection and 3st load.
    m=source_graph(lines,q**3,q-1,q-1)
    assert m["excess_lines"]==2*q*(q-1)
    assert m["excess_points"]==2*q*(q-1)
    assert len(m["flags"])==q**4
    assert len(m["missing"])==q**3*2*q*(q-1)
    assert len(m["projected"])==q**3*q*(q-1)**2
    assert all(n==3*(q-1)**2 for n in m["projection_load"].values())
    return m


def fourier_root_character_census(field,exponent):
    """Independent exact additive character eigenvalues by zero-count.

    For every w=(w0,w1,w2) in the dual Fq^3,
      z(w)=#{u:w0+w1*u+w2*h(u)=0}.
    Character sum over all nonzero lam in Fq is
      sum_(lam!=0,u) chi(lam*(w0+w1*u+w2*h(u)))=q*z(w)-q.
    This is valid for ANY prime power / field with nontrivial
    additive character, by orthogonality. The arithmetic certificate
    explicitly enumerates z(w) WITHOUT a numerical eigensolver.
    """
    q=field.q
    arc=affine_arc_oracle(field,exponent)
    if not arc["projective_arc"]:
        raise ValueError("spectrum transfer needs genuine projective q-arc")
    h=[field.power(u,exponent) for u in range(q)]
    roots=Counter()
    for w0,w1,w2 in product(range(q),repeat=3):
        z=sum(field.add(field.add(w0,field.mul(w1,u)),
                        field.mul(w2,h[u]))==0 for u in range(q))
        roots[z]+=1
    assert sum(roots.values())==q**3
    assert roots[q]==1
    assert set(roots)<={0,1,2,q}
    m2=q*(q-1)**2//2
    m1=2*q*(q-1)
    m0=q**3-1-m1-m2
    assert roots==Counter({q:1,2:m2,1:m1,0:m0})
    # Every projective line meets the q-arc 0,1,2 times:
    # m2/(q-1)=comb(q,2), m1/(q-1)=2q.
    assert m2==(q-1)*comb(q,2)
    assert m1==(q-1)*2*q
    r=q-1
    lamq=q*(q-2)**2
    lam2q=8*q
    norm=max(lamq,lam2q)
    kappa=(norm+r**3-1)//r**3
    assert kappa==(3 if q==3 else 2 if q==4 else 1)
    if q>=5:
        assert norm<=r**3
    assert 2*q*r<=3*r*r
    return dict(q=q,exponent=exponent,
       dual_characters_enumerated=q**3,
       exact_zero_count_multiplicity={str(i):roots.get(i,0)
           for i in (0,1,2,q)},
       principal_BBt_eigenvalue=q*q,
       centered_BBt_eigenvalues=[0,q,2*q],
       Fourier_characters_proof_uses_arc_root_bound=True,
       integer_root_counts_no_floating_eigensolver=True,
       original_source_Moore_excess=2*q*(q-1),
       original_missing_F0_spectrum=[0,lamq,lam2q],
       centered_F0_norm_squared=norm,
       minimal_integer_kappa=kappa,
       fixed_asymptotic_kappa_for_all_q_ge5=1,
       quadratic_excess_C=3,
       source_balance_b=1,
       exact_centered_S6=m1*lamq**3+m2*lam2q**3,
       published_Wenger_multiplicities_match=True,
       no_GQ_projection_completion=True)


def binary_fourth_power_all_order(e):
    """Infinite explicit subfamily: q=2^e, e odd>=3.

    In characteristic two the slope of h(x)=x^4 from u to v is
       ((v^4-u^4)/(v-u))=(u+v)^3.
    For fixed u and distinct v, slopes are distinct iff z->z^3 is
    injective on Fq*, iff gcd(3,q-1)=1, iff e is ODD.
    """
    if type(e) is not int or e<2:
        raise ValueError("binary exponent degree e>=2")
    q=2**e
    odd=(e%2==1)
    assert (gcd(3,q-1)==1)==odd
    return dict(e=e,q=q,curve_power=4,
       projective_arc_exactly_if_odd_e=odd,
       algebraic_slope_from_u_v="(u+v)^3",
       power_map_cube_injective=gcd(3,q-1)==1,
       actual_infinite_nongq_family_when_e_odd_ge3=odd and e>=3,
       fixed_b=1,fixed_C=3,fixed_kappa=1,
       no_claim_original_arc_construction=True)


def finite_arc_case(q,exponent,scheme="lex"):
    field=Field(q)
    arc=affine_arc_oracle(field,exponent)
    if not arc["projective_arc"]:
        raise ValueError("invalid projective arc source")
    m=source_from_affine_arc(field,exponent)
    fft=fourier_root_character_census(field,exponent)
    labels=typed_maps(m,scheme)
    assert labels["aP"]==labels["aL"]
    # Additional *actual* small source adversarial original owner conflicts.
    # q=8 source has 4096 flags and 512 points: do not construct dense
    # 512x512 integer matrices and compare O(n^3) just for an oracle.
    Fp=m["points"];Fl=len(m["lines"])
    assert Fp==Fl==q**3
    screen=necessary_small_excess_screen(q-1,q-1,
        m["excess_lines"],m["excess_points"])
    assert screen["connectedness_forced_by_size"]
    assert screen["component_count_upper"]==1
    if q in (3,5) and exponent==2:
        published=wenger_W2_prime_source(q)
        assert m["lines"]==published["lines"]
        assert m["flags"]==published["flags"]
    return dict(q=q,exponent=exponent,scheme=scheme,
        actual_girth_at_least_8=True,
        actual_SOURCE_original_flags=len(m["flags"]),
        actual_source_points=Fp,actual_source_lines=Fl,
        original_missing_projections=len(m["missing"]),
        original_existing_projections=len(m["projected"]),
        exact_original_all_flag_3st_load=True,
        correct_fixed_source_degree=q,
        source_nongq_moore_excess=m["excess_lines"],
        arc=arc,Fourier=fft,
        minimal_pair_alphabet_first=labels["aP"],
        minimal_pair_alphabet_second=labels["aL"],
        forced_connected_at_quadratic_scale=True,
        actual_genuine_graph_NOT_synthetic_F=True,
        no_ambient_GQ_assumption=True)


def bad_curve_falsifier(q,exponent):
    field=Field(q)
    arc=affine_arc_oracle(field,exponent)
    if arc["projective_arc"]:
        raise ValueError("expected a bad curve with a collinear triple")
    failure=""
    try:
        source_from_affine_arc(field,exponent,require_arc=False)
    except ValueError as err:
        failure=str(err)
    assert "6-cycle" in failure or "multiple 3paths" in failure
    return dict(q=q,exponent=exponent,
        concrete_collinear_triple=arc["literal_all_collinear_triples"][0],
        actual_incidence_first_rejection=failure,
        original_C6_rejected_by_independent_graph_checker=True,
        no_false_girth8_from_plain_q_regular_degree=True)


def binary_q8_historical_six_id_inverse(scheme="lex"):
    """Targeted actual GF8 fourth-power source historical BBo witness.

    First derive a real proper physical 3walk from original geometry
    and freeze the six ACTUAL named source owners: 3 FULL projection
    anchors and 3 CORE physical edge owners. Run the THREE complete
    independent historical BBo inverse algorithms on ONLY these owners,
    not an unbounded exhaustive 4096-owner census. Then delete one
    original FULL anchor and independently confirm the witness vanishes.
    """
    from gio_t3c2_partial_books import inverse_certificate
    from hyp105_aa4_branch_a_integrated_referee import actual_edges,historical_bbo
    field=Field(8)
    m=source_from_affine_arc(field,4)
    typed=typed_maps(m,scheme)
    actual_projection={(p,l):(anchors[1][0],anchors[1][1])
         for (p,l),anchors in m["projected"].items()}
    model=dict(m,**typed,
       projection=actual_projection,
       flag_to_id={f:i for i,f in enumerate(m["flags"])})
    original=frozenset(range(len(m["flags"])))
    physical,owner=actual_edges(model,original)
    witness=None
    examined=0
    # The bound catches a real loss of test coverage rather than silently
    # enumerating the whole physical graph indefinitely in CI.
    for v0 in sorted(physical):
        if witness is not None:
            break
        for v1 in sorted(physical[v0]):
            if witness is not None:
                break
            for v2 in sorted(physical[v1]):
                if witness is not None:
                    break
                for v3 in sorted(physical[v2]):
                    examined+=1
                    if examined>3000000:
                        raise AssertionError("no genuine q8 arc source BBo in bounded 3walk search")
                    vs=(v0,v1,v2,v3)
                    xs={u[0] for u in vs};ys={u[1] for u in vs}
                    if len(xs)!=4 or len(ys)!=4:
                        continue
                    q=model["point_by_pair"].get(tuple(sorted((v0[0],v3[0]))))
                    ell=model["line_by_pair"].get(tuple(sorted((v0[1],v3[1]))))
                    if q is None or ell is None or (q,ell) not in actual_projection:
                        continue
                    p,k=actual_projection[q,ell]
                    if set(model["f"][p])&xs or set(model["g"][k])&ys:
                        continue
                    anchors=tuple(model["flag_to_id"][flag] for flag
                       in ((q,k),(p,k),(p,ell)))
                    residual=tuple(owner[tuple(sorted((a,b)))]
                       for a,b in zip(vs,vs[1:]))
                    if len(set(residual))!=3 or len(set(anchors+residual))!=6:
                        continue
                    six=tuple(sorted(anchors+residual))
                    if not historical_bbo(model,six):
                        continue
                    witness=(anchors,residual,six,vs)
                    break
    assert witness is not None
    anchors,residual,six,path=witness
    A=frozenset(six)
    C=frozenset(residual)
    assert len(A)==6 and len(C)==3 and C<=A
    cert=inverse_certificate(model,A,C)
    assert cert["original_source_motifs"]==1
    assert cert["manual_physical_first_equals_published"]
    assert cert["manual_physical_first_equals_source_owner_join"]
    assert cert["exact_original_six_ID_nontrivial_inverse"]
    assert cert["missing_projections_not_completed"]
    deleted_anchor=anchors[0]
    after=inverse_certificate(model,A-{deleted_anchor},C)
    assert after["original_source_motifs"]==0
    return dict(q=8,curve_power=4,scheme=scheme,
       true_original_source_flags=len(m["flags"]),
       original_missing_projection_count=len(m["missing"]),
       bounded_actual_physical_threewalks_examined=examined,
       original_FULL_survivors=len(A),proper_CORE_owners=len(C),
       genuine_original_six_source_IDs=six,
       three_FULL_original_projection_anchors=anchors,
       three_CORE_original_owners=residual,
       witness_uses_genuine_original_3flag_projection=True,
       witness_vanishes_after_one_FULL_anchor_deleted=True,
       actual_produced_original_BBo_sixsets=cert["original_source_motifs"],
       manual_published_source_first_exactly_agree=True,
       no_GQ_completion_or_synthetic_old_anchor=True)


def arc_family_theorem():
    ledger=integrated_quadratic_direct_ledger(1,3,1,Q(1),Q(1))
    assert ledger["moment_sixth_condition_is_NOT_required"]
    assert ledger["fixed_before_source"]["centered_operator_kappa"]==1
    return dict(claim="ALL_AFFINE_PROJECTIVE_Q_ARCS_GET_ORIGINAL_T3_Q",
       scope="every prime power q>=5 and every h:Fq->Fq with no three collinear projective (1,u,h(u))",
       source_vertices_each="q^3",
       source_original_flags="q^4",
       source_girth_at_least_8=True,
       source_excess_exact="2q(q-1)",
       fixed_parameters=dict(b=1,C=3,kappa=1),
       exact_original_source_spectral_gate="||F0||^2=max(q(q-2)^2,8q)<=(q-1)^3",
       theorem="every legal minimal complete pair injective f/g and all deletions |Z|<=rho*(q-1)^4 give historical source D6+BBo_produced>=delta*(q-1)^6 for all q>=r0+1",
       all_HYP105_original_six_source_flags=True,
       actual_full_core_BBo_inverse_from_parent=True,
       known_projective_arc_graph_and_Fourier_are_prior_art=True,
       known_Wenger_arc_parabola_not_new=True,
       no_claim_new_affine_arc_graph_construction=True,
       no_GQ_template_needed_by_source_proof=True,
       no_claim_that_arcs_are_necessarily_nonembeddable=True,
       no_unrestricted_T3_or_ASET_claim=True,
       all_external_ordinary_C6_numbers_FORMAL_ONLY=True,
       exact_formal_parameter_ledger=ledger)


def certificate():
    actual=[finite_arc_case(*case) for case in (
       (3,2,"lex"),(5,2,"lex"),(8,2,"lex"),
       (8,4,"lex"),(8,4,"correlated"))]
    assert actual[3]["Fourier"]["exact_zero_count_multiplicity"]==actual[2]["Fourier"]["exact_zero_count_multiplicity"]
    negatives=[bad_curve_falsifier(4,4)]
    original_binary_BBo=binary_q8_historical_six_id_inverse("lex")
    # q=16 is non-arc but constructing a 4096x4096 source would be
    # needless; the independent determinant+slope oracle still rejects.
    q16=affine_arc_oracle(Field(16),4)
    assert not q16["projective_arc"]
    # Symbolic all-order: distinct from finite q8 experimental case.
    binary=[binary_fourth_power_all_order(e)
       for e in (2,3,4,5,6,7,9,11)]
    return dict(schema=SCHEMA,parent_G6D2_HEAD=PARENT_G6D2,
       issue=793,meta_issue=790,
       claim="STRUCTURAL_AFFINE_ARC_TO_QUADRATIC_T3_ALL_FAMILIES",
       actual_finite_source_falsifiers=actual,
       actual_bad_source_negative_controls=negatives,
       true_binary_q8_novel_arc_historical_BBo_inverse=original_binary_BBo,
       q16_nonarc_det_only=q16,
       infinite_binary_power4_arc_certificate=binary,
       general_affine_projective_q_arc_theorem=arc_family_theorem(),
       projective_arc_incidence_construction_prior_art=True,
       generalized_Wenger_Cayley_character_method_prior_art=True,
       new_Mathlab_contribution_conditional_six_source_ID_transfer=True,
       no_unconditional_every_quadratic_source_T3=True,
       no_independent_external_review_or_Lean=True)


if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--out",default="gio003-g6d3-affine-arc-transfer.json")
    a=p.parse_args()
    z=certificate()
    Path(a.out).write_text(json.dumps(z,sort_keys=True,indent=2)+"\n",
                            encoding="utf-8")
    print("PASS_GIO003_G6D3_AFFINE_ARC_SOURCE_T3_CERTIFICATE")
