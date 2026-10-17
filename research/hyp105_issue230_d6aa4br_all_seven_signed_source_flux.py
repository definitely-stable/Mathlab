"""AA4-BR: all-seven genuine-original GF5 signed LINE-image-switching flux.

True original source six-incidence multiplicities determine at most ONE
historical positive class, independent of every physical labeling.
A source-factor transposition therefore births or kills a class-Q, never
transports the SAME Q between two distinct positive GF5 classes.
Proof for every genuine W(3,2^h), h>=1; finite oracle actual W32 only.
The signed flux need NOT be positive on an arbitrary initial f,g.
"""
from collections import Counter
from itertools import combinations, permutations
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_g5e2b3e1b0_seven_signature import (
    R3_CERTIFIED_FLOORS, classify_seven_prechecked,
)
from hyp105_g5e2b3e1a_fixed_leading import selected_left_six

SEVEN=tuple(R3_CERTIFIED_FLOORS)

def immutable_original_sixflag_class(Q,inc):
    """Possible accepted tag determined by six DISTINCT original source flags."""
    inc=tuple(tuple(t) for t in inc)
    Q=tuple(Q)
    if len(Q)!=6 or len(set(Q))!=6 or any(
        type(j) is not int or j<0 or j>=len(inc) for j in Q):
        raise ValueError("exactly SIX different original incidence flag IDs")
    if any(len(e)!=2 or any(type(v) is not int or v<0 for v in e)
           for e in inc):
        raise ValueError("invalid original point/line factor IDs")
    p=tuple(inc[j][0] for j in Q)
    l=tuple(inc[j][1] for j in Q)
    profiles={(1,1,1,1,1,1):"A",(1,1,1,1,2):"B",(2,2,2):"C"}
    P=profiles.get(tuple(sorted(Counter(p).values())))
    L=profiles.get(tuple(sorted(Counter(l).values())))
    if (P,L)==("A","A"): return "D6"
    if (P,L)==("B","A"): return "B-left/A-right"
    if (P,L)==("A","B"): return "A-left/B-right"
    if {P,L}=={"A","C"}: return "C/A"
    if {P,L}=={"B","C"}: return "C/B"
    if (P,L)==("B","B"):
        twicep=next(u for u,n in Counter(p).items() if n==2)
        twicel=next(u for u,n in Counter(l).items() if n==2)
        common=sum(p[i]==twicep and l[i]==twicel for i in range(6))
        if common not in (0,1):
            raise ValueError("duplicated original incidence")
        return "B/B-overlap" if common else "B/B-disjoint"
    return None

def exact_original_W32_signed_index(model):
    """All authentic 62,370 LEFT-physical Q, indexed by genuine LINE IDs."""
    s,V,a,inc,f,g,_,_=_original_source(model)
    if (s,V,a)!=(2,15,6):
        raise ValueError("only real complete symplectic W32 finite oracle")
    rows=tuple(Q for Q,_ in selected_left_six(model))
    if len(rows)!=62370 or len(set(rows))!=62370:
        raise AssertionError("true original W32 left six-flag census changed")
    posting=[set() for _ in range(V)]
    kinds=[]
    for i,Q in enumerate(rows):
        kinds.append(immutable_original_sixflag_class(Q,inc))
        for source_l in {inc[j][1] for j in Q}:
            posting[source_l].add(i)
    return dict(rows=rows,source_class=tuple(kinds),
                line_posting=tuple(frozenset(s) for s in posting),
                incidences=inc,left=f,right=g)

def exact_original_W32_signed_swap(model,u,v,index=None):
    """Exact signed birth/death counts for WHOLE original line factor images."""
    s,V,a,inc,f,g,_,_=_original_source(model)
    if (s,V,a)!=(2,15,6):
        raise ValueError("true original W32 finite reference only")
    if any(type(i) is not int or i<0 or i>=V for i in (u,v)) or u==v:
        raise ValueError("two distinct actual original line source IDs")
    if index is None:index=exact_original_W32_signed_index(model)
    if (index["incidences"],index["left"],index["right"])!=(inc,f,g):
        raise ValueError("index belongs to another complete original global map")
    new=list(g)
    new[u],new[v]=new[v],new[u]
    new=tuple(new)
    if set(new)!=set(g):raise AssertionError("global right support mutated")
    touched=index["line_posting"][u] | index["line_posting"][v]
    born=Counter();dead=Counter();persist=Counter()
    witnesses=[]
    for row in sorted(touched):
        Q=index["rows"][row]
        old=classify_seven_prechecked(Q,f,g,inc)
        now=classify_seven_prechecked(Q,f,new,inc)
        static=index["source_class"][row]
        if (old is not None and old!=static) or (now is not None and now!=static):
            raise AssertionError("true ORIGINAL Q changed positive GF5 class")
        if old is None and now is not None:
            born[now]+=1
            if len(witnesses)<12:witnesses.append(("birth",now,Q))
        elif old is not None and now is None:
            dead[old]+=1
            if len(witnesses)<12:witnesses.append(("death",old,Q))
        elif old is not None:
            persist[old]+=1
    delta={c:born[c]-dead[c] for c in SEVEN}
    return {
      "actual_source_factor_swap":(u,v),
      "new_complete_global_original_LINE_map":new,
      "touched_true_original_Q":len(touched),
      "all_original_left_Q":len(index["rows"]),
      "births":{c:born[c] for c in SEVEN},
      "deaths":{c:dead[c] for c in SEVEN},
      "persisting_touched":{c:persist[c] for c in SEVEN},
      "signed_class_deltas":delta,
      "signed_seven_total_delta":sum(delta.values()),
      "signed_seven_GF5_R3_floor_numerator_delta":
          sum(R3_CERTIFIED_FLOORS[c]*delta[c] for c in SEVEN),
      "original_sixflag_transition_witnesses":tuple(witnesses),
      "one_same_original_Q_cross_positive_class_transition":False,
      "all_h_central_original_positive_bound_NOT_PROVED":True,
      "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }

def exact_permutation_involution_balance(maps,u,v,score):
    """Classical FULL closed permutation-orbit signed drift cancellation."""
    maps=tuple(tuple(row) for row in maps)
    if not maps or len(set(maps))!=len(maps):
        raise ValueError("unique nonempty original complete permutation orbit")
    n=len(maps[0]); support=set(maps[0])
    if not 0<=u<n or not 0<=v<n or u==v or any(
        len(x)!=n or set(x)!=support for x in maps):
        raise ValueError("invalid original source swap or complete support")
    entire=set(maps)
    pos=neg=0
    for m in maps:
        nextmap=list(m);nextmap[u],nextmap[v]=nextmap[v],nextmap[u]
        target=tuple(nextmap)
        if target not in entire:raise ValueError("incomplete swap-closed orbit")
        d=score(target)-score(m)
        if type(d) is not int:raise ValueError("historical count must be integer")
        pos+=max(d,0);neg+=max(-d,0)
    if pos!=neg:raise AssertionError("involution net signed flux nonzero")
    return dict(positive=pos,negative=neg,net=0,
                original_center_sign_known=False)
