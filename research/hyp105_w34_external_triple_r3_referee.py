"""HYP-105 AA4-W34EX: bounded-memory EXACT ORIGINAL GF(5) triple-sum R3.

Proves and implements for all n (within explicit 12-byte record domain):
  full signed R3 = number of unordered pairs of disjoint ORIGINAL
  three-flag subsets with EQUAL complete GF(5)^m sums.

For actual symplectic W(3,4), n=425 and m=28, there are 12,704,100
triple sums. The exact 28-digit base-5 signature fits 66 bits.
A canonical ORIGINAL triple code fits 27 bits. Each entry thus fits
12 bytes; 256 deterministic on-disk radix buckets cover ALL entries,
with NO probabilistic hash, sampling, or false-negative possibility.

For each equal-sum bucket of k distinct triples, count disjoint
pairs in O(k), without k^2 pair scans, by
  C(k,2) - sum_i C(deg_i,2) + sum_{i<j} C(deg_ij,2).
This inclusion-exclusion is exact because two DISTINCT triples
can share one or two ORIGINAL source IDs, never three.

Run on GitHub-hosted Linux; this is not a new asymptotic ASET theorem.
"""
from collections import Counter
from contextlib import ExitStack
from itertools import combinations, groupby
from pathlib import Path
import hashlib
import json
import math
import tempfile

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_original_gf5_deterministic_extraction_referee import PALETTES


RECORD_BYTES=12
ORIGINAL_TRIPLE_CODE_BITS=27
CODE_MASK=(1<<ORIGINAL_TRIPLE_CODE_BITS)-1
DIGIT_POWERS=(1,5,25,125)
BASE=625
RADIX_BUCKET_COUNT=256
W34_ORIGINAL_S=4
W34_ORIGINAL_N=425
W34_DIMENSION=28
W34_TRIPLES=12_704_100


