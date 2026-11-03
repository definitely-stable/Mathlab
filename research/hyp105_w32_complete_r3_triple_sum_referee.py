"""HYP-105 AA4-FULLR3: full true W(3,2) ORIGINAL 3-vs-3 GF(5) audit.

Core exact all-N theorem: a signed six-distinct-source-flag 3-vs-3
collision is IDENTICAL to a pair of DISJOINT original-flag triples
having EQUAL full GF(5)^m sums. Every such collision is counted once
up to switching the two triples. Thus enumerating C(N,3) triples
and matching equal field vectors is complete regardless of *any*
physical-coordinate degree/multiplicity profile, unlike the seven
6+6 degree-two leading-class census.

For true W32: N=45, m=12; only C(45,3)=14,190 triple sums need
hashing, instead of C(45,6)=8,145,060 sixsets x ten signs.
Individual source palettes remain globally fixed per ORIGINAL ID.
"""
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path
import json

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_original_gf5_deterministic_extraction_referee import PALETTES
from hyp105_w32_sevenclass_global_deterministic_gf5_referee import (
    _source_palette_by_id, true_original_w32_seven_hypergraph,
    hypergraph_direct_event_census
)

N_FLAGS=45
M_COORDS=12
N_TRIPLES=14190
N_SEXTUPLES=8145060
AFFINE_CHECKSUM=4


def committed_sevenclass_indices():
    """Read actual parent #711 45-original-ID full-coefficient certificates."""
    path=Path(__file__).with_name(
        "hyp105_w32_sevenclass_original_45flag_certificates.json")
    data=json.loads(path.read_text(encoding="utf-8"))
    if (not data["selected_family_only"] or not data["not_full_R3"]
        or data["new_ASET_exponent_proved"]):
        raise AssertionError("selected-only sevenclass scope wrongly promoted")
    out={}
    for scheme in ("lex","reverse-line"):
        c=data["certificates"][scheme]
        indices=tuple(c["palette_indices_in_original_flag_ID_order"])
        if (len(indices)!=N_FLAGS or
            any(type(i) is not int or not 0<=i<len(PALETTES) for i in indices)
            or tuple(_source_palette_by_id(scheme,c["deterministic_seed"],N_FLAGS))
               !=indices or c["exact_direct_signed_events"]!=0):
            raise AssertionError("corrupt actual ORIGINAL source certificate")
        out[scheme]=indices
    return out


def true_original_source_vectors(model, palette_indices):
    """Construct 12 GF5 coordinates from physical ORIGINAL source flags.

    No derived or synthetic original IDs: source index is the exact
    position in model['incidences'] for the unchanged true W32 geometry.
    """
    if (model.get("s")!=2 or model.get("N")!=N_FLAGS or
        model.get("a")!=6 or len(model.get("incidences",()))!=N_FLAGS
        or len(set(model["incidences"]))!=N_FLAGS):
        raise ValueError("only complete actual 45-original-flag W32 K6 allowed")
    if (len(palette_indices)!=N_FLAGS or
        any(type(x) is not int or not 0<=x<51 for x in palette_indices)):
        raise ValueError("one legal ORIGINAL GF5 palette index for all 45 flags")
    f=tuple(model["left_labels"]);g=tuple(model["right_labels"])
    if (len(set(f))!=15 or len(set(g))!=15
        or any(len(t)!=2 or t[0]>=t[1] or t[0]<0 or t[1]>=6
               for t in f+g)):
        raise ValueError("not two separate complete pair-label bijections of K6")
    result=[]
    for source_id,(p,line) in enumerate(model["incidences"]):
        physical=(f[p][0],f[p][1],6+g[line][0],6+g[line][1])
        if len(set(physical))!=4:
            raise AssertionError("not a true 2+2 physical support")
        weights=PALETTES[palette_indices[source_id]]
        vector=[0]*M_COORDS
        for coordinate,w in zip(physical,weights):
            vector[coordinate]=w
        if (len([x for x in vector if x])!=4 or
            sum(vector)%5!=AFFINE_CHECKSUM):
            raise AssertionError("source GF5 support/checksum violated")
        result.append(tuple(vector))
    if len(set(result))!=N_FLAGS:
        raise AssertionError("two different original source IDs duplicate their vectors")
    return tuple(result)


def _field_sum(vectors, ids):
    """Independent digitwise GF(5) addition, not integer carry addition."""
    return bytes(sum(vectors[i][k] for i in ids)%5 for k in range(M_COORDS))


def _direct_signed_six_column_check(vectors, positives,negatives):
    """Independent 12 physical coordinate equations, all original IDs."""
    if (len(positives)!=len(negatives)!=3 or
        set(positives)&set(negatives)):
        raise ValueError("true distinct 3-vs-3 source triples required")
    return all((sum(vectors[i][k] for i in positives)
                -sum(vectors[j][k] for j in negatives))%5==0
               for k in range(M_COORDS))


