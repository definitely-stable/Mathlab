"""HYP-105 #230 D6-AA4-A: source-forest support and positional-stratum transport.

Exact all-h local source-girth support for 130x130 physical pattern pairs.
Exact W32 original-incidence source-partition Fréchet relaxation, deliberately
NOT a globally consistent injective-label assignment or universal Omega bound.
"""
from collections import Counter, defaultdict
from itertools import combinations, combinations_with_replacement
from math import comb

from hyp105_issue230_d6aa_positional_tensor import (
    POSITION_PAIRS, WEIGHTS, local_signature, classify_position_signatures,
)

EXPECTED_PAIR_SUPPORT = {
    "forbidden": 630,
    "not_seven_AA": 4840,
    "D6": 60,
    "B-left/A-right": 3150,
    "A-left/B-right": 3150,
    "C/A": 2100,
    "C/B": 1080,
    "B/B-overlap": 1080,
    "B/B-disjoint": 810,
}


def positional_graphs():
    """Independent labeled multigraph generator; no reference seven classifier."""
    out = []
    for edges in combinations_with_replacement(POSITION_PAIRS, 6):
        degree = [0] * 6
        for a, b in edges:
            degree[a] += 1
            degree[b] += 1
        if degree == [2] * 6:
            out.append(edges)
    if len(out) != 130:
        raise AssertionError("expected 130 positional 2-regular multigraphs")
    return tuple(out)


def equality_partition(factors):
    """First-occurrence IDs retain all six ORIGINAL ordered positions."""
    seen = {}
    output = []
    for factor in factors:
        if factor not in seen:
            seen[factor] = len(seen)
        output.append(seen[factor])
    if len(output) != 6:
        raise ValueError("exactly six ORIGINAL incidence positions required")
    return tuple(output)


def graph_source_partition(graph):
    """Original typed factors coincide iff their physical coordinate PAIRS coincide."""
    if len(graph) != 6:
        raise ValueError("six 2-regular positional graph edges required")
    physical_pair_at_position = tuple(
        tuple(i for i,edge in enumerate(graph) if position in edge)
        for position in range(6)
    )
    if any(len(pair) != 2 for pair in physical_pair_at_position):
        raise ValueError("not a positional degree-two graph")
    return equality_partition(physical_pair_at_position)


def graph_original_signature(graph):
    """Reconstruct each physical column as exactly two coordinate-edge IDs."""
    six_pairs = tuple(tuple(k for k,e in enumerate(graph) if i in e)
                      for i in range(6))
    sig = local_signature(six_pairs)
    if not sig["regular"] or sig["position_graph"] != graph:
        raise AssertionError("positional graph reconstruction drift")
    return sig


def source_forest_info(left_partition, right_partition):
    """Simple-incidence + girth-eight necessary support, on six source edges.

    Any genuine W(3,s) six-edge subgraph is a forest since girth=8.
    Here we check exactly this abstract six-edge forest condition, NOT
    guaranteed embeddability into a particular finite W(3,s).
    """
    if len(left_partition) != 6 or len(right_partition) != 6:
        raise ValueError("six indexed ORIGINAL point/line positions required")
    rows = tuple(zip(left_partition, right_partition))
    if len(set(rows)) != 6:
        return {"valid": False, "reason": "duplicate_original_incidence"}
    parent = {}
    size = {}

    def find(v):
        parent.setdefault(v,v)
        size.setdefault(v,1)
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v

    for p,l in rows:
        u,v = find(("p",p)),find(("l",l))
        if u == v:
            return {"valid": False, "reason": "source_cycle_shorter_than_girth8"}
        if size[u] < size[v]:
            u,v=v,u
        parent[v]=u
        size[u]+=size[v]
    components = defaultdict(int)
    for p,l in rows:
        root=find(("p",p))
        components[root]+=1
    return {"valid": True, "path_lengths": tuple(sorted(
        components.values(), reverse=True)), "reason": None}


