"""HYP-105 AA4-BBOINV: inverse ORIGINAL six-ID B/B-overlap source bridge.

Independent of *all* physical 3-walk generators, GQ projection enumeration,
source-exposure postings, full/core mixed blocker code, and all-h probabilistic
arguments. Given one genuine ORIGINAL six-incidence set, determine the UNIQUE
source anchor (q,ell),(p,ell),(p,r) from the intersection of the repeated
original point p and original line ell. The remaining THREE actual original
flag IDs yield unique physical THREE-edge coordinate paths on EACH side,
if the historical physical B/B degree-2 criteria hold. Their ORIGINAL flag
order must agree in one of the two orientations on both sides.

The number of associated source-backed, coordinate-PROPER, UNBLOCKED
DIRECTED physical 3-paths is EXACTLY 0 or 2, never 1 or >2, for EVERY
dyadic W(3,s), every globally injected complete f,g and every true original
B/B-overlap six-ID set. This is a local combinatorial inverse proof,
independent of the original source GQ projection lemma. The latter ensures
forward images choose precisely this unique anchor.

An arbitrary true ORIGINAL core I and deleted-original-flag set Z accept
the two paths iff all three non-anchor IDs belong to I and none of the SIX
IDs belongs to Z. The three source anchors need NOT be in the core.
"""
from collections import Counter
from itertools import combinations


def _oriented_three_edge_factor_paths(remaining_ids, flags, pair_labels, side):
    """Independent simple graph edge-chain oracle, not physical walk DFS.

    For each of THREE genuine original IDs, take its associated physical
    pair edge from a single typed factor side. Recognize one C4-minus-edge
    chain P4 and return BOTH possible oriented coordinate sequences and
    their true ORIGINAL-ID edge orders.
    """
    if len(remaining_ids)!=3 or len(set(remaining_ids))!=3:
        raise ValueError("three distinct original source flag IDs required")
    adj={}
    edge_owner={}
    for fid in remaining_ids:
        factor=flags[fid][side]
        u,v=pair_labels[factor]
        if u==v:
            return ()
        edge=frozenset((u,v))
        if edge in edge_owner:
            return ()
        edge_owner[edge]=fid
        adj.setdefault(u,set()).add(v)
        adj.setdefault(v,set()).add(u)
    if len(adj)!=4 or sorted(len(ns) for ns in adj.values())!=[1,1,2,2]:
        return ()
    ends=sorted(u for u,ns in adj.items() if len(ns)==1)
    candidates=[]
    for first in ends:
        coords=[first];orders=[]
        while len(coords)<4:
            fresh=[v for v in adj[coords[-1]] if v not in coords]
            if len(fresh)!=1:
                return ()
            v=fresh[0]
            orders.append(edge_owner[frozenset((coords[-1],v))])
            coords.append(v)
        if len(set(coords))!=4 or len(set(orders))!=3:
            return ()
        candidates.append((tuple(coords),tuple(orders)))
    if candidates[0][0]!=tuple(reversed(candidates[1][0])):
        raise AssertionError("P4 graph chain must have two reverse orientations")
    return tuple(candidates)


