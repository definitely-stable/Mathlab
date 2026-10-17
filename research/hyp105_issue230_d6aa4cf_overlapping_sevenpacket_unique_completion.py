"""HYP-105 AA4-CF: genuine original sevenpacket overlap, five-edge unique completion.

Sixpacket families A=(0,1,2,3,4,5), B=(0,1,2,3,4,6) share
five WHOLE original LINE-factor swap packets and have DISTINCT sixth
packets. Their physical right 2regular masks live on ONE 128-state
cube of complete globally injected original right maps.

If original six-incidence Q_A and Q_B select the same original LINE
factor in each shared packet, then no common complete global map can
make BOTH six-edge projections physical 2factors: the common five
unordered physical edges admit at most ONE completing physical edge.
The two actual sixth edges are globally DISTINCT by injection.

Mixed pair Gram J(t,u) is computed exactly on the SAME global cube;
a source-first joint weighted physical UPPER surrogate is an exact
bilinear contraction. This is NOT an original-center positive GF5
lower bound, and no all-h root A/B/C claim is made.
"""
from collections import Counter
from fractions import Fraction

from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4bq_all_seven_reverse_switching import (
    apply_disjoint_factor_swaps, validate_disjoint_factor_swaps,
)
from hyp105_issue230_d6aa4ce_shared_sixpacket_xor_coupling import (
    orientation_of_true_original_Q,
)
from hyp105_issue230_d6aa4by_original_independent_2factor_kernel import (
    original_six_packet_source_line_A, physical_right_is_six_vertex_two_regular,
)
from hyp105_issue230_d6aa4br_all_seven_signed_source_flux import (
    immutable_original_sixflag_class,
)
from hyp105_g5e2b3e1b0_seven_signature import (
    R3_CERTIFIED_FLOORS, classify_seven_prechecked,
)
from hyp105_g5e2b3e1a_fixed_leading import selected_left_six

PACKETS7 = tuple((2*i,2*i+1) for i in range(7))
SEVEN=7
CUBE=1<<SEVEN
FAMILIES={"A":(0,1,2,3,4,5),"B":(0,1,2,3,4,6)}
FIVE_MASK=31


def _validate(g, packets):
    full=tuple(tuple(e) for e in g)
    pairs=validate_disjoint_factor_swaps(len(full),packets)
    if len(pairs)!=SEVEN:
        raise ValueError("exactly 7 disjoint WHOLE ORIGINAL LINE packets needed")
    normalized=[]
    for e in full:
        if len(e)!=2 or any(type(z) is not int or z<0 for z in e) or e[0]==e[1]:
            raise ValueError("each original physical pair-edge has two distinct coordinates")
        normalized.append(tuple(sorted(e)))
    if len(set(normalized))!=len(normalized):
        raise ValueError("original full right physical pair map must be injective")
    return tuple(normalized),pairs


def _regular6(edges):
    degree=Counter(v for e in edges for v in e)
    return int(len(degree)==6 and all(n==2 for n in degree.values()))


def original_shared_five_graph_unique_completion(edges5, sixth1, sixth2):
    """Executable five-edge deterministic uniqueness falsifier.

    Input: 5 distinct unordered edges, and TWO globally distinct
    candidate sixth physical edges, all distinct. At most one of the
    two candidate physical six-edge degree-two graphs is admissible.
    """
    whole=tuple(tuple(sorted(e)) for e in (*edges5,sixth1,sixth2))
    if len(edges5)!=5 or any(len(e)!=2 or e[0]==e[1] for e in whole):
        raise ValueError("five distinct physical edges and two sixth edges required")
    if len(set(whole))!=7:
        raise ValueError("all seven candidate physical edges must be distinct")
    a,b=(_regular6(whole[:5]+(whole[j],)) for j in (5,6))
    if a and b:
        raise AssertionError("five fixed physical edges accepted two distinct completions")
    return a,b


def _lift_orientation(local_mask, family):
    if family not in FAMILIES or type(local_mask) is not int or not 0<=local_mask<64:
        raise ValueError("six actual original source packet orientation bits required")
    return sum((1<<global_idx)
               for local_i,global_idx in enumerate(FAMILIES[family])
               if local_mask>>local_i&1)


def source_original_orientation_7(Q,inc,pairs,V,family):
    """SAME true six original incidence IDs at all 128 complete maps."""
    if family not in FAMILIES:raise ValueError("family A or B")
    pairs=validate_disjoint_factor_swaps(V,pairs)
    if len(pairs)!=SEVEN:
        raise ValueError("exactly seven globally disjoint original LINE packets required")
    sub=tuple(pairs[i] for i in FAMILIES[family])
    t=orientation_of_true_original_Q(Q,inc,sub,V)
    return _lift_orientation(t,family)


