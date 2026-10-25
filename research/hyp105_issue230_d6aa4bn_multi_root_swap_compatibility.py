"""AA4-BN: exact compatibility and minimum swaps for multiple ORIGINAL root repairs.

Pure partial-permutation completion is classical; new research scope is the
same-global-map, same-original-six-incidence-ID GF(5) certificate interface.
No theorem asserts that two arbitrary roots have compatible candidates.
"""
from collections import Counter
from itertools import combinations

from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4q_two_sided_seven_join import independent_joint_classify


def optimal_prescribed_global_swaps(original, root_prescriptions, protected=()):
    """Exact globally injective simultaneous completion and Cayley minimum.

    root_prescriptions: iterable of iterable (ORIGINAL factor ID, full occupied
    physical pair image). Different original IDs cannot share target images;
    shared source IDs must agree across roots. 'protected' original factor
    images are fixed at EVERY intermediate step, including all actual root pins.

    Returns a shortest sequence of whole-factor image transpositions, or
    raises ValueError with a typed candidate-specific conflict. No physical
    endpoint swaps, no per-Q random re-labeling.
    """
    original=tuple(tuple(sorted(e)) for e in original)
    V=len(original)
    if V<2 or len(set(original))!=V or any(
        len(e)!=2 or e[0]==e[1] or
        any(type(x) is not int or x<0 for x in e)
        for e in original):
        raise ValueError("original map must be globally injected physical pairs")
    pins=tuple(protected)
    if any(type(i) is not int or not 0<=i<V for i in pins) or len(set(pins))!=len(pins):
        raise ValueError("protected ORIGINAL source factor IDs must be distinct and valid")
    frozen=set(pins)
    owners={e:i for i,e in enumerate(original)}
    assignments={}
    groups=tuple(tuple(group) for group in root_prescriptions)
    for group in groups:
        for entry in group:
            try: i,edge=entry
            except (ValueError,TypeError):
                raise ValueError("each prescribed mapping needs source ID and physical edge") from None
            if type(i) is not int or i<0 or i>=V:
                raise ValueError("prescribed ORIGINAL source factor out of range")
            try: target=tuple(sorted(edge))
            except TypeError:
                raise ValueError("invalid desired physical pair image") from None
            if len(target)!=2 or target not in owners:
                raise ValueError("target image absent from the fixed occupied support")
            if i in assignments and assignments[i]!=target:
                raise ValueError("SOURCE_CONFLICT: shared ORIGINAL factor has different targets")
            assignments[i]=target
    target_owners={}
    for source,target in assignments.items():
        if target in target_owners and target_owners[target]!=source:
            raise ValueError("TARGET_CONFLICT: different source factors demand one occupied edge")
        target_owners[target]=source
        if source in frozen and original[source]!=target:
            raise ValueError("PIN_CONFLICT: prescribed rooted source factor must remain fixed")
        if owners[target] in frozen and owners[target]!=source:
            raise ValueError("PIN_CONFLICT: target belongs to protected ORIGINAL factor")
    arrows={source:owners[target] for source,target in assignments.items()
            if original[source]!=target}
    indegree=Counter(arrows.values())
    if any(v>1 for v in indegree.values()):
        raise AssertionError("injective target check did not enforce indegree<=1")
    out=list(original)
    swaps=[]
    paths=[]
    cycles=[]
    seen=set()

    def swap(u,v):
        if u in frozen or v in frozen or u==v:
            raise AssertionError("invalid global original factor-image transposition")
        out[u],out[v]=out[v],out[u]
        swaps.append((u,v))
        if any(out[i]!=original[i] for i in pins):
            raise AssertionError("pinned original images changed")

    # Disjoint open paths: do their arrows in FORWARD order.
    for root in sorted(arrows):
        if indegree[root] or root in seen:
            continue
        path=[root]
        while path[-1] in arrows:
            node=path[-1]
            if node in seen:
                raise AssertionError("partial matching contains an unexpected tail merge")
            seen.add(node)
            following=arrows[node]
            swap(node,following)
            path.append(following)
        paths.append(tuple(path))

    # Remaining components must be directed cycles.
    for root in sorted(arrows):
        if root in seen:
            continue
        component=[]
        cur=root
        while cur not in seen:
            seen.add(cur)
            component.append(cur)
            cur=arrows[cur]
        if cur!=root or len(component)<2:
            raise AssertionError("non-cycle remains after open-path decomposition")
        for u,v in zip(component,component[1:]):
            swap(u,v)
        cycles.append(tuple(component))

    minimum=len(arrows)-len(cycles)
    if len(swaps)!=minimum or len(set(out))!=V or set(out)!=set(original):
        raise AssertionError("Cayley-minimum globally injected completion invalid")
    if any(out[i]!=target for i,target in assignments.items()):
        raise AssertionError("a prescribed original source image is unmet")
    return {
        "initial_full_global_map":original,
        "final_full_global_map":tuple(out),
        "all_original_source_constraints":tuple(sorted(assignments.items())),
        "all_protected_original_factor_IDs":pins,
        "candidate_matching_arcs":tuple(sorted(arrows.items())),
        "open_source_owner_paths":tuple(paths),
        "closed_source_owner_cycles":tuple(cycles),
        "number_nontrivial_arcs":len(arrows),
        "number_nontrivial_closed_cycles":len(cycles),
        "exact_minimum_image_transpositions":minimum,
        "actual_shortest_global_transpositions":tuple(swaps),
        "compatible_for_THESE_selected_root_Q_and_targets":True,
        "arbitrary_two_root_candidates_compatible_NOT_PROVED":True,
        "original_fixed_map_seven_GF5_lower_NOT_PROVED":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def original_multi_cherry_candidate_minimum(model,side,candidates):
    """Check AND optimally realize simultaneously SELECTED true six-Q targets.

    Every candidate {'root':p, 'flags':(alpha,beta), 'Q':six original
    incidence IDs, 'target':six whole physical pair edges,
    'free_assignments':((source_id,physical_pair), ...)}.

    Same global original opposite factor map for EVERY Q. A candidate's
    images are required to form exact historical B/A or A/B, verified
    independently after all prescriptions merge. Each root's TWO
    ORIGINAL opposite factor pins remain unchanged throughout.
    This is NOT an exhaustive oracle over all possible Q and targets.
    """
    if type(side) is not int or side not in (0,1):
        raise ValueError("original typed side required")
    s,V,a,inc,f,g,byP,byL=_original_source(model)
    first=(f,g)[side]
    other=(g,f)[side]
    by=(byP,byL)[side]
    candidates=tuple(candidates)
    if len(candidates)<1:
        raise ValueError("at least one genuine original cherry certificate needed")
    prescriptions=[]
    protected=set()
    verified=[]
    occupied=set(other)
    for candidate in candidates:
        root=candidate["root"]
        if type(root) is not int or not 0<=root<V:
            raise ValueError("original cherry factor ID invalid")
        flags=tuple(candidate["flags"])
        Q=tuple(candidate["Q"])
        if len(flags)!=2 or len(set(flags))!=2 or any(
            type(j) is not int or j not in by[root] for j in flags):
            raise ValueError("two genuine incidence flags through actual original source root required")
        if len(Q)!=6 or len(set(Q))!=6 or any(
            type(j) is not int or j<0 or j>=len(inc) for j in Q):
            raise ValueError("six DIFFERENT original incidence IDs required")
        if not set(flags)<=set(Q):
            raise ValueError("both actual rooted flags must belong to the SAME original six-Q")
        roots=Counter(inc[j][side] for j in Q)
        if roots.get(root)!=2 or sorted(roots.values())!=[1,1,1,1,2]:
            raise ValueError("original source first side must have B-profile with this cherry root")
        coords=Counter(col for j in Q for col in first[inc[j][side]])
        if len(coords)!=6 or set(coords.values())!={2}:
            raise ValueError("first-side physical source projection not genuine six-coordinate B")
        oppids=tuple(inc[j][1-side] for j in Q)
        if len(set(oppids))!=6:
            raise ValueError("six genuine original opposite source factor IDs must be distinct")
        pins=tuple(inc[j][1-side] for j in flags)
        target=tuple(tuple(sorted(edge)) for edge in candidate["target"])
        if len(target)!=6 or len(set(target))!=6 or not set(target)<=occupied:
            raise ValueError("physical target must be six distinct occupied original images")
        degree=Counter(v for edge in target for v in edge)
        if len(degree)!=6 or set(degree.values())!={2}:
            raise ValueError("target must be genuine simple A/2factor on six coordinates")
        if not {other[i] for i in pins}<=set(target):
            raise ValueError("both globally pinned opposite source physical images required in target")
        free=set(oppids)-set(pins)
        req=tuple((src,tuple(sorted(e))) for src,e in candidate["free_assignments"])
        if len(req)!=4 or set(src for src,_ in req)!=free or set(edge for _,edge in req)!=(set(target)-{other[i] for i in pins}):
            raise ValueError("one-to-one assignment of four true original nonpin factors to four residual target edges required")
        protected.update(pins)
        prescriptions.append(req)
        verified.append({"root":root,"flags":flags,"Q":Q,"target":target})
    repaired=optimal_prescribed_global_swaps(other,prescriptions,tuple(sorted(protected)))
    after=dict(model)
    after["right_labels" if side==0 else "left_labels"]=repaired["final_full_global_map"]
    tags=[]
    for candidate in verified:
        Q=candidate["Q"]
        profile=("B","A") if side==0 else ("A","B")
        tag=independent_joint_classify(
            Q,*profile,inc,after["left_labels"],after["right_labels"])
        expected="B-left/A-right" if side==0 else "A-left/B-right"
        if tag!=expected:
            raise AssertionError(f"true-original historical GF5 target {tag} != {expected}")
        tags.append(tag)
    return {**repaired, "actual_true_original_cherry_certificates":tuple(verified),
            "same_new_original_full_global_map_satisfies_EVERY_given_certificate":True,
            "accepted_original_seven_GF5_tags":tuple(tags),
            "repaired_original_complete_model":after,
            "source_incidence_IDs_immutable":True}


def candidate_from_target(model,side,root,flags,Q,physical_target):
    """Canonical specified target ordering; may conflict with other candidates."""
    s,V,a,inc,f,g,byP,byL=_original_source(model)
    other=(g,f)[side]
    pins={inc[j][1-side] for j in flags}
    free=sorted({inc[j][1-side] for j in Q}-pins)
    images=sorted(set(physical_target)-{other[i] for i in pins})
    if len(free)!=4 or len(images)!=4:
        raise ValueError("selected true original six-Q has no four distinct free factors/edges")
    return {"root":root,"flags":tuple(flags),"Q":tuple(Q),
            "target":tuple(physical_target),
            "free_assignments":tuple(zip(free,images))}