def inverse_original_BBo_paths(ids, original_flags, f, g, *,core_ids=None,
                                deleted_ids=()):
    """Full inverse source sixset -> 0 or 2 explicit physical directed paths.

    Returns () if NOT a historically B/B-overlap source sextuple or if the
    right and left THREE-ID chain orders cannot be aligned. The inverse
    does not call the historical classifier, forward source projection,
    or any physical path enumerator; test oracle cross-checks them.

    Malformed genuine original ID inputs fail CLOSED with ValueError.
    """
    ids=tuple(ids)
    n=len(original_flags)
    if (len(ids)!=6 or len(set(ids))!=6 or
        any(type(i) is not int or not 0<=i<n for i in ids)):
        raise ValueError("exactly six distinct valid ORIGINAL incidence IDs")
    if (len(set(original_flags))!=n or
        any(type(p) is not int or type(ell) is not int or
            not 0<=p<len(f) or not 0<=ell<len(g)
            for p,ell in original_flags)):
        raise ValueError("original true source ID factors must be simple and legal")
    Z=set(deleted_ids)
    if (len(Z)!=len(tuple(deleted_ids)) or
        any(type(i) is not int or not 0<=i<n for i in Z)):
        raise ValueError("invalid forbidden ORIGINAL incidence IDs")
    I=(None if core_ids is None else set(core_ids))
    if I is not None and (
        len(I)!=len(tuple(core_ids)) or
        any(type(i) is not int or not 0<=i<n for i in I)):
        raise ValueError("invalid core ORIGINAL incidence IDs")
    if any(i in Z for i in ids):
        return ()
    pp=Counter(original_flags[i][0] for i in ids)
    ll=Counter(original_flags[i][1] for i in ids)
    if sorted(pp.values())!=[1,1,1,1,2] or sorted(ll.values())!=[1,1,1,1,2]:
        return ()
    p=next(p for p,cnt in pp.items() if cnt==2)
    ell=next(ell for ell,cnt in ll.items() if cnt==2)
    if (p,ell) not in [original_flags[i] for i in ids]:
        return ()  # original B/B-DISJOINT, not historical B/B-overlap
    shared=next(i for i in ids if original_flags[i]==(p,ell))
    partner_p=next(i for i in ids if original_flags[i][0]==p and i!=shared)
    partner_ell=next(i for i in ids if original_flags[i][1]==ell and i!=shared)
    anchors={shared,partner_p,partner_ell}
    if len(anchors)!=3:
        raise AssertionError("true original B/B-overlap has unique three-ID anchor")
    remaining=tuple(i for i in ids if i not in anchors)
    if I is not None and any(i not in I for i in remaining):
        return ()
    # Historical physical-degree TWO criterion per typed half:
    # repeated source point/line pair label disjoint from the C4
    # formed by the four singly used source point/line factors.
    for side,labels,repeated in ((0,f,p),(1,g,ell)):
        deg=Counter()
        for fid in ids:
            fact=original_flags[fid][side]
            if fact==repeated:
                continue
            u,v=labels[fact]
            deg[u]+=1
            deg[v]+=1
        if len(deg)!=4 or set(deg.values())!={2}:
            return ()
        if set(labels[repeated]) & set(deg):
            return ()
    left=_oriented_three_edge_factor_paths(remaining,original_flags,f,0)
    right=_oriented_three_edge_factor_paths(remaining,original_flags,g,1)
    if not left or not right:
        return ()
    paths=[]
    for xcoords,order_l in left:
        for ycoords,order_r in right:
            if order_l!=order_r:
                continue
            path=tuple(zip(xcoords,ycoords))
            for j,fid in enumerate(order_l):
                pnt,lin=original_flags[fid]
                if {path[j][0],path[j+1][0]}!=set(f[pnt]) or (
                    {path[j][1],path[j+1][1]}!=set(g[lin])):
                    raise AssertionError("inverse original source diagonal provenance broken")
            paths.append((tuple(path),order_l))
    if len(paths) not in (0,2):
        raise AssertionError("B/B-overlap original sixset has either ZERO or TWO aligned directed 3-paths")
    if len(paths)==2:
        if (paths[1][0]!=tuple(reversed(paths[0][0])) or
            paths[1][1]!=tuple(reversed(paths[0][1]))):
            raise AssertionError("the exactly two original paths must be reversals")
        if any(len({v[0] for v in path})!=4 or
               len({v[1] for v in path})!=4
               for path,_ in paths):
            raise AssertionError("original reconstructed physical paths not proper")
    return tuple(paths)


def independent_inverse_W32_census(original_model, *,right_labels=None,
                                   core_ids=None,deleted_ids=()):
    """Genuine historical complete BBo sixsets; independently invert them.

    Restrict enumerations to the existing 62,370 true original LEFT
    candidate sextuples and classify them using historical GF5 code.
    Unlike forward physical path enumeration, the objects iterated
    here are SOURCE sixsets first.
    """
    from hyp105_g5e2b3e1a_fixed_leading import selected_left_six
    from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked
    flags=original_model["incidences"]
    f=original_model["left_labels"]
    g=(original_model["right_labels"] if right_labels is None else right_labels)
    n_bb=n0=n2=0
    produced={}
    for ids,kind in selected_left_six(original_model):
        if kind!="B":
            continue
        if classify_seven_prechecked(ids,f,g,flags)!="B/B-overlap":
            continue
        n_bb+=1
        inverse=inverse_original_BBo_paths(
            ids,flags,f,g,core_ids=core_ids,deleted_ids=deleted_ids)
        if len(inverse)==0:
            n0+=1
        else:
            if len(inverse)!=2:
                raise AssertionError("inverse multiplicity must be two")
            n2+=1
            produced[tuple(ids)]=inverse
    if n0+n2!=n_bb:
        raise AssertionError("original full BBo inverse partition invalid")
    return {
        "all_h_original_BBo_0_or_2_inverse_paths":True,
        "historical_original_BBo_sixsets":n_bb,
        "eligible_inverse_sixsets":n2,
        "ineligible_inverse_sixsets":n0,
        "directed_inverse_source_paths":2*n2,
        "inverse_paths_by_original_sixset":produced,
        "external_GQ_projection_not_used_to_build_inverse":True,
        "finite_census_not_all_h_proof":True,
    }
