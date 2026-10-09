"""HYP-105 G5-E2-B3.2-D: SAME-label four/six GF(5) risk diagnostics.

All-s proved NECESSARY obstruction:
 R2(B_s) >= F4*Q4(s)/51^4, F4=exact signed GF5 C4/C4 flow count.
Here Q4(s) is #factor-disjoint 4-sets with matching left/right *dual*
column C4, not the general count of four-column GF5 trades.
Uniform independent injective labels satisfy EXACTLY
 E[Q4(s)]=3*M4(G_s)*((a)_4/(K)_4)^2=Theta(s^4),
where M4(G_s) is the exact number of factor-4-matchings.
These are strict all-h MODEL statements, no general per-label lower.
The finite checker avoids binom(425,4), and computes FULL unit-weighted
T4 separately; exact full-palette GF5 R2/R3 is ONLY for one disclosed,
deterministic, 7-column witness-enriched subset of the SAME labeling.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb
import json

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_g5e2b3c_plucker_shift import plucker_shift_model
from hyp105_g5e2b3b2_coincident_cycles import (
    check_input, exact_coincident_c6,
)
from hyp105_g5e1_motifs import topology_gate
from hyp105_g5e2b1_energy import (
    risk_from_pair_energy, single_signed_trade_mitm,
)

C4_LEFT=((0,1),(1,2),(2,3),(0,3))
C4_FOUR_SUPPORTS=tuple(tuple(C4_LEFT[i] +
                           tuple(4+x for x in C4_LEFT[i]))
                       for i in range(4))
C4_SIGNS=(1,-1,1,-1)


def closed_form_c4_GF5_flow_weight():
    """Pure algebraic identity: 531 valid nowhere-zero checksum4 flows.

    For each of four adjacent C4 column-vertex pairs there are TWO
    colored physical coordinate edges. Let t_i be their GF5 sum.
    Each column checksum imposes t_(i-1)+t_i=4 mod 5, hence along
    C4 we have t0=t2=t, t1=t3=4-t. For each t in GF5, its
    2-coordinate nonzero representations number 4 if t=0,
    otherwise 3 (all 5 minus the zero first/zero second cases).
    Sum_{t in GF5} c(t)^2 * c(4-t)^2 = 2*4^2*3^2 + 3*3^4 = 531.
    This is a FOUR-column GF5 template count, not all family R2.
    """
    counts=tuple(sum(1 for x in range(1,5)
                     for y in range(1,5) if (x+y)%5==t)
                 for t in range(5))
    if counts != (4,3,3,3,3):
        raise AssertionError("GF5 nonzero two-coordinate count wrong")
    result=sum(counts[t]**2*counts[(4-t)%5]**2 for t in range(5))
    if result!=531:
        raise AssertionError("closed-form GF5 four-cycle weight changed")
    return result


def exact_c4_GF5_flow_weight():
    """Independently implemented 51^2-side GF5 additive-energy oracle."""
    w=single_signed_trade_mitm(C4_FOUR_SUPPORTS,C4_SIGNS,8)
    f=w["weighted_flow_count"]
    if f != closed_form_c4_GF5_flow_weight():
        raise AssertionError("independent exact GF5 C4 MITM vs closed form mismatch")
    return f


def physical_four_cycles(labels, alphabet):
    """Every undirected simple C4 of a simple physical K_a subgraph ONCE.

    Four physical vertices; C4 unique up to cyclic rotations and reversal.
    Anchor the minimum physical vertex first; keep a smaller first
    neighbor than the last. Return the four named factor endpoint IDs
    in their cyclic physical-edge order. Distinct input pairs mandatory.
    """
    if alphabet<4 or len(set(labels))!=len(labels):
        raise ValueError("injective physical pair labels required")
    adj=[[] for _ in range(alphabet)]
    for idx,pair in enumerate(labels):
        if len(pair)!=2 or not (0<=pair[0]<pair[1]<alphabet):
            raise ValueError("invalid physical pair")
        u,v=pair
        adj[u].append((v,idx))
        adj[v].append((u,idx))
    adj=[tuple(sorted(a)) for a in adj]
    for anchor in range(alphabet):
        for j,ej in adj[anchor]:
            if j<=anchor:
                continue
            for k,ek in adj[j]:
                if k<=anchor or k==j:
                    continue
                for last,e_last in adj[k]:
                    if last<=j or last<=anchor:
                        # Canonical orientation: j < last.
                        continue
                    if last==anchor or last==j:
                        continue
                    for end,e_end in adj[last]:
                        if end==anchor:
                            if len({ej,ek,e_last,e_end})!=4:
                                raise AssertionError("C4 repeated pair edge")
                            yield (ej,ek,e_last,e_end)


def exact_coincident_c4(model, cycle_limit=60000, witness_limit=3):
    """Full Q4 of a finite pair-injective GQ factor incidence system.

    For each left C4, join four REAL incident line endpoints with
    distinct lines whose right pair labels form the SAME column C4.
    Right physical pair edges must share four distinct successive
    coordinates. Equal column-adjacency sets is checked as well.
    Complexity bounded by O(C4(left)*Delta^4), no binom(N,4).
    """
    alphabet,left,right,incidences=check_input(model)
    options=[[] for _ in left]
    edge_lookup={}
    for i,(p,l) in enumerate(incidences):
        options[p].append(l)
        edge_lookup[(p,l)]=i
    for row in options:
        row.sort()
    cycles=0
    Q=0
    witnesses=[]
    for points in physical_four_cycles(left,alphabet):
        cycles+=1
        if cycles>cycle_limit:
            raise RuntimeError("exact four-cycle resource budget exhausted")
        # Four physical line-pair labels may form a cycle in any
        # orientation. The dual adjacency must be same (0-1-2-3-0).
        selected=[]
        used=set()
        shared=[]

        def walk(depth):
            nonlocal Q
            if depth==4:
                pairs=[right[l] for l in selected]
                close=set(pairs[3]) & set(pairs[0])
                if len(close)!=1 or next(iter(close)) in shared:
                    return
                if len(set(shared+list(close)))!=4:
                    return
                colids=tuple(edge_lookup[(p,l)]
                             for p,l in zip(points,selected))
                if len(set(colids))!=4:
                    raise AssertionError("factor incidence not matching")
                Q+=1
                if len(witnesses)<witness_limit:
                    witnesses.append(colids)
                return
            for line in options[points[depth]]:
                if line in used:
                    continue
                pair=right[line]
                intersection=() if not selected else (
                    set(right[selected[-1]]) & set(pair))
                if selected and (len(intersection)!=1 or
                                 next(iter(intersection)) in shared):
                    continue
                used.add(line)
                selected.append(line)
                if depth:
                    shared.append(next(iter(intersection)))
                walk(depth+1)
                if depth:
                    shared.pop()
                selected.pop()
                used.remove(line)

        walk(0)
    weight=exact_c4_GF5_flow_weight()
    return {
        "Q4":Q,
        "physical_left_C4":cycles,
        "witnesses":witnesses,
        "GF5_C4_flow_weight":weight,
        "fixed_label_R2_lower":f"{weight*Q}/51^4",
        "all_h_strict_R2_upper_proved":False,
        "complete_full_51_palette_R2":False,
    }


def exact_unit_T4(supports,dimension,max_pairs=105000):
    """Full exact UNIT signed-2v2 event census by pair sum signatures.

    Weight all ones is GF5 admissible checksum4. For two unit columns
    any coordinate sum is at most 2; using radix-5 integers has NO
    carries even when adding two pair signatures. Different supports
    guarantee pair signature collisions cannot overlap a column ID.
    Counts all distinct unordered signed 2v2 events and all distinct
    4-column sets admitting >=1 such event.
    """
    if len(supports)<4 or comb(len(supports),2)>max_pairs:
        raise ValueError("unit four-event pair budget exceeded")
    if len({tuple(sorted(s)) for s in supports})!=len(supports):
        raise ValueError("duplicate physical columns")
    weights=[5**i for i in range(dimension)]
    columns=[]
    for row in supports:
        if len(row)!=4 or len(set(row))!=4 or not all(
                isinstance(i,int) and 0<=i<dimension for i in row):
            raise ValueError("invalid exact support4")
        columns.append(sum(weights[i] for i in row))
    groups=defaultdict(list)
    for i,j in combinations(range(len(columns)),2):
        groups[columns[i]+columns[j]].append((i,j))
    events=0
    subsets=set()
    for bucket in groups.values():
        if len(bucket)<2:
            continue
        for x,y in combinations(bucket,2):
            ids=x+y
            if len(set(ids))!=4:
                raise AssertionError("distinct column signatures permit no shared-ID energy collisions")
            events+=1
            subsets.add(tuple(sorted(ids)))
    return {
        "N":len(supports),"pairs":comb(len(supports),2),
        "unit_signed_four_events":events,
        "unit_four_subsets":len(subsets),
        "unit_R2_probability_floor":f"{events}/51^4",
        "GF5_weighted_exact_R2":False,
        "asymptotic_R2_upper_proved":False,
    }


def selected_c6_witness_sample(model,extra=1):
    """Disclosure: purposively witness-enriched, NOT random/representative."""
    report=exact_coincident_c6(model)
    witnesses=report["witness_column_ids_in_canonical_left_cycle_order"]
    if not witnesses:
        raise AssertionError("required positive C6 witness absent")
    six=list(witnesses[0])
    if len(six)!=6 or len(set(six))!=6:
        raise AssertionError("witness not six distinct column IDs")
    six+= [i for i in range(model["N"]) if i not in six][:extra]
    if len(six)!=6+extra:
        raise AssertionError("not enough unique sample columns")
    return tuple(six),report["exact_coincident_C6_factor_matchings_D"]


def exact_weighted_sample(model,selected=None,max_GF5_events=12):
    """Exact full 51-palette R2 and ALL exact GF5 3v3 events on 7 columns.

    For 7 columns at most 7*10=70 different 3v3 events.
    Topology is only a ZERO-FLOW gate; surviving events get exact
    51^3-side GF5 meet-in-middle (not guessed positive).
    """
    if selected is None:
        selected,Ds=selected_c6_witness_sample(model)
    else:
        selected=tuple(selected)
        Ds=None
    if len(selected)!=7 or len(set(selected))!=7:
        raise ValueError("seven distinct selected column IDs required")
    if any(i<0 or i>=model["N"] for i in selected):
        raise ValueError("column outside real incidence")
    supports=tuple(model["supports"][i] for i in selected)
    R2=risk_from_pair_energy(supports,model["m"],max_local_assignments=150000)
    numerator=0
    candidates=0
    positive=0
    positive_witnesses=[]
    for six in combinations(range(7),6):
        for plus in combinations(six,3):
            minus=tuple(i for i in six if i not in plus)
            if plus>=minus:
                continue
            sub=tuple(supports[i] for i in plus+minus)
            signs=(1,1,1,-1,-1,-1)
            if not topology_gate(sub,signs,model["a"])[
                    "potential_nonzero_flow"]:
                continue
            candidates+=1
            if candidates>max_GF5_events:
                raise RuntimeError("exact 51^3-side GF5 event budget exhausted")
            exact=single_signed_trade_mitm(sub,signs,model["m"])
            flow=exact["weighted_flow_count"]
            numerator+=flow
            if flow:
                positive+=1
                if len(positive_witnesses)<3:
                    positive_witnesses.append({
                        "column_ids":[selected[i] for i in plus+minus],
                        "signs":[1,1,1,-1,-1,-1],
                        "GF5_flow_assignments":flow,
                    })
    if positive<1 or numerator<5643:
        raise AssertionError("required alternating C6 GF5 positive event lost")
    return {
        "N_in_full_model":model["N"],
        "selected_column_ids":selected,
        "selection_rule":"first canonical exact coincident-C6 witness + lowest unused column",
        "full_model_coincident_C6_D":Ds,
        "sample_exact_GF5_R2":str(R2["R2"]),
        "sample_exact_GF5_R2_numerator":R2["exact_disjoint_weight_assignments"],
        "sample_GF5_R2_denominator":51**4,
        "sample_all_six_signed_events":comb(7,6)*comb(6,3)//2,
        "sample_necessary_core_survivors":candidates,
        "sample_positive_GF5_six_events":positive,
        "sample_exact_GF5_R3":f"{numerator}/{51**6}",
        "sample_exact_GF5_R3_numerator":numerator,
        "sample_positive_examples":positive_witnesses,
        "whole_family_exact_GF5_R2":False,
        "whole_family_exact_GF5_R3":False,
        "strict_all_h_R2_R3_upper":False,
    }


def all_h_expected_Q4_lower(s):
    """Symbolic-uniform-in-h matching C4 expectation LOWER, not per label.

    #of factor 4-matchings is M4(G_s).
      E[Q4] = 3*M4 * ((a)_4/(K)_4)^2 (exact).
    Use greedy M4 >= product_{j=0}^3(N-2j*Delta)/24.
    This yields E[Q4] = Omega(s^4) and combined with existing
    accepted E[R2]=O(s^4), exact Theta(s^4) independent-label risk.
    """
    if not isinstance(s,int) or s<2 or s & (s-1):
        raise ValueError("s=2^h, h>=1 required")
    V=(s+1)*(s*s+1)
    N=V*(s+1)
    delta=s+1
    a=2
    while comb(a,2)<V:
        a+=1
    K=comb(a,2)
    m4=Fraction(1)
    for j in range(4):
        m4*=Fraction(N-2*j*delta,j+1)
    physical=Fraction(1)
    for j in range(4):
        physical*=Fraction(a-j,K-j)
    lower=3*m4*physical**2
    return {
        "s":s, "a":a, "K":K, "N":N,
        "factor_matching_count_lower":m4,
        "exact_E_Q4_identity":"3*M4(G_s)*((a)_4/(K)_4)^2",
        "E_Q4_lower":lower,
        "E_R2_lower":lower*exact_c4_GF5_flow_weight()/51**4,
        "asymptotic":"E[R2]=Theta(s^4) for independent uniform pair injections ONLY",
        "individual_R2_lower":False,
        "new_ASET_exponent":False,
    }


def report():
    results=[]
    for h in (1,2):
        for scheme in ("plucker-lex-mincollision","old-reverse-line"):
            model=(plucker_shift_model(h,"plucker-lex-mincollision")
                   if scheme!="old-reverse-line"
                   else pair_labeled_symplectic(h,"reverse-line"))
            q=exact_coincident_c4(model)
            u=exact_unit_T4(model["supports"],model["m"])
            chosen,Ds=selected_c6_witness_sample(model)
            local=exact_weighted_sample(model,chosen)
            results.append({
                "s":model["s"],"N":model["N"],"scheme":scheme,
                "Q4":q["Q4"],"unit_T4_signed_events":u["unit_signed_four_events"],
                "unit_T4_distinct_support_sets":u["unit_four_subsets"],
                "D6":Ds,
                "four_event_exact_GF5_weight":q["GF5_C4_flow_weight"],
                "full_R2_lower_from_Q4":q["fixed_label_R2_lower"],
                "exact_GF5_R2_on_selected_7":local["sample_exact_GF5_R2"],
                "exact_GF5_R3_on_selected_7":local["sample_exact_GF5_R3"],
                "positive_3v3_events_on_selected_7":
                    local["sample_positive_GF5_six_events"],
                "full_family_R2_R3_exact":False,
            })
    return {"cases":results,
            "all_h_theorem":"R2>=F4*Q4/51^4, E[Q4]=3*M4*P_C4^2",
            "all_h_R2_R3_upper_proved":False,
            "new_ASET_exponent":False}


if __name__=="__main__":
    print(json.dumps(report(),sort_keys=True,indent=2))
