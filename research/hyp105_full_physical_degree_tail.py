"""Exact finite original-ID selector for HYP-105-FULL-PHYSICAL-DEGREE-TAIL.md.

Checks true W(3,2)/W(3,4) sources; it does not computationally prove the
all-h tail theorem or the root seven-class claim. No Mathlab file is edited.
"""
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, product
import json
from pathlib import Path
import sys

from hyp105_b1_symplectic import symplectic_gq
from hyp105_physical_degree_energy import minimal_alphabet, _verify_typed_injections
from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked


@lru_cache(None)
def genuine_source(power):
    if type(power) is not int or power not in (1, 2):
        raise ValueError("finite source oracle supports h=1,2 only")
    _, points, lines, flags = symplectic_gq(power)
    s = 1 << power
    V = (s+1)*(s*s+1)
    assert len(points) == len(lines) == V and len(flags) == V*(s+1)
    pencils = [set() for _ in points]
    for p,ell in flags: pencils[p].add(ell)
    assert all(len(z) == s+1 for z in pencils)
    assert all(len(pencils[p] & pencils[q]) <= 1 for p,q in combinations(range(V),2))
    # Independent original GQ projection check on the entire true geometry.
    for p in range(V):
        for ell,line in enumerate(lines):
            if ell not in pencils[p]:
                assert sum(bool(pencils[p] & pencils[q]) for q in line) == 1
    return s,V,tuple(flags)


def diagonals(flag, f, g):
    p,ell = flag
    x,xx = f[p]; y,yy = g[ell]
    return tuple(tuple(sorted(e)) for e in (((x,y),(xx,yy)),((x,yy),(xx,y))))


def physical(ids, flags, f, g):
    adjacency, provenance = defaultdict(set),{}
    for i in ids:
        for edge in diagonals(flags[i],f,g):
            assert edge not in provenance
            provenance[edge] = i
            u,v = edge
            adjacency[u].add(v); adjacency[v].add(u)
    return dict(adjacency),provenance


def conflict_graph(ids, flags, f, g):
    buckets = defaultdict(list)
    for i in ids:
        p,ell = flags[i]
        for y in g[ell]: buckets["point",p,y].append(i)
        for x in f[p]: buckets["line",ell,x].append(i)
    adjacency = {i:set() for i in ids}
    mf = mg = 0
    for key,members in buckets.items():
        pairs = tuple(combinations(members,2))
        if key[0] == "point": mg += len(pairs)
        else: mf += len(pairs)
        for i,j in pairs:
            assert j not in adjacency[i], "source conflict counted twice"
            adjacency[i].add(j); adjacency[j].add(i)
    # Independent source-pair-major oracle, without coordinate buckets.
    direct,dmf,dmg = set(),0,0
    fs,gs = list(map(set,f)),list(map(set,g))
    for i,j in combinations(ids,2):
        p,ell = flags[i]; q,m = flags[j]
        left = p == q and bool(gs[ell] & gs[m])
        right = ell == m and bool(fs[p] & fs[q])
        assert not (left and right)
        dmg += left; dmf += right
        if left or right: direct.add((i,j))
    assert direct == {(i,j) for i in adjacency for j in adjacency[i] if i<j}
    assert (mf,mg) == (dmf,dmg) and len(direct) == mf+mg
    return adjacency,mf,mg


def min_degree_independent(adjacency):
    cw = sum((Fraction(1,len(ns)+1) for ns in adjacency.values()),Fraction())
    remaining,chosen = set(adjacency),[]
    while remaining:
        v = min(remaining,key=lambda u:(len(adjacency[u] & remaining),u))
        chosen.append(v)
        remaining.difference_update((adjacency[v] & remaining) | {v})
    assert len(chosen) >= cw
    assert all(j not in adjacency[i] for i,j in combinations(chosen,2))
    return tuple(sorted(chosen)),cw