def graph_type(graph):
    partition = graph_source_partition(graph)
    degree = Counter(partition)
    profile = tuple(sorted(degree.values(),reverse=True))
    return {(1,1,1,1,1,1): "A",
            (2,1,1,1,1): "B",
            (2,2,2): "C"}[profile]


def independent_seven_tag(g,h,*, supported=True):
    """Independent combinatorial class oracle, without AA1 Phi dependency."""
    if not supported:
        return None
    a,b = graph_type(g),graph_type(h)
    if a == b == "A":
        if g == h:
            neighbors = {i: set() for i in range(6)}
            for u,v in g:
                neighbors[u].add(v)
                neighbors[v].add(u)
            found={0}
            todo=[0]
            while todo:
                for v in neighbors[todo.pop()]:
                    if v not in found:
                        found.add(v)
                        todo.append(v)
            if len(found) == 6:
                return "D6"
        return None
    if (a,b)==("B","A"):
        return "B-left/A-right"
    if (a,b)==("A","B"):
        return "A-left/B-right"
    if {a,b}=={"A","C"}:
        return "C/A"
    if {a,b}=={"B","C"}:
        return "C/B"
    if a==b=="B":
        pl,pr=graph_source_partition(g),graph_source_partition(h)
        l2=next(v for v,c in Counter(pl).items() if c==2)
        r2=next(v for v,c in Counter(pr).items() if c==2)
        ol={i for i,p in enumerate(pl) if p==l2}
        or_={i for i,p in enumerate(pr) if p==r2}
        return "B/B-overlap" if ol & or_ else "B/B-disjoint"
    return None


def all_130_squared_source_support():
    graphs = positional_graphs()
    counts=Counter()
    reasons=Counter()
    paths=defaultdict(Counter)
    originals = {g: graph_original_signature(g) for g in graphs}
    parts = {g: graph_source_partition(g) for g in graphs}
    for g in graphs:
        for h in graphs:
            status=source_forest_info(parts[g],parts[h])
            if not status["valid"]:
                counts["forbidden"]+=1
                reasons[status["reason"]]+=1
                continue
            tag=independent_seven_tag(g,h)
            # Historic Phi is checked only for SOURCE-ADMISSIBLE pairs.
            if classify_position_signatures(originals[g],originals[h])!=tag:
                raise AssertionError("new source support and accepted Phi disagree")
            key=tag or "not_seven_AA"
            counts[key]+=1
            paths[key][status["path_lengths"]]+=1
            if tag is None and not (graph_type(g)==graph_type(h)=="A"):
                raise AssertionError("non-AA admissible regular pair incorrectly rejected")
    if dict(counts)!=EXPECTED_PAIR_SUPPORT:
        raise AssertionError(f"source-support census changed: {dict(counts)}")
    expected_paths={
        "D6": (1,1,1,1,1,1),
        "not_seven_AA": (1,1,1,1,1,1),
        "B-left/A-right": (2,1,1,1,1),
        "A-left/B-right": (2,1,1,1,1),
        "C/A": (2,2,2),
        "C/B": (4,2),
        "B/B-overlap": (3,1,1,1),
        "B/B-disjoint": (2,2,1,1),
    }
    for tag,expected in expected_paths.items():
        if set(paths[tag])!={expected}:
            raise AssertionError("wrong source linear forest shape for "+tag)
    return {"pair_patterns":16900,"admissible_abstract_source_forests":16270,
            "excluded_by_girth_or_duplicate":630,
            "allowed_positive_positional_pairs":11430,
            "allowed_nonseven_AA_pairs":4840,
            "by_class":dict(counts),"excluded_reasons":dict(reasons),
            "source_path_shapes":{tag:list(expected) for tag,expected in expected_paths.items()},
            "all_h_scope":"necessary abstract girth-eight/simple incidence, not embedding sufficiency"}