def physical_overlapping_masks(g,packets=PACKETS7):
    """A and B masks from ONE complete g, 14 distinct source-factor images."""
    full,pairs=_validate(g,packets)
    images=tuple((full[u],full[v]) for u,v in pairs)
    out={}
    for family,subset in FAMILIES.items():
        chosen=tuple(images[i] for i in subset)
        bitmask=[]
        for x in range(CUBE):
            actual=tuple(chosen[j][(x>>source_idx)&1]
                         for j,source_idx in enumerate(subset))
            bitmask.append(_regular6(actual))
        out[family]=tuple(bitmask)
    # FIVE actual source factors / physical edge images shared at each
    # SAME global state; exclusive sixth actual edges globally distinct.
    if any(out["A"][x] and out["B"][x] for x in range(CUBE)):
        raise AssertionError("one fixed physical 5-edge graph had two completions")
    return {"A":out["A"],"B":out["B"],"packets":pairs,"edges":images,
            "A_active":sum(out["A"]),"B_active":sum(out["B"]),
            "unshifted_joint_active":0}


def _translated_full_mask(base, lifted_orientation):
    return sum((1<<x) for x in range(CUBE) if base[x^lifted_orientation])


def mixed_pair_gram(masks):
    """Exact 64x64 mixed physical pair Gram on ONE 7D cube.

    Entry J[t,u] counts full 128 global maps at which A-orientation t
    and B-orientation u are simultaneously physical 2regular.
    Bitset intersection is an exact arithmetic shortcut, not a
    probabilistic model.
    """
    if len(masks["A"])!=CUBE or len(masks["B"])!=CUBE:
        raise ValueError("128-state actual physical family masks required")
    L={family:tuple(_translated_full_mask(
        masks[family],_lift_orientation(t,family)) for t in range(64))
       for family in FAMILIES}
    matrix=tuple(tuple((L["A"][t]&L["B"][u]).bit_count()
                       for u in range(64)) for t in range(64))
    if any(matrix[t][u] for t in range(64) for u in range(64)
           if (t&FIVE_MASK)==(u&FIVE_MASK)):
        raise AssertionError("same five ORIGINAL LINE pins accepted two distinct sixth edges")
    if any(x<0 or x>128 for row in matrix for x in row):
        raise AssertionError("mixed physical Gram cardinality invalid")
    return {"J":matrix,"A_masks":L["A"],"B_masks":L["B"],
            "same_five_orientation_zero":True,
            "max_joint_maps":max(max(row) for row in matrix),
            "positive_orientation_pair_count":sum(bool(x) for row in matrix for x in row)}


def source_families_W32(model,packets=PACKETS7):
    """Original left SIX-DISTINCT-incidence source class and two families."""
    s,V,a,inc,f,g,_,_=_original_source(model)
    if (s,V,a)!=(2,15,6):
        raise ValueError("TRUE original W32 only; all-h proof separate")
    g,pairs=_validate(g,packets)
    H={k:[0]*64 for k in FAMILIES}
    N={k:[0]*64 for k in FAMILIES}
    Q={k:[] for k in FAMILIES}
    for flags,_ in selected_left_six(model):
        tag=immutable_original_sixflag_class(flags,inc)
        if tag not in R3_CERTIFIED_FLOORS:
            continue
        for fam,idx in FAMILIES.items():
            sub=tuple(pairs[i] for i in idx)
            if original_six_packet_source_line_A(flags,inc,sub,V):
                orient=orientation_of_true_original_Q(flags,inc,sub,V)
                weight=R3_CERTIFIED_FLOORS[tag]
                H[fam][orient]+=weight
                N[fam][orient]+=1
                Q[fam].append((tuple(flags),orient,weight,tag))
    if any(not Q[k] for k in FAMILIES):
        raise AssertionError("real W32 true source Q must populate both sixpacket families")
    if {q for q,_,_,_ in Q["A"]}&{q for q,_,_,_ in Q["B"]}:
        raise AssertionError("one six-original-ID Q cannot hit SEVEN distinct LINE packets")
    return {"H":{k:tuple(v) for k,v in H.items()},
            "N":{k:tuple(v) for k,v in N.items()},
            "Q":{k:tuple(v) for k,v in Q.items()},
            "counts":{k:len(v) for k,v in Q.items()},
            "source_only_f_not_redrawn_g":True}


