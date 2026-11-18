"""AA4-HEAVY-C6-INVERSE: ORIGINAL proper C6 hypotheses and minimality.

All-h combinatorial lemmas proved in the companion manuscript, NOT by
finite source tests. This referee rebuilds every physical edge and
ORIGINAL flag owner without importing any old heavy, source-inverse,
cycle, or seven-family classifier. The only fixture import is the true
symplectic source constructor genuine_symplectic_source(s) for s=2,4.

This slice establishes additional original GQ RED-TEAM NECESSITY controls:
 - no LEFT cut: genuine J-independent physical C6 repeats x (gap3);
 - no RIGHT cut: genuine J-independent physical C6 repeats y (gap3);
 - no J independence: two real typed cuts preserve physical C6 with
   a repeated x coordinate (gap2) and a genuine original pencil clash.
"""
from collections import Counter, defaultdict
from itertools import combinations
from math import comb
import json

SCHEMA="mathlab.hyp105.original-heavy-c6-inverse-minimal.v1"
STATUS="OPEN_WITH_FORMAL_BLOCKER"


def minimal_a(V):
    a=2
    while comb(a,2)<V:
        a+=1
    return a


def _e(u,v):
    if u==v:
        raise ValueError("physical edge is a loop")
    return tuple(sorted((u,v)))


def canonical_cycle(v):
    v=tuple(v)
    if len(v)!=6 or len(set(v))!=6:
        raise ValueError("not a six distinct physical vertices")
    return min(tuple(w[k:]+w[:k]) for w in (v,v[::-1])
               for k in range(6))


def _matching(flags,mode):
    """Six genuine W(3,s) named flags, optionally a repeated source point."""
    result=[]
    points=set()
    lines=set()
    if mode=="duplicate_point":
        bp=defaultdict(list)
        for i,(p,l) in enumerate(flags):
            bp[p].append(i)
        p=sorted(k for k,v in bp.items() if len(v)>=2)[0]
        result=bp[p][:2]
        points.add(p)
        lines.update(flags[i][1] for i in result)
    for i,(p,l) in enumerate(flags):
        if len(result)==6:
            break
        if p in points or l in lines:
            continue
        result.append(i)
        points.add(p)
        lines.add(l)
    if len(result)!=6 or len(lines)!=6:
        raise AssertionError("genuine symplectic source failed six-flag matching")
    if mode=="duplicate_point":
        assert len(points)==5
    else:
        assert len(points)==6
    return tuple(result)


def _labels(V,a,flags,ids,coord,kind):
    """Assign six desired cyclic owner pairs, fill complete global injections."""
    labels=[None]*V
    used=set()
    for j,i in enumerate(ids):
        p,l=flags[i]
        factor=p if kind=="point" else l
        pair=tuple(sorted((coord[j],coord[(j+1)%6])))
        if pair[0]==pair[1]:
            raise AssertionError("not a physical diagonal")
        if labels[factor] is not None and labels[factor]!=pair:
            raise AssertionError("repeated original factor has inconsistent pair")
        labels[factor]=pair
        used.add(pair)
    available=iter(p for p in combinations(range(a),2) if p not in used)
    for j in range(V):
        if labels[j] is None:
            labels[j]=next(available)
    if len(set(labels))!=V:
        raise AssertionError("global ORIGINAL pair injection violated")
    return tuple(labels)


