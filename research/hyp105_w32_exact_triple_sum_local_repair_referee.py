"""AA4-FULLR3-LREPAIR: exact local GF(5) triple-sum collision descent.

When changing ONE ORIGINAL source-flag palette c_i, only the
C(N-1,2) triples containing i change. Equal sums between TWO affected
triples cancel c_i and are constant. Equality between TWO unaffected
triples is constant. Only equality between one affected and one
unaffected triple changes. Exact global 3-sum collision improvement
therefore reduces to 51 evaluations against C(N-1,2) pair sums,
not scanning all sixsets or reweighting every original flag.

This is a finite W32 deterministic repair HEURISTIC, not an
asymptotic all-h zero-existence theorem or guaranteed local descent
for arbitrary f,g. Each accepted move is INDEPENDENTLY checked by
a fresh full triple-sum census on all 14,190 original triples.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json

from hyp105_original_gf5_deterministic_extraction_referee import PALETTES
from hyp105_w32_complete_r3_triple_sum_referee import (
    _field_sum,_sums_by_cardinality,
    true_original_source_vectors,full_original_r3_triple_hash_census,
    committed_sevenclass_indices,
)
from hyp105_w32_sevenclass_global_deterministic_gf5_referee import (
    true_original_w32_seven_hypergraph,
)


def _replacement_source_vector(model,source_id,palette_index):
    if type(source_id) is not int or not 0<=source_id<45:
        raise ValueError("one real original source ID 0..44 required")
    if type(palette_index) is not int or not 0<=palette_index<51:
        raise ValueError("one real GF5 checksum4 51-palette index required")
    point,line=model["incidences"][source_id]
    f=model["left_labels"][point];g=model["right_labels"][line]
    coords=(f[0],f[1],6+g[0],6+g[1])
    out=[0]*12
    for j,coord in enumerate(coords):
        out[coord]=PALETTES[palette_index][j]
    if sum(out)%5!=4 or sum(v!=0 for v in out)!=4:
        raise AssertionError("not original globally immutable typed support")
    return tuple(out)


def _full_triple_duplicate_count(vectors):
    return _sums_by_cardinality(vectors,3)[1]


def _collision_owners(vectors):
    grouped,_=_sums_by_cardinality(vectors,3)
    impact=Counter()
    for trios in grouped.values():
        if len(trios)<2:continue
        for t in trios:
            for i in t:
                impact[i]+=len(trios)-1
    return tuple(sorted(impact,key=lambda i:(-impact[i],i)))


def exact_one_original_source_palette_repair(model,indices,source_id):
    """Independently recompute and select ALL 51 exact local candidates.

    For a fixed source ID i:
      U = {triples without i}, fixed (N-1 choose 3) group counts
      I_t = {i,u,v}, u<v, changes with palette t.

    total collisions = C(U,U) + C(I_t,I_t) + C(U,I_t).
    The first two terms are independent of palette t.
    Enumerate all 946 pairs (u,v) for a W32 source and all 51 palettes;
    optimize only C(U,I_t). Returned delta is verified independently
    on ALL 14190 triple sums after any accepted replacement.
    """
    if (len(indices)!=45 or any(type(x) is not int or not 0<=x<51
                                for x in indices)):
        raise ValueError("exact one GF5 palette for all 45 ORIGINAL IDs")
    vectors=true_original_source_vectors(model,indices)
    replacement=_replacement_source_vector(model,source_id,indices[source_id])
    if replacement!=vectors[source_id]:
        raise AssertionError("source-ID palette does not recreate original physical column")
    others=tuple(i for i in range(45) if i!=source_id)
    unaffected=Counter(_field_sum(vectors,q)
                       for q in combinations(others,3))
    pair_sums=tuple(_field_sum(vectors,q)
                    for q in combinations(others,2))
    if sum(unaffected.values())!=13244 or len(pair_sums)!=946:
        raise AssertionError("true ORIGINAL 44-source separation miscount")
    def cross(v):
        return sum(unaffected.get(bytes((v[k]+p[k])%5
                             for k in range(12)),0) for p in pair_sums)
    old_cross=cross(replacement)
    candidates=[]
    for t in range(51):
        trial=_replacement_source_vector(model,source_id,t)
        candidates.append((cross(trial),t))
    if candidates[indices[source_id]][0]!=old_cross:
        raise AssertionError("original self-candidate conditional count incorrect")
    minimum,idx=min(candidates)
    if minimum>=old_cross:
        return {
            "indices":tuple(indices),"source_ID":source_id,
            "old_cross":old_cross,"new_cross":old_cross,
            "improvement":0,"changed":False,"all_51_candidates_checked":True
        }
    updated=list(indices);updated[source_id]=idx
    newer=true_original_source_vectors(model,updated)
    old_global=_full_triple_duplicate_count(vectors)
    new_global=_full_triple_duplicate_count(newer)
    if new_global!=old_global+minimum-old_cross:
        raise AssertionError("local repaired ORIGINAL full R3 count not exact")
    if new_global>=old_global:
        raise AssertionError("local exact improvement did not improve global objective")
    return {
        "indices":tuple(updated),"source_ID":source_id,
        "old_cross":old_cross,"new_cross":minimum,
        "improvement":old_cross-minimum,
        "before_complete_three_subset_collision_pairs":old_global,
        "after_complete_three_subset_collision_pairs":new_global,
        "changed":True,"all_51_candidates_checked":True,
    }


def deterministic_full_original_45flag_repair(model,indices,*,max_sweeps=8):
    """Exact one-original-flag-at-a-time collision descent.

    Does NOT claim guaranteed convergence to zero. Every accepted
    step strictly decreases a NONNEGATIVE INTEGER count of all equal
    distinct triple sums. On stopping report exact remaining full R3.
    """
    if type(max_sweeps) is not int or max_sweeps<0:
        raise ValueError("nonnegative exact source-descent sweep budget")
    current=tuple(indices)
    vec=true_original_source_vectors(model,current)
    initial=_full_triple_duplicate_count(vec)
    steps=[]
    for sweep in range(max_sweeps):
        prev=_full_triple_duplicate_count(true_original_source_vectors(model,current))
        if prev==0:break
        owners=_collision_owners(true_original_source_vectors(model,current))
        if not owners:
            raise AssertionError("nonzero full triple duplicate but no source owners")
        improvements=0
        for source_id in owners:
            new=exact_one_original_source_palette_repair(model,current,source_id)
            if new["changed"]:
                current=new["indices"]
                steps.append({
                    "sweep":sweep,"source_ID":source_id,
                    "old_cross":new["old_cross"],
                    "new_cross":new["new_cross"],
                    "remaining_exact_duplicate_three_sum_pairs":
                        new["after_complete_three_subset_collision_pairs"]
                })
                improvements+=1
                if new["after_complete_three_subset_collision_pairs"]==0:
                    break
        if not improvements:
            break
    final_vectors=true_original_source_vectors(model,current)
    final=_full_triple_duplicate_count(final_vectors)
    if final>initial:
        raise AssertionError("strictly improving original source descent regressed")
    return {
        "original_45_flag_palette_indices":current,
        "initial_exact_three_subset_collision_pairs":initial,
        "final_exact_three_subset_collision_pairs":final,
        "source_palette_updates":tuple(steps),
        "fully_collision_free_0_to_3":final==0,
        "bounded_descent_not_universal_all_h_theorem":True,
    }


def repair_saved_full_W32_certificates():
    """Repair both frozen #711 full original source array assignments."""
    parent=committed_sevenclass_indices()
    out={}
    for scheme in ("lex","reverse-line"):
        family=true_original_w32_seven_hypergraph(scheme)
        revised=deterministic_full_original_45flag_repair(
            family["source"],parent[scheme],max_sweeps=8)
        verified=full_original_r3_triple_hash_census(
            family["source"],revised["original_45_flag_palette_indices"],
            leading_original_sixsets=(m["ids"] for m in family["motifs"]),
            max_witnesses=4)
        if (verified["duplicate_equal_3_sum_pairs"]!=
            revised["final_exact_three_subset_collision_pairs"]):
            raise AssertionError("repair vs independent full GF5 sextuple census mismatch")
        if (revised["fully_collision_free_0_to_3"]!=
            verified["all_45_original_source_0_to_3_subset_sums_unique"]):
            raise AssertionError("repair misclassified actual full ORIGINAL ASET")
        out[scheme]={
            "exact_global_zero_0_to_3_achieved":
                revised["fully_collision_free_0_to_3"],
            "previous_equal_triple_pairs":
                revised["initial_exact_three_subset_collision_pairs"],
            "final_equal_triple_pairs":
                revised["final_exact_three_subset_collision_pairs"],
            "source_updates":revised["source_palette_updates"],
            "final_complete_original_45_flag_palette_indices":
                revised["original_45_flag_palette_indices"],
            "independently_checked_true_full_R3":
                verified["FULL_original_distinct_sixflag_3v3_signed_events"],
            "full_0_to_3_original_subset_sums_unique":
                verified["all_45_original_source_0_to_3_subset_sums_unique"],
            "no_asymptotic_claim":True,
        }
    return out


if __name__=="__main__":
    print(json.dumps(repair_saved_full_W32_certificates(),indent=2,sort_keys=True))