def shared_twofamily_W32(model,packets=PACKETS7,verify_original=False):
    """Exact true W32 ORIGINAL sevenpacket mixed necessary physical certificate."""
    s,V,a,inc,f,g,_,_=_original_source(model)
    g,pairs=_validate(g,packets)
    physical=physical_overlapping_masks(g,pairs)
    source=source_families_W32(model,pairs)
    gram=mixed_pair_gram(physical)
    H=source["H"]; N=source["N"]; J=gram["J"]
    A=gram["A_masks"]; B=gram["B_masks"]
    fA=tuple(sum(H["A"][t]*((A[t]>>x)&1) for t in range(64))
             for x in range(CUBE))
    fB=tuple(sum(H["B"][u]*((B[u]>>x)&1) for u in range(64))
             for x in range(CUBE))
    direct=sum(fA[x]*fB[x] for x in range(CUBE))
    by_gram=sum(H["A"][t]*H["B"][u]*J[t][u]
                for t in range(64) for u in range(64))
    if direct!=by_gram:
        raise AssertionError("mixed sevenpacket second moment != true XOR pair Gram")
    # The EXACT count of TRUE ORIGINAL Q_A x Q_B pairs whose five
    # source LINE pins AGREE; each such pair is impossible at EVERY
    # full original globally injected map.
    same_five_N=sum(N["A"][t]*N["B"][u]
                    for t in range(64) for u in range(64)
                    if (t&FIVE_MASK)==(u&FIVE_MASK))
    same_five_H=sum(H["A"][t]*H["B"][u]
                    for t in range(64) for u in range(64)
                    if (t&FIVE_MASK)==(u&FIVE_MASK))
    zero_J_N=sum(N["A"][t]*N["B"][u]
                    for t in range(64) for u in range(64) if J[t][u]==0)
    zero_J_H=sum(H["A"][t]*H["B"][u]
                    for t in range(64) for u in range(64) if J[t][u]==0)
    if zero_J_N<same_five_N or zero_J_H<same_five_H:
        raise AssertionError("mixed physical impossibility must include unique-completion charge")
    actual={}
    if verify_original:
        maps=tuple(apply_disjoint_factor_swaps(
            g,pairs,tuple(j for j in range(SEVEN) if (x>>j)&1))
            for x in range(CUBE))
        for fam in FAMILIES:
            scores=[0]*CUBE
            for Q,torient,weight,tag in source["Q"][fam]:
                lifted=_lift_orientation(torient,fam)
                for x in range(CUBE):
                    phys=physical_right_is_six_vertex_two_regular(Q,inc,maps[x])
                    if int(phys)!=int((gram[fam+"_masks"][torient]>>x)&1):
                        raise AssertionError("literal TRUE original physical Q != 7D translated family mask")
                    accepted=classify_seven_prechecked(Q,f,maps[x],inc)
                    if accepted is not None:
                        if not phys or accepted!=tag:
                            raise AssertionError("true historical GF5 must be physical-mask subset")
                        scores[x]+=weight
            envelope=fA if fam=="A" else fB
            if any(scores[x]>envelope[x] for x in range(CUBE)):
                raise AssertionError("historical GF5 exceeded true twofamily physical envelope")
            actual[fam]=tuple(scores)
        for t in range(64):
            if not N["A"][t]:continue
            for u in range(64):
                if N["B"][u] and (t&FIVE_MASK)==(u&FIVE_MASK):
                    if gram["A_masks"][t]&gram["B_masks"][u]:
                        raise AssertionError("true original crossfamily matching pins overlapped")
    return {
        "s":s,"original_source_Q_counts":source["counts"],
        "physical_A_active":physical["A_active"],"physical_B_active":physical["B_active"],
        "mixed_physical_Gram_J":J,
        "source_unweighted_histograms":N,
        "source_weighted_histograms":H,
        "total_crossfamily_original_Q_pairs":source["counts"]["A"]*source["counts"]["B"],
        "five_pins_same_source_Q_pairs_forbidden":same_five_N,
        "five_pins_same_weight_products_forbidden":same_five_H,
        "total_physically_forbidden_original_Q_pairs":zero_J_N,
        "total_physically_forbidden_weight_products":zero_J_H,
        "physically_joint_possible_orientation_pairs":gram["positive_orientation_pair_count"],
        "physical_family_envelope_A":fA,"physical_family_envelope_B":fB,
        "mixed_envelope_cross_moment_sum":direct,
        "mixed_envelope_cross_moment_by_Gram":by_gram,
        "historical_selected_Q_weighted_7cube":actual,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }
