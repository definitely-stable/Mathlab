"""HYP-105 issue #230 final evidence: named forest catalog and same-map seven-class/Q4.

Finite evidence is not a mathematical proof or an external peer-review receipt.
Independently reconstruct the named endpoint partition universe, the possible
leafless physical projection sizes, and exact W32 same-map motif sets.
"""
from collections import Counter, defaultdict
from functools import lru_cache
from fractions import Fraction as Q
from itertools import combinations, permutations, product
from math import comb
import argparse
import hashlib
import json
import csv
from pathlib import Path

from hyp105_low_publication_partition_referee import model
from hyp105_g5e2b3_forests import six_projection_coefficients
from hyp105_g5e2b3e1b0_seven_signature import seven_census

SCHEMA="mathlab.hyp105.branch-a-final-evidence.v1"
FLOORS={"D6":5643,"B-left/A-right":45600,"A-left/B-right":45600,
        "C/A":43320,"C/B":49050,"B/B-overlap":51750,"B/B-disjoint":45010}
PROFILES={(1,)*6:"A",(2,1,1,1,1):"B",(2,2,2):"C"}


def set_partitions(items):
    """Independent subset-of-first recursion, NOT restricted-growth recursion."""
    if not items:
        yield ()
        return
    anchor,*rest=items
    for n in range(len(rest)+1):
        for sub in combinations(rest,n):
            block=(anchor,)+sub
            rem=tuple(v for v in rest if v not in sub)
            for trailing in set_partitions(rem):
                yield (block,)+trailing


def encode(blocks):
    z=[-1]*6
    for i,b in enumerate(blocks):
        for j in b:
            if z[j]!=-1:
                raise AssertionError("partition overlapping block")
            z[j]=i
    if -1 in z:
        raise AssertionError("partition missing named position")
    return tuple(z)


def profile(p):
    return tuple(sorted(Counter(p).values(),reverse=True))


def forest_components(left,right):
    """Independent typed adjacency traversal, rejects duplicate incidences/cycles."""
    if len(set(zip(left,right)))!=6:
        return None
    adj=defaultdict(set)
    for p,l in zip(left,right):
        a=(0,p);b=(1,l)
        adj[a].add(b);adj[b].add(a)
    unseen=set(adj);components=0
    while unseen:
        start=unseen.pop()
        stack=[start];nodes={start}
        while stack:
            u=stack.pop()
            for v in adj[u]:
                if v not in nodes:
                    nodes.add(v);unseen.remove(v);stack.append(v)
        if sum(len(adj[v]) for v in nodes)!=2*(len(nodes)-1):
            return None
        components+=1
    return components


@lru_cache(maxsize=None)
def projection_sizes(part):
    """Independent feasibility only: actual simple label pairs with weights.

    No assumption that a possible projection supports a positive GF5 event.
    No identification of two typed physical projections across colors.
    """
    if tuple(sorted(part,reverse=True))!=part or sum(part)!=6:
        raise ValueError("canonical six occurrences required")
    weights=tuple(set(permutations(part)));r=len(part)
    valid=[]
    for v in range(2,7):
        pairs=tuple(combinations(range(v),2))
        if len(pairs)<r:
            continue
        found=False
        for shape in combinations(pairs,r):
            if len({x for e in shape for x in e})!=v:
                continue
            for assignment in weights:
                deg=[0]*v
                for (a,b),w in zip(shape,assignment):
                    deg[a]+=w;deg[b]+=w
                if min(deg)>=2:
                    found=True;break
            if found:break
        if found:valid.append(v)
    # Historical weighted counting is a distinct crosscheck of feasibility.
    assert tuple(valid)==tuple(v for v,c in six_projection_coefficients(part) if c>0)
    return tuple(valid)


def leading_class(left,right):
    a=PROFILES[profile(left)];b=PROFILES[profile(right)]
    if a==b=="A":return "A/A (D6 subset; other physical templates not accepted)"
    if (a,b)==("B","A"):return "B-left/A-right"
    if (a,b)==("A","B"):return "A-left/B-right"
    if {a,b}=={"C","A"}:return "C/A"
    if {a,b}=={"C","B"}:return "C/B"
    if a==b=="B":
        x=next(i for i,n in Counter(left).items() if n==2)
        y=next(i for i,n in Counter(right).items() if n==2)
        return "B/B-overlap" if any(p==x and l==y for p,l in zip(left,right)) else "B/B-disjoint"
    raise AssertionError("unexpected leading forest type")