def planted_source(s,mode):
    """Complete true W32/W34 source and actual physical C6 with source controls."""
    from hyp105_original_defect_factor_referee import genuine_symplectic_source
    if s not in (2,4):
        raise ValueError("only genuine finite W32/W34 fixtures")
    flags=tuple(genuine_symplectic_source(s))
    V=(s+1)*(s*s+1)
    if len(flags)!=(s+1)*V or len(set(flags))!=len(flags):
        raise AssertionError("source is not true named symplectic W3s flags")
    a=minimal_a(V)
    if mode=="proper":
        xs=(0,1,2,3,4,5)
        ys=(0,1,2,3,4,5)
        ids=_matching(flags,"matching")
    elif mode=="drop_left_cut":
        xs=(0,1,2,0,3,4)  # gap THREE original x collision
        ys=(0,1,2,3,4,5)
        ids=_matching(flags,"matching")
    elif mode=="drop_right_cut":
        xs=(0,1,2,3,4,5)
        ys=(0,1,2,0,3,4)  # gap THREE original y collision
        ids=_matching(flags,"matching")
    elif mode=="drop_J_independence":
        xs=(0,1,0,2,3,4)  # gap TWO source-point cherry
        ys=(0,1,2,3,4,5)
        ids=_matching(flags,"duplicate_point")
    else:
        raise ValueError("unknown mandatory genuine ORIGINAL negative control")
    f=_labels(V,a,flags,ids,xs,"point")
    g=_labels(V,a,flags,ids,ys,"line")
    planted=tuple(zip(xs,ys))
    assert len(set(planted))==6
    return dict(s=s,V=V,a=a,flags=flags,f=f,g=g,
                ids=ids,mode=mode,planted=planted)


def true_owned_edges(c,retained):
    """Each retained REAL flag owns BOTH disjoint rectangle diagonals."""
    flags,f,g=c["flags"],c["f"],c["g"]
    ids=tuple(retained)
    if len(ids)!=len(set(ids)) or any(
        type(i)!=int or i<0 or i>=len(flags) for i in ids):
        raise ValueError("duplicate/invalid original flag ID")
    owner={}
    per={}
    for i in ids:
        p,l=flags[i]
        x,z=f[p]
        y,w=g[l]
        diag=(_e((x,y),(z,w)),_e((x,w),(z,y)))
        if len(set(diag))!=2 or set(diag[0])&set(diag[1]):
            raise AssertionError("two ORIGINAL diagonals are not disjoint")
        for edge in diag:
            if edge in owner:
                raise AssertionError("distinct named original flags own one edge")
            owner[edge]=i
        per[i]=diag
    if len(owner)!=2*len(ids):
        raise AssertionError("original owner lost a physical diagonal")
    return owner,per


def source_conflicts(c,retained):
    """Source pencil J: same p + overlapping g or same l + overlapping f."""
    flags,f,g=c["flags"],c["f"],c["g"]
    ids=tuple(retained)
    J={i:set() for i in ids}
    for i,j in combinations(ids,2):
        p,l=flags[i]
        q,r=flags[j]
        if (p==q and bool(set(g[l])&set(g[r])) or
            l==r and bool(set(f[p])&set(f[q]))):
            J[i].add(j)
            J[j].add(i)
    return J


def two_cuts(c,ids,owner,mode):
    """One actual globally consistent color of both physical factor alphabets."""
    if mode=="proper":
        bx={i:i%2 for i in range(6)}
        by={i:i%2 for i in range(6)}
    elif mode=="drop_left_cut":
        bx=None
        by={i:i%2 for i in range(6)}
    elif mode=="drop_right_cut":
        bx={i:i%2 for i in range(6)}
        by=None
    elif mode=="drop_J_independence":
        bx={0:0,1:1,2:1,3:0,4:1}
        by={i:i%2 for i in range(6)}
    else:
        raise ValueError("unknown case")
    # Fill unconstrained symbols with 0, never relabel the original pair maps.
    if bx is not None: bx={i:bx.get(i,0) for i in range(c["a"])}
    if by is not None: by={i:by.get(i,0) for i in range(c["a"])}
    retained={}
    for edge,i in owner.items():
        u,v=edge
        if bx is not None and bx[u[0]]==bx[v[0]]:
            continue
        if by is not None and by[u[1]]==by[v[1]]:
            continue
        retained[edge]=i
    return retained,bx,by


def _adj(edges):
    adj=defaultdict(set)
    for u,v in edges:
        adj[u].add(v)
        adj[v].add(u)
    return adj


