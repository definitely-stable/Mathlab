"""HYP-105 C24-B8-I: independently replayable global-injection cylinder cover.

A finite proof tree partitions every WHOLE injective original-right completion
of one pinned cylinder. Each branch explicitly covers EVERY currently unused
physical edge. Each leaf has independently re-evaluated S; a pruned subtree
has an independently re-evaluated pointwise original-source lower >= threshold.

This is a scoped certificate for ONE fixed left f and ONE fixed pinned RIGHT
cylinder, not a universal all-h positive S lower. A root with no pins is
permitted, but large searches fail closed at explicit budgets.
"""
from itertools import combinations

from hyp105_g5e2b3e1c24b8h_joint_source_cylinder import validate_problem


def _setup(n,m,pinned,order,threshold,max_nodes,max_leaves):
    validate_problem((),pinned,n,m)
    free=tuple(i for i in range(n) if i not in pinned)
    if (not isinstance(order,(list,tuple)) or len(order)!=len(free)
            or set(order)!=set(free) or
            any(type(i) is not int for i in order)):
        raise ValueError("branch order must contain every and only unpinned original line")
    if (threshold is not None and
            (type(threshold) is not int or threshold<0)):
        raise ValueError("nonnegative integer threshold or None required")
    if (type(max_nodes) is not int or max_nodes<1 or
            type(max_leaves) is not int or max_leaves<1):
        raise ValueError("positive exact finite tree budgets needed")
    return tuple(order)


def _integer_score(score,assignment):
    result=score(dict(assignment))
    if type(result) is not int or result<0:
        raise ValueError("exact nonnegative integer ORIGINAL source score required")
    return result


def _integer_floor(floor,assignment):
    result=floor(dict(assignment))
    if type(result) is not int:
        raise ValueError("exact integer pointwise floor required")
    return result


def build_cover(n,m,root_pinned,order,score,*,threshold=None,floor=None,
                floor_max_depth=0,max_nodes=1500,max_leaves=600):
    """Build deterministic finite proof tree; NO hidden symmetry quotient.

    floor is a source-derived pointwise lower on all globally coherent
    completions. If any floor >= threshold, pruning is logically sound.
    If floor is unavailable or weak, branch over all unused physical host
    edges, retaining a valid exhaustive certificate under strict budgets.
    """
    ordered=_setup(n,m,root_pinned,order,threshold,max_nodes,max_leaves)
    if (not callable(score) or (floor is not None and not callable(floor)) or
            type(floor_max_depth) is not int or floor_max_depth<0):
        raise ValueError("score and optional floor must be callable; valid depth needed")
    if floor is not None and threshold is None:
        raise ValueError("pruning floor needs an explicit threshold")
    count={"nodes":0,"branches":0,"leaves":0,"prunes":0,"floors_evaluated":0}
    def visit(pinned,depth):
        count["nodes"]+=1
        if count["nodes"]>max_nodes:
            raise ValueError("global cover node budget exceeded (fail closed)")
        if (threshold is not None and floor is not None and
                depth<=floor_max_depth):
            count["floors_evaluated"]+=1
            lb=_integer_floor(floor,pinned)
            if lb>=threshold:
                count["prunes"]+=1
                return {"kind":"prune","bound":lb}
        if depth==len(ordered):
            count["leaves"]+=1
            if count["leaves"]>max_leaves:
                raise ValueError("global cover leaf budget exceeded (fail closed)")
            value=_integer_score(score,pinned)
            return {"kind":"leaf","score":value}
        i=ordered[depth]
        available=tuple(e for e in range(m) if e not in pinned.values())
        if len(available)<len(ordered)-depth:
            raise AssertionError("cannot globally inject all residual original lines")
        count["branches"]+=1
        children=[]
        for e in available:
            child={**pinned,i:e}
            children.append({"edge":e,"node":visit(child,depth+1)})
        return {"kind":"branch","line":i,"children":children}
    root=visit(dict(root_pinned),0)
    return {
        "schema":"hyp105.c24b8i.global-injection-cover.v1",
        "n":n,"m":m,
        "root_pinned":[[i,root_pinned[i]] for i in sorted(root_pinned)],
        "order":list(ordered),
        "threshold":threshold,
        "floor_max_depth":floor_max_depth,
        "tree":root,
        "builder_counts":dict(count),
        "scope":"one fixed original left f and one pinned right cylinder",
        "no_global_unpinned_or_all_h_positive_claim":True,
    }