def _add_four_digit_table():
    """Exactly GF(5)^4 addition indexed by base-5 grouped digits."""
    digits=tuple(tuple((x//DIGIT_POWERS[j])%5 for j in range(4))
                 for x in range(BASE))
    return tuple(sum(((a[k]+b[k])%5)*DIGIT_POWERS[k] for k in range(4))
                 for a in digits for b in digits)


def exact_gf5_original_vectors(model,indices,*,source_ids=None):
    n=model["N"]
    m=model["m"]
    a=model["a"]
    flags=tuple(model["incidences"])
    f=tuple(model["left_labels"])
    g=tuple(model["right_labels"])
    if (model["s"] not in (2,4) or m!=2*a or a not in (6,14)
        or len(flags)!=n or len(set(flags))!=n
        or len(f)!=model["v"] or len(g)!=model["v"]
        or len(set(f))!=len(f) or len(set(g))!=len(g)):
        raise ValueError("only complete TRUE original W32/W34 pair-injected source")
    if (len(indices)!=n or
        any(type(t) is not int or not 0<=t<51 for t in indices)):
        raise ValueError("one 51-valued checksum4 palette per ORIGINAL flag")
    ids=tuple(range(n)) if source_ids is None else tuple(source_ids)
    if (len(set(ids))!=len(ids) or
        any(type(i) is not int or not 0<=i<n for i in ids)):
        raise ValueError("distinct original source subset IDs only")
    vectors=[]
    for source_id in ids:
        p,ell=flags[source_id]
        coords=(f[p][0],f[p][1],a+g[ell][0],a+g[ell][1])
        if len(set(coords))!=4:
            raise AssertionError("false original 2+2 source support")
        coef=PALETTES[indices[source_id]]
        v=[0]*m
        for c,w in zip(coords,coef):
            v[c]=w
        if (sum(v)%5!=4 or sum(bool(x) for x in v)!=4):
            raise AssertionError("ORIGINAL GF5 checksum/support illegal")
        vectors.append(tuple(v))
    return ids,tuple(vectors)


def _packed_four_groups(vectors):
    if not vectors:return ()
    m=len(vectors[0])
    if m not in (12,28) or m%4:
        raise ValueError("only true original physical source m=12/28")
    out=[]
    for v in vectors:
        if len(v)!=m or any(type(x) is not int or x<0 or x>4 for x in v):
            raise ValueError("GF5 physical source coordinates 0..4 required")
        out.append(tuple(sum(v[4*t+j]*DIGIT_POWERS[j] for j in range(4))
                         for t in range(m//4)))
    return tuple(out)


def _gf5_encoded(v):
    """SECOND exact full-coordinate encoder independent of limb table."""
    out=0
    for digit in reversed(v):
        out=5*out+digit
    return out


def _signature_from_grouped_add(p,q,add):
    signature=0
    for x,y in zip(reversed(p),reversed(q)):
        signature=BASE*signature+add[BASE*x+y]
    return signature


def _decode_record_triple(raw_code,n):
    i,remainder=divmod(raw_code,n*n)
    j,k=divmod(remainder,n)
    if not 0<=i<j<k<n:
        raise AssertionError("corrupt canonical three-original-ID disk record")
    return (i,j,k)


def _write_bucket_id(signature):
    """Deterministic exact partition; equal signatures always same bucket.

    XOR folding is an indexing optimization, not a lossy hash:
    FULL 66-bit base-5 signature is retained in every disk record.
    """
    if type(signature) is not int or signature<0:
        raise ValueError("nonnegative exact GF5 signature")
    return (signature ^ (signature>>11) ^ (signature>>22)
            ^ (signature>>33) ^ (signature>>44) ^ (signature>>55))&255


def _write_exact_original_triple_records(parts,outdir,*,max_triples):
    n=len(parts)
    if n>=425+1:
        raise ValueError("12-byte canonical source triplet record only n<=425")
    total=math.comb(n,3) if n>=3 else 0
    if (type(max_triples) is not int or max_triples<0
        or total>max_triples):
        raise ValueError("explicit full ORIGINAL triple budget exceeded")
    add=_add_four_digit_table()
    positions=len(parts[0]) if parts else 0
    if positions not in (3,7):
        raise ValueError("original true 12/28 physical coordinate groups")
    expected_signature_max=5**(4*positions)
    if (expected_signature_max.bit_length()+ORIGINAL_TRIPLE_CODE_BITS
            >8*RECORD_BYTES):
        raise AssertionError("exact source signature overflows lossless 12-byte record")
    paths=[outdir/(f"{u:02x}.triple") for u in range(RADIX_BUCKET_COUNT)]
    sizes=[0]*RADIX_BUCKET_COUNT
    with ExitStack() as stack:
        fds=tuple(stack.enter_context(open(path,"wb",buffering=131072))
                  for path in paths)
        count=0
        for i in range(n-2):
            pi=parts[i]
            for j in range(i+1,n-1):
                pj=parts[j]
                pair=tuple(add[BASE*pi[g]+pj[g]]
                           for g in range(positions))
                flat_base=(i*n+j)*n
                for k in range(j+1,n):
                    signature=_signature_from_grouped_add(pair,parts[k],add)
                    if signature>=expected_signature_max:
                        raise AssertionError("GF5 packed signature out of range")
                    original_triple_code=flat_base+k
                    if original_triple_code>=1<<ORIGINAL_TRIPLE_CODE_BITS:
                        raise AssertionError("ORIGINAL source triple code does not fit 27 bits")
                    packed=(signature<<ORIGINAL_TRIPLE_CODE_BITS)|original_triple_code
                    b=_write_bucket_id(signature)
                    fds[b].write(packed.to_bytes(RECORD_BYTES,"big"))
                    sizes[b]+=1
                    count+=1
    if count!=total or sum(sizes)!=total:
        raise AssertionError("missing or duplicated full ORIGINAL GF5 triple")
    return paths,tuple(sizes)


def _all_1_2_source_sum_collisions(vectors,parts,add):
    n=len(parts)
    singles=Counter(_gf5_encoded(v) for v in vectors)
    pairs=Counter()
    for i in range(n):
        for j in range(i+1,n):
            q=_signature_from_grouped_add(parts[i],parts[j],add)
            pairs[q]+=1
    one_pairs=sum(x*(x-1)//2 for x in singles.values())
    two_pairs=sum(x*(x-1)//2 for x in pairs.values())
    if sum(singles.values())!=n or sum(pairs.values())!=math.comb(n,2):
        raise AssertionError("missing SOURCE 1/2-subset sums")
    return {
        "one_source_sum_collisions":one_pairs,
        "two_source_sum_collisions":two_pairs,
        "distinct_one_source_sums":len(singles),
        "distinct_two_source_sums":len(pairs),
    }


def _bucket_disjoint_pair_census(same_signature_records,n):
    """Exact O(k) inclusion-exclusion on SOURCE triple overlaps."""
    a=len(same_signature_records)
    if a<2:return (0,0,0)
    one=Counter()
    two=Counter()
    seen=set()
    for code in same_signature_records:
        if code in seen:
            raise AssertionError("duplicate ORIGINAL source three-subset record")
        seen.add(code)
        t=_decode_record_triple(code,n)
        one.update(t)
        two.update(combinations(t,2))
    total=a*(a-1)//2
    shared=sum(x*(x-1)//2 for x in one.values())-sum(
        x*(x-1)//2 for x in two.values())
    disjoint=total-shared
    if not 0<=disjoint<=total or not 0<=shared<=total:
        raise AssertionError("SOURCE intersection lattice lost original triple pairs")
    return total,shared,disjoint


def _source_sixset_coordinate_profiles(model,six):
    flags=model["incidences"]
    profiles=[]
    for side,labels in ((0,model["left_labels"]),(1,model["right_labels"])):
        freq=Counter(coord for i in six
                     for coord in labels[flags[i][side]])
        if 1 in freq.values():
            raise AssertionError("real GF5 signed source cancellation contains singleton")
        profiles.append(tuple(sorted(freq.values(),reverse=True)))
    return tuple(profiles)


def _witness_disjoint_pairs(records,n,*,max_pairs):
    if max_pairs==0:return ()
    triples=tuple(_decode_record_triple(z,n) for z in records)
    results=[]
    for ix,t in enumerate(triples):
        chosen=set(t)
        for u in triples[ix+1:]:
            if not chosen.intersection(u):
                results.append((t,u))
                if len(results)==max_pairs:return tuple(results)
    return tuple(results)


def exact_full_original_external_r3(
    model,indices,*,source_ids=None,max_triples=12_704_100,
    max_bucket_bytes=200_000_000,max_witnesses=8,
):
    """Proof-preserving external-disk full k=3 ORIGINAL GF5 audit.

    Sorting all exact signatures within deterministic radix bucket
    proves completeness. Every equal pair in the full 12.7m stream
    must appear in exactly one group because equal exact base5
    signatures have identical deterministic bucket IDs.
    """
    if type(max_bucket_bytes) is not int or max_bucket_bytes<12:
        raise ValueError("positive exact external radix memory bound required")
    if type(max_witnesses) is not int or max_witnesses<0:
        raise ValueError("nonnegative true ORIGINAL signed witness budget")
    ids,vectors=exact_gf5_original_vectors(model,indices,source_ids=source_ids)
    n=len(ids)
    if n<3:raise ValueError("at least three ORIGINAL flags required")
    parts=_packed_four_groups(vectors)
    add=_add_four_digit_table()
    short=_all_1_2_source_sum_collisions(vectors,parts,add)
    number_of_triples=math.comb(n,3)
    signed=overlap=identical=0
    distinct_sigs=0
    full_processed=0
    largest_bucket=0
    witness=[]
    profiles=Counter()
    nontrivial_signature_groups=0
    with tempfile.TemporaryDirectory(prefix="hyp105-full-original-r3-") as folder:
        paths,sizes=_write_exact_original_triple_records(
            parts,Path(folder),max_triples=max_triples)
        for p,num in zip(paths,sizes):
            if not num:continue
            expected_bytes=RECORD_BYTES*num
            if expected_bytes>max_bucket_bytes:
                raise ValueError(
                    "exact W34 triple bucket exceeds independent memory cap; "
                    "do not return a partial result")
            raw=p.read_bytes()
            if len(raw)!=expected_bytes:
                raise AssertionError("truncated ORIGINAL triple spool")
            largest_bucket=max(largest_bucket,num)
            # Sorted complete 12-byte lossless exact GF5+source-ID records:
            rows=sorted(int.from_bytes(raw[j:j+RECORD_BYTES],"big")
                        for j in range(0,len(raw),RECORD_BYTES))
            del raw
            full_processed+=len(rows)
            for signature,group in groupby(rows,key=lambda z:z>>ORIGINAL_TRIPLE_CODE_BITS):
                codes=tuple(v&CODE_MASK for v in group)
                distinct_sigs+=1
                if len(codes)<2:continue
                nontrivial_signature_groups+=1
                total,shared,disjoint=_bucket_disjoint_pair_census(codes,n)
                identical+=total
                overlap+=shared
                signed+=disjoint
                if disjoint and (len(witness)<max_witnesses):
                    for first,second in _witness_disjoint_pairs(
                            codes,n,max_pairs=max_witnesses-len(witness)):
                        a=tuple(ids[v] for v in first)
                        b=tuple(ids[v] for v in second)
                        physical_a=tuple(vectors[v] for v in first)
                        physical_b=tuple(vectors[v] for v in second)
                        actual1=tuple(sum(c[q] for c in physical_a)%5
                                      for q in range(model["m"]))
                        actual2=tuple(sum(c[q] for c in physical_b)%5
                                      for q in range(model["m"]))
                        if actual1!=actual2 or _gf5_encoded(actual1)!=signature:
                            raise AssertionError(
                                "independent complete GF5 physical signed witness failed")
                        six=tuple(sorted(a+b))
                        profile=_source_sixset_coordinate_profiles(model,six)
                        witness.append({
                            "six_distinct_ORIGINAL_flag_IDs":six,
                            "positive_ORIGINAL_three":a,
                            "negative_ORIGINAL_three":b,
                            "actual_original_point_line_incidence_flags":
                                tuple(model["incidences"][k] for k in six),
                            "two_original_physical_coordinate_profiles":profile,
                            "complete_GF5_physical_sum":actual1,
                            "verified_exact_28_or_12_coordinate_equations":True,
                        })
                # Source profiles for at most finite explicitly emitted
                # witnesses, not a fabricated population histogram.
            del rows
    if (full_processed!=number_of_triples
        or identical!=signed+overlap):
        raise AssertionError("lost ORIGINAL three-subset source or collision pairs")
    # NEW ALL-N INDEPENDENT R2 -> R3 overlapping-triplet identity.
    # All original columns are distinct: each has a different actual
    # 2+2 source support under separate globally pair-injective f,g.
    # A two-subset equal-sum pair cannot share one source ID without
    # implying equal singleton original columns. Thus each duplicate
    # 2-sum is a genuine disjoint 2v2 signed source event.
    # Every equal-sum pair of distinct triples with one shared ID is
    # exactly such a 2v2 event extended by any of the n-4 other IDs.
    # Overlap of TWO triple IDs would imply equal singleton columns.
    if short["one_source_sum_collisions"]!=0:
        raise AssertionError("true globally injected ORIGINAL source has equal columns")
    independent_r2_overlap=(n-4)*short["two_source_sum_collisions"]
    if independent_r2_overlap!=overlap:
        raise AssertionError(
            ("exact source R2 -> overlap triple-pair identity failed",
             independent_r2_overlap,overlap))
    independent_full_r3=identical-independent_r2_overlap
    if independent_full_r3!=signed:
        raise AssertionError(
            ("two independent full original GF5 R3 methods disagree",
             independent_full_r3,signed))
    if not distinct_sigs or not number_of_triples:
        raise AssertionError("empty full ORIGINAL triple census")
    zero_all=sum((short["one_source_sum_collisions"],
                  short["two_source_sum_collisions"],identical))==0
    return {
        "source_s":model["s"],
        "source_m_GF5_physical_coordinates":model["m"],
        "source_legal_ORIGINAL_flag_ID_count":len(model["incidences"]),
        "selected_original_flag_count":n,
        "all_425_original_flags_in_scope":n==425,
        "all_source_triple_count":number_of_triples,
        "all_source_sixsets_implicitly_covered":math.comb(n,6) if n>=6 else 0,
        "all_triples_exact_external_disk_records_processed":full_processed,
        "distinct_complete_GF5_three_source_sums":distinct_sigs,
        "equal_sum_pairs_of_distinct_ORIGINAL_triples":identical,
        "equal_triples_sharing_original_ID_not_signed_R3":overlap,
        "FULL_six_distinct_original_ID_3v3_signed_event_count":signed,
        "independently_derived_signed_R3_using_all_R2_overlap_identity":
            independent_full_r3,
        "R2_signed_2v2_events_exact":short["two_source_sum_collisions"],
        "independent_original_R2_to_R3_overlap_multiplier":n-4,
        "independent_original_R2_to_R3_overlap_identity_verified":True,
        "no_false_negative_from_hashed_or_sampled_sums":True,
        "complete_source_GF5_zero_to_three_ASET":zero_all,
        "all_original_1_2_source_sum_checks":short,
        "nontrivial_full_source_signature_groups":nontrivial_signature_groups,
        "peak_one_sorted_external_bucket_records":largest_bucket,
        "peak_one_sorted_external_bucket_bytes":largest_bucket*RECORD_BYTES,
        "exact_on_disk_bucket_bytes":number_of_triples*RECORD_BYTES,
        "verified_independent_true_source_witnesses":tuple(witness),
        "does_not_prove_all_h_or_new_asymptotic_exponent":True,
    }


def deterministic_original_checksum_palettes(model,*,seed=0):
    """All original IDs get a single global legal 51-pattern, no resampling.

    A deterministic *control* assignment, NOT a universally proven
    zero-risk assignment or a random-expectation theorem.
    """
    if type(seed) is not int or seed<0:
        raise ValueError("nonnegative original source palette seed")
    if model["s"] not in (2,4) or model["N"] not in (45,425):
        raise ValueError("true supported original geometry only")
    return tuple(int.from_bytes(hashlib.sha256(
        ("HYP105-W34EX-v1/"+model["scheme"]+"/"+str(seed)+"/"+
         str(original_id)).encode()).digest()[:8],"big")%51
                 for original_id in range(model["N"]))


def report_w34_exact(*,schemes=("lex",),seed=0):
    """Full genuine W34 ORIGINAL GF5 R3, exact & memory-budgeted."""
    out=[]
    for scheme in schemes:
        if scheme not in ("lex","reverse-line"):
            raise ValueError("original W34 scheme unsupported")
        model=pair_labeled_symplectic(2,scheme)
        if (model["s"]!=4 or model["N"]!=425 or model["m"]!=28
            or len(set(model["incidences"]))!=425):
            raise AssertionError("wrong genuine symplectic W34 source")
        indices=deterministic_original_checksum_palettes(model,seed=seed)
        result=exact_full_original_external_r3(
            model,indices,max_triples=W34_TRIPLES,max_witnesses=8)
        if (result["all_source_triple_count"]!=W34_TRIPLES or
            result["all_425_original_flags_in_scope"] is not True):
            raise AssertionError("not a FULL true W34 source R3 census")
        if seed==0:
            # Source-backed exact W34 first-run pinned regression,
            # NEVER an asymptotic conjecture or another GF5 map.
            expected={
                "lex":(86,3,1349,1263),
                "reverse-line":(96,1,517,421),
            }[scheme]
            observed=(
                result["FULL_six_distinct_original_ID_3v3_signed_event_count"],
                result["R2_signed_2v2_events_exact"],
                result["equal_sum_pairs_of_distinct_ORIGINAL_triples"],
                result["equal_triples_sharing_original_ID_not_signed_R3"],
            )
            if observed!=expected:
                raise AssertionError(("real original W34 seed0 full census drift",
                                     scheme,observed,expected))
        out.append({
            "scheme":scheme,"seed":seed,
            "all_original_source_425_palettes_same_single_global_assignment":True,
            "risk":result,
        })
    return {
        "claim":"EXACT full W(3,4) ORIGINAL fixed-map GF5 R3 census",
        "all_original_source_IDs_must_be_counted":True,
        "has_no_all_h_new_exponent_claim":True,
        "complete_schemes":out,
    }


if __name__=="__main__":
    import argparse
    parser=argparse.ArgumentParser(
        description="EXACT full true original W34 GF5 3v3 on one fixed map")
    parser.add_argument("--scheme",choices=("lex","reverse-line"),
                        default="lex")
    parser.add_argument("--seed",type=int,default=0)
    args=parser.parse_args()
    print(json.dumps(report_w34_exact(schemes=(args.scheme,),seed=args.seed),
                     sort_keys=True,indent=2))
