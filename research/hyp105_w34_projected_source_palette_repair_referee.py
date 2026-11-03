"""AA4-W34-LOCAL: exact 51-palette projected ORIGINAL GF(5) source repair.

For a globally fixed source flag i, all equal-GF5-triple-sum pairs
fall in U/U, A_i/A_i or U/A_i. U/U and A_i/A_i are invariant under
changing c_i; only cross term U/A_i changes.

A_i triples are {i,j,k}; U triples avoid i. In the 24 physical
coordinates OUTSIDE the unchanged 2+2 support of original flag i,
a putative equality requires s(U)|_outside == s({j,k})|_outside.
This enables ONE exact pass over all C(424,3)=12,614,424 original
other-source triples to compute the cross-collision count for ALL
51 possible nonzero checksum4 source palettes. The remaining four
physical GF5 differences determine exactly WHICH palette would
create the equality. There is NO random fingerprint or 51 rescans.

This is a finite, source-preserving, full-3sum collision descent,
not an all-h theorem or a guaranteed source-zero construction.
Accepted W34 edits are independently checked by a COMPLETE fresh
12,704,100-triple external original GF5 R3 census.
"""
from collections import Counter,defaultdict
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import json
import math

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_original_gf5_deterministic_extraction_referee import PALETTES
from hyp105_w34_external_triple_r3_referee import (
    BASE,DIGIT_POWERS,_add_four_digit_table,_packed_four_groups,
    _signature_from_grouped_add,exact_gf5_original_vectors,
    exact_full_original_external_r3,deterministic_original_checksum_palettes,
)