def _sextuple_degree_profile(model, ids):
    """All real original-coordinate multiplicity profiles, not 6+6 only."""
    profiles=[]
    flags=model["incidences"]
    for h,labels in ((0,model["left_labels"]),
                     (1,model["right_labels"])):
        degrees=Counter(coord for i in ids
                        for coord in labels[flags[i][h]])
        if sum(degrees.values())!=12:
            raise AssertionError("original six flags do not supply twelve incidences")
        if any(n==1 for n in degrees.values()):
            raise AssertionError("zero signed vector with a singleton coordinate")
        profiles.append(tuple(sorted(degrees.values(),reverse=True)))
    return tuple(profiles)


def _sums_by_cardinality(vectors,k):
    """Exact all-subset encoded signatures; emit all equal-sum pair counts."""
    if type(k) is not int or k not in (1,2,3):
        raise ValueError("only positive source subset cardinalities 1..3")
    signatures=defaultdict(list)
    for indices in combinations(range(len(vectors)),k):
        signatures[_field_sum(vectors,indices)].append(indices)
    collision_pairs=sum(len(q)*(len(q)-1)//2 for q in signatures.values())
    return signatures,collision_pairs


def full_original_r3_triple_hash_census(model, indices, *,
                                        leading_original_sixsets=None,
                                        max_witnesses=30):
    """Exact FULL balanced 3+3 source collision census and 0..3 ASET test.

    Every possible six-distinct ORIGINAL source ID set is covered:
    each 3+3 signed event has exactly one unordered pair of source
    triples after identifying overall sign reversal. Distinct
    original source triples with equal sums but overlapping IDs
    are counted SEPARATELY, and are NOT falsely included in R3.
    """
    if type(max_witnesses) is not int or max_witnesses<0:
        raise ValueError("nonnegative exact witness budget only")
    vectors=true_original_source_vectors(model,indices)
    lead=set() if leading_original_sixsets is None else set(
        leading_original_sixsets)
    for s in lead:
        if len(s)!=6 or len(set(s))!=6:
            raise ValueError("invalid real original leading sixset")
    single,one_collisions=_sums_by_cardinality(vectors,1)
    doubles,two_collisions=_sums_by_cardinality(vectors,2)
    triples,three_collisions=_sums_by_cardinality(vectors,3)
    if sum(map(len,triples.values()))!=N_TRIPLES:
        raise AssertionError("not every true ORIGINAL 3-subset counted")
    signed_events=0
    signed_leading=0
    signed_outside=0
    overlapping_triples=0
    sextuple_hits=Counter()
    outside_profiles=Counter()
    samples=[]
    for bucket in triples.values():
        if len(bucket)<2:continue
        for j,a in enumerate(bucket):
            for b in bucket[j+1:]:
                overlap=len(set(a)&set(b))
                if overlap:
                    overlapping_triples+=1
                    continue
                if not _direct_signed_six_column_check(vectors,a,b):
                    raise AssertionError("false GF5 triple signature collision")
                ids=tuple(sorted(a+b))
                signed_events+=1
                sextuple_hits[ids]+=1
                if ids in lead:
                    signed_leading+=1
                else:
                    signed_outside+=1
                    outside_profiles[_sextuple_degree_profile(model,ids)]+=1
                if len(samples)<max_witnesses:
                    samples.append({
                        "six_original_source_IDs":ids,
                        "positive_three_original_IDs":a,
                        "negative_three_original_IDs":b,
                        "original_point_line_flags":
                            tuple(model["incidences"][i] for i in ids),
                        "original_coordinate_degree_profiles":
                            _sextuple_degree_profile(model,ids),
                        "true_GF5_twelve_coordinate_equal_triple_sums":
                            tuple(_field_sum(vectors,a)),
                        "in_seven_leading_family":ids in lead,
                    })
    if (three_collisions!=overlapping_triples+signed_events
        or signed_events!=signed_leading+signed_outside):
        raise AssertionError("lost identical GF5 triple pair or ORIGINAL signed event")
    # Independent subset sum uniqueness check 1/2/3; common affine
    # checksum=4 forbids all unequal-cardinality collisions (mod 5).
    full_aset=(one_collisions==two_collisions==three_collisions==0)
    if signed_events==0 and (one_collisions or two_collisions or overlapping_triples):
        raise AssertionError("unexpected overlap-only triple equality not resolved by full R3")
    return {
        "source_flag_count":N_FLAGS,
        "source_dimension_GF5":M_COORDS,
        "all_original_one_subset_count":N_FLAGS,
        "all_original_two_subset_count":N_FLAGS*(N_FLAGS-1)//2,
        "all_original_three_subset_count":N_TRIPLES,
        "all_original_distinct_sixsets_implicitly_covered":N_SEXTUPLES,
        "distinct_full_GF5_triple_sums":len(triples),
        "duplicate_equal_1_sum_pairs":one_collisions,
        "duplicate_equal_2_sum_pairs":two_collisions,
        "duplicate_equal_3_sum_pairs":three_collisions,
        "overlapping_equal_triple_pairs_excluded_from_R3":overlapping_triples,
        "FULL_original_distinct_sixflag_3v3_signed_events":signed_events,
        "actual_signed_events_in_seven_leading_family":signed_leading,
        "actual_signed_events_OUTSIDE_seven_family":signed_outside,
        "distinct_original_sixsets_with_FULL_3v3_event":len(sextuple_hits),
        "other_coordinate_multiplicity_signed_event_profiles":
            {str(k):v for k,v in sorted(outside_profiles.items())},
        "sample_true_original_signed_event_witnesses":samples,
        "all_45_original_source_0_to_3_subset_sums_unique":full_aset,
        "does_not_infer_all_h_or_new_exponent":True,
    }


def independent_small_universe_brute_3v3(vectors,universe):
    """Wholly different O(C(k,6)*10*12) control, never uses triple hash."""
    universe=tuple(universe)
    if (len(universe)>12 or len(universe)<6 or
        len(set(universe))!=len(universe) or any(
            type(i) is not int or not 0<=i<len(vectors) for i in universe)):
        raise ValueError("distinct six to twelve ORIGINAL source IDs needed")
    events=set()
    for six in combinations(sorted(universe),6):
        for plus_tail in combinations(six[1:],2):
            plus=(six[0],)+plus_tail
            minus=tuple(i for i in six if i not in plus)
            if _direct_signed_six_column_check(vectors,plus,minus):
                events.add((six,plus))
    return events


def independent_small_universe_hash_3v3(vectors,universe):
    """Same mathematical equivalence, different enumeration from direct."""
    universe=set(universe)
    keys=defaultdict(list)
    for three in combinations(sorted(universe),3):
        keys[_field_sum(vectors,three)].append(three)
    result=set()
    for Q in keys.values():
        for x,y in combinations(Q,2):
            if set(x)&set(y):continue
            six=tuple(sorted(x+y))
            plus=tuple(sorted(x)) if six[0] in x else tuple(sorted(y))
            result.add((six,plus))
    return result


def saved_seven_vs_full_r3_report(*,max_search_seed=64):
    """Exact full risk on #711 static witnesses and deterministic extension.

    A zero full-ASet assignment is sought by a bounded reproducible
    search; if not found, report evidence and fail-closed in the search.
    The full R3 audit of SAVED sevenclass witnesses is unconditional
    on search success and MUST be reported, even if R3>0.
    """
    saved=committed_sevenclass_indices()
    out=[]
    for scheme in ("lex","reverse-line"):
        family=true_original_w32_seven_hypergraph(scheme)
        source=family["source"]
        leading={m["ids"] for m in family["motifs"]}
        saved_result=full_original_r3_triple_hash_census(
            source,saved[scheme],leading_original_sixsets=leading)
        assignment={i:PALETTES[j] for i,j in enumerate(saved[scheme])}
        leading_direct=hypergraph_direct_event_census(
            family,assignment,independent_parity=True)
        if (leading_direct["actual_ten_sign_event_count"]!=
            saved_result["actual_signed_events_in_seven_leading_family"]):
            raise AssertionError("signed 3+3 event census disagrees with independent sevenclass physical oracle")
        if leading_direct["actual_ten_sign_event_count"]!=0:
            raise AssertionError("frozen parent seven leading certificate no longer zero")
        found=None
        for seed in range(max_search_seed):
            idx=_source_palette_by_id(scheme,seed,N_FLAGS)
            value=full_original_r3_triple_hash_census(
                source,idx,leading_original_sixsets=leading,max_witnesses=0)
            if value["all_45_original_source_0_to_3_subset_sums_unique"]:
                found={
                    "source_seed":seed,
                    "complete_original_45_flag_palette_indices":idx,
                    "actual_FULL_R3_signed_events":value[
                        "FULL_original_distinct_sixflag_3v3_signed_events"],
                    "all_0_to_3_original_subset_sums_unique":True,
                }
                break
        out.append({
            "scheme":scheme,
            "selected_sevenclass_original_sixsets":len(leading),
            "saved_sevenclass_certificate_full_r3":saved_result,
            "source_prior_sevenclass_zero_preserved":True,
            "first_full_ASET_witness_if_found":found,
            "full_ASET_bounded_search_did_not_prove_universal_existence":
                True,
        })
    return {
        "true_original_source":"complete W(3,2) 45 source flags x 12 GF5 physical coordinates",
        "schemes":out,"new_all_h_triple_sum_bijection":True,
        "all_45_full_original_sixID_G5_subset_collisions_covered":True,
        "no_new_all_h_ASSET_exponent_claim":True,
    }


if __name__=="__main__":
    print(json.dumps(saved_seven_vs_full_r3_report(),indent=2,sort_keys=True))
