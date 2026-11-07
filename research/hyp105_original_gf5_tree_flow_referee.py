"""AA4-GF5TREE: independently recertify genuine ORIGINAL D6/BBo GF(5) weights.

This module does NOT import the historical Fourier/dual-orbit flow evaluator
or seven-family GF(5) classifier. It derives the full 51-element column
palette from nonzero F5 variables, counts signed flows via a spanning
forest and nonzero chord assignments, and crosschecks selected cases with
a separate 51^3 meet-in-the-middle direct palette count.

Nine B/B-overlap six-column templates and ten balanced unordered signs
cover ALL dyadic original W(3,s) fixed correlated globally pair-injective
f,g whenever the six-ID source topology is B/B-overlap; the exact signed
weight depends only on the source-column two-factor dual graphs.

Positive weights do not prove existence of Omega(s^6) sixsets and are not
a professional acceptance of the global HYP-105 Branch A chain.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations, product
from math import comb
from pathlib import Path
import hashlib
import json

ROOT_STATUS = "OPEN_WITH_FORMAL_BLOCKER"
FIELD = 5
SIGN_MASKS = tuple(sum(1 << i for i in (0,) + t)
                   for t in combinations(range(1, 6), 2))


def column_palette():
    """Derive ALL 51 checksum-four GF(5)* column assignments."""
    rows = tuple(p for p in product(range(1, FIELD), repeat=4)
                 if sum(p) % FIELD == 4)
    if len(rows) != 51 or len(set(rows)) != 51:
        raise AssertionError("nonzero GF5 column palette not 51")
    return rows


def four_cycles(vertices):
    """All THREE simple unoriented C4 edge sets on four named vertices."""
    vertices = tuple(sorted(vertices))
    if len(vertices) != 4 or len(set(vertices)) != 4:
        raise ValueError("four distinct column vertices required")
    first = vertices[0]
    out = {
        tuple(sorted(tuple(sorted((v[j], v[(j+1) % 4])))
                     for j in range(4)))
        for v in ((first,) + rest for rest in permutations(vertices[1:]))
    }
    if len(out) != 3:
        raise AssertionError("C4 labeled combinatorial completeness failed")
    return tuple(sorted(out))


def bbo_templates():
    """All B/B-overlap two-factor pairs up to simultaneous SIX-column labels.

    WLOG the twice-used left original point occupies columns 0,1,
    the twice-used right original line occupies columns 0,2.
    The remaining four columns per factor form a simple C4, 3 choices
    independently on left/right = precisely NINE templates.
    Physical coordinate symbols are edges of the 6-column dual graph;
    repeated original pair contributes TWO distinct parallel edges.
    """
    left = four_cycles((2,3,4,5))
    right = four_cycles((1,3,4,5))
    out = []
    for i, L in enumerate(left):
        for j, R in enumerate(right):
            edges = ((0,1),(0,1)) + L + ((0,2),(0,2)) + R
            out.append((i,j,edges))
    if len(out) != 9 or len({z[2] for z in out}) != 9:
        raise AssertionError("B/B-overlap original two-factor coverage false")
    return tuple(out)


def aligned_d6_edges():
    """One dual C6 on source column IDs, twice (left and right blocks)."""
    cycle = ((0,1),(1,2),(2,3),(3,4),(4,5),(0,5))
    return cycle + cycle


def _validate_flow_graph(edges, plus_mask):
    edges = tuple(tuple(e) for e in edges)
    if (type(plus_mask) is not int or not 0 <= plus_mask < 64
            or plus_mask.bit_count() != 3):
        raise ValueError("exact balanced 3+3 sign mask required")
    if (len(edges) != 12 or
            any(len(e) != 2 or any(type(x) is not int or x < 0 or x > 5
                                   for x in e) or e[0] >= e[1] for e in edges)):
        raise ValueError("12 nonloop physical coordinates as dual edges required")
    degree = Counter(x for e in edges for x in e)
    if len(degree) != 6 or any(degree[i] != 4 for i in range(6)):
        raise ValueError("six original support-four columns required")
    return edges


def flow_count_by_tree_chords(edges, plus_mask):
    """Independent integer GF5 flow count; no Fourier or inclusion-exclusion.

    At each of 12 physical coordinates, exact signed cancellation gives
    x_(column i)=-x_(column j). Assign an oriented nonzero edge variable
    t_e. The column checksum-four condition becomes an incidence-system
    B*t = b, with b_i = 4*sign_i in F5.
    Pick a deterministic spanning forest. All non-tree edges (chords)
    are arbitrary NONZERO field variables, and tree edge values are
    uniquely forced by leaf elimination. Each permitted chord assignment
    contributes exactly one original six-column 51-palette configuration.
    Parallel dual edges are distinct physical coordinate variables.
    """
    edges = _validate_flow_graph(edges, plus_mask)
    dsu = list(range(6))

    def root(x):
        while dsu[x] != x:
            x = dsu[x]
        return x

    tree = []
    chords = []
    for u,v in edges:
        a,b = root(u),root(v)
        if a != b:
            dsu[b] = a
            tree.append((u,v))
        else:
            chords.append((u,v))
    adj = [[] for _ in range(6)]
    for u,v in tree:
        adj[u].append(v)
        adj[v].append(u)
    parent = [-1]*6
    visit = []
    for seed in range(6):
        if parent[seed] != -1:
            continue
        parent[seed] = seed
        stack = [seed]
        while stack:
            x = stack.pop()
            visit.append(x)
            for y in adj[x]:
                if parent[y] == -1:
                    parent[y] = x
                    stack.append(y)
    if len(visit) != 6 or len(tree) + len(chords) != 12:
        raise AssertionError("spanning forest not complete")
    bvec = [4 if plus_mask & (1 << i) else 1 for i in range(6)]
    components = defaultdict(list)
    for i in range(6):
        components[root(i)].append(i)
    if any(sum(bvec[i] for i in v) % 5 for v in components.values()):
        return 0

    count = 0
    for values in product((1,2,3,4), repeat=len(chords)):
        remaining = bvec.copy()
        for (u,v),t in zip(chords,values):
            remaining[u] = (remaining[u]-t) % FIELD
            remaining[v] = (remaining[v]+t) % FIELD
        good = True
        for v in reversed(visit):
            par = parent[v]
            if par == v:
                if remaining[v] != 0:
                    good = False
                    break
                continue
            # At v the oriented tree edge has coefficient +/-1,
            # hence its variable is nonzero iff residual demand is nonzero.
            if remaining[v] == 0:
                good = False
                break
            remaining[par] = (remaining[par] + remaining[v]) % FIELD
        if good:
            count += 1
    if not 0 <= count <= 51**6:
        raise AssertionError("invalid exact nowherezero GF5 original coefficient")
    return count


def flow_count_direct_51_palette_mitm(edges, plus_mask):
    """A genuinely different oracle: all 51 explicit rows, 51^3 join.

    Split the six actual columns into 3+3, enumerate all 51^3 choices on
    EACH half, store the weighted physical-coordinate residue signature,
    and join complementary signatures. No spanning trees, chords, graph
    rank, dual Fourier or inclusion-exclusion are used in this oracle.
    """
    edges = _validate_flow_graph(edges, plus_mask)
    supports = [[] for _ in range(6)]
    for coordinate, (u,v) in enumerate(edges):
        supports[u].append(coordinate)
        supports[v].append(coordinate)
    if any(len(s) != 4 for s in supports):
        raise AssertionError("non-four-support GF5 column")
    palettes = []
    for i in range(6):
        sign = 1 if plus_mask & (1 << i) else 4
        options = []
        for values in column_palette():
            arr = [0]*12
            for j, value in zip(supports[i],values):
                arr[j] = (value*sign) % FIELD
            options.append(bytes(arr))
        palettes.append(options)

    def half_hist(start):
        first, second, third = palettes[start:start+3]
        mass = Counter()
        for a in first:
            for b in second:
                temp = tuple((u+v) % FIELD for u,v in zip(a,b))
                for c in third:
                    signature = bytes((u+v) % FIELD for u,v in zip(temp,c))
                    mass[signature] += 1
        if sum(mass.values()) != 51**3:
            raise AssertionError("direct GF5 half-palette incomplete")
        return mass

    left = half_hist(0)
    right = half_hist(3)
    total = sum(count * right.get(bytes((-z) % FIELD for z in key),0)
                for key,count in left.items())
    if not 0 <= total <= 51**6:
        raise AssertionError("GF5 direct 51-palette join count invalid")
    return total


def template_census():
    signs = SIGN_MASKS
    results = []
    for ix,iy,edges in bbo_templates():
        values = tuple(flow_count_by_tree_chords(edges,m) for m in signs)
        results.append({"left_C4":ix,"right_C4":iy,
                        "signed_weights":values,
                        "minimum":min(values),"sum_ten_signs":sum(values)})
    d6_edges = aligned_d6_edges()
    d6_values = tuple(flow_count_by_tree_chords(d6_edges,m) for m in signs)
    # Since the aligned D6 has six edge owners in one factor C6,
    # its designated alternate sign uses source columns 0,2,4 positive.
    d6_alternating_mask = sum(1 << j for j in (0,2,4))
    designated = d6_values[signs.index(d6_alternating_mask)]
    if (len(results) != 9 or len(signs) != 10 or
            any(len(z["signed_weights"]) != 10 for z in results)):
        raise AssertionError("all universal six-ID template events not enumerated")
    digest = hashlib.sha256(json.dumps(
        {"BBo":[z["signed_weights"] for z in results],
         "D6":d6_values},separators=(",",":")).encode()).hexdigest()
    independent_mitm = {
        "BBo_min_example":flow_count_direct_51_palette_mitm(
            bbo_templates()[0][2],7),
        "BBo_other_sign":flow_count_direct_51_palette_mitm(
            bbo_templates()[0][2],25),
        "D6_alternating":flow_count_direct_51_palette_mitm(
            d6_edges,d6_alternating_mask),
        "D6_other_sign":flow_count_direct_51_palette_mitm(d6_edges,7),
    }
    if (independent_mitm["BBo_min_example"] != results[0]["signed_weights"][0]
            or independent_mitm["BBo_other_sign"] != results[0]["signed_weights"][7]
            or independent_mitm["D6_alternating"] != designated
            or independent_mitm["D6_other_sign"] != d6_values[0]):
        raise AssertionError("GF5 independent 51-palette vs tree-chord mismatch")
    return {
        "schema":"mathlab.hyp105.original-gf5-tree-flow-templates.v1",
        "templates_BBo":results,
        "balanced_sign_masks":signs,
        "BBo_signed_events":9*10,
        "BBo_minimum_per_sign":min(z["minimum"] for z in results),
        "BBo_minimum_ten_sign_total":min(z["sum_ten_signs"] for z in results),
        "BBo_maximum_ten_sign_total":max(z["sum_ten_signs"] for z in results),
        "BBo_total_sign_sum_distribution":dict(sorted(Counter(
            z["sum_ten_signs"] for z in results).items())),
        "D6_signed_weights":d6_values,
        "D6_alternating_mask":d6_alternating_mask,
        "D6_alternating_signed_weight":designated,
        "D6_ten_sign_total":sum(d6_values),
        "D6_minimum_per_sign":min(d6_values),
        "independent_full_51_palette_MITM":independent_mitm,
        "exact_all_template_weights_SHA256":digest,
        "full_original_branch_A_accepted":False,
    }


def original_case(h,scheme,shift=0):
    """Minimal honest W32/W34 original source and complete f,g injections."""
    from hyp105_full_physical_degree_tail import genuine_source
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    if type(h) is not int or h not in (1,2) or type(shift) is not int:
        raise ValueError("real original W32/W34 finite oracle parameters required")
    s,V,flags = genuine_source(h)
    model = pair_labeled_symplectic(h,scheme)
    f = tuple(map(tuple,model["left_labels"]))
    g = tuple(map(tuple,model["right_labels"]))
    if shift:
        g = g[shift % V:] + g[:shift % V]
    a = 2
    while comb(a,2) < V:
        a += 1
    palette = set(combinations(range(a),2))
    if (len(f)!=V or len(g)!=V or len(set(f))!=V or len(set(g))!=V
            or any(p not in palette for p in f+g)
            or len(flags)!=(s+1)*V or len(set(flags))!=len(flags)):
        raise ValueError("not complete genuine ORIGINAL GQ with injected f,g")
    return {"s":s,"V":V,"a":a,"flags":tuple(flags),"f":f,"g":g}


def source_dual_edges(case,ids):
    """12 physical-coordinate dual edges on the six actual original columns.

    Return None for any source sixset without exactly six distinct physical
    coordinates used TWICE in each typed factor. The resulting edges
    preserve the identities of six named ORIGINAL incidence flags.
    """
    flags,f,g=case["flags"],case["f"],case["g"]
    ids=tuple(ids)
    if (len(ids)!=6 or len(set(ids))!=6 or
            any(type(i) is not int or not 0<=i<len(flags) for i in ids)):
        raise ValueError("six DISTINCT actual original incidence IDs required")
    duals=[]
    for typ in (0,1):
        usage=defaultdict(list)
        for j,i in enumerate(ids):
            point,line=flags[i]
            for sym in (f[point] if typ==0 else g[line]):
                usage[sym].append(j)
        if len(usage)!=6 or any(len(occ)!=2 for occ in usage.values()):
            return None
        duals.append(tuple(tuple(sorted(pair))
                           for _,pair in sorted(usage.items())))
    return tuple(duals[0]+duals[1]), tuple(duals[0]), tuple(duals[1])


def _connected_cycle4(edges,nodes):
    if len(edges)!=4 or len(set(edges))!=4:
        return False
    nodes=set(nodes)
    if len(nodes)!=4 or any(u not in nodes or v not in nodes for u,v in edges):
        return False
    g=defaultdict(set)
    for u,v in edges:g[u].add(v);g[v].add(u)
    if any(len(g[x])!=2 for x in nodes):
        return False
    seen={next(iter(nodes))}
    stack=list(seen)
    while stack:
        for w in g[stack.pop()]:
            if w not in seen:seen.add(w);stack.append(w)
    return len(seen)==4


def _connected_cycle6(edges):
    if len(edges)!=6 or len(set(edges))!=6:
        return False
    adj=defaultdict(set)
    for u,v in edges:adj[u].add(v);adj[v].add(u)
    if len(adj)!=6 or any(len(adj[i])!=2 for i in range(6)):
        return False
    reached={0};queue=[0]
    while queue:
        for n in adj[queue.pop()]:
            if n not in reached:reached.add(n);queue.append(n)
    return len(reached)==6


def six_source_class(case,ids):
    """Original source-only class using original IDs and both actual duals."""
    dual=source_dual_edges(case,ids)
    if dual is None:return None
    edges,left,right=dual
    if (_connected_cycle6(left) and _connected_cycle6(right)
            and Counter(left)==Counter(right)):
        # SOURCE D6 requires original point and line owners separately
        # distinct, rather than only two physical dual six-cycles.
        flags=case["flags"]
        if (len({flags[i][0] for i in ids})==6 and
                len({flags[i][1] for i in ids})==6):
            return "D6"
    flags=case["flags"]
    points=Counter(flags[i][0] for i in ids)
    lines=Counter(flags[i][1] for i in ids)
    if (len(points)!=5 or len(lines)!=5 or
            sorted(points.values())!=[1,1,1,1,2] or
            sorted(lines.values())!=[1,1,1,1,2]):
        return None
    p=next(k for k,v in points.items() if v==2)
    ell=next(k for k,v in lines.items() if v==2)
    if sum(flags[i]==(p,ell) for i in ids)!=1:
        return None
    repeated=[]
    for factor in (left,right):
        freq=Counter(factor)
        same=[pair for pair,n in freq.items() if n==2]
        if len(same)!=1 or len(freq)!=5:
            return None
        pair=same[0]
        rest=[edge for edge in factor if edge!=pair]
        if not _connected_cycle4(rest,set(range(6))-set(pair)):
            return None
        repeated.append(set(pair))
    if len(repeated[0]&repeated[1])!=1:
        return None
    return "B/B-overlap"


def original_six_GF5_weights(case,ids):
    klass=six_source_class(case,ids)
    if klass not in ("D6","B/B-overlap"):
        return None
    edges, left, right=source_dual_edges(case,ids)
    weights=tuple(flow_count_by_tree_chords(edges,mask) for mask in SIGN_MASKS)
    if klass=="B/B-overlap":
        if min(weights)<5175 or sum(weights)<53526:
            raise AssertionError("actual true ORIGINAL BBo violates template GF5 floor")
    else:
        if sum(weights)!=54162 or min(weights)<5265:
            raise AssertionError("actual true ORIGINAL D6 changed ten-sign flow total")
    return {"class":klass,"source_six_incidence_IDs":list(ids),
            "ten_balanced_sign_exact_GF5_weights":list(weights),
            "minimum_one_sign":min(weights),
            "all_ten_sign_total":sum(weights)}


def exhaustive_W32_original_BBo_GF5(scheme):
    """All 10,935 true ORIGINAL LEFT-B sixsets, historical BBo subset exact."""
    c=original_case(1,scheme)
    f=c["f"]
    if c["a"]!=6 or c["V"]!=15:
        raise AssertionError("true original W32 small 15-source model changed")
    inv={pair:p for p,pair in enumerate(f)}
    bypoint=defaultdict(list)
    for i,(p,ell) in enumerate(c["flags"]):
        bypoint[p].append(i)
    accepted=[]
    candidates=0
    for p in range(15):
        remainder=tuple(sorted(set(range(6))-set(f[p])))
        for c4 in four_cycles(remainder):
            original_points=tuple(inv[e] for e in c4)
            for doubled in combinations(bypoint[p],2):
                for singles in product(*(bypoint[q] for q in original_points)):
                    ids=tuple(sorted(doubled+singles))
                    candidates+=1
                    if six_source_class(c,ids)=="B/B-overlap":
                        accepted.append(ids)
    if candidates!=10935 or len(set(accepted))!=len(accepted):
        raise AssertionError("genuine W32 source LEFT-B exhaustive census broken")
    witnesses=[]
    mins=[];sums=[]
    for ids in accepted:
        result=original_six_GF5_weights(c,ids)
        if result is None:
            raise AssertionError("original BBo six-ID disappeared during GF5 count")
        mins.append(result["minimum_one_sign"])
        sums.append(result["all_ten_sign_total"])
        if len(witnesses)<3:witnesses.append(result)
    return {"s":2,"scheme":scheme,
            "all_original_LEFT_B_candidate_source_sixsets":candidates,
            "complete_original_BBo_sixsets":len(accepted),
            "least_actual_original_BBo_signed_weight":min(mins) if mins else None,
            "least_actual_original_BBo_all_signs_total":min(sums) if sums else None,
            "first_three_genuine_source_GF5_witnesses":witnesses}


def canonical_original_GF5_report():
    root=Path(__file__).parent
    templates=template_census()
    low=json.loads((root/"hyp105_original_lowtail_alln_energy_certificates.json").read_text())
    heavy=json.loads((root/"hyp105_original_deletion_adaptive_heavy_tail_certificates.json").read_text())
    bbo_full=[exhaustive_W32_original_BBo_GF5(z) for z in ("lex","reverse-line")]
    w34=[]
    for z in low["genuine_true_original_cases"]:
        if z["s"]!=4:continue
        c=original_case(2,z["scheme"])
        allsets=z["real_positive_original_BBo_six_IDs"]
        idx=sorted({0,len(allsets)//2,len(allsets)-1})
        selected=[]
        for j in idx:
            ids=tuple(allsets[j])
            if set(ids)&set(z["deleted_original_flag_IDs"]):
                raise AssertionError("deleted ORIGINAL flag ID accepted")
            selected.append(original_six_GF5_weights(c,ids))
        w34.append({"s":4,"scheme":z["scheme"],"actual_original_BBo_samples":selected})
    d6=[]
    for z in heavy["genuine_source_cases"]:
        if z.get("empty_tail") or z["s"]!=4:continue
        c=original_case(2,z["scheme"])
        for ids in z["true_original_D6_six_flag_IDs_selected"]:
            if set(ids)&set(z["deleted_original_flag_IDs"]):
                raise AssertionError("deleted original D6 source witness")
            result=original_six_GF5_weights(c,ids)
            if result is None or result["class"]!="D6":
                raise AssertionError("true original heavy D6 not recognized")
            d6.append(dict(s=4,scheme=z["scheme"],**result))
    if [x["complete_original_BBo_sixsets"] for x in bbo_full]!=[8,7]:
        raise AssertionError("genuine W32 original BBo class count mismatch")
    if len(w34)!=2 or len(d6)!=3:
        raise AssertionError("missing genuine W34 original positive six-ID source oracles")
    return {"schema":"mathlab.hyp105.original-gf5-tree-flow-referee.v1",
            "status":ROOT_STATUS,
            "allh_structural_GF5_templates_checked":True,
            "full_original_Branch_A_accepted":False,
            "uniform_BBo_per_sign_lower":templates["BBo_minimum_per_sign"],
            "uniform_BBo_all_ten_sign_lower":templates["BBo_minimum_ten_sign_total"],
            "uniform_D6_designated_alternating_flow":templates["D6_alternating_signed_weight"],
            "uniform_D6_all_ten_sign_total":templates["D6_ten_sign_total"],
            "template_evidence":templates,
            "exhaustive_actual_W32_BBo_GF5":bbo_full,
            "actual_W34_BBo_GF5_witnesses":w34,
            "actual_W34_D6_GF5_witnesses":d6}


if __name__=="__main__":
    print("AA4_ORIGINAL_GF5_TREE_FLOW_CERTIFICATE="+json.dumps(
        canonical_original_GF5_report(),sort_keys=True,separators=(",",":")),
        flush=True)