def source_key(ids, incidences):
    """Canonical equality partitions of six SORTED ORIGINAL incidence IDs."""
    if len(ids)!=6 or tuple(sorted(ids))!=tuple(ids) or len(set(ids))!=6:
        raise ValueError("six sorted distinct ORIGINAL incidence IDs required")
    ps,ls=[],[]
    for i in ids:
        p,l=incidences[i]
        ps.append(p)
        ls.append(l)
    return equality_partition(ps),equality_partition(ls)


def exact_binary_coupling(n,left,right):
    """Exact sharp Fréchet overlap and integer two-bit coupling certificate."""
    if any(type(x) is not int or x<0 for x in (n,left,right)) or max(left,right)>n:
        raise ValueError("one-sided cardinalities must be in [0,n]")
    both=max(0,left+right-n)
    result={"both":both,"left_only":left-both,
            "right_only":right-both,"neither":n-left-right+both}
    if any(v<0 for v in result.values()) or sum(result.values())!=n:
        raise AssertionError("conditional binary transport certificate failed")
    return result


def one_sided_candidate_margins(model,side):
    """Exact W32 one-sided physical 2-regular counts by SOURCE partition."""
    from hyp105_g5e2b3e1a_fixed_leading import selected_left_six
    if model["s"]!=2 or model["N"]!=45:
        raise ValueError("only W32 finite source strata permitted")
    E=tuple(model["incidences"])
    m=dict(model)
    if side=="right":
        m["left_labels"]=model["right_labels"]
        m["right_labels"]=model["left_labels"]
        m["incidences"]=tuple((l,p) for p,l in E)
    elif side!="left":
        raise ValueError("typed side must be left or right")
    counts=Counter()
    seen=set()
    for ids,_ in selected_left_six(m):
        if ids in seen:
            raise AssertionError("one-sided generator repeated original Q")
        seen.add(ids)
        counts[source_key(ids,E)]+=1
    if len(seen)!=62370:
        raise AssertionError("W32 62,370 one-sided candidate census changed")
    return counts


def original_source_histogram(incidences,active_keys,*,budget=8145060):
    """Exact ALL C(45,6) source strata, ONE scan independent of physical maps."""
    E=tuple(incidences)
    if len(E)!=45 or len(set(E))!=45 or comb(len(E),6)!=8145060:
        raise ValueError("full source audit restricted to original W32 45 incidences")
    if budget!=8145060:
        raise ValueError("no incomplete original sixset scan accepted")
    selected=set(active_keys)
    counts=Counter()
    n=0
    for ids in combinations(range(len(E)),6):
        n+=1
        key=source_key(ids,E)
        if key in selected:
            counts[key]+=1
    if n!=budget:
        raise AssertionError("incomplete W32 original C(45,6) scan")
    return counts


def observed_original_seven(model):
    """Actual GF5-necessary census and nonseven regular crosscheck."""
    from hyp105_g5e2b3e1a_fixed_leading import selected_left_six
    from hyp105_issue230_d6aa_positional_tensor import classify_original_six
    E=tuple(model["incidences"])
    L,R=model["left_labels"],model["right_labels"]
    pos=Counter()
    proxy=0
    rejected=Counter()
    for ids,_ in selected_left_six(model):
        six=tuple(E[i] for i in ids)
        r=local_signature(tuple(R[l] for p,l in six))
        actual=classify_original_six(six,L,R)
        if actual:
            pos[actual]+=1
        if r["regular"]:
            proxy+=1
            if actual is None:
                # Source support theorem says ONLY A/A nonalignment remains.
                p=tuple(p for p,l in six)
                if len(set(p))!=6 or len(set(l for p,l in six))!=6:
                    raise AssertionError("non-AA false positive contradicts source support")
                rejected["A/A_nonmatching"]+=1
    return {"S":sum(pos.values()),"by_class":dict(pos),
            "proxy":proxy,"false_positive_types":dict(rejected),
            "GF5_floor_numerator":sum(pos[k]*v for k,v in WEIGHTS.items())}


