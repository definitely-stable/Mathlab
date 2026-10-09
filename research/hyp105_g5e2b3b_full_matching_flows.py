"""HYP-105 E2-B3.1-B1: complete six-FACTOR-MATCHING leafless GF5 flow census.

Every original six-incidence matching has six distinct factor vertices per
side, so injective pair labels produce two SIMPLE six-edge physical
graphs. For any positive GF5 3v3 trade, each physical coordinate has
degree >=2. Six edges give 12 stubs, so each physical graph has 4..6
vertices. We enumerate ALL possibilities, with colored halves and the
unordered global +/- sign partition kept distinct. We do NOT classify
nonmatching factor forests, or bound their multiplicities in W(3,s).

Each physical coordinate independently carries nonzero GF5 weights
whose signed sum is zero. A half-block histogram indexed by the SIX
column checksum contributions can be convolved with the other half:
 F(left,right)=sum_z H_left(z)*H_right(4-z).
The full coefficient palette 51 is enforced by the column sum =4 and
all four per-column entries nonzero. This finite reduction applies for
any order s=2^h; the exhaustive calculation is a computer-checked
finite-template certificate, not a newly proved all-h R3 upper.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations, permutations, product
import json

N=6
ALL=(1<<N)-1
SIGNS=(1,1,1,-1,-1,-1)


def transform_profile(profile, perm):
    """Simultaneous named-column permutation; physical symbols unlabelled."""
    if len(perm)!=N or set(perm)!=set(range(N)):
        raise ValueError("expected an S6 named-column permutation")
    return tuple(sorted(
        sum(1<<perm[i] for i in range(N) if mask & (1<<i))
        for mask in profile))


def signed_stabilizer_group():
    """S3 x S3, extended by global sign swap: 3!*3!*2 = 72."""
    return (tuple(p+q for p in permutations(range(3))
                      for q in permutations(range(3,6))) +
            tuple(q+p for q in permutations(range(3,6))
                      for p in permutations(range(3))))


def validate_profile(profile):
    """Every column must be one distinct physical pair; no degree-one."""
    if not isinstance(profile,tuple) or not 4<=len(profile)<=6:
        raise ValueError("between four and six physical vertices required")
    if tuple(sorted(profile))!=profile or len(set(profile))!=len(profile):
        raise ValueError("canonical distinct physical coordinate masks required")
    if any(not isinstance(x,int) or x<=0 or x>ALL or x.bit_count()<2
           for x in profile):
        raise ValueError("no degree-one or invalid physical coordinate")
    pair_labels=[]
    for col in range(N):
        coordinates=tuple(i for i,mask in enumerate(profile)
                          if mask & (1<<col))
        if len(coordinates)!=2:
            raise ValueError("each column has two coordinates per half")
        pair_labels.append(coordinates)
    if len(set(pair_labels))!=N:
        raise ValueError("factor matching requires six different pairs")
    return True


@lru_cache(maxsize=1)
def projection_types():
    """All *named-column* simple six-edge min-degree-two pair graphs.

    Enumerate 6-of-K_v unlabeled physical-edge subsets and all 6! edge
    ID assignments, canonicalizing physical coordinates by their column
    occurrence bitmasks. No assumed orbit list, no hardcoded signatures.
    """
    answer=set()
    for v in (4,5,6):
        edges=tuple(combinations(range(v),2))
        for chosen in combinations(edges,N):
            if any(sum(i in edge for edge in chosen)<2 for i in range(v)):
                continue
            for named in permutations(chosen):
                signature=tuple(sorted(sum(
                    1<<j for j,edge in enumerate(named) if i in edge)
                    for i in range(v)))
                answer.add(signature)
    result=tuple(sorted(answer))
    if len(result)!=610 or Counter(map(len,result))!={4:30,5:510,6:70}:
        raise AssertionError("6-edge min-degree-two projection census failed")
    if any(not validate_profile(p) for p in result):
        raise AssertionError("invalid enumerated physical pair injection")
    return result


@lru_cache(maxsize=64)
def nonzero_coordinate_options(mask):
    """Nonzero GF5 coordinate weights with signed (3v3) zero sum."""
    if not isinstance(mask,int) or mask<1 or mask>ALL or mask.bit_count()<2:
        raise ValueError("a coordinate must touch at least two columns")
    ids=tuple(i for i in range(N) if mask>>i &1)
    result=[]
    for early in product(range(1,5),repeat=len(ids)-1):
        total=sum(SIGNS[i]*value for i,value in zip(ids[:-1],early))
        last=(-total*SIGNS[ids[-1]])%5
        if last:
            result.append(tuple(zip(ids,early+(last,))))
    # Standard character-sum zero coefficient:
    # number of nonzero d-tuples summing to zero = (4^d+4*(-1)^d)/5.
    d=len(ids)
    if len(result)!=(4**d+4*((-1)**d))//5:
        raise AssertionError("GF5 nonzero coordinate convolution coefficient")
    return tuple(result)


@lru_cache(maxsize=700)
def half_checksum_histogram(profile):
    """Exact contribution histogram on GF5^6 (no 51^6 enumeration)."""
    validate_profile(profile)
    options=tuple(nonzero_coordinate_options(mask) for mask in profile)
    histogram=Counter()
    for assignment in product(*options):
        sums=[0]*N
        for group in assignment:
            for col,coefficient in group:
                sums[col]+=coefficient
        histogram[tuple(x%5 for x in sums)]+=1
    required=1
    for group in options:
        required*=len(group)
    if sum(histogram.values())!=required:
        raise AssertionError("coordinate assignments were lost")
    if any(sum(SIGNS[i]*z for i,z in enumerate(key))%5
           for key in histogram):
        raise AssertionError("coordinate conservation broken in histogram")
    return histogram


def exact_pair_GF5_flow(left,right):
    """Complete full 51-pattern positive/zero signed 3v3 probability numerator."""
    l=half_checksum_histogram(left)
    r=half_checksum_histogram(right)
    return sum(count * r.get(tuple((4-x)%5 for x in z),0)
               for z,count in l.items())


def supports_for_profiles(left,right):
    """Six true split support-four columns for independent MITM cross-check."""
    validate_profile(left)
    validate_profile(right)
    rows=[]
    for col in range(N):
        a=[i for i,mask in enumerate(left) if mask & (1<<col)]
        b=[len(left)+i for i,mask in enumerate(right)
           if mask & (1<<col)]
        rows.append(tuple(a+b))
    if len(set(rows))!=N or any(len(row)!=4 for row in rows):
        raise AssertionError("the projected matching is not split support4")
    return tuple(rows)


def matching_signed_orbit_representatives():
    """Enumerate all labeled cases modulo S3xS3 and global sign flip.

    Instead of checking 610^2*10 cases separately:
    (i) canonical left orbits under H, (ii) quotient each right by the
    H-stabilizer of the chosen left. Orbit mass = 10*m_left*m_right.
    This transports ALL 10 unordered balanced sign partitions.
    Left/right physical colors are NOT exchangeable.
    """
    types=projection_types()
    group=signed_stabilizer_group()
    if len(group)!=72 or len(set(group))!=72:
        raise AssertionError("sign-partition stabilizer size")
    left_orbits=Counter(min(transform_profile(p,g) for g in group)
                        for p in types)
    if len(left_orbits)!=20 or sum(left_orbits.values())!=610:
        raise AssertionError("left color signed orbit census")
    result=[]
    total=0
    for left,lmass in sorted(left_orbits.items()):
        stabilizer=tuple(g for g in group
                         if transform_profile(left,g)==left)
        if len(stabilizer)*lmass!=72:
            raise AssertionError("orbit-stabilizer failed")
        right_orbits=Counter(min(transform_profile(p,g) for g in stabilizer)
                             for p in types)
        if sum(right_orbits.values())!=610:
            raise AssertionError("right orbit partition")
        for right,rmass in sorted(right_orbits.items()):
            weight=10*lmass*rmass
            result.append((left,right,weight))
            total+=weight
    if len(result)!=5486 or total!=10*610**2:
        raise AssertionError("exact labeled two-color signed mass lost")
    return tuple(result)


def exhaustive_matching_census():
    """Complete, model-scoped finite certificate for all matching six-sets.

    Output multiplicities count 3+3 balanced signed events on six NAMED
    original factor matching edges. They do not count actual W(3,s)
    occurrences of physical projection types, and cannot imply an R3
    exponent. Algebraic checksum solution counts are integers.
    """
    signed=Counter()
    representatives=Counter()
    representative_examples={}
    minpositive=None
    maxpositive=0
    for left,right,mass in matching_signed_orbit_representatives():
        flow=exact_pair_GF5_flow(left,right)
        status="positive" if flow>0 else "zero"
        key=(len(left),len(right),status)
        signed[key]+=mass
        representatives[key]+=1
        if key not in representative_examples:
            representative_examples[key]=(left,right,flow)
        if flow:
            minpositive=flow if minpositive is None else min(minpositive,flow)
            maxpositive=max(maxpositive,flow)
    if sum(signed.values())!=3721000 or sum(representatives.values())!=5486:
        raise AssertionError("lost any six-matching signed template")
    zero=sum(v for (left,right,status),v in signed.items()
             if status=="zero")
    if zero!=100 or signed.get((6,6,"zero"))!=100:
        raise AssertionError("zero-flow cases must all be known 6+6")
    if minpositive!=4806 or maxpositive!=135001:
        raise AssertionError("GF5 flow coefficient extremum regression")
    return {
        "model":"six factor-disjoint GQ incidences, two injective pair labels, full GF5 checksum4",
        "projection_types_total":len(projection_types()),
        "projection_types_by_physical_vertices":
            dict(sorted(Counter(map(len,projection_types())).items())),
        "balanced_unordered_3v3_partitions":10,
        "all_labeled_signed_templates":sum(signed.values()),
        "signed_color_preserving_orbits":sum(representatives.values()),
        "labeled_signed_by_vleft_vright_status":{
            f"{a}/{b}/{status}":n for (a,b,status),n in sorted(signed.items())},
        "orbit_count_by_vleft_vright_status":{
            f"{a}/{b}/{status}":n for (a,b,status),n in sorted(representatives.items())},
        "positive_labeled_signed_templates":sum(
            n for (a,b,status),n in signed.items() if status=="positive"),
        "zero_labeled_signed_templates":zero,
        "min_positive_GF5_weight_assignments":minpositive,
        "max_positive_GF5_weight_assignments":maxpositive,
        "examples":{
            f"{a}/{b}/{status}":{"left":left,"right":right,
                                   "GF5_flow_assignments":flow}
            for (a,b,status),(left,right,flow) in
            sorted(representative_examples.items())},
        "proof_type":"finite exhaustive 5486-orbit certificate; all-h template transfer",
        "all_6_factor_matching_leafless_cases_classified":True,
        "all_11663_factor_forest_shapes_classified":False,
        "fixed_label_full_R3_upper_proved":False,
        "new_ASET_exponent_proved":False,
    }


if __name__=="__main__":
    print(json.dumps(exhaustive_matching_census(),sort_keys=True,indent=2))