def graph_first_cycles(edges):
    """Independent actual physical DFS, canonical unoriented source C6 census."""
    adj=_adj(edges)
    found=set()
    for start in sorted(adj):
        stack=[(start,)]
        while stack:
            walk=stack.pop()
            if len(walk)==6:
                if start in adj[walk[-1]]:
                    found.add(canonical_cycle(walk))
                continue
            for nxt in adj[walk[-1]]:
                if nxt not in walk and nxt>=start:
                    stack.append(walk+(nxt,))
    return tuple(sorted(found))


def _factor_inverse(ids,c,owner,primary):
    """Source-first inverse with primary factor x OR independent y.

    Source-only factor cycle: six different ORIGINAL point/line IDs,
    one connected 2-regular six-symbol physical factor cycle. Its edge
    order is forced. Intersections of consecutive OTHER-factor pairs
    are unique since source other factors are globally different.
    """
    ids=tuple(ids)
    if len(ids)!=6 or len(set(ids))!=6:
        return None
    flags,f,g=c["flags"],c["f"],c["g"]
    if any(type(i)!=int or i<0 or i>=len(flags) for i in ids):
        return None
    if len({flags[i][0] for i in ids})!=6 or len(
        {flags[i][1] for i in ids})!=6:
        return None
    if primary=="x":
        first=[f[flags[i][0]] for i in ids]
        second={i:g[flags[i][1]] for i in ids}
    elif primary=="y":
        first=[g[flags[i][1]] for i in ids]
        second={i:f[flags[i][0]] for i in ids}
    else:
        raise ValueError("only original typed x or y source inverse")
    fa=defaultdict(set)
    key={}
    for i,(a,b) in zip(ids,first):
        if a==b or _e(a,b) in key:
            return None
        fa[a].add(b);fa[b].add(a)
        key[_e(a,b)]=i
    if len(fa)!=6 or any(len(v)!=2 for v in fa.values()):
        return None
    start=min(fa)
    a=start
    seq=[start]
    prev=None
    while True:
        cand=sorted(fa[a]-({prev} if prev is not None else set()))
        if not cand:
            return None
        next_a=cand[0]
        if next_a==start:
            if len(seq)!=6:
                return None
            break
        if next_a in seq or len(seq)>=6:
            return None
        prev,a=a,next_a
        seq.append(a)
    owners=[key[_e(seq[j],seq[(j+1)%6])] for j in range(6)]
    if len(set(owners))!=6 or set(owners)!=set(ids):
        return None
    other=[]
    for j in range(6):
        prev_pair=set(second[owners[(j-1)%6]])
        next_pair=set(second[owners[j]])
        meet=prev_pair&next_pair
        if len(meet)!=1:
            return None
        other.append(next(iter(meet)))
    if len(set(other))!=6:
        return None
    if primary=="x":
        cycle=tuple(zip(seq,other))
    else:
        cycle=tuple(zip(other,seq))
    for j in range(6):
        edge=_e(cycle[j],cycle[(j+1)%6])
        if owner.get(edge)!=owners[j]:
            return None
    return canonical_cycle(cycle)


def inverse_x(ids,c,owner):
    return _factor_inverse(ids,c,owner,"x")


def inverse_y(ids,c,owner):
    return _factor_inverse(ids,c,owner,"y")


