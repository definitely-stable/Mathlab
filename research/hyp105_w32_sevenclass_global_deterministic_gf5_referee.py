"""HYP-105 AA4-SEVENDET: complete seven leading original-sixset W32 CSP.

New structural lemma: for fixed nonzero GF(5) 4-entry palettes, each
physical coordinate equation sigma_i*a + sigma_j*b = 0 imposes a UNIQUE
GF(2) parity constraint on the two balanced +/- sign variables, or is
impossible. Connected original column-dual graphs admit AT MOST ONE
global-sign-unordered balanced event per original sixset.

This finite true-original W(3,2) program inventories EVERY accepted
seven-class 6+6-coordinate leafless sixset for the fixed maps lex
and reverse-line, recomputes all ten sign weights using a separate
exact 5^5 potential oracle, and emits a concrete zero-event palette
assignment to ALL 45 ORIGINAL source incidence flag IDs.

This is NOT the full R3; other non-6+6-column families are not excluded.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
from functools import lru_cache

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_g5e2b3e1a_fixed_leading import selected_left_six
from hyp105_g5e2b3e1b0_seven_signature import seven_census
from hyp105_original_gf5_deterministic_extraction_referee import (
    PALETTES,SIGNS,DENOM,_source_coordinate_edges,
)
from hyp105_original_aligned_bbo_gf5_fourier_referee import (
    gf5_fourier_potential_oracle,
)

CLASSES=("D6","B-left/A-right","A-left/B-right",
         "C/A","C/B","B/B-overlap","B/B-disjoint")
PINNED={
    "lex":{
        "counts":(15,98,110,13,1,8,14),
        "numerator":14874594,
        "sum_by_class":(812430,5627064,6213834,819300,59982,428832,913152)
    },
    "reverse-line":{
        "counts":(3,77,74,1,1,7,6),
        "numerator":9330448,
        "sum_by_class":(162486,4231006,4087738,63132,53718,374682,357686)
    }
}
assert len(PALETTES)==51 and len(SIGNS)==10


def _column_dual_and_type(ids,flags,labels,side):
    freq=Counter(flags[i][side] for i in ids)
    fprofile=tuple(sorted(freq.values(),reverse=True))
    pattern={
        (1,1,1,1,1,1):"A",
        (2,1,1,1,1):"B",
        (2,2,2):"C"
    }.get(fprofile)
    if pattern is None:return None,None
    positions=defaultdict(list)
    for col,id_ in enumerate(ids):
        for coord in labels[flags[id_][side]]:
            positions[coord].append(col)
    if len(positions)!=6 or any(len(x)!=2 for x in positions.values()):
        return None,None
    dual=tuple(sorted(tuple(sorted(v)) for v in positions.values()))
    return pattern,dual


def _is_simple_sixcycle(edges):
    if len(edges)!=6 or len(set(edges))!=6:
        return False
    a=[set() for _ in range(6)]
    for i,j in edges:
        if i==j:return False
        a[i].add(j);a[j].add(i)
    if any(len(v)!=2 for v in a):return False
    seen={0};stack=[0]
    while stack:
        for nxt in a[stack.pop()]:
            if nxt not in seen:
                seen.add(nxt);stack.append(nxt)
    return len(seen)==6


def independent_seven_source_class(ids,flags,f,g):
    """Independent of both historical seven/half-profile classifiers."""
    ids=tuple(sorted(ids))
    if len(ids)!=6 or len(set(ids))!=6 or any(
            type(i) is not int or i<0 or i>=len(flags) for i in ids):
        raise ValueError("six distinct ORIGINAL flag IDs required")
    lhs,left=_column_dual_and_type(ids,flags,f,0)
    rhs,right=_column_dual_and_type(ids,flags,g,1)
    if lhs is None or rhs is None:return None
    if lhs=="A" and rhs=="A":
        return "D6" if left==right and _is_simple_sixcycle(left) else None
    if lhs=="B" and rhs=="A":return "B-left/A-right"
    if lhs=="A" and rhs=="B":return "A-left/B-right"
    if {lhs,rhs}=={"C","A"}:return "C/A"
    if {lhs,rhs}=={"C","B"}:return "C/B"
    if lhs==rhs=="B":
        repeated_p=next(k for k,n in Counter(flags[i][0] for i in ids).items()
                        if n==2)
        repeated_l=next(k for k,n in Counter(flags[i][1] for i in ids).items()
                        if n==2)
        shared=sum(flags[i]==(repeated_p,repeated_l) for i in ids)
        if shared not in (0,1):
            raise AssertionError("duplicate ORIGINAL incidence or repeated factor ambiguity")
        return "B/B-overlap" if shared==1 else "B/B-disjoint"
    return None


def true_original_w32_seven_hypergraph(scheme):
    """Full *seven-class selected leading family*, not all 45C6 sixsets."""
    if scheme not in PINNED:
        raise ValueError("only the two exact previously audited W32 maps")
    model=pair_labeled_symplectic(1,scheme)
    if (model["N"]!=45 or model["v"]!=15 or model["a"]!=6 or
        len(set(model["incidences"]))!=45):
        raise AssertionError("not complete true original W32 K6 source")
    flags=tuple(model["incidences"])
    f=tuple(model["left_labels"]);g=tuple(model["right_labels"])
    accepted=seven_census(model,independent_checks=False,witness_sets=True)
    if (accepted["left_6coordinate_candidates"]!=62370 or
        accepted["S_seven"]!=sum(PINNED[scheme]["counts"])):
        raise AssertionError("original exhaustive source six-column census regressed")
    real={}
    seen=set()
    # Independently reconstruct source factor profiles and named physical
    # coordinate 2-factors for ALL 62,370 source-selected candidates.
    for ids,_left in selected_left_six(model):
        if ids in seen:raise AssertionError("original source candidate duplicate")
        seen.add(ids)
        actual=independent_seven_source_class(ids,flags,f,g)
        historic=accepted["sets"].get(ids)
        if actual!=historic:
            raise AssertionError(("independent real source classifier differs",ids,actual,historic))
        if actual is not None:
            edges,sides=_source_coordinate_edges(flags,ids,f,g)
            if len(edges)!=12 or len(sides[0])!=6 or len(sides[1])!=6:
                raise AssertionError("not six physical coordinates on BOTH true types")
            real[ids]={"ids":ids,"kind":actual,"edges":edges}
    if len(seen)!=62370 or set(real)!=set(accepted["sets"]):
        raise AssertionError("full seven original-sixset family incomplete")
    census=Counter(m["kind"] for m in real.values())
    if tuple(census[k] for k in CLASSES)!=PINNED[scheme]["counts"]:
        raise AssertionError("independently reconstructed seven-class counts changed")
    usage=Counter(i for m in real.values() for i in m["ids"])
    incidence_pairs=Counter()
    ordered=tuple(real[k] for k in sorted(real))
    for n,m in enumerate(ordered):
        s=set(m["ids"])
        for other in ordered[n+1:]:
            common=len(s.intersection(other["ids"]))
            incidence_pairs[common]+=1
    return {
        "scheme":scheme,"source":model,
        "motifs":ordered,"counts":dict((k,census[k]) for k in CLASSES),
        "selected_original_sixsets":len(ordered),
        "physical_leading_candidates":len(seen),
        "original_source_flag_degree":dict(sorted(usage.items())),
        "overlap_size_histogram":dict(sorted(incidence_pairs.items())),
        "all_45_original_flag_count":len(flags),
        "full_original_GQ_source":True,
        "not_all_possible_six_source_ID_subsets":True,
    }


@lru_cache(maxsize=8192)
def _one_signed_gf5_weight(dual,plus):
    return gf5_fourier_potential_oracle(dual,plus)


def independent_all_ten_exact_expected_risk(family):
    """Recompute all accepted sixsets and signs with #708 5^5-potential
    GF5 oracle; independent of historical 782-dual support Fourier.
    """
    scheme=family["scheme"]
    sums=Counter()
    for m in family["motifs"]:
        dual=tuple((i,j) for i,_slot_i,j,_slot_j in m["edges"])
        sums[m["kind"]]+=sum(_one_signed_gf5_weight(dual,p) for p in SIGNS)
    expected=tuple(sums[k] for k in CLASSES)
    if expected!=PINNED[scheme]["sum_by_class"]:
        raise AssertionError(("third-oracle exact GF5 seven-class mass mismatch",
                              scheme,expected,PINNED[scheme]["sum_by_class"]))
    total=sum(expected)
    if total!=PINNED[scheme]["numerator"] or not total<DENOM:
        raise AssertionError("no certified <1 exact leading-seven-family expectation")
    return {
        "source_scheme":scheme,
        "exact_GF5_ten_sign_mass_by_class":dict(zip(CLASSES,expected)),
        "all_selected_original_sevenclass_signed_mass_numerator":total,
        "GF5_51_palette_power6":DENOM,
        "exact_mean_signed_events":Fraction(total,DENOM),
        "union_bound_probability_no_signed_events_at_least":1-Fraction(total,DENOM),
        "zero_exists_for_all_selected_sevenclass_sixsets":True,
        "not_full_R3":True,
    }


def _source_palette_by_id(scheme,seed,n):
    """Deterministic hash-domain fixture, NOT a proof of bounded seed search."""
    if type(seed) is not int or seed<0:
        raise ValueError("nonnegative deterministic search seed")
    return tuple(int.from_bytes(sha256(
        ("HYP105-W32-SEVENDET-V1/"+scheme+"/"+str(seed)+"/"+str(i)).encode()
    ).digest()[:8],"big")%51 for i in range(n))


def slow_direct_original_sign_events(motif,assignment):
    """Independent reference: brute ALL 10 named balanced signs, every
    12 true source coordinate equations, no GF2 parity algorithm.
    """
    out=[]
    for plus in SIGNS:
        sig=[1 if j in plus else -1 for j in range(6)]
        if all((sig[i]*assignment[motif["ids"][i]][slot_i]
                +sig[j]*assignment[motif["ids"][j]][slot_j])%5==0
               for i,slot_i,j,slot_j in motif["edges"]):
            out.append(tuple(sorted(plus)))
    return tuple(out)


def parity_sign_events(motif,assignment):
    """NEW exact all-h signed-event reduction: GF5 physical cancellations
    become an affine GF2 parity system on the six ORIGINAL sign bits.

    If a==b (GF5), signs must be opposite; if a+b==0, signs must be
    equal; otherwise the single physical coordinate is impossible.
    Reuse same original-ID palette within every motif, and enumerate
    only free connected-component flips (not ten complete GF5 scans).
    """
    ids=motif["ids"]
    if any(i not in assignment or assignment[i] not in PALETTES for i in ids):
        raise ValueError("missing/illegal genuine original source palette")
    adj=[[] for _ in range(6)]
    for i,slot_i,j,slot_j in motif["edges"]:
        x=assignment[ids[i]][slot_i]
        y=assignment[ids[j]][slot_j]
        if x==y:
            parity=1
        elif (x+y)%5==0:
            parity=0
        else:
            return ()
        adj[i].append((j,parity));adj[j].append((i,parity))
    bits=[None]*6
    comps=[]
    for start in range(6):
        if bits[start] is not None:continue
        bits[start]=0
        component=[start]
        for u in component:
            for v,xor in adj[u]:
                proposed=bits[u]^xor
                if bits[v] is None:
                    bits[v]=proposed;component.append(v)
                elif bits[v]!=proposed:
                    return ()
        comps.append(tuple(component))
    valid=[]
    # One bit per connected component is freely invertible; fix sign
    # on canonical original column 0 to + to quotient global negation.
    for choices in product((0,1),repeat=len(comps)):
        chosen=list(bits)
        for component,flip in zip(comps,choices):
            for u in component:chosen[u]^=flip
        if chosen[0]!=1 or sum(chosen)!=3:
            continue
        valid.append(tuple(i for i,bit in enumerate(chosen) if bit))
    result=tuple(sorted(valid))
    if len(set(result))!=len(result) or len(result)>10:
        raise AssertionError("invalid balanced sign orbit under original column parity")
    return result


def hypergraph_direct_event_census(family, assignment, *,independent_parity=True):
    """Every selected ORIGINAL sixset, every signed event on one map.
    No expectation, likelihood, Monte Carlo, or zero-by-assertion.
    """
    n=family["all_45_original_flag_count"]
    if (len(assignment)!=n or
        any(i not in assignment or assignment[i] not in PALETTES for i in range(n))):
        raise ValueError("one valid checksum4 GF5 palette per all 45 ORIGINAL flags")
    byclass=Counter()
    witnesses=[]
    parity_histo=Counter()
    for m in family["motifs"]:
        events=parity_sign_events(m,assignment)
        parity_histo[len(events)]+=1
        if independent_parity:
            direct=slow_direct_original_sign_events(m,assignment)
            if events!=direct:
                raise AssertionError(("parity physical GF2 signed SAT differs from direct GF5",
                                      m["ids"],events,direct))
        if events:
            byclass[m["kind"]]+=len(events)
            witnesses.extend((m["ids"],sgn) for sgn in events)
    return {
        "actual_ten_sign_event_count":len(witnesses),
        "colliding_original_sixset_count":sum(v for n,v in parity_histo.items() if n),
        "event_count_by_original_class":dict((k,byclass[k]) for k in CLASSES),
        "number_sign_events_per_original_sixset_histogram":dict(sorted(parity_histo.items())),
        "actual_ORIGINAL_signed_event_witnesses":tuple(witnesses),
        "exact_physical_parity_vs_brute_GF5_oracle_checked":independent_parity,
    }


def find_actual_global_sevenclass_zero_certificate(family,*,max_seeds=64):
    """Deterministic finite search with a full direct check, not
    guaranteed to succeed under arbitrary unseen source f,g.
    Existence for two chosen W32 maps follows separately from <1
    exact Fourier expectation, NOT the empirical finite search.
    """
    if type(max_seeds) is not int or max_seeds<1:
        raise ValueError("positive deterministic finite search budget required")
    n=family["all_45_original_flag_count"]
    reference=tuple(PALETTES[0] for _ in range(n))
    baseline=hypergraph_direct_event_census(
        family,dict(enumerate(reference)),independent_parity=True)
    for seed in range(max_seeds):
        indices=_source_palette_by_id(family["scheme"],seed,n)
        assign={i:PALETTES[index] for i,index in enumerate(indices)}
        result=hypergraph_direct_event_census(
            family,assign,independent_parity=True)
        if result["actual_ten_sign_event_count"]==0:
            return {
                "scheme":family["scheme"],
                "tested_complete_original_sixset_count":len(family["motifs"]),
                "certified_original_flags":n,
                "seed":seed,
                "original_flag_palette_indices":indices,
                "original_flag_palettes":assign,
                "all_ones_reference_actual_signed_events":
                    baseline["actual_ten_sign_event_count"],
                "zero_selected_sevenclass_actual_signed_events":0,
                "physical_SAT_parity_and_direct_GF5_fully_agree":
                    result["exact_physical_parity_vs_brute_GF5_oracle_checked"],
                "excludes_full_R3_or_unselected_ORIGINAL_sixset_claim":True,
            }
    raise AssertionError("bounded deterministic search failed; no zero claim")


def check_supplied_full_original_certificate(family,indices):
    """External reproducibility: neither trust search nor signed count."""
    if (len(indices)!=45 or
        any(type(i) is not int or not 0<=i<51 for i in indices)):
        raise ValueError("exactly 45 legal ORIGINAL source palette indices needed")
    assignment={i:PALETTES[k] for i,k in enumerate(indices)}
    r=hypergraph_direct_event_census(
        family,assignment,independent_parity=True)
    if r["actual_ten_sign_event_count"]!=0:
        raise ValueError("claimed zero-event original source certificate is false")
    return r


def report():
    out=[]
    for scheme in ("lex","reverse-line"):
        family=true_original_w32_seven_hypergraph(scheme)
        f=independent_all_ten_exact_expected_risk(family)
        witness=find_actual_global_sevenclass_zero_certificate(family)
        independently=check_supplied_full_original_certificate(
            family,witness["original_flag_palette_indices"])
        out.append({
            "source_scheme":scheme,
            "sevenclass_original_sixsets":family["counts"],
            "accepted_original_sixset_total":len(family["motifs"]),
            "all_original_source_flag_count":family["all_45_original_flag_count"],
            "exact_all_seven_GF5_event_mean":str(f["exact_mean_signed_events"]),
            "exact_at_least_fraction_zero_palette_assignments":
                str(f["union_bound_probability_no_signed_events_at_least"]),
            "source_sextuple_overlap_histogram":family["overlap_size_histogram"],
            "first_successful_deterministic_seed":witness["seed"],
            "complete_45_original_flag_GF5_palette_indices":
                witness["original_flag_palette_indices"],
            "all_ones_actual_events":witness["all_ones_reference_actual_signed_events"],
            "actual_zero_sevenclass_signed_events":
                independently["actual_ten_sign_event_count"],
            "not_total_R3":True,
        })
    return {
        "source":"actual ORIGINAL symplectic W(3,2); two fixed K6 pair maps",
        "finite_seven_leading_family_risk_certificates":out,
        "scoped_all_h_6_column_GF5_parity_lemma":True,
        "does_not_bound_other_original_motifs_or_new_ASET_exponent":True,
    }


if __name__=="__main__":
    import json
    print(json.dumps(report(),indent=2,sort_keys=True))
