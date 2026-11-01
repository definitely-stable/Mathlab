"""AA4-D6INV: independent CANONICAL ORIGINAL six-ID -> physical C6 inverse.

The rainbow C6 <-> ORIGINAL D6 statement is PRE-EXISTING (#652).
NEW: explicit edge-ID-labelled dual 6-cycle reconstruction independent of
physical cycle DFS, source-flag ownership and selected graph, with rigorous
no-cherry/two-cut ALL-h ordinary-C6 -> ORIGINAL D6 lifting verification.

Requires only actual separately pair-injective f,g, genuine original flag
incidence IDs for W32/W34 finite verification. Combinatorial inverse
works for arbitrary underlying simple incidence relation, all h.
"""
from collections import Counter, defaultdict
from itertools import combinations
from math import comb

from hyp105_full_physical_degree_tail import genuine_source


def _typed_source(flags, f, g):
    """Check unique abstract ORIGINAL IDs and distinct typed factor labels."""
    flags=tuple(tuple(a) for a in flags)
    f=tuple(tuple(a) for a in f)
    g=tuple(tuple(a) for a in g)
    if (not f or not g or len(set(flags))!=len(flags) or
        any(type(p) is not int or type(l) is not int or
            p<0 or p>=len(f) or l<0 or l>=len(g) for p,l in flags)):
        raise ValueError("genuine original incidence IDs must be distinct and typed")
    if (any(len(e)!=2 or e[0]>=e[1] or e[0]<0 or
            type(e[0]) is not int or type(e[1]) is not int
            for e in f+g)
        or len(set(f))!=len(f) or len(set(g))!=len(g)):
        raise ValueError("complete original factor pair maps must be separately injective")
    return flags,f,g


def _canonical_vertex_cycle(cycle):
    """Unoriented unrooted physical simple cycle unique canonical order."""
    x=tuple(cycle)
    if len(x)!=6 or len(set(x))!=6:
        raise ValueError("a simple physical six-cycle required")
    out=[]
    for z in (x,x[::-1]):
        for k in range(6):
            out.append(z[k:]+z[:k])
    return min(out)


def physical_original_edge_graph(flags,f,g,ids=None,sector=None,
                                 left_colors=None,right_colors=None):
    """Actual original BOTH flag diagonals (or an explicitly selected sector).

    The unpaired sector contains exactly ONE physical edge per retained
    genuine ORIGINAL flag, never clones a flag source ID.
    """
    flags,f,g=_typed_source(flags,f,g)
    I=tuple(range(len(flags))) if ids is None else tuple(ids)
    if len(I)!=len(set(I)) or any(type(i) is not int or i<0 or i>=len(flags) for i in I):
        raise ValueError("source subset must consist of distinct actual ORIGINAL IDs")
    if sector is not None and sector not in (0,1):
        raise ValueError("physical parity sector must be 0,1 or None")
    if sector is not None:
        if (left_colors is None or right_colors is None or
            any(type(c) is not int or c not in (0,1) for c in left_colors) or
            any(type(c) is not int or c not in (0,1) for c in right_colors)):
            raise ValueError("both exact binary typed cuts required for sector selection")
    owners={}
    graph=defaultdict(set)
    for i in I:
        p,l=flags[i]; x,z=f[p]; y,w=g[l]
        if sector is not None:
            if (max(x,z)>=len(left_colors) or max(y,w)>=len(right_colors) or
                left_colors[x]==left_colors[z] or right_colors[y]==right_colors[w]):
                raise ValueError("selected original source flag not bichromatic on both cuts")
        count=0
        for u,v in (((x,y),(z,w)),((x,w),(z,y))):
            if sector is not None:
                if (left_colors[u[0]]^right_colors[u[1]])!=sector:continue
                if (left_colors[v[0]]^right_colors[v[1]])!=sector:
                    raise AssertionError("paired physical flag edge crossed parity sectors")
            e=frozenset((u,v))
            if e in owners or len(e)!=2:
                raise AssertionError("real original physical edges have unique source flag owners")
            owners[e]=i
            graph[u].add(v);graph[v].add(u)
            count+=1
        if count!=(1 if sector is not None else 2):
            raise AssertionError("incorrect original paired/unpaired edge population")
    return dict(graph),owners


