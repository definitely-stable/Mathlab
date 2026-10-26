"""HYP-105 #230 AA4-CWNO: supersextic completion noise in coherent packets.

Conditional on the *infinite genuine symplectic paired-subfield packing
construction* of PR #651: every coherent packet has one first-copy hub
(c_j,c_j), and a common base incidence flag (p,l) belongs to a given
packet's retained F_j iff hub j is adjacent to free corner (z_p,Z_l).

For t=2^k, k>=4, s=t^2, n=(t+1)(t^2+1), d=t+1,
e=n*d, R=floor(n/256), any three packets have common base flags
E>=5e/8. For each triple of hubs, each chosen designated x-return
at one hub and each third free corner with a different source point
forms TWO distinct simple (not rainbow) physical C6s.

All such cycles have exactly ONE x-returning wedge. No overcount
between different hub triples or the chosen wedge/third free corner.
  W2x >= (15/32)*binom(R,3)*e^2*d
      >= 2^(-33)*t^18 = 2^(-33)*s^9.
The universal genuine-GQ source spectral pencil upper is
  Jx <= 2V(s-1)+2(s^2+1)(a-1) <= 9s^4,
so the average over ALL x-returning physical wedges
  mean comp6 >= 2^(-33)/9 * s^5.

This refutes proposed map-uniform average O(s^2), even O(s^4),
on the dyadic subsequence s=t^2, *provided PR #651's source
packing theorem is valid*. It does NOT refute root accepted 7 GF5
six-source-ID Omega(s^6): that same coherent packet family has
abundant positive accepted D6; these defective C6s are not D6.

Finite W(3,4) protected 3-hub/3-free template below independently
tests the local structural C6 mechanism, not infinite packet packing.
"""
from itertools import combinations
from math import comb, isqrt

from hyp105_b1_symplectic import symplectic_gq
from hyp105_physical_degree_energy import minimal_alphabet, _verify_typed_injections
from hyp105_physical_rainbow_c6 import build_original_physical_graph
from hyp105_local_return_completion_kernel import (
    returning_wedge_completion_kernel, independent_four_path_dfs,
)


def coherent_packet_completion_lower(k):
    """EXACT-integer arithmetic for k>=4; source packet existence is prior #651.

    Fractions are represented as numerators, NOT rounded to false equalities.
    This validates coefficient gates, not actual construction of huge fields.
    """
    if type(k) is not int or k<4:
        raise ValueError("coherent three-packet lemma requires k>=4")
    t=1<<k
    s=t*t
    n=(t+1)*(t*t+1)
    d=t+1
    e=n*d
    R=n//256
    V=(s+1)*(s*s+1)
    # Avoid an O(a) minimal_alphabet loop: k=128 would mean an
    # astronomical physical alphabet; symbolic constant audits must
    # run in logarithmic time with integer square root.
    a=(1+isqrt(1+8*V))//2
    if comb(a,2)<V:
        a+=1
    if R<3 or 512*R<n or comb(2*s*s+1,2)<V:
        raise AssertionError("packet count/minimal physical alphabet gate failed")
    # For any 3 source-paired packets E>=e-3*(e/8)=5e/8.
    # Original-source point-pencils in the common E carry at least
    # 5ed/32 unordered distinct-line cherries by Cauchy-Schwarz.
    # Every such cherry has >=e/2 distinct-point free z corners.
    if 5*d<8 or n<8:
        raise AssertionError("pencil common-flag lower assumptions failed")
    lower_num=15*comb(R,3)*e*e*d
    lower_den=32
    if lower_num*2**33 < lower_den*t**18:
        raise AssertionError("infinite source-packet W2x lower constant failed")

    uniform_J=2*V*(s-1)+2*(s*s+1)*(a-1)
    if (V>2*s**3 or a-1>2*s*s or
            4*(s*s+1)>5*s*s or uniform_J>9*s**4):
        raise AssertionError("genuine source spectral Jx<=9s^4 gate failed")
    return {
        "k":k,"t":t,"s":s,"n":n,"d":d,"e":e,"R":R,
        "V":V,"a":a,
        "triple_common_base_flags_lower_num":5*e,
        "triple_common_base_flags_lower_den":8,
        "chosen_hub_x_pencil_cherries_lower_num":5*e*d,
        "chosen_hub_x_pencil_cherries_lower_den":32,
        "W2x_lower_numerator":lower_num,
        "W2x_lower_denominator":lower_den,
        "W2x_universal_power_lower_denominator":2**33,
        "universal_Jx_spectral_integer_upper":uniform_J,
        "universal_Jx_coarse_upper":9*s**4,
        "mean_comp_lower_numerator":lower_num,
        "mean_comp_lower_denominator":lower_den*uniform_J,
        "mean_comp_coarse_power_lower_denominator":9*2**33,
        "all_h_mean_O_s2_falsified_conditional_on_PR651_packing":True,
        "pr651_packing_independently_reproved_here":False,
        "root_GF5_sevenclass_disproved":False,
    }