@lru_cache(None)
def _subtract_to_gf5_palette():
    """Exact 625x625 difference table, -1 unless a legal checksum4 palette."""
    bypattern={tuple(p):i for i,p in enumerate(PALETTES)}
    digits=tuple(tuple((x//DIGIT_POWERS[j])%5 for j in range(4))
                 for x in range(BASE))
    table=tuple(bypattern.get(tuple((x[j]-y[j])%5 for j in range(4)),-1)
                for x in digits for y in digits)
    assert len(table)==390625
    return table


def _real_original_source_support(model,source_id):
    n=model["N"];a=model["a"]
    if type(source_id) is not int or not 0<=source_id<n:
        raise ValueError("real original source ID in range required")
    p,ell=model["incidences"][source_id]
    coords=(model["left_labels"][p][0],model["left_labels"][p][1],
            a+model["right_labels"][ell][0],
            a+model["right_labels"][ell][1])
    if len(set(coords))!=4:
        raise AssertionError("not 2+2 genuine original source physical coordinates")
    return coords


def _gf5_four_support_projection(model,source_id):
    """Lossless split into outside 24D and inside 4D coordinates.

    Every original full GF5^m vector has a unique pair
    (outside_key, inside_key), each obtained via exact base-five
    digit extraction. The outside key is independent of the
    source flag i coefficients.
    """
    m=model["m"]
    if m not in (12,28) or m%4:
        raise ValueError("only true W32/W34 original 4-GF5-digit groups")
    chosen=_real_original_source_support(model,source_id)
    outside=tuple(k for k in range(m) if k not in chosen)
    if len(outside)!=m-4:
        raise AssertionError("four original support coordinates not unique")
    outpos={q:j for j,q in enumerate(outside)}
    inpos={q:j for j,q in enumerate(chosen)}
    out_luts=[]
    in_luts=[]
    for group in range(m//4):
        o=[];inside=[]
        for val in range(BASE):
            opart=0;ipart=0
            for k in range(4):
                real=4*group+k
                digit=(val//DIGIT_POWERS[k])%5
                if real in outpos:
                    opart+=digit*5**outpos[real]
                else:
                    ipart+=digit*5**inpos[real]
            o.append(opart);inside.append(ipart)
        out_luts.append(tuple(o));in_luts.append(tuple(inside))
    return tuple(out_luts),tuple(in_luts),outside,chosen


def _two_sum_collision_source_pairs(model,indices):
    """All true original equal-2sum source pairs, no expected risk."""
    ids,vectors=exact_gf5_original_vectors(model,indices)
    n=len(ids)
    parts=_packed_four_groups(vectors)
    add=_add_four_digit_table()
    grouped=defaultdict(list)
    for i in range(n-1):
        a=parts[i]
        for j in range(i+1,n):
            b=parts[j]
            signature=_signature_from_grouped_add(a,b,add)
            grouped[signature].append((i,j))
    witness=[]
    for values in grouped.values():
        for x,y in combinations(values,2):
            if set(x)&set(y):
                raise AssertionError("distinct ORIGINAL source columns duplicate")
            witness.append((x,y))
    return tuple(sorted(witness))


def source_palette_51_exact_cross_histogram(model,indices,source_id,
                                          *,max_other_triples=12_614_424):
    """Exact all-51 GF5 conditional cross counts in ONE other-triple pass.

    U is all triples not containing i. A_i contains flag i plus a
    two-subset of other original IDs. Each equality U == A_i is
    equivalent to outside(U) == outside(pair) and
    palette_i == inside(U) - inside(pair) in GF5^4.

    Crucially, the all-51 histogram is built by determining the
    REQUIRED palette of each matching projected pair, instead of
    rehashing the entire triple space 51 times.
    """
    ids,vectors=exact_gf5_original_vectors(model,indices)
    n=len(ids)
    if n<6 or n>425:
        raise ValueError("only genuine full real W32/W34 source scope")
    if type(max_other_triples) is not int or max_other_triples<0:
        raise ValueError("nonnegative full source other-triple budget")
    expected=math.comb(n-1,3)
    if expected>max_other_triples:
        raise ValueError("incomplete exact original source budget: fail CLOSED")
    other=tuple(i for i in range(n) if i!=source_id)
    if len(other)!=n-1:
        raise ValueError("real original source ID missing")
    add=_add_four_digit_table()
    subtract=_subtract_to_gf5_palette()
    parts=_packed_four_groups(vectors)
    out_luts,in_luts,out_coords,support=_gf5_four_support_projection(
        model,source_id)
    ng=len(out_luts)
    if ng!=len(parts[0]):
        raise AssertionError("source projection is not physical model dimension")
    other_parts=tuple(parts[i] for i in other)

    # 89,676 W34 pair entries, indexed by their EXACT outside
    # physical GF5^24 sum, with 4D inside sum multiplicities.
    indexed=defaultdict(Counter)
    pairs=0
    for u in range(n-2):
        a=other_parts[u]
        for v in range(u+1,n-1):
            b=other_parts[v]
            outside=inside=0
            for k in range(ng):
                limb=add[BASE*a[k]+b[k]]
                outside+=out_luts[k][limb]
                inside+=in_luts[k][limb]
            indexed[outside][inside]+=1
            pairs+=1
    if pairs!=math.comb(n-1,2):
        raise AssertionError("missing real original two-other-source subset")

    histogram=[0]*51
    three_count=0
    projected_matches=0
    palette_possible_matches=0
    for u in range(n-3):
        a=other_parts[u]
        for v in range(u+1,n-2):
            b=other_parts[v]
            pair=tuple(add[BASE*a[k]+b[k]] for k in range(ng))
            for w in range(v+1,n-1):
                c=other_parts[w]
                outside=0
                limbs=[]
                for k in range(ng):
                    limb=add[BASE*pair[k]+c[k]]
                    outside+=out_luts[k][limb]
                    limbs.append(limb)
                three_count+=1
                possible=indexed.get(outside)
                if possible is None:continue
                inside=sum(in_luts[k][limbs[k]] for k in range(ng))
                for pair_inside,multiplicity in possible.items():
                    projected_matches+=multiplicity
                    which=subtract[BASE*inside+pair_inside]
                    if which>=0:
                        histogram[which]+=multiplicity
                        palette_possible_matches+=multiplicity
    if three_count!=expected:
        raise AssertionError("not every other three-original-flag subset visited")
    if any(h<0 for h in histogram):
        raise AssertionError("negative exact original GF5 local projection count")
    old=histogram[indices[source_id]]
    best=min(range(51),key=lambda k:(histogram[k],k))
    return {
        "original_source_id":source_id,
        "original_source_support":support,
        "outside_original_GF5_coordinate_count":len(out_coords),
        "source_other_pair_count":pairs,
        "source_other_triples_processed":three_count,
        "cross_collision_count_current_palette":old,
        "all_51_exact_cross_counts":tuple(histogram),
        "minimum_cross_count":histogram[best],
        "lex_first_best_palette_index":best,
        "strict_improvement":old-histogram[best],
        "projected_pair_triple_equalities":projected_matches,
        "projected_pair_triple_equalities_with_legal_GF5_palette":
            palette_possible_matches,
        "exact_full_source_no_sampling":True,
    }


def _initial_w34_risk_certificates():
    path=Path(__file__).with_name(
        "hyp105_w34_full_425flag_r3_seed0_certificates.json")
    c=json.loads(path.read_text(encoding="utf-8"))
    if (c["source_ORIGINAL_flag_count"]!=425
        or c["true_original_triple_count"]!=12704100
        or c["fixed_source_seed"]!=0
        or c["new_asymptotic_exponent_proved"]):
        raise AssertionError("wrong genuine complete W34 original baseline")
    return c


def exact_W34_r2_first_local_source_repair(scheme,*,seed=0,
                                           max_evaluations=3,
                                           max_source_updates=2):
    """Finite W34 source-local R2-first repair, not a zero-risk claim.

    R2 hotspots: choose real source IDs participating in known exact
    original equal-2sum pairs. Each evaluated i receives the EXACT
    51-palette cross D3 histogram (one full other-triple pass).
    Accept only strict D3 decrease. Recompute actual R2 by independent
    real source pair sums after every accepted edit.
    A final NEW complete external full 12,704,100-triple W34 census
    MUST match the predicted exact D3 and R2 and R3 identity.
    """
    if (scheme not in ("lex","reverse-line")
        or type(seed) is not int or seed!=0):
        raise ValueError("only pinned genuine W34 original seed0 schemes")
    if (type(max_evaluations) is not int or max_evaluations<0
        or type(max_source_updates) is not int or max_source_updates<0
        or max_source_updates>max_evaluations):
        raise ValueError("nonnegative bounded ORIGINAL source repair budgets")
    model=pair_labeled_symplectic(2,scheme)
    if (model["N"]!=425 or model["m"]!=28 or model["s"]!=4
        or len(set(model["incidences"]))!=425):
        raise AssertionError("not complete true source symplectic W34")
    previous=_initial_w34_risk_certificates()["schemes"][scheme][
        "exact_complete_source_risk"]
    indices=list(deterministic_original_checksum_palettes(model,seed=seed))
    old_pairs=_two_sum_collision_source_pairs(model,indices)
    expectedD2=previous["all_original_1_2_source_sum_checks"][
        "two_source_sum_collisions"]
    if len(old_pairs)!=expectedD2:
        raise AssertionError(("historical W34 baseline R2 drift",
                              len(old_pairs),expectedD2))
    expectedD3=previous["equal_sum_pairs_of_distinct_ORIGINAL_triples"]
    totalD3=expectedD3
    steps=[]
    evaluated=[]
    while len(evaluated)<max_evaluations and len(steps)<max_source_updates:
        pairs=_two_sum_collision_source_pairs(model,indices)
        if not pairs:break
        degree=Counter(i for a,b in pairs for i in a+b)
        ranked=tuple(sorted(degree,key=lambda x:(-degree[x],x)))
        choice=next((i for i in ranked if i not in evaluated),None)
        if choice is None:break
        result=source_palette_51_exact_cross_histogram(
            model,tuple(indices),choice)
        evaluated.append(choice)
        improvement=result["strict_improvement"]
        if not improvement:continue
        prior_index=indices[choice]
        indices[choice]=result["lex_first_best_palette_index"]
        newD3=totalD3-improvement
        if newD3<0 or newD3>=totalD3:
            raise AssertionError("SOURCE-local GF5 D3 objective failed to decrease")
        newD2=len(_two_sum_collision_source_pairs(model,indices))
        if newD2<0 or newD2>newD3:
            raise AssertionError("GF5 source 2-sum risk exceeds 3-sum overlap")
        steps.append({
            "original_source_id":choice,
            "original_prior_palette_index":prior_index,
            "original_new_palette_index":indices[choice],
            "real_source_D2_before":len(pairs),
            "real_source_D2_after":newD2,
            "full_D3_before":totalD3,
            "full_D3_after":newD3,
            "all_51_source_palettes_exactly_evaluated":True,
            "source_other_triples_processed":result[
                "source_other_triples_processed"],
            "source_cross_cost_all_51":result["all_51_exact_cross_counts"],
        })
        totalD3=newD3
    # FULL independent proof gate: rerun all 12.7 million actual original
    # triples, recheck their EXACT full GF5^28 collision signatures,
    # full two-sum collisions, 6-DISTINCT source signed risk and overlap.
    final=exact_full_original_external_r3(
        model,tuple(indices),max_triples=12704100,max_witnesses=8)
    newD2=len(_two_sum_collision_source_pairs(model,indices))
    if (final["equal_sum_pairs_of_distinct_ORIGINAL_triples"]!=totalD3
        or final["R2_signed_2v2_events_exact"]!=newD2
        or final["FULL_six_distinct_original_ID_3v3_signed_event_count"]
           !=totalD3-421*newD2
        or not final[
            "independent_original_R2_to_R3_overlap_identity_verified"]):
        raise AssertionError("source-local W34 exact count vs INDEPENDENT full census failed")
    return {
        "fixed_original_scheme":scheme,
        "source_seed":seed,
        "source_original_flag_count":425,
        "original_full_D2_before":expectedD2,
        "original_full_D3_before":expectedD3,
        "original_full_signed_R3_before":previous[
            "FULL_six_distinct_original_ID_3v3_signed_event_count"],
        "evaluated_original_source_IDs":tuple(evaluated),
        "accepted_true_original_source_changes":tuple(steps),
        "changed_original_flag_count":len(steps),
        "all_425_ORIGINAL_flag_palette_indices":tuple(indices),
        "new_exact_full_source_R2":newD2,
        "new_exact_full_source_D3":totalD3,
        "new_exact_full_source_signed_R3":final[
            "FULL_six_distinct_original_ID_3v3_signed_event_count"],
        "full_0_to_3_ASET_success":final[
            "complete_source_GF5_zero_to_three_ASET"],
        "all_12_704_100_original_triples_independently_rechecked":final[
            "all_triples_exact_external_disk_records_processed"]==12704100,
        "full_original_exact_signed_witnesses":final[
            "verified_independent_true_source_witnesses"],
        "no_all_h_or_source_zero_guarantee":True,
    }


def report(*,scheme="lex",max_evaluations=3,max_source_updates=2):
    return {
        "research":"W34 exact 24D projected cross GF5 palette 51 oracle",
        "full_source":exact_W34_r2_first_local_source_repair(
            scheme,max_evaluations=max_evaluations,
            max_source_updates=max_source_updates),
        "new_asymptotic_ASET_exponent_proved":False,
    }


if __name__=="__main__":
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument("--scheme",choices=("lex","reverse-line"),
                        default="lex")
    parser.add_argument("--max-evaluations",type=int,default=3)
    parser.add_argument("--max-source-updates",type=int,default=2)
    args=parser.parse_args()
    print(json.dumps(report(
        scheme=args.scheme,max_evaluations=args.max_evaluations,
        max_source_updates=args.max_source_updates),
        sort_keys=True,indent=2))