def check_source_finite(c):
    """All six real original source IDs and true physical edge graph."""
    ids=c["ids"]
    owner,per=true_owned_edges(c,ids)
    J=source_conflicts(c,ids)
    chosen,bx,by=two_cuts(c,ids,owner,c["mode"])
    cycles=graph_first_cycles(chosen)
    planted=canonical_cycle(c["planted"])
    if planted not in cycles:
        raise AssertionError("planted original source C6 vanished from expected cuts")
    collision=Counter()
    nonproper=[]
    inverses={}
    source_proper={}
    for cyc in cycles:
        original=tuple(owner[_e(cyc[j],cyc[(j+1)%6])]
                       for j in range(6))
        ids_set=tuple(sorted(original))
        proper=(len({v[0] for v in cyc})==6 and
                len({v[1] for v in cyc})==6)
        if proper:
            if len(set(original))!=6:
                raise AssertionError("proper selected source C6 repeats owner")
            collision[ids_set]+=1
            x=inverse_x(ids_set,c,chosen)
            y=inverse_y(ids_set,c,chosen)
            if x!=cyc or y!=cyc:
                raise AssertionError("source-first dual inverse disagrees with independent physical DFS")
            inverses[ids_set]=(x,y)
            source_proper[ids_set]=cyc
        else:
            nonproper.append(cyc)
    if max(collision.values(),default=0)>1:
        raise AssertionError("two proper physical C6 share one unordered original six-ID set")
    if c["mode"]=="proper":
        assert not any(J.values())
        assert bx is not None and by is not None
        assert len(cycles)==1 and len(collision)==1 and not nonproper
        assert inverse_x(tuple(sorted(ids)),c,chosen)==planted
    elif c["mode"]=="drop_left_cut":
        assert not any(J.values()) and bx is None and by is not None
        assert len({v[0] for v in planted})<6 and len({v[1] for v in planted})==6
        assert planted in nonproper
    elif c["mode"]=="drop_right_cut":
        assert not any(J.values()) and bx is not None and by is None
        assert len({v[1] for v in planted})<6 and len({v[0] for v in planted})==6
        assert planted in nonproper
    elif c["mode"]=="drop_J_independence":
        assert sum(len(z) for z in J.values())//2>0
        assert bx is not None and by is not None
        assert len({v[0] for v in planted})<6 and planted in nonproper
    return dict(s=c["s"],mode=c["mode"],
        original_flags_total=len(c["flags"]),
        original_source_sixID=tuple(sorted(ids)),
        original_source_distinct_points=len({c["flags"][i][0] for i in ids}),
        original_source_distinct_lines=len({c["flags"][i][1] for i in ids}),
        original_true_physical_diagonals=len(owner),
        selected_true_diagonals=len(chosen),
        actual_original_J_conflicts=sum(map(len,J.values()))//2,
        x_cut_enabled=bx is not None,
        y_cut_enabled=by is not None,
        graph_first_unoriented_C6=len(cycles),
        source_proper_C6=len(collision),
        physical_improper_C6=len(nonproper),
        planted_six_original_physical_C6=planted,
        proof_condition_fulfilled=(not any(J.values()) and bx is not None and by is not None),
        for_all_proper_sixsets_dual_source_first_inverse_exact=all(
            x==y for x,y in inverses.values()),
        no_two_proper_C6_share_six_original_IDs=all(q==1 for q in collision.values()))


def certificate():
    rows=[check_source_finite(planted_source(s,mode)) for s in (2,4)
          for mode in ("proper","drop_left_cut","drop_right_cut",
                       "drop_J_independence")]
    if not len(rows)==8:
        raise AssertionError("incomplete genuine symplectic source falsification")
    if not all(r["no_two_proper_C6_share_six_original_IDs"] for r in rows):
        raise AssertionError("collision in source-sixID C6 inverse")
    return dict(schema=SCHEMA,issue=230,parent_pr=771,status=STATUS,
        all_h_proper_C6_from_source_J_independence_and_both_typed_cuts_proved_in_manuscript=True,
        all_h_source_sixID_unoriented_cycle_unique_lift_proved_in_manuscript=True,
        all_h_no_extra_twelve_or_six_factor_in_C6_to_D6=True,
        all_h_original_source_point_line_dual_C6_inverse=True,
        both_cuts_and_original_J_independence_individually_necessary_for_given_proof_sufficient_condition=True,
        full_physical_original_W32_W34_adversarial_rows=rows,
        root_PROVED_A=False,global_LOW_acceptance=False,
        general_ASET_exponent_claimed=False)


if __name__=="__main__":
    print("AA4_HEAVY_C6_MINIMAL_CERTIFICATE="+json.dumps(
        certificate(),sort_keys=True,separators=(",",":")))