def protected_three_hub_source_witness_w34():
    """Finite 3-hub x-return template with real ORIGINAL W(3,4) flags.

    Greedy deterministic disjoint source factors across three packets:
    each hub has TWO flags through a common original point plus ONE
    flag through a distinct point, so its physical adjacency contains
    free corners a=(3,5), c=(3,6), z=(4,7).
    The two 3-hub C6 completions of a-h0-c use real original
    incidence IDs, six unique source flags in each selected C6,
    but only five physical x-coordinate symbols (in fact <=5).
    It does not instantiate an infinite subfield packing.
    """
    _,points,lines,flags=symplectic_gq(2)
    V=85
    a=minimal_alphabet(V)
    if a!=14:
        raise AssertionError("wrong physical alphabet")
    incident=[[] for _ in range(V)]
    for p,l in flags:
        incident[p].append(l)
    for row in incident:
        row.sort()
    chosen=[]
    used_points=set()
    used_lines=set()
    for hub in range(3):
        found=None
        for p in range(V):
            if p in used_points:
                continue
            first=[l for l in incident[p] if l not in used_lines]
            if len(first)<2:
                continue
            two=first[:2]
            for q in range(V):
                if q==p or q in used_points:
                    continue
                avail=[l for l in incident[q]
                       if l not in used_lines and l not in two]
                if avail:
                    found=(p,q,two[0],two[1],avail[0])
                    break
            if found is not None:
                break
        if found is None:
            raise AssertionError("cannot instantiate three genuine source packets")
        p,q,l1,l2,l3=found
        chosen.append(found)
        used_points.update((p,q))
        used_lines.update((l1,l2,l3))
    f=[None]*V
    g=[None]*V
    source=set(flags)
    protected={}
    hubs=[]
    for j,(p,q,l1,l2,l3) in enumerate(chosen):
        for pair in ((p,l1),(p,l2),(q,l3)):
            if pair not in source:
                raise AssertionError("template uses nonexistent original source flag")
        f[p]=(j,3)
        f[q]=(j,4)
        g[l1]=(j,5)
        g[l2]=(j,6)
        g[l3]=(j,7)
        hubs.append((j,j))
        protected[j]=((p,l1),(p,l2),(q,l3))
    all_pairs=list(combinations(range(a),2))
    for labels in (f,g):
        occupied={pair for pair in labels if pair is not None}
        unused=iter(pair for pair in all_pairs if pair not in occupied)
        for k in range(V):
            if labels[k] is None:
                labels[k]=next(unused)
    _verify_typed_injections(a,V,f,g)
    adj,source_arcs=build_original_physical_graph(4,f,g,flags)
    A=(3,5)
    C=(3,6)
    Z=(4,7)
    h0,h1,h2=hubs
    cycles=(
        (A,h0,C,h1,Z,h2),
        (A,h0,C,h2,Z,h1),
    )
    source_ids=[]
    for cyc in cycles:
        if len(set(cyc))!=6:
            raise AssertionError("non-simple physical six-cycle")
        for i in range(6):
            if cyc[(i+1)%6] not in adj[cyc[i]]:
                raise AssertionError("protected 6cycle missing original source flag edge")
        ids=tuple(source_arcs[cyc[i],cyc[(i+1)%6]] for i in range(6))
        if len(set(ids))!=6:
            raise AssertionError("protected cycle uses a repeated original incidence ID")
        if len({v[0] for v in cyc})==6:
            raise AssertionError("protected x-return cycle accidentally rainbow")
        source_ids.append(ids)
    if len({frozenset(ids) for ids in source_ids})!=2:
        raise AssertionError("different hub assignments gave same original source sixset")
    k=returning_wedge_completion_kernel(adj,A,h0,C)
    if k<2 or independent_four_path_dfs(adj,A,h0,C)!=k:
        raise AssertionError("genuine source x-return wedge lacks two independently certified cycles")
    actual0=flags[source_arcs[A,h0]]
    actual1=flags[source_arcs[h0,C]]
    if actual0[0]!=actual1[0] or actual0[1]==actual1[1]:
        raise AssertionError("not two original flags sharing one source point")
    return {
        "s":4,"V":V,"a":a,
        "protected_hubs":tuple(hubs),
        "protected_free_corners":(A,C,Z),
        "protected_source_packets":tuple(chosen),
        "protected_cycles":cycles,
        "six_actual_original_source_flag_IDs_per_cycle":tuple(source_ids),
        "both_protected_cycles_have_six_distinct_original_flags":True,
        "actual_kernel_completion_count_at_hub0":k,
        "source_pencil_backtrack_certified":True,
        "infinite_subfield_packing_instantiated":False,
        "root_sevenclass_disproved":False,
    }