def coordinate_cut(ids, labels, endpoint, flags, a):
    colors = {}
    def doubled_expectation():
        score = 0
        for i in ids:
            x,y = labels[flags[i][endpoint]]
            score += 2*(colors[x] != colors[y]) if x in colors and y in colors else 1
        return score
    for x in range(a):
        colors[x] = 0; score0 = doubled_expectation()
        colors[x] = 1; score1 = doubled_expectation()
        colors[x] = int(score1 > score0)
    retained = tuple(i for i in ids if colors[labels[flags[i][endpoint]][0]] !=
                     colors[labels[flags[i][endpoint]][1]])
    assert 2*len(retained) >= len(ids)
    return retained,tuple(colors[x] for x in range(a))


def verify_selected(ids, flags, f, g, lc, rc):
    resources = set()
    for i in ids:
        p,ell = flags[i]
        assert lc[f[p][0]] != lc[f[p][1]] and rc[g[ell][0]] != rc[g[ell][1]]
        for z in [("point",p,y) for y in g[ell]] + [("line",ell,x) for x in f[p]]:
            assert z not in resources
            resources.add(z)
    adjacency,provenance = physical(ids,flags,f,g)
    for v,ns in adjacency.items():
        assert len({w[0] for w in ns}) == len({w[1] for w in ns}) == len(ns)
    nb3 = 0
    for v0 in adjacency:
        for v1 in adjacency[v0]:
            for v2 in adjacency[v1]-{v0}:
                for v3 in adjacency[v2]-{v1}:
                    path = (v0,v1,v2,v3)
                    assert len({v[0] for v in path}) == len({v[1] for v in path}) == 4
                    nb3 += 1
    sixsets = set()
    cycles = 0
    def visit(path):
        nonlocal cycles
        if len(path) == 6:
            if path[0] not in adjacency[path[-1]] or path[1] >= path[-1]: return
            assert len({v[0] for v in path}) == len({v[1] for v in path}) == 6
            original = tuple(sorted(provenance[tuple(sorted((path[i],path[(i+1)%6])))] for i in range(6)))
            assert len(set(original)) == len({flags[i][0] for i in original}) == len({flags[i][1] for i in original}) == 6
            assert original not in sixsets
            assert classify_seven_prechecked(original,f,g,flags) == "D6"
            sixsets.add(original); cycles += 1
            return
        for w in adjacency[path[-1]]:
            if w > path[0] and w not in path: visit(path+(w,))
    for root in sorted(adjacency): visit((root,))
    return adjacency,provenance,{"ordinary_C6":cycles,"accepted_original_D6":len(sixsets),
                                "oriented_NB3":nb3,"all_NB3_coordinate_proper":True}


