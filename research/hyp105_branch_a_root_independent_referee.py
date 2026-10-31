"""HYP-105 AA4-ROOTREF: independent root constant ledger and ORIGINAL-ID falsifiers.

The ALL-h proof is in docs/research/HYP-105-BRANCH-A-ROOT-REFEREE.md.
This is not a numerical evaluation of the published graph constants C,c.
No parent proof/oracle functions are used to generate expected results; only
the genuine symplectic W(3,2^h) SOURCE incidence generator is imported.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb, isqrt

from hyp105_full_physical_degree_tail import genuine_source


def _ceil_fraction(q):
    return -(-q.numerator // q.denominator)


def _ceil_sqrt(n):
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("nonnegative integer square root input required")
    r = isqrt(n)
    return r if r * r == n else r + 1


def independent_root_threshold(C, c, *, sharpened=True):
    """EXACT conditional dyadic threshold for ANY positive RATIONAL trial C,c.

    C,c are *symbolic placeholders* for unknown external SS6 constants.
    No floating point, guessed theorem constants, or synthetic large GQ.
    The bound is a sufficient upper threshold, not the least true h0.
    """
    if type(C) not in (int, Fraction) or type(c) not in (int, Fraction):
        raise ValueError("only exact integer/Fraction constants (not float or bool)")
    C, c = Fraction(C), Fraction(c)
    if C <= 0 or c <= 0:
        raise ValueError("external SS6 constants must be positive")
    e = 58 if sharpened else 59
    T = max(1, _ceil_fraction(Fraction(2**e) * C**3))
    delta = min(Fraction(1, 8), c / 2**108)
    K = 64
    sigma2_inv = 16 * (K + 1)**2
    sigma3_inv = 64 * (K + 1)**3
    L6 = 24 + 288*T*T
    L4_ceil = 2 * sigma2_inv**2 * _ceil_sqrt(8*L6) + 40*T
    B0_ceil = 64 * _ceil_sqrt((K+1)*T)
    # LE² = 21 * sigma3_inv² * L6: no irrational rounding.
    endpoint = 144 * 21 * sigma3_inv**2 * L6
    mixed = 48**8 * (B0_ceil*T*L4_ceil)**4
    first = 816*T
    s0 = max(64, first, endpoint, mixed)
    h0 = max(1, (s0-1).bit_length())
    assert (1 << h0) >= s0 and (h0 == 1 or (1 << (h0-1)) < s0)
    assert first <= s0 and endpoint <= s0 and mixed <= s0
    # 2^58 C³ corresponds to the stronger #684 true full H chunk proof.
    # 1/8^12 / 2^72 = 1/2^108 is the unchanged ORIGINAL D6 floor.
    assert delta > 0 and delta <= Fraction(1,8)
    return {
        "T": T, "delta": delta, "h0": h0, "s0": s0,
        "degree_tail_exponent": e, "sigma2_inv": sigma2_inv,
        "sigma3_inv": sigma3_inv, "L6": L6,
        "L4_ceil": L4_ceil, "B0_ceil": B0_ceil,
        "threshold_short_returns": first,
        "threshold_weighted_endpoint": endpoint,
        "threshold_full_core_blockers": mixed,
        "symbolic_external_constants_only": True,
    }


def check_root_error_inequality(C, c, h, *, sharpened=True):
    """Exact algebraic confirmation at a requested dyadic exponent h."""
    a = independent_root_threshold(C, c, sharpened=sharpened)
    if not isinstance(h, int) or isinstance(h, bool) or h < 1:
        raise ValueError("h must be an integer >=1")
    s = 1 << h
    # Bound each loss, after the 0/2 ORIGINAL BBo map, by s^6/24.
    loss1 = 34*a["T"]*s**5
    # Square to avoid irrational LE and B0 coefficients.
    # LE/2*s^(11/2) <= s^6/24 iff s>=144 LE².
    loss2_ok = s >= 144*21*a["sigma3_inv"]**2*a["L6"]
    # 2 sqrt(B0*T*L4)*s^(47/8) <= s6/24 iff
    # s >= 48^8*(B0*T*L4)^4; ceiling bounds are conservative.
    loss3_ok = s >= a["threshold_full_core_blockers"]
    return {
        "short_return_loss_le_1_24": 24*loss1 <= s**6,
        "endpoint_loss_le_1_24": loss2_ok,
        "mixed_loss_le_1_24": loss3_ok,
        "three_losses_certified": 24*loss1 <= s**6 and loss2_ok and loss3_ok,
        "bound_BBo_at_least_s6_over8": 24*loss1 <= s**6 and loss2_ok and loss3_ok,
    }


def _validate_pair_labels(V, labels):
    a = 2
    while comb(a, 2) < V:
        a += 1
    pairs = tuple(tuple(x) for x in labels)
    if (len(pairs) != V or len(set(pairs)) != V or
        any(len(p) != 2 or not (0 <= p[0] < p[1] < a) for p in pairs)):
        raise ValueError("not a globally injected complete ORIGINAL pair map")
    return a, pairs


def _source_books_endpoint_audit(s, V, flags, f, g, a):
    point_lines = [set() for _ in range(V)]
    line_points = [set() for _ in range(V)]
    for p, ell in flags:
        point_lines[p].add(ell)
        line_points[ell].add(p)
    if (len(flags) != V*(s+1) or
        any(len(v) != s+1 for v in point_lines+line_points)):
        raise AssertionError("source pencils not genuine regular W(3,s)")
    # Mf: unordered point pairs on a common line sharing an f-symbol.
    # Mg: unordered line pairs through a point sharing a g-symbol.
    Mf = sum(bool(set(f[p]) & set(f[q]))
             for ps in line_points for p,q in combinations(sorted(ps), 2))
    Mg = sum(bool(set(g[ell]) & set(g[r]))
             for ls in point_lines for ell,r in combinations(sorted(ls), 2))
    # Completely independent ORIGINAL incidence flag conflict scan.
    conflicts = [set() for _ in flags]
    for i,(p,ell) in enumerate(flags):
        for j in range(i+1,len(flags)):
            q,r = flags[j]
            if ((p == q and bool(set(g[ell]) & set(g[r]))) or
                (ell == r and bool(set(f[p]) & set(f[q])))):
                conflicts[i].add(j)
                conflicts[j].add(i)
    conflict_edges = sum(map(len,conflicts))//2
    if conflict_edges != Mf+Mg:
        raise AssertionError("point/line pencil books and original flag conflicts differ")
    Cs = (s*s+1)*(s*s+a-2)
    if Mf > Cs or Mg > Cs:
        raise AssertionError("GQ source spectral collision-book universal bound failed")
    neighbors = [set() for _ in range(V)]
    for p in range(V):
        neighbors[p] = (set().union(*(line_points[ell] for ell in point_lines[p]))
                        - {p})
    leftbad = rightbad = overlap = nonincident = 0
    for q in range(V):
        for r in range(V):
            if q in line_points[r]:
                continue
            nonincident += 1
            anchors = line_points[r] & neighbors[q]
            if len(anchors) != 1:
                raise AssertionError("full ORIGINAL GQ unique projection failed")
            p = next(iter(anchors))
            ells = point_lines[q] & point_lines[p]
            if len(ells) != 1:
                raise AssertionError("connecting ORIGINAL line not unique")
            ell = next(iter(ells))
            A = bool(set(f[q]) & set(f[p]))
            B = bool(set(g[r]) & set(g[ell]))
            leftbad += A
            rightbad += B
            overlap += A and B
    N = len(flags)
    if nonincident != V*V-N:
        raise AssertionError("nonincident original endpoint population wrong")
    if leftbad != 2*s*Mf or rightbad != 2*s*Mg:
        raise AssertionError("source original endpoint identities broken")
    M = comb(a,2)
    actual_exceptional = 4*(M*M-V*V) + 4*N + 4*(leftbad+rightbad-overlap)
    formula_exceptional = 4*(M*M-V*V)+4*N+8*s*(Mf+Mg)-4*overlap
    if actual_exceptional != formula_exceptional:
        raise AssertionError("original four-class endpoint partition failed")
    if actual_exceptional + 4*(nonincident-(leftbad+rightbad-overlap)) != 4*M*M:
        raise AssertionError("original endpoint populations do not partition physical cells")
    if s >= 64 and actual_exceptional >= 21*s**5:
        raise AssertionError("independent original endpoint bound >=21s^5")
    return {
        "Mf": Mf, "Mg": Mg, "Cs": Cs, "conflict_edges": conflict_edges,
        "conflicts": conflicts, "N": N, "nonincident": nonincident,
        "leftbad": leftbad, "rightbad": rightbad, "bad_overlap_J": overlap,
        "four_class_exception_population": actual_exceptional,
        "endpoint_class_partition_exact": True,
    }


def _colors_that_keep_half(ids, flags, labels, a, side):
    # Conditional expectations independently on ACTUAL coordinate symbols.
    colors = [None]*a
    for coord in range(a):
        best = None
        for value in (0, 1):
            colors[coord] = value
            expected = Fraction(0)
            for i in ids:
                p = flags[i][side]
                x,y = labels[p]
                if colors[x] is None or colors[y] is None:
                    expected += Fraction(1,2)
                else:
                    expected += int(colors[x] != colors[y])
            if best is None or expected > best[0]:
                best = (expected, value)
        colors[coord] = best[1]
    retained = tuple(i for i in ids if colors[labels[flags[i][side]][0]]
                     != colors[labels[flags[i][side]][1]])
    if 2*len(retained) < len(ids):
        raise AssertionError("bichromatic coordinate cut below half expectation")
    return retained, colors


def _selected_graph_and_cycles(flags, f, g, ids):
    adj = defaultdict(set)
    owners = {}
    for i in ids:
        p,ell = flags[i]
        x,z = f[p]
        y,w = g[ell]
        for u,v in (((x,y),(z,w)),((x,w),(z,y))):
            key = frozenset((u,v))
            if key in owners:
                raise AssertionError("multiple original owners for one physical edge")
            adj[u].add(v);adj[v].add(u);owners[key]=i
    if len(owners) != 2*len(ids):
        raise AssertionError("both true physical diagonals not preserved")
    # Row/column cherry-freeness: endpoints of any two-step physical path.
    for center,ns in adj.items():
        ns=tuple(ns)
        for u,v in combinations(ns,2):
            if u[0]==v[0] or u[1]==v[1]:
                raise AssertionError("original source-ID selector failed no-cherry property")
    cycles=set()
    def key_of(path):
        c=tuple(path)
        return min(tuple(c[k:]+c[:k]) for k in range(6))
    # Canonicalize both traversal directions; cycle count = unoriented.
    def canon(path):
        t=list(path);r=list(reversed(t))
        return min(key_of(t),key_of(r))
    def walk(start,path):
        if len(path)==6:
            if start in adj[path[-1]]:
                cycles.add(canon(path))
            return
        for q in adj[path[-1]]:
            if q not in path:
                walk(start,path+[q])
    for start in adj:
        walk(start,[start])
    original_sixsets=set()
    for cycle in cycles:
        if len({x for x,y in cycle}) != 6 or len({y for x,y in cycle}) != 6:
            raise AssertionError("nonproper physical C6")
        ids6=tuple(owners[frozenset((cycle[k],cycle[(k+1)%6]))]
                   for k in range(6))
        if (len(set(ids6))!=6 or
            len({flags[i][0] for i in ids6})!=6 or
            len({flags[i][1] for i in ids6})!=6):
            raise AssertionError("not an accepted ORIGINAL six-flag D6 profile")
        q=frozenset(ids6)
        if q in original_sixsets:
            raise AssertionError("different physical C6 represent SAME original D6 sixset")
        original_sixsets.add(q)
    return {"selected_original_flags":len(ids), "selected_physical_edges":len(owners),
            "accepted_original_D6_from_selected_graph":len(original_sixsets),
            "cycle_original_sixsets":original_sixsets}


def original_root_falsifier(power, f, g, *, pinned_original_flags=None):
    """Source-first and physical-first checks on genuine W(3,2^h), h=1,2.

    Optional pinned six IDs must already form a legitimate original conflict
    independent set; used for planted positive ORIGINAL D6 control.
    """
    if type(power) is not int or power not in (1,2):
        raise ValueError("genuine finite original source supports h=1,2")
    s,V,flags=genuine_source(power)
    a,f=_validate_pair_labels(V,f)
    ag,g=_validate_pair_labels(V,g)
    if a != ag:
        raise ValueError("physical typed alphabets do not match")
    audit=_source_books_endpoint_audit(s,V,flags,f,g,a)
    conflicts=audit.pop("conflicts")
    if pinned_original_flags is None:
        alive=set(range(len(flags)))
        selected=[]
        while alive:
            i=min(alive, key=lambda j:(len(conflicts[j]&alive),j))
            selected.append(i)
            alive.difference_update(conflicts[i]|{i})
        carowei=sum((Fraction(1,len(ns)+1) for ns in conflicts), Fraction(0))
        if len(selected)<carowei:
            raise AssertionError("Caro-Wei original conflict graph selection failed")
    else:
        selected=tuple(pinned_original_flags)
        if (len(set(selected))!=len(selected) or
            any(type(i) is not int or not 0<=i<len(flags) for i in selected)):
            raise ValueError("invalid pinned ORIGINAL source flag IDs")
        if any(j in conflicts[i] for i,j in combinations(selected,2)):
            raise ValueError("pinned original flags are source-conflicting")
    after_left,c1=_colors_that_keep_half(selected,flags,f,a,0)
    after_right,c2=_colors_that_keep_half(after_left,flags,g,a,1)
    assert 4*len(after_right)>=len(selected)
    selected_report=_selected_graph_and_cycles(flags,f,g,after_right)
    # Independently reconstruct ORIGINAL full physical graph from actual IDs.
    full_graph=_selected_graph_and_cycles_unchecked_degree(flags,f,g)
    if full_graph["edges"]!=2*len(flags) or full_graph["degree_sum"]!=4*len(flags):
        raise AssertionError("physical full source exact edge/degree conservation failed")
    return {
        "s":s,"V":V,"original_flag_count":len(flags),
        "source_books":audit,
        "full_physical_degree_sum":full_graph["degree_sum"],
        "full_physical_edges":full_graph["edges"],
        "precut_original_flags":len(selected),
        **selected_report, "all_checks_passed":True,
    }


def _selected_graph_and_cycles_unchecked_degree(flags,f,g):
    owners={}
    degree=Counter()
    for i,(p,ell) in enumerate(flags):
        x,z=f[p];y,w=g[ell]
        for u,v in (((x,y),(z,w)),((x,w),(z,y))):
            edge=frozenset((u,v))
            if edge in owners:
                raise AssertionError("two ORIGINAL sources have same physical edge")
            owners[edge]=i
            degree[u]+=1; degree[v]+=1
    return {"edges":len(owners),"degree_sum":sum(degree.values())}


def planted_original_sixcycle(power):
    """Build valid completely injected f,g with six ORIGINAL matching IDs
    spelling the SAME physical six-cycle on both typed coordinates.
    Remaining original labels fill unused physical K_a edges injectively.
    """
    s,V,flags=genuine_source(power)
    a=2
    while comb(a,2)<V:a+=1
    if a<6:raise ValueError("cannot plant physical sixcycle")
    used_p=set();used_l=set();matching=[]
    for i,(p,ell) in enumerate(flags):
        if p not in used_p and ell not in used_l:
            matching.append(i);used_p.add(p);used_l.add(ell)
            if len(matching)==6:break
    if len(matching)!=6:
        raise AssertionError("genuine source lacks original matching size 6")
    ordered_six=[tuple(sorted((i,(i+1)%6))) for i in range(6)]
    allpairs=list(combinations(range(a),2))
    extra=[x for x in allpairs if x not in set(ordered_six)]
    f=[None]*V;g=[None]*V
    for i,edge in zip(matching,ordered_six):
        p,ell=flags[i]
        f[p]=edge;g[ell]=edge
    fi=gi=0
    for j in range(V):
        if f[j] is None:
            f[j]=extra[fi];fi+=1
        if g[j] is None:
            g[j]=extra[gi];gi+=1
    return tuple(f),tuple(g),tuple(matching)