def source_sixset_canonical_inverse(flags,f,g,six_ids):
    """All-h CONSTRUCTIVE ORIGINAL source six-ID D6 inverse.

    Do NOT search physical C6s. Build the two edge-labelled coordinate
    intersection graphs on the SAME six actual flag IDs. Each must form
    one connected SIX-edge ordinary C6 and have EXACTLY the same
    edge-ID adjacency. Then the physical corner between two
    consecutive ORIGINAL flag IDs is the UNIQUE pair of shared
    coordinate symbols. Nothing else can realize the same sixset.
    Return the single reconstructed unoriented physical C6 or None.
    """
    flags,f,g=_typed_source(flags,f,g)
    ids=tuple(six_ids)
    if len(ids)!=6 or len(set(ids))!=6 or any(
        type(i) is not int or i<0 or i>=len(flags) for i in ids):
        raise ValueError("six distinct real original source IDs required")
    src=[flags[i] for i in ids]
    if len({p for p,l in src})!=6 or len({l for p,l in src})!=6:
        return None
    pairleft={i:f[flags[i][0]] for i in ids}
    pairright={i:g[flags[i][1]] for i in ids}
    def edge_adjacency(pairs):
        incidence=defaultdict(list)
        for i in ids:
            for v in pairs[i]:incidence[v].append(i)
        if len(incidence)!=6 or any(len(srcids)!=2 for srcids in incidence.values()):
            return None
        adj={i:set() for i in ids}
        for srcids in incidence.values():
            a,b=srcids
            adj[a].add(b);adj[b].add(a)
        if any(len(ns)!=2 for ns in adj.values()):
            return None
        visited=set();stack=[min(ids)]
        while stack:
            x=stack.pop()
            if x in visited:continue
            visited.add(x)
            stack.extend(adj[x]-visited)
        return adj if len(visited)==6 else None
    la=edge_adjacency(pairleft)
    ra=edge_adjacency(pairright)
    if la is None or ra is None or la!=ra:return None
    order=[min(ids)]
    prev=None
    for k in range(5):
        next_choices=sorted(la[order[-1]]-({prev} if prev is not None else set()))
        if not next_choices:return None
        nxt=next_choices[0]
        if nxt in order:return None
        prev,order=order[-1],order+[nxt]
    if order[0] not in la[order[-1]] or len(set(order))!=6:
        raise AssertionError("reconstructed six-source edge order not simple cycle")
    corners=[]
    for j in range(6):
        i=order[j];nxt=order[(j+1)%6]
        x=set(pairleft[i])&set(pairleft[nxt])
        y=set(pairright[i])&set(pairright[nxt])
        if len(x)!=1 or len(y)!=1:
            raise AssertionError("named-original-flag neighbor coordinate intersection not unique")
        corners.append((next(iter(x)),next(iter(y))))
    if (len({v[0] for v in corners})!=6 or
        len({v[1] for v in corners})!=6):
        raise AssertionError("matched two original edge C6s not coordinate rainbow")
    for j,i in enumerate(order):
        u=corners[j-1];v=corners[j]
        if (tuple(sorted((u[0],v[0])))!=pairleft[i] or
            tuple(sorted((u[1],v[1])))!=pairright[i]):
            raise AssertionError("inverse reconstructed an edge with wrong true original flag ID")
    return _canonical_vertex_cycle(corners)


def direct_canonical_physical_sixcycles(graph):
    """INDEPENDENT graph-first simple-C6 DFS, no original inverse used."""
    found=set()
    for root in sorted(graph):
        path=[root];used={root}
        def go():
            if len(path)==6:
                if root in graph[path[-1]] and path[1]<path[-1]:
                    yield tuple(path)
                return
            for nxt in sorted(graph[path[-1]]):
                if nxt<=root or nxt in used:continue
                used.add(nxt);path.append(nxt)
                yield from go()
                path.pop();used.remove(nxt)
        found.update(_canonical_vertex_cycle(c) for c in go())
    return frozenset(found)