def finite_tail_selector(power, f, g, threshold=Fraction(1), *, source_subset=None):
    s,V,flags = genuine_source(power)
    a = minimal_alphabet(V)
    f,g = tuple(map(tuple,f)),tuple(map(tuple,g))
    _verify_typed_injections(a,V,f,g)
    threshold = Fraction(threshold)
    if threshold <= 0: raise ValueError("positive T required")
    full,full_provenance = physical(range(len(flags)),flags,f,g)
    heavy = {v for v in full if len(full[v]) > threshold*s}
    tail_edges = {edge for edge in full_provenance if set(edge) & heavy}
    witnesses = {}
    for i in range(len(flags)):
        options = [edge for edge in diagonals(flags[i],f,g) if set(edge) & heavy]
        if options: witnesses[i] = min(options)
    ids = tuple(sorted(witnesses))
    if source_subset is not None:
        requested = tuple(source_subset)
        if len(set(requested)) != len(requested) or any(type(i) is not int or i not in witnesses for i in requested):
            raise ValueError("subset IDs must be distinct genuine IDs with heavy witness edges")
        ids = tuple(sorted(requested))
    if source_subset is None: assert 2*len(ids) >= len(tail_edges)
    adjacency,mf,mg = conflict_graph(ids,flags,f,g)
    C_s = (s-1)*V+(s*s+1)*(a-1)
    assert max(mf,mg) <= C_s
    independent,cw = min_degree_independent(adjacency)
    L,E = len(ids),mf+mg
    assert len(independent)*(2*E+L) >= L*L
    left,lc = coordinate_cut(independent,f,0,flags,a)
    retained,rc = coordinate_cut(left,g,1,flags,a)
    assert 4*len(retained)*(4*C_s+L) >= L*L
    selected,provenance,cycles = verify_selected(retained,flags,f,g,lc,rc)
    assert len(provenance) == 2*len(retained)
    sides = [[],[]]
    for i in retained:
        edge = witnesses[i]
        assert provenance.get(edge) == i, "heavy witness disappeared"
        endpoint = min(set(edge) & heavy)
        sides[lc[endpoint[0]]].append(i)
    side = int(len(sides[1]) > len(sides[0]))
    chunk_report = None
    if retained:
        R = {v for v in heavy if lc[v[0]] == side}
        Y = sorted(v for v in selected if lc[v[0]] != side)
        r = len(R)
        chunks = [Y[i:i+r] for i in range(0,len(Y),r)]
        def edge_count(chunk): return sum(len(selected.get(v,set()) & set(chunk)) for v in R)
        chunk = max(chunks,key=lambda z:(edge_count(z),tuple(z)))
        edges,nvertices = edge_count(chunk),r+len(chunk)
        assert 2*len(sides[side]) >= len(retained)
        assert Fraction(edges,nvertices) >= Fraction(len(retained),8*a*a)
        chunk_report = {"heavy_side_vertices":r,"opposite_chunks":len(chunks),
                        "chunk_vertices":nvertices,"chunk_edges":edges,
                        "density_numerator":edges,"density_denominator":nvertices}
    return {"s":s,"V":V,"a":a,"T_numerator":threshold.numerator,"T_denominator":threshold.denominator,
            "full_physical_edges":len(full_provenance),"heavy_vertices":len(heavy),"tail_edges":len(tail_edges),
            "input_original_ids":L,"conflict_edges":E,"M_f_restricted":mf,"M_g_restricted":mg,
            "exact_source_book_bound":C_s,"Caro_Wei_numerator":cw.numerator,"Caro_Wei_denominator":cw.denominator,
            "independent_original_ids":len(independent),"after_left_cut":len(left),
            "retained_original_ids":len(retained),"retained_source_ids":list(retained),
            "retained_physical_edges":len(provenance),"preserved_heavy_witnesses":len(retained),
            "balanced_chunk":chunk_report,**cycles,
            "all_h_tail_theorem_numerically_proved":False,"root_seven_lower_proved":False}


def planted_original_k44():
    _,V,flags = genuine_source(2)
    bypoint = [[] for _ in range(V)]
    for p,ell in flags: bypoint[p].append(ell)
    owner = {}
    def augment(p,seen):
        for ell in bypoint[p]:
            if ell in seen: continue
            seen.add(ell)
            if ell not in owner or augment(owner[ell],seen):
                owner[ell] = p
                return True
        return False
    assert all(augment(p,set()) for p in range(16))
    original = sorted((p,ell) for ell,p in owner.items())
    f,g = [None]*V,[None]*V
    for (hub,free),(p,ell) in zip(product(range(4),range(4,8)),original):
        f[p] = g[ell] = (hub,free)
    for labels in (f,g):
        used = {x for x in labels if x is not None}
        unused = iter(pair for pair in combinations(range(14),2) if pair not in used)
        for i in range(V):
            if labels[i] is None: labels[i] = next(unused)
    lookup = {flag:i for i,flag in enumerate(flags)}
    return tuple(f),tuple(g),tuple(lookup[z] for z in original)