@lru_cache(maxsize=1)
def named_catalog():
    parts=sorted(encode(p) for p in set_partitions(tuple(range(6))))
    assert len(parts)==len(set(parts))==203
    prof={p:profile(p) for p in parts}
    sizes={p:projection_sizes(prof[p]) for p in parts}
    rows=[]
    for left in parts:
        if not sizes[left]:continue
        for right in parts:
            if not sizes[right]:continue
            c=forest_components(left,right)
            if c is None:continue
            rl,rr=len(prof[left]),len(prof[right])
            assert c==rl+rr-6 and c>=1
            v,w=max(sizes[left]),max(sizes[right])
            # Independent algebra: 3*c+6 - (3/2)*(2*r_l-v+2*r_r-w).
            power=Q(3*c+6)-Q(3,2)*(2*rl-v+2*rr-w)
            assert power==Q(3,2)*(v+w)-12
            lead=power==6
            rows.append(dict(id="".join(map(str,left))+":"+"".join(map(str,right)),
                left_partition=list(left),right_partition=list(right),
                left_profile=list(prof[left]),right_profile=list(prof[right]),
                components=c,left_leafless_sizes=list(sizes[left]),
                right_leafless_sizes=list(sizes[right]),
                independent_label_necessary_power=str(power),
                stratum="LEADING" if lead else "SUBLEADING_NECESSARY_ONLY",
                historical_class=leading_class(left,right) if lead else None,
                all_physical_templates_positive=False))
    assert len(rows)==11663 and len({z["id"] for z in rows})==11663
    return tuple(rows)


def historical_model(m):
    f,g=m["f"],m["g"]
    return dict(a=m["a"],s=m["s"],N=len(m["flags"]),
        incidences=m["flags"],left_labels=f,right_labels=g,m=2*m["a"],
        supports=[tuple(f[p])+tuple(m["a"]+x for x in g[l]) for p,l in m["flags"]])


def dual_of(pairs,num):
    fibres=defaultdict(list)
    for i,edge in enumerate(pairs):
        for x in edge:fibres[x].append(i)
    if len(fibres)!=num or any(len(z)!=2 for z in fibres.values()):
        return None
    return tuple(sorted(tuple(z) for z in fibres.values()))


def connected_simple_cycle(dual,n):
    if dual is None or len(set(dual))!=n:return False
    adj=defaultdict(set)
    for u,v in dual:
        if u==v:return False
        adj[u].add(v);adj[v].add(u)
    if set(adj)!=set(range(n)) or any(len(x)!=2 for x in adj.values()):
        return False
    seen={0};stack=[0]
    while stack:
        for v in adj[stack.pop()]:
            if v not in seen:seen.add(v);stack.append(v)
    return len(seen)==n


def classify(m,ids):
    fs=[m["flags"][i] for i in ids]
    p,l=zip(*fs)
    cp,cl=profile(p),profile(l)
    a,b=PROFILES.get(cp),PROFILES.get(cl)
    if not a or not b:return None
    x=dual_of([m["f"][i] for i in p],6)
    y=dual_of([m["g"][i] for i in l],6)
    if x is None or y is None:return None
    if a==b=="A":
        return "D6" if x==y and connected_simple_cycle(x,6) else None
    if (a,b)==("B","A"):return "B-left/A-right"
    if (a,b)==("A","B"):return "A-left/B-right"
    if {a,b}=={"C","A"}:return "C/A"
    if {a,b}=={"C","B"}:return "C/B"
    if a==b=="B":
        rp=next(i for i,n in Counter(p).items() if n==2)
        rl=next(i for i,n in Counter(l).items() if n==2)
        return "B/B-overlap" if (rp,rl) in fs else "B/B-disjoint"
    return None


def independent_left_candidates(m):
    """Enumerate all distinct left factor pairs, weight placements and flag choices."""
    assert m["s"]==2 and m["a"]==6
    by=defaultdict(list)
    for i,(p,l) in enumerate(m["flags"]):by[p].append(i)
    for part,kind in PROFILES.items():
        for ps in combinations(range(m["V"]),len(part)):
            for weights in sorted(set(permutations(part))):
                d=Counter()
                for p,w in zip(ps,weights):
                    for symbol in m["f"][p]:d[symbol]+=w
                if len(d)!=6 or set(d.values())!={2}:continue
                for seq in product(*(tuple(combinations(by[p],w)) for p,w in zip(ps,weights))):
                    yield tuple(sorted(i for tup in seq for i in tup)),kind


