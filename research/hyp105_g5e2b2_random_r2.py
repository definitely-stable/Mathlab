"""HYP-105 G5-E2-B2: all-s random-label FOUR-trade expected-risk bound.

Proof is elementary, conditional on the ALREADY PUBLISHED symplectic GQ
incidence girth eight. For every s=2^h, independent uniformly random
injective mappings of each part's V vertices into K_a coordinate pairs
give E_label[R2] = O(s^4) = O(m^(8/3)). This is ONE of TWO needed risk
exponents, not a new ASET power or scientific priority claim.

The functions below certify the complete finite 4-edge factor-forest
case split symbolically and exact small coordinate-pair probabilities.
No enumeration of 425^4 edge sets or GF5 51^4 weight choices.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from math import comb
import json


def falling(n, k):
    if not isinstance(n,int) or not isinstance(k,int) or n<0 or k<0:
        raise ValueError("falling factorial requires nonnegative ints")
    result=1
    for i in range(k):
        result*=n-i
    return result


def leafless_projection_probability(alphabet_size, multiplicities):
    """Exact probability for up to FOUR projected edge occurrences.

    Distinct abstract vertex labels receive pairwise DISTINCT uniformly
    injected unordered pairs from K_a. Multiplicities count how many of
    the four selected factor edges share each abstract vertex.
    A 4-edge projected pair-multigraph with no degree-one coordinate
    must have one of:
      4          one pair repeated 4 times;
      2+2        two different pair labels repeated twice each;
      2+1+1      three different pair labels making a triangle;
      1+1+1+1    four different pair labels making a simple C4.
    """
    if not isinstance(alphabet_size,int) or alphabet_size<4:
        raise ValueError("coordinate alphabet must be at least four")
    mult=tuple(sorted(tuple(multiplicities),reverse=True))
    if not mult or any(not isinstance(x,int) or x<=0 for x in mult) or sum(mult)!=4:
        raise ValueError("positive multiplicities must sum to four")
    pair_count=comb(alphabet_size,2)
    if mult in ((4,), (2,2)):
        return Fraction(1)
    if mult==(3,1):
        return Fraction(0)
    if mult==(2,1,1):
        # Ordered three distinct pair labels form a triangle exactly
        # in (a)_3 ways: choose triangle vertices and permute 3 edges.
        return Fraction(falling(alphabet_size,3),falling(pair_count,3))
    if mult==(1,1,1,1):
        # For each four-coordinate vertex set there are 3 undirected
        # squares and 4! assignments to the four named factor vertices.
        return Fraction(3*falling(alphabet_size,4),falling(pair_count,4))
    raise AssertionError("partition of four unhandled")


def complete_small_projection_oracle(alphabet_size, multiplicities):
    """Independent exhaustive injective pair-label check, a<=6 ONLY."""
    if alphabet_size>6:
        raise ValueError("exact factorial label verification capped at a<=6")
    mult=tuple(multiplicities)
    if sum(mult)!=4:
        raise ValueError("multiplicities must sum to four")
    palette=tuple(combinations(range(alphabet_size),2))
    good=0
    total=0
    for chosen in permutations(palette,len(mult)):
        count=Counter()
        for pair, repeats in zip(chosen,mult):
            count[pair[0]]+=repeats
            count[pair[1]]+=repeats
        good+=all(d>=2 for d in count.values())
        total+=1
    if total != falling(len(palette),len(mult)):
        raise AssertionError("exhaustive enumeration was incomplete")
    return Fraction(good,total)


def factor_partition_shapes(t=4):
    """All partitions of four named original graph edges, Bell(4)=15."""
    if t!=4:
        raise ValueError("only four-edge factor shape used in this theorem")
    def build(seq):
        if len(seq)==t:
            yield tuple(seq)
        else:
            for label in range(max(seq)+2):
                yield from build(seq+[label])
    result=tuple(build([0]))
    if len(result)!=15 or len(set(result))!=15:
        raise AssertionError("Bell(4)=15 enumeration check failed")
    return result


def is_factor_forest(left, right):
    """Independent union-find on projected *factor* graph, NOT K_a."""
    if len(left)!=4 or len(right)!=4:
        raise ValueError("four incidence edges required")
    rL=max(left)+1
    parent=list(range(rL+max(right)+1))
    def root(v):
        while parent[v]!=v:
            v=parent[v]
        return v
    for l,r in zip(left,right):
        a,b=root(l),root(rL+r)
        if a==b:
            return False
        parent[b]=a
    return True


def projection_s_exponent(multiplicities):
    """Power of s lost from a~s^(3/2) pair-label 2-core probability."""
    part=tuple(sorted(multiplicities,reverse=True))
    if part in ((4,), (2,2)):
        return Fraction(0)
    if part == (3,1):
        return None
    if part==(2,1,1):
        return Fraction(9,2)  # a^-3 ~ s^-9/2
    if part==(1,1,1,1):
        return Fraction(6)    # a^-4 ~ s^-6
    raise ValueError("unexpected 4-edge multiplicity")


def four_edge_forest_exponents():
    """Complete finite case classification, symbolically valid ALL h.

    Any <=4-edge subgraph of bipartite GQ incidence girth8 is a forest.
    For a shape with rL left/rR right factor vertices and c components,
    #factor copies <= V^c * Delta^4 (times finite shape count),
    V=Theta(s^3), Delta=Theta(s), giving s^(3c+4).
    Independent pair-label projections contribute a factor s^(-lossL-lossR).
    """
    entries=[]
    shapes=factor_partition_shapes()
    for left in shapes:
        for right in shapes:
            if len(set(zip(left,right)))!=4:
                continue  # duplicate factor edge cannot be selected
            if not is_factor_forest(left,right):
                continue  # cannot embed in C4/C6-free GQ
            lc=tuple(sorted(Counter(left).values(),reverse=True))
            rc=tuple(sorted(Counter(right).values(),reverse=True))
            loss_l=projection_s_exponent(lc)
            loss_r=projection_s_exponent(rc)
            if loss_l is None or loss_r is None:
                continue
            rL=len(lc)
            rR=len(rc)
            c=rL+rR-4
            if c<1:
                raise AssertionError("four-edge forest must have c>=1")
            exponent=Fraction(3*c+4)-loss_l-loss_r
            entries.append({
                "left_partition":left, "right_partition":right,
                "left_profile":lc, "right_profile":rc,
                "components":c, "exponent_in_s":exponent,
            })
    if not entries:
        raise AssertionError("finite 4-edge graph shape catalog unexpectedly empty")
    maximum=max(e["exponent_in_s"] for e in entries)
    if maximum>4:
        raise AssertionError("all-s E[R2]=O(s^4) theorem countermodel found")
    return entries


def four_edge_profile_table():
    entries=four_edge_forest_exponents()
    table={}
    for x in entries:
        key=(x["left_profile"], x["right_profile"])
        table[key]={
            "multiplicity_patterns":table.get(key,{}).get("multiplicity_patterns",0)+1,
            "forest_components":x["components"],
            "s_exponent_bound":str(x["exponent_in_s"]),
        }
    return table


def theorem_report():
    entries=four_edge_forest_exponents()
    table=four_edge_profile_table()
    def key(x):
        return "/".join(map(str,x))
    return {
        "family":"published symplectic W(3,s), s=2^h, incidence girth8",
        "pair_label_model":"independent uniform injective point/line maps into K_a pairs",
        "GF5_collision_model":"independent 51 all-nonzero checksum4 patterns",
        "factor_4_edge_forest_shapes_checked":len(entries),
        "positive_profile_pairs":{
            key(k[0])+" × "+key(k[1]):v
            for k,v in sorted(table.items())
        },
        "maximum_power_in_s":str(max(e["exponent_in_s"] for e in entries)),
        "proved_expected_R2_upper":"O(s^4) = O(m^(8/3))",
        "proved_expected_R3_upper":None,
        "published_expected_R3_lower":"Omega(m^4) in independent uniform labeling model",
        "new_aset_lower_exponent_proven":False,
        "priority_novelty_verified":False,
    }


if __name__=="__main__":
    print(json.dumps(theorem_report(),indent=2,sort_keys=True))