def conditional_original_strata_report():
    """Fixed-W32 conditional 2x2 transport; not complete assignment relaxation.

    The exact source-key partition keeps BOTH six-position endpoint-equality
    patterns; marginals retain only one-sided physical regular INDICATORS.
    Within each key, we permit arbitrary re-pairings of different original
    sixsets, so the pseudo-coupling is not asserted globally realizable.
    """
    from hyp105_issue230_projection import fixture
    models={scheme:fixture(1,scheme) for scheme in ("S68","S72")}
    E=tuple(models["S68"]["incidences"])
    if E!=tuple(models["S72"]["incidences"]):
        raise AssertionError("true ORIGINAL geometry changed between W32 schemes")
    margins={}
    active=set()
    for scheme,m in models.items():
        L=one_sided_candidate_margins(m,"left")
        R=one_sided_candidate_margins(m,"right")
        active.update(L)
        active.update(R)
        margins[scheme]=(L,R)
    totals=original_source_histogram(E,active)
    records=[]
    for scheme,m in models.items():
        L,R=margins[scheme]
        minimum_joint_regular=0
        minimum_seven_from_nonAA=0
        occupied_groups=0
        max_dual_overlap=0
        for key in set(L)|set(R):
            count=totals[key]
            l,r=L[key],R[key]
            coupling=exact_binary_coupling(count,l,r)
            forced=coupling["both"]
            minimum_joint_regular+=forced
            if forced:
                occupied_groups+=1
                max_dual_overlap=max(max_dual_overlap,forced)
                if key[0]!=(0,1,2,3,4,5) or key[1]!=(0,1,2,3,4,5):
                    # Both 2-regular on genuine source Q, non-AA necessarily
                    # one of accepted classes by the all-h forest support.
                    minimum_seven_from_nonAA+=forced
        actual=observed_original_seven(m)
        if (actual["S"] not in (68,72)
                or minimum_seven_from_nonAA>actual["S"]
                or minimum_joint_regular>actual["proxy"]):
            raise AssertionError("Fréchet bound exceeds actual original geometry")
        records.append({
            "scheme":scheme,
            "original_sixsets":comb(45,6),
            "source_sixposition_keys_with_regular_marginal":len(set(L)|set(R)),
            "left_regular_original_sixsets":sum(L.values()),
            "right_regular_original_sixsets":sum(R.values()),
            "sharp_frechet_minimum_joint_regular":minimum_joint_regular,
            "valid_nonAA_GF5_seven_lower_from_source_partition_marginals":
                minimum_seven_from_nonAA,
            "strata_forcing_regular_overlap":occupied_groups,
            "max_per_stratum_forced_regular_overlap":max_dual_overlap,
            "actual":actual,
            "requires_global_assignment_extension":True,
        })
    return {"scope":"true W(3,2), both types; same original incidences S68/S72",
            "retained_source_information":"both exact six-position factor equality partitions",
            "source_strata_are_not_global_assignment_marginals":True,
            "source_partition_denominator_enumerated_once":comb(45,6),
            "records":records,
            "all_h_positive_bound_proved":False,"Branch_A":"OPEN","Branch_B":"OPEN"}


def report():
    return {
        "slice":"HYP105-ISSUE230-D6-AA4-A-SOURCE-FOREST-TRANSPORT",
        "source_support":all_130_squared_source_support(),
        "w32_source_stratified_transport":conditional_original_strata_report(),
        "status":"RESTRICTED_THEOREM_C_OPEN_FEASIBILITY",
        "all_h_positive_GF5_bound":False,
        "full_R3_upper":False,
        "Branch_A":"OPEN","Branch_B":"OPEN",
    }


if __name__=="__main__":
    import json
    print(json.dumps(report(),sort_keys=True,indent=2))