def exact_bad_endpoint_population(power, f, g):
    """Two independent exact methods: source books vs all true projections."""
    s,V,flags = genuine_source(power)
    f,g = tuple(map(tuple,f)),tuple(map(tuple,g))
    _verify_typed_injections(minimal_alphabet(V),V,f,g)
    _,mf,mg = conflict_graph(tuple(range(len(flags))),flags,f,g)
    bypoint,byline = [set() for _ in range(V)],[set() for _ in range(V)]
    for p,ell in flags:
        bypoint[p].add(ell); byline[ell].add(p)
    left = right = both = total = 0
    fs,gs = list(map(set,f)),list(map(set,g))
    for q in range(V):
        for r in range(V):
            if r in bypoint[q]: continue
            candidates = [(p,bypoint[p] & bypoint[q]) for p in byline[r]
                          if bypoint[p] & bypoint[q]]
            assert len(candidates) == 1
            p,connecting = candidates[0]
            assert len(connecting) == 1
            ell = next(iter(connecting))
            L,R = bool(fs[p] & fs[q]),bool(gs[ell] & gs[r])
            left += L; right += R; both += L and R; total += 1
    assert left == 2*s*mf and right == 2*s*mg
    assert total == V*(V-(s+1))
    C_s = (s-1)*V+(s*s+1)*(minimal_alphabet(V)-1)
    union = left+right-both
    assert union <= 4*s*C_s
    return {"s":s,"M_f":mf,"M_g":mg,"left_endpoint_bad":left,
            "right_endpoint_bad":right,"both_endpoint_bad":both,
            "union_endpoint_bad":union,"all_nonincident_endpoint_pairs":total,
            "union_spectral_upper":4*s*C_s,
            "exact_2s_book_identities_verified":True,
            "path_weighted_endpoint_mass_bounded":False}


def report():
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    cases,endpoint_cases = [],[]
    for power in (1,2):
        for scheme in ("lex","reverse-line"):
            model = pair_labeled_symplectic(power,scheme)
            endpoint_cases.append({"map":f"W3{1<<power}-{scheme}",
                **exact_bad_endpoint_population(power,model["left_labels"],model["right_labels"])})
            for threshold in (Fraction(1,2),Fraction(1),Fraction(2)):
                cases.append({"map":f"W3{1<<power}-{scheme}",**finite_tail_selector(
                    power,model["left_labels"],model["right_labels"],threshold)})
    certificate = json.loads(Path(sys.modules["hyp105_physical_degree_energy"].__file__).with_name(
        "hyp105_w34_adversarial_certificate.json").read_text())
    for threshold in (Fraction(1),Fraction(2),Fraction(4)):
        cases.append({"map":"W34-adversarial",**finite_tail_selector(2,certificate["f"],certificate["g"],threshold)})
    endpoint_cases.append({"map":"W34-adversarial",
        **exact_bad_endpoint_population(2,certificate["f"],certificate["g"])})
    f,g,ids = planted_original_k44()
    planted = finite_tail_selector(2,f,g,Fraction(1,4),source_subset=ids)
    assert planted["retained_original_ids"] == 16 and planted["accepted_original_D6"] == 96
    cases.append({"map":"W34-protected-true-K44",**planted})
    endpoint_cases.append({"map":"W34-protected-true-K44",**exact_bad_endpoint_population(2,f,g)})
    return {"scope":"exact finite original-ID selector/provenance evidence; no root closure",
            "cases":cases,"endpoint_cases":endpoint_cases,"all_h_tail_proof":"HYP-105-FULL-PHYSICAL-DEGREE-TAIL.md",
            "full_palette_GF5_D6_structural_class_checked":True,"root_seven_lower_proved":False}


if __name__ == "__main__":
    result = report()
    directory = Path(sys.argv[1]) if len(sys.argv)>1 else Path("/tmp/hyp105-full-degree-tail")
    directory.mkdir(parents=True, exist_ok=True)
    output = directory / "full_physical_degree_tail_results.json"
    output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"cases":len(result["cases"]),"protected_original_D6":result["cases"][-1]["accepted_original_D6"],
                      "output":str(output),"root_seven_lower_proved":False},sort_keys=True))