def independent_original_six_id_inverse_referee(flags,f,g,ids=None,
                                                left_colors=None,right_colors=None,
                                                sector=None,edge_filter=None):
    """Exact SOURCE-FIRST inverse vs distinct PHYSICAL-FIRST C6 census.

    Works on arbitrary abstract simple original incidence source.
    The W32/W34 input is real original symplectic W3s; no fabricated
    source factors are introduced during genuine finite tests.

    With no cuts, ordinary C6 may be NONRAINBOW; these must be
    detected explicitly, never claimed original D6.
    """
    flags,f,g=_typed_source(flags,f,g)
    graph,owners=physical_original_edge_graph(
        flags,f,g,ids,left_colors=left_colors,
        right_colors=right_colors,sector=sector)
    if edge_filter is not None:
        keep=set(frozenset(e) for e in edge_filter)
        if not keep<=set(owners):
            raise ValueError("subgraph must contain only ACTUAL source physical edges")
        owners={edge:i for edge,i in owners.items() if edge in keep}
        graph=defaultdict(set)
        for edge in owners:
            u,v=tuple(edge)
            graph[u].add(v);graph[v].add(u)
        graph=dict(graph)
    if left_colors is not None and right_colors is not None:
        if (any(type(c) is not int or c not in (0,1) for c in left_colors+right_colors)
            or any(left_colors[u[0]]==left_colors[v[0]] or
                   right_colors[u[1]]==right_colors[v[1]]
                   for e in owners for u,v in (tuple(e),))):
            raise ValueError("physical subgraph violates coherent double cuts")
        # Source cherry-free: adjacent physical neighbors have distinct
        # point & line COORDINATES; sufficient to make all physical
        # C6s coordinate-rainbow, using both binary color cuts.
        for v,ns in graph.items():
            if len({w[0] for w in ns})!=len(ns) or len({w[1] for w in ns})!=len(ns):
                raise ValueError("source selected pencil conflicts: physical cherry")
    cycles=direct_canonical_physical_sixcycles(graph)
    original_to_physical={}
    defects=0
    for C in cycles:
        ids6=tuple(owners[frozenset((C[j],C[(j+1)%6]))] for j in range(6))
        rainbow=(len({v[0] for v in C})==6 and
                 len({v[1] for v in C})==6)
        if not rainbow:
            defects+=1
            continue
        if len(set(ids6))!=6:
            raise AssertionError("physical rainbow C6 reused true original source ID")
        result=source_sixset_canonical_inverse(flags,f,g,ids6)
        if result!=C:
            raise AssertionError("independent ORIGINAL source six-ID inverse disagrees with physical graph DFS")
        key=frozenset(ids6)
        if key in original_to_physical:
            raise AssertionError("two distinct physical C6 share SAME original source SIX IDs")
        original_to_physical[key]=result
    if left_colors is not None and right_colors is not None and defects:
        raise AssertionError("source-no-cherry plus two cuts failed coordinate-rainbow C6 theorem")
    return {
        "actual_source_flag_IDs_in_full_relation":len(flags),
        "actual_physical_undirected_edges":len(owners),
        "ordinary_simple_unoriented_C6":len(cycles),
        "nonrainbow_ordinary_C6":defects,
        "rainbow_ordinary_C6":len(original_to_physical),
        "distinct_TRUE_original_D6_sixsets":len(original_to_physical),
        "all_rainbow_C6_reconstructed_BY_SOURCE_ONLY":True,
        "repeated_original_sixset_count":0,
        "every_ordinary_C6_source_D6_if_coherent":bool(
            left_colors is not None and right_colors is not None),
        "physical_cycle_to_original_sixset":tuple(
            sorted(((tuple(sorted(k)),v) for k,v in original_to_physical.items()))),
    }


def true_original_gq_six_id_inverse_referee(power,f,g,ids=None,
                                            left_colors=None,right_colors=None,
                                            sector=None,edge_filter=None):
    if type(power) is not int or power not in (1,2):
        raise ValueError("finite oracle only true original W32/W34")
    s,V,flags=genuine_source(power)
    if len(f)!=V or len(g)!=V:raise ValueError("complete genuine original factor maps required")
    return dict(
        s=s,V=V,
        **independent_original_six_id_inverse_referee(
            flags,f,g,ids,left_colors,right_colors,sector,edge_filter)
    )


def exhaustive_original_sixset_inverse_table(flags,f,g,ids,limit=10000):
    """SOURCE-FIRST, exhaustive genuine-original six-ID C6 table.

    Completely independent of all graph-first DFS and its owner sets.
    Only suitable for bounded original ID subsets, NEVER a claim of
    exhaustive full W(3,s) enumeration at large s. Uses exactly the
    original source six IDs, no projected surrogate.
    """
    flags,f,g=_typed_source(flags,f,g)
    ids=tuple(ids)
    if (len(set(ids))!=len(ids) or
        any(type(i) is not int or i<0 or i>=len(flags) for i in ids)):
        raise ValueError("only distinct real ORIGINAL source IDs")
    if type(limit) is not int or limit<1:
        raise ValueError("positive integer exhaustive source cap required")
    n=comb(len(ids),6) if len(ids)>=6 else 0
    if n>limit:
        raise ValueError("explicit original source sixset limit exceeded")
    original={}
    for six in combinations(sorted(ids),6):
        candidate=source_sixset_canonical_inverse(flags,f,g,six)
        if candidate is not None:
            original[six]=candidate
    if len(set(original.values()))!=len(original):
        raise AssertionError("two genuine original six-ID D6 sets reconstruct the same physical C6")
    return {
        "source_sixsets_exhaustively_tested":n,
        "source_D6_exact_count":len(original),
        "source_only_inverse_lookup":tuple(sorted(original.items())),
        "source_first_not_using_physical_cycle_DFS":True,
    }