def replay_cover(certificate,score,*,floor=None,max_nodes=1500,max_leaves=600):
    """Independent structural/cost verifier. NO trust in builder counts/tree.

    Check exact branch completeness at every internal node, every leaf
    with independently supplied score oracle, and every prune with independently
    supplied source-based lower. Return MINIMUM CERTIFIED LOWER, not falsely
    an exact minimum if ANY pruning was used.
    """
    if not isinstance(certificate,dict) or certificate.get("schema")!=(
            "hyp105.c24b8i.global-injection-cover.v1"):
        raise ValueError("unsupported or missing proof-tree schema")
    try:
        n,m=certificate["n"],certificate["m"]
        pins=certificate["root_pinned"]
        if (not isinstance(pins,list) or any(
                not isinstance(p,(tuple,list)) or len(p)!=2 for p in pins)):
            raise ValueError("noncanonical root pins")
        root=dict(tuple(x) for x in pins)
        if len(root)!=len(pins) or pins!=[[i,root[i]] for i in sorted(root)]:
            raise ValueError("duplicate/unsorted pinned right labels")
        threshold=certificate["threshold"]
        order=_setup(n,m,root,certificate["order"],threshold,max_nodes,max_leaves)
        depth_limit=certificate["floor_max_depth"]
        if type(depth_limit) is not int or depth_limit<0:
            raise ValueError("invalid pruning depth")
        if not callable(score) or (floor is not None and not callable(floor)):
            raise ValueError("independent score/floor oracles required")
    except (KeyError,TypeError) as e:
        raise ValueError("invalid global proof envelope") from e
    count={"nodes":0,"branches":0,"leaves":0,"prunes":0,"floors_evaluated":0}
    def verify(node,pinned,depth):
        if not isinstance(node,dict):
            raise ValueError("malformed proof node")
        count["nodes"]+=1
        if count["nodes"]>max_nodes:
            raise ValueError("replay node budget exceeded")
        kind=node.get("kind")
        if kind=="prune":
            if (set(node)!={"kind","bound"} or threshold is None or
                    floor is None or depth>depth_limit):
                raise ValueError("unauthorized pruning")
            val=_integer_floor(floor,pinned)
            count["floors_evaluated"]+=1
            count["prunes"]+=1
            if type(node["bound"]) is not int or node["bound"]!=val or val<threshold:
                raise ValueError("forged or insufficient pointwise bound")
            return val
        if kind=="leaf":
            if set(node)!={"kind","score"} or depth!=len(order):
                raise ValueError("incorrect global leaf")
            count["leaves"]+=1
            if count["leaves"]>max_leaves:
                raise ValueError("replay leaf budget exceeded")
            val=_integer_score(score,pinned)
            if type(node["score"]) is not int or node["score"]!=val:
                raise ValueError("leaf original source score does not reproduce")
            return val
        if kind!="branch" or set(node)!={"kind","line","children"}:
            raise ValueError("invalid branch or proof-tree node type")
        if depth>=len(order) or node["line"]!=order[depth]:
            raise ValueError("invalid original right-line splitting order")
        children=node["children"]
        if not isinstance(children,list):
            raise ValueError("branch edges not explicitly enumerated")
        expected=[e for e in range(m) if e not in pinned.values()]
        if ([child.get("edge") if isinstance(child,dict) else None
             for child in children]!=expected or
                any(not isinstance(ch,dict) or set(ch)!={"edge","node"}
                    for ch in children)):
            raise ValueError("incomplete/duplicate/incorrect global edge cover")
        count["branches"]+=1
        return min(verify(child["node"],{**pinned,order[depth]:child["edge"]},depth+1)
                   for child in children)
    lower=verify(certificate.get("tree"),root,0)
    if count!=certificate.get("builder_counts"):
        raise ValueError("builder/replayer node count mismatch")
    return {
        "certified_cylinder_score_lower":lower,
        "positive_threshold_proven":threshold is not None and lower>=threshold,
        "exact_cylinder_minimum":lower if count["prunes"]==0 else None,
        "has_pruned_subtrees":count["prunes"]>0,
        "global_branch_coverage_verified":True,
        "independent_original_source_score_verified_at_each_leaf":True,
        "independent_pointwise_bound_recomputed_at_each_prune":True,
        "root_pinned_lines":len(root),
        "whole_global_injection_leaf_count":count["leaves"],
        "pruned_subtree_count":count["prunes"],
        "node_count":count["nodes"],
        "NO_all_h_unpinned_omega_s6_conclusion":True,
    }