def exact_q4_physical(m):
    """Count actual rainbow ordinary 4-cycles, unique original four-ID sets."""
    adj,own=m["adj"],m["owned"];sets=set()
    for start in sorted(adj):
        for v in adj[start]:
            if v<=start:continue
            for w in adj[v]:
                if w<=start or w[0] in (start[0],v[0]) or w[1] in (start[1],v[1]):continue
                for z in adj[w]&adj[start]:
                    if z<=v or len({q[0] for q in (start,v,w,z)})!=4 or len({q[1] for q in (start,v,w,z)})!=4:continue
                    path=(start,v,w,z)
                    ids=tuple(sorted(own[tuple(sorted(e))] for e in zip(path,path[1:]+path[:1])))
                    assert len(set(ids))==4
                    fs=[m["flags"][i] for i in ids]
                    dx=dual_of([m["f"][p] for p,l in fs],4)
                    dy=dual_of([m["g"][l] for p,l in fs],4)
                    assert dx==dy and connected_simple_cycle(dx,4)
                    assert ids not in sets
                    sets.add(ids)
    return len(sets)


@lru_cache(maxsize=3)
def joint_case(scheme):
    m=model(2,scheme,"full");seen=set();found={};types=Counter()
    for ids,kind in independent_left_candidates(m):
        assert ids not in seen
        seen.add(ids);types[kind]+=1
        tag=classify(m,ids)
        if tag:found[ids]=tag
    assert len(seen)==62370 and types==Counter(A=51030,B=10935,C=405)
    h=seven_census(historical_model(m),independent_checks=True,witness_sets=True)
    assert found==h["sets"]
    q4=exact_q4_physical(m)
    assert q4==h["Q4"]
    counts={k:Counter(found.values())[k] for k in FLOORS}
    floor=sum(counts[k]*v for k,v in FLOORS.items())
    assert floor==h["GF5_seven_lower_numerator"]
    map_hash=hashlib.sha256(json.dumps([m["flags"],m["f"],m["g"]],separators=(",",":")).encode()).hexdigest()
    return dict(s=2,scheme=scheme,same_original_map_sha256=map_hash,
        original_source_flags=len(m["flags"]),counts=counts,Q4=q4,
        S_seven=sum(counts.values()),D6_plus_BBo=counts["D6"]+counts["B/B-overlap"],
        certified_R3_floor_numerator=floor,certified_R3_floor_denominator=51**6,
        certified_Q4_R2_floor_numerator=531*q4,certified_Q4_R2_floor_denominator=51**4,
        independent_source_sets_agree=True,independent_Q4_count_agrees=True,
        full_weighted_R2_R3_computed=False)


def certificate(rows=None):
    rows=named_catalog() if rows is None else tuple(rows)
    by_stratum=Counter(z["stratum"] for z in rows)
    by_power=Counter(z["independent_label_necessary_power"] for z in rows)
    leading=Counter(z["historical_class"] for z in rows if z["stratum"]=="LEADING")
    assert by_stratum==Counter(LEADING=631,SUBLEADING_NECESSARY_ONLY=11032)
    assert leading=={
        "A/A (D6 subset; other physical templates not accepted)":1,
        "B-left/A-right":15,"A-left/B-right":15,"C/A":30,"C/B":360,
        "B/B-overlap":120,"B/B-disjoint":90}
    digest=hashlib.sha256(json.dumps(rows,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    return dict(schema=SCHEMA,issue=230,parent_pr=787,partition_catalog_rows=len(rows),
        catalog_sha256=digest,by_stratum=dict(by_stratum),by_power=dict(by_power),
        leading_partition_categories=dict(leading),
        subleading_not_GF5_positive_classified=True,
        fixed_label_subleading_upper_claimed=False,
        same_map_joint_cases=[joint_case(s) for s in ("lex","reverse","correlated")],
        mathematical_review_verdict="NO_FATAL_GAP_FOUND_INTERNAL_REVIEW",
        repository_status="OPEN_WITH_FORMAL_BLOCKER",
        independent_external_review_received=False,
        postmerge_main_CI_verified=False,
        new_ASET_exponent=False)


def write_artifacts(directory):
    directory=Path(directory);directory.mkdir(parents=True,exist_ok=True)
    rows=named_catalog()
    cert=certificate(rows)
    (directory/"named_original_partition_index.json").write_text(
        json.dumps(rows,sort_keys=True,indent=1)+"\n",encoding="utf-8")
    with (directory/"named_original_partition_index.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]))
        w.writeheader();w.writerows(rows)
    (directory/"certificate.json").write_text(json.dumps(cert,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    return cert


if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--out",default="hyp105-final-evidence")
    args=p.parse_args()
    print("HYP105_BRANCH_A_FINAL_EVIDENCE="+json.dumps(write_artifacts(args.out),sort_keys=True))
