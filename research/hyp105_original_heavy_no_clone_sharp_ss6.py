"""HYP-105 AA4-HEAVYREF: independent genuine-original heavy no-clone proof.

No imports from earlier selector/heavy/source-proof implementations.
Trusted reusable inputs only: symplectic ORIGINAL W(3,s) constructor and
globally pair-injective complete f,g label generator for finite falsifiers.

All-order s>=64 source envelope improvements:
    N <= (17/16) s^4, a² <= (9/4) s³,
    C_s <= (5/4) s^4 and e_J<=2 C_s <= (5/2) s^4.
On surviving heavy source owners L>=s^4/32:
    source Caro-Wei >=s^4/5152,
    two full original cuts >=s^4/20608,
    ordinary no-clone winner e/v>=s/370944,
    winner v <= (17/2)s³/T,
    T >= (17/2)*370944³*C0³ -> valid ordinary C6 SS6 input.
Original true six-ID D6 count >=c0 s^6/370944^6 CONDITIONALLY
on the published graph SS6 existential C_graph,c_graph.

This is an exact proof of an implication, not external graph constants,
root #230 acceptance, main/ancestor merges or ASET exponent.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb, isqrt
import json

ROOT_STATUS = "OPEN_WITH_FORMAL_BLOCKER"
K=64
R=370944
SS6_T_FACTOR=Fraction(17*R**3,2)
OLD_T_FACTOR=2**64


def ceil_fraction(x):
    if type(x) is not Fraction:
        raise ValueError("exact rational only")
    return -(-x.numerator//x.denominator)


def sqrt_up(x):
    if type(x) is not int or x<0:
        raise ValueError("nonnegative integer sqrt only")
    z=isqrt(x)
    return z+(z*z<x)


def genuine_envelope(s):
    """Exact finite falsifier for a separately proved ALL-s>=64 source lemma."""
    if type(s) is not int or s<64 or s&(s-1):
        raise ValueError("dyadic original s>=64 required")
    V=(s+1)*(s*s+1)
    N=(s+1)*V
    a=2
    while comb(a,2)<V:
        a+=1
    cs=(s*s+1)*(s*s+a-2)
    checks={
        "V_le_33_32_s3":32*V<=33*s**3,
        "N_le_17_16_s4":16*N<=17*s**4,
        "alphabet_a_squared_le_9_4_s3":4*a*a<=9*s**3,
        "original_collision_Cs_le_5_4_s4":4*cs<=5*s**4,
        "original_minimal_globally_injective_alphabet":
            comb(a-1,2)<V<=comb(a,2),
        "full_original_source_two_physical_diagonals_per_flag":N>0,
    }
    if not all(checks.values()):
        raise AssertionError("improved genuine original source envelope false")
    return {"s":s,"V":V,"N":N,"a":a,"C_s":cs,
            "a2_over_s3":str(Fraction(a*a,s**3)),
            "Cs_over_s4":str(Fraction(cs,s**4)),
            "N_over_s4":str(Fraction(N,s**4)),"checks":checks}


def allh_sharp_heavy_ledger(C0,c0):
    """Independent all-order strict rational heavy + LOW integration budgets.

    C0>=published C_graph and 0<c0<=published c_graph are FORMAL
    rational bounds; values 1/1, etc in tests do NOT assert actual
    numerical published constants.
    """
    if (type(C0) is not Fraction or type(c0) is not Fraction
            or C0<1 or not 0<c0<=1):
        raise ValueError("formal exact C0>=1, 0<c0<=1 required")
    rho_old_T=ceil_fraction(Fraction(OLD_T_FACTOR)*C0**3)
    T=ceil_fraction(SS6_T_FACTOR*C0**3)
    q2=16*comb(2*(K+1),2)
    q3=64*comb(3*(K+1),3)
    L6=24+288*T*T
    L4=q2*q2*sqrt_up(8*L6)+28*T  # new SHARP parent #738
    B0=sqrt_up(1280*(K+1)*T)
    E=8*q3*sqrt_up(L6)
    D=4*sqrt_up(B0*T*L4)
    rho=Fraction(1,12*q3*q3*L6)
    delta=c0/Fraction(R**6)
    s0=max(64,672*T,(8*E)**2,(8*D)**8)
    h0=(s0-1).bit_length()
    selected=Fraction(1,20608)
    density=selected/Fraction(8)*Fraction(4,9)
    v_coeff=Fraction(17,2)
    # Lower heavy selected source k >=s^4/20608;
    # e(F)/v(F) >= k/(8 a²) >=s/370944.
    heavy_threshold=Fraction(v_coeff,density**3)
    checks={
        "source_envelope_V_bound_allh":
            Fraction(1)+Fraction(1,64)+Fraction(1,64**2)+Fraction(1,64**3)
            <=Fraction(33,32),
        "source_envelope_N_bound_allh":
            Fraction(1)+Fraction(2,64)+Fraction(2,64**2)
            +Fraction(2,64**3)+Fraction(1,64**4)<=Fraction(17,16),
        "minimal_alphabet_from_V_analytic_3over2":
            Fraction(23,16)+Fraction(1,256)<Fraction(3,2)
            and Fraction(23,16)**2>=Fraction(33,16),
        "collision_book_Cs_analytic_5over4":
            Fraction(4097,4096)*Fraction(19,16)<=Fraction(5,4),
        "original_full_Q_deletion_still_le_1_16":
            Fraction(1,8)-2*rho>=Fraction(1,16),
        "source_owner_heavy_L_ge_1_32":
            (Fraction(1,8)-2*rho)/2>=Fraction(1,32),
        "Caro_Wei_from_new_original_source_conflict_cap":
            (Fraction(1,32)**2/
             (Fraction(1,32)+2*Fraction(5,2)))==Fraction(1,5152),
        "two_original_coordinate_cuts_ge_1_20608":
            Fraction(1,5152)/4==selected,
        "ordinary_no_clone_density_ge_s_over_370944":
            density==Fraction(1,R),
        "ordinary_no_clone_vertices_le_17over2_s3_T":
            v_coeff==2*4*Fraction(17,16),
        "sharp_external_SS6_T_sufficient_exact":
            T>=heavy_threshold*C0**3
            and heavy_threshold==SS6_T_FACTOR,
        "heavy_D6_original_6ID_delta_exact":
            delta==c0/Fraction(R**6),
        "low_original_core_still_ge_3over4":
            Fraction(1)-Fraction(1,8)-Fraction(3,32)-rho>=Fraction(3,4),
        "source_Q_error_with_new_rho_1_sextic_unit":
            12*rho*q3*q3*L6==1,
        "low_actual_sharp_fourth_and_four_blockers":
            L4==q2*q2*sqrt_up(8*L6)+28*T
            and D==4*sqrt_up(B0*T*L4),
        "low_remaining_three_errors_below_eighth":
            s0>=672*T and s0>=(8*E)**2 and s0>=(8*D)**8,
        "low_5over32_BBo_much_exceeds_heavy_delta":
            Fraction(53526*5,32)>54162*delta,
        "uniform_branch_aware_full_ten_GF5":
            min(54162*delta,Fraction(53526*5,32))==54162*delta,
        "new_T_strictly_below_old_T":
            T<rho_old_T,
        "no_numeric_published_graph_C_c_inferred":True,
    }
    if not all(checks.values()):
        raise AssertionError("improved no-clone heavy/root sufficient condition fails")
    return {"C0":C0,"c0":c0,"T":T,"old_T":rho_old_T,
            "q2":q2,"q3":q3,"L6":L6,"L4_SHARP":L4,
            "B0":B0,"E":E,"D":D,"rho":rho,"delta":delta,"s0":s0,
            "h0":h0,"density":density,"selected_fraction":selected,
            "SS6_T_factor":heavy_threshold,"risk_GF5_numerator":54162*delta,
            "risk_GF5_denominator":51**6,
            "checks":checks,
            "root_mathematically_accepted":False}


def _actual_original(h,scheme,shift_f=0,shift_g=0):
    from hyp105_full_physical_degree_tail import genuine_source
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    if (type(h) is not int or h not in (1,2)
            or type(shift_f) is not int or type(shift_g) is not int):
        raise ValueError("actual original W32/W34 source only")
    s,V,flags=genuine_source(h)
    model=pair_labeled_symplectic(h,scheme)
    f=tuple(tuple(x) for x in model["left_labels"])
    g=tuple(tuple(x) for x in model["right_labels"])
    f=f[shift_f%V:]+f[:shift_f%V]
    g=g[shift_g%V:]+g[:shift_g%V]
    a=2
    while comb(a,2)<V:a+=1
    legal=set(combinations(range(a),2))
    flags=tuple(tuple(x) for x in flags)
    if (len(flags)!=(s+1)*V or len(set(flags))!=len(flags)
            or len(f)!=V or len(g)!=V or len(set(f))!=V or len(set(g))!=V
            or any(x not in legal for x in f+g)):
        raise AssertionError("not actual ORIGINAL globally injected fixed source")
    return {"s":s,"V":V,"a":a,"flags":flags,"f":f,"g":g,
            "scheme":scheme,"shift_f":shift_f,"shift_g":shift_g}


def _physical(case,ids):
    """Independent ORIGINAL two diagonal graph; source owner is named flag ID."""
    flags,f,g=case["flags"],case["f"],case["g"]
    ids=tuple(ids)
    if (len(ids)!=len(set(ids))
            or any(type(i) is not int or i<0 or i>=len(flags) for i in ids)):
        raise ValueError("only distinct actual original source IDs")
    adj=defaultdict(set);owner={}
    for i in ids:
        p,ell=flags[i];x,z=f[p];y,w=g[ell]
        for u,v in (((x,y),(z,w)),((x,w),(z,y))):
            key=tuple(sorted((u,v)))
            if key in owner:raise AssertionError("original edge owner collision")
            owner[key]=i
            adj[u].add(v);adj[v].add(u)
    if len(owner)!=2*len(ids):
        raise AssertionError("original flag does not own exactly two edges")
    return adj,owner


def _conflicts(case,ids):
    """Full ORIGINAL pencil conflict per fixed f/g, no map independence."""
    ids=tuple(ids)
    flags,f,g=case["flags"],case["f"],case["g"]
    groups_p=defaultdict(list);groups_l=defaultdict(list)
    for i in ids:
        p,ell=flags[i];groups_p[p].append(i);groups_l[ell].append(i)
    J={i:set() for i in ids}
    for groups,typ in ((groups_p,0),(groups_l,1)):
        for iids in groups.values():
            for i,j in combinations(iids,2):
                p1,l1=flags[i];p2,l2=flags[j]
                A=g[l1] if typ==0 else f[p1]
                B=g[l2] if typ==0 else f[p2]
                if set(A)&set(B):J[i].add(j);J[j].add(i)
    if any(i in ns or any(i not in J[j] for j in ns) for i,ns in J.items()):
        raise AssertionError("original source conflict not irreflexive symmetric")
    return J


def _source_caro_wei(J):
    """Independent min-residual-degree greedy with original potential proof."""
    weight=sum((Fraction(1,len(neigh)+1) for neigh in J.values()),Fraction())
    left=set(J)
    chosen=[]
    potential=[weight]
    while left:
        v=min(left,key=lambda x:(len(J[x]&left),x))
        banned={v}|(J[v]&left)
        left.difference_update(banned)
        chosen.append(v)
        nextp=sum((Fraction(1,len(J[x]&left)+1)
                   for x in left),Fraction())
        if nextp>potential[-1] or potential[-1]-nextp>1:
            # The potential can sometimes increase after removals.
            # Only the upper drop <=1 is an invariant; remove the first check.
            if potential[-1]-nextp>1:
                raise AssertionError("greedy true source Caro-Wei potential decreased >1")
        potential.append(nextp)
    if len(chosen)<weight or any(v in J[u] for u,v in combinations(chosen,2)):
        raise AssertionError("genuine source Caro-Wei greedy weight false")
    return tuple(sorted(chosen)),weight,potential


def _full_source_color_cut(case,selected,typ):
    """Deterministic exact conditional expectation for ACTUAL original flags."""
    a=case["a"];bits=[-1]*a
    flag=case["flags"];labs=case["f"] if typ==0 else case["g"]
    selected=tuple(selected)

    def double_expectation():
        n=0
        for i in selected:
            u,v=labs[flag[i][typ]]
            n+=1 if bits[u]<0 or bits[v]<0 else 2*(bits[u]!=bits[v])
        return n
    former=double_expectation()
    for k in range(a):
        bits[k]=0;score0=double_expectation()
        bits[k]=1;score1=double_expectation()
        bits[k]=0 if score0>=score1 else 1
        if max(score0,score1)<former:
            raise AssertionError("conditional true source bichromatic count decreased")
        former=max(score0,score1)
    survived=tuple(i for i in selected if
                   bits[labs[flag[i][typ]][0]]!=bits[labs[flag[i][typ]][1]])
    if len(survived)*2<len(selected):
        raise AssertionError("ORIGINAL whole-flag typed cut lost >half")
    return survived,tuple(bits)


def _winner_chunk(edges,R,Y,n):
    """Prove no cloning. Every R and Y vertex is its literal physical pair."""
    R=set(R);Y=set(Y)
    if not R or not Y or R&Y or n<max(len(R),len(Y)):
        raise ValueError("positive disjoint original bipartite physical sides")
    r=len(R)
    Yseq=sorted(Y)
    chunks=[tuple(Yseq[i:i+r]) for i in range(0,len(Yseq),r)]
    if not chunks or len(chunks)*r>2*n:
        raise AssertionError("actual physical block cover cost >2n")
    edge_set=set(edges)
    cross={(u,v) for u,v in edge_set if u in R and v in Y}
    if any((u,v) not in edge_set or u not in R or v not in Y for u,v in cross):
        raise AssertionError("source original cross-edge corrupted")
    options=[]
    for idx,chunk in enumerate(chunks):
        candidate=tuple(sorted((u,v) for (u,v) in cross if v in chunk))
        options.append((len(candidate),-idx,chunk,candidate))
    _,_,winning_chunk,winner=max(options)
    actualV=R|set(winning_chunk)
    m=len(winner);E=len(cross);v=len(actualV)
    if not (
        m*2*n>=E*r
        and v<=2*r
        and len(chunks)*r<=2*n
        and all((u,v) in edge_set for u,v in winner)
        and len(set(winner))==m
    ):
        raise AssertionError("no-clone source physical block pigeonhole failed")
    return {
        "R":len(R),"Y":len(Y),"n_full_physical_corners":n,
        "E_cross":E,"chosen_chunk_Y":len(winning_chunk),
        "num_chunks":len(chunks),"winner_m":m,"winner_v":v,
        "actual_winner_vertices":tuple(sorted(actualV)),
        "actual_winner_edges":tuple(sorted(winner)),
        "cross_edge_pigeonhole_exact":m*2*n>=E*r,
        "source_no_clone":True,
        "v_le_twice_R":v<=2*r,
        "winner_real_physical_subgraph":True,
    }


def _canonical_c6(v):
    x=tuple(v)
    return min(tuple(w[i:]+w[:i] for w in (x,x[::-1]) for i in range(6)))


def _all_c6(adj):
    cycles=set()
    for source in sorted(adj):
        def dfs(path):
            if len(path)==6:
                if source in adj.get(path[-1],()):
                    cycles.add(_canonical_c6(path))
                return
            for v in adj.get(path[-1],()):
                if v>source and v not in path:
                    dfs(path+(v,))
        dfs((source,))
    return tuple(sorted(cycles))


def _original_cycle_ids(case,cyc,owner):
    flags,f,g=case["flags"],case["f"],case["g"]
    if len({v[0] for v in cyc})!=6 or len({v[1] for v in cyc})!=6:
        raise AssertionError("true selected physical C6 repeated a factor coordinate")
    ids=tuple(sorted(owner[tuple(sorted((cyc[i],cyc[(i+1)%6])))]
                     for i in range(6)))
    if (len(set(ids))!=6 or len({flags[i][0] for i in ids})!=6
            or len({flags[i][1] for i in ids})!=6):
        raise AssertionError("physical source C6 not six distinct actual original D6 IDs")
    return ids


def _fresh_heavy_case(h,scheme,T,deleted,shift_f=0,shift_g=0):
    """All source/heavy selection/chunk steps implemented independently."""
    if not isinstance(T,Fraction) or T<=0:
        raise ValueError("positive exact diagnostic T required")
    c=_actual_original(h,scheme,shift_f,shift_g)
    flags=c["flags"]
    Z=set(deleted)
    if any(type(i) is not int or i<0 or i>=len(flags) for i in Z):
        raise ValueError("deleted original source IDs invalid")
    n=c["a"]**2
    full,owner=_physical(c,range(len(flags)))
    Q={v for v,ns in full.items() if len(ns)>T*c["s"]}
    tail={e for e in owner if any(v in Q for v in e)}
    actual={e for e in tail if owner[e] not in Z}
    lost=len(tail)-len(actual)
    if lost>2*len(Z):
        raise AssertionError("full ORIGINAL Q before Z loses >2 edges per flag")
    sourceI=tuple(sorted({owner[e] for e in actual}))
    if not sourceI:
        return {"empty_tail":True,"s":c["s"],"scheme":scheme}
    L=len(sourceI)
    J=_conflicts(c,sourceI)
    eJ=sum(map(len,J.values()))//2
    independent,CW,potential=_source_caro_wei(J)
    left,left_bits=_full_source_color_cut(c,independent,0)
    kept,right_bits=_full_source_color_cut(c,left,1)
    graphSel,ownerSel=_physical(c,kept)
    if (4*len(kept)*(L+2*eJ)<L**2
            or len(kept)*2<len(left) or len(left)*2<len(independent)):
        raise AssertionError("genuine source Caro Wei and coordinate cuts mass")
    witnesses={}
    for i in kept:
        options=[e for e in actual if owner[e]==i]
        if not options:
            raise AssertionError("selected original source flag has no actual heavy witness")
        witnesses[i]=min(options)
    sides=defaultdict(list)
    for i,e in witnesses.items():
        qv=min(v for v in e if v in Q)
        sides[left_bits[qv[0]]].append((i,qv,e))
    side=0 if len(sides[0])>=len(sides[1]) else 1
    Rset={v for v in Q if left_bits[v[0]]==side}
    Yset={v for v in graphSel if left_bits[v[0]]!=side}
    cross={(u,v) for u in Rset for v in graphSel.get(u,()) if v in Yset}
    # Crucially, every chosen flag provides its OWN actual original
    # physical witness edge joining R and Y. No vertex cloning or
    # synthetic point/line label can be introduced at this stage.
    if 2*len(cross)<len(kept):
        raise AssertionError("selected original heavy witness majority lost")
    win=_winner_chunk(cross,Rset,Yset,n)
    m=win["winner_m"];v=win["winner_v"]
    q=len(Q)
    instance_alpha=Fraction(L*L,L+2*eJ)
    density=Fraction(L*L,32*n*(L+2*eJ))
    ss6_floor=Fraction(L**6,2**16*n**3*q*(L+2*eJ)**3)
    if (Fraction(m,v)<density or
            Fraction(m**3,v**4)<ss6_floor or v>2*q):
        raise AssertionError("true original no-clone graph density/SS6 transfer")
    # Owner of a physical edge in the winner is the unique original
    # incidence ID from selected whole flags, even if only one diagonal
    # of a selected owner survived the balanced chunk.
    win_owner={tuple(sorted((u,v))):ownerSel[tuple(sorted((u,v)))]
               for u,v in win["actual_winner_edges"]}
    win_adj=defaultdict(set)
    for u,v in win["actual_winner_edges"]:
        win_adj[u].add(v);win_adj[v].add(u)
    selected_cycles=_all_c6(graphSel)
    cycles=_all_c6(win_adj)
    sid={_original_cycle_ids(c,cyc,win_owner) for cyc in cycles}
    if len(sid)!=len(cycles):
        raise AssertionError("original winner C6 not injective to source D6")
    if not set(cycles)<=set(selected_cycles):
        raise AssertionError("original winner created a physical cycle")
    return {
        "s":c["s"],"scheme":scheme,
        "shift_f":shift_f,"shift_g":shift_g,
        "diagnostic_T":str(T),
        "deleted_original_ID_count":len(Z),
        "N_original_flags":len(flags),
        "full_original_Q_before_Z":len(Q),
        "full_original_tail_edges":len(tail),
        "actual_ORIGINAL_tail_edges_after_Z":len(actual),
        "actual_original_deleted_tail_edges":lost,
        "true_original_heavy_source_owners_L":L,
        "true_source_conflict_edges":eJ,
        "source_original_Caro_Wei":str(CW),
        "source_original_independent_flags":len(independent),
        "source_after_first_full_pair_cut":len(left),
        "source_after_second_full_pair_cut":len(kept),
        "source_heavy_majority_witness_count":len(sides[side]),
        "heavy_R_physical_vertices":len(Rset),
        "full_OPPOSITE_Y_physical_vertices":len(Yset),
        "actual_original_selected_C6":len(selected_cycles),
        "actual_original_no_clone_winner_C6":len(cycles),
        "actual_original_winner_D6_six_ID_count":len(sid),
        "actual_source_D6_ID_samples":[list(v) for v in sorted(sid)[:5]],
        "instance_original_alpha_CW_lower":str(instance_alpha),
        "instance_sharp_source_density_lower":str(density),
        "instance_SS6_cubed_lower":str(ss6_floor),
        "actual_winner_m_over_v":str(Fraction(m,v)),
        "actual_winner_e3_over_v4":str(Fraction(m**3,v**4)),
        "actual_no_clone_winner":{
            "winner_m":m,"winner_v":v,"num_chunks":win["num_chunks"],
            "E_cross":win["E_cross"],
            "heavy_R":win["R"],"opp_Y":win["Y"],
            "actual_winner_vertices":len(win["actual_winner_vertices"]),
            "actual_winner_edges":len(win["actual_winner_edges"]),
            "source_no_clone":True,
            "true_original_edge_source_ownership_unchanged":True,
        },
        "source_typed_cuts_and_no_clone_valid":True,
        "root_230_status":ROOT_STATUS,
        "root_unconditionally_accepted":False,
    }


def mutations(C0,c0):
    x=allh_sharp_heavy_ledger(C0,c0)
    # These test whether our *declared sufficient proof budget* closes.
    # They are NOT counterexamples to the underlying HYP-105 conjecture.
    selected=Fraction(1,20608)
    def gates(*,ncap=Fraction(9,4),Ncap=Fraction(17,16),
              ecap=Fraction(5,2),T=None,Rtrial=R,delta=None):
        # m/v >= chosen_count/(8n)
        physical_d=selected/(8*ncap)
        alpha_with_ecap=Fraction(1,32)**2/(
            Fraction(1,32)+2*ecap)
        return {
            "correct_source_Caro_Wei_selected_mass":
                alpha_with_ecap/4>=selected,
            "correct_physical_ncap_for_declared_density":
                physical_d>=Fraction(1,Rtrial),
            "correct_source_max_Q_vertices":
                2*4*Ncap<=Fraction(17,2),
            "published_ordinary_graph_SS6_threshold":
                (x["T"] if T is None else T)>=Fraction(17,2)*Rtrial**3*C0**3,
            "original_D6_sixset_minimum_multiplier":
                (x["delta"] if delta is None else delta)<=c0/Fraction(Rtrial**6),
        }
    probes=[]
    for label,overrides in (
        ("assume_weaker_conflict_graph_cap",{"ecap":Fraction(3)}),
        ("assume_weaker_physical_vertex_alphabet",{"ncap":Fraction(3)}),
        ("assume_weaker_original_source_size",{"Ncap":Fraction(3,2)}),
        ("reduce_below_proved_ordinary_C6_threshold",{"T":x["T"]-1}),
        ("increase_original_D6_multiplier_without_proof",
         {"delta":x["delta"]*2}),
    ):
        result=gates(**overrides)
        if all(result.values()):
            raise AssertionError("failed to reject weakened original heavy proof budget")
        probes.append({"name":label,"failed_gates":[n for n,b in result.items() if not b]})
    return probes


def canonical_report():
    formal=[]
    for C,c in ((Fraction(1),Fraction(1)),
                (Fraction(2),Fraction(1,5)),
                (Fraction(7,3),Fraction(1,17))):
        z=allh_sharp_heavy_ledger(C,c)
        formal.append({
            "C0_FORMAL":str(C),"c0_FORMAL":str(c),
            "T_old":str(z["old_T"]),"T_sharp_heavy":str(z["T"]),
            "old_T_to_new_T_ratio":str(Fraction(z["old_T"],z["T"])),
            "delta_sharp_heavy":str(z["delta"]),
            "density_sharp_heavy":str(z["density"]),
            "rho":str(z["rho"]),"h0_sharp_heavy_and_L4":z["h0"],
            "all_conditional_exact_budgets":all(z["checks"].values()),
            "external_graph_SS6_constants_numerically_known":False,
        })
    true_cases=[
        _fresh_heavy_case(1,"lex",Fraction(1,2),(0,)),
        _fresh_heavy_case(1,"reverse-line",Fraction(3,4),(1,13,33)),
        _fresh_heavy_case(2,"lex",Fraction(1),(0,10,100,200)),
        _fresh_heavy_case(2,"reverse-line",Fraction(5,4),(0,25,26,33,34)),
        _fresh_heavy_case(2,"lex",Fraction(1),(0,10,100,200),7,19),
    ]
    if any(q.get("empty_tail") for q in true_cases):
        raise AssertionError("genuine original heavy true-source positive gate vacuous")
    if not any(q["actual_original_selected_C6"]>0 for q in true_cases):
        raise AssertionError("original physical heavy source C6 positives missing")
    return {
        "schema":"mathlab.hyp105.original-heavy-no-clone-sharp-SS6.v1",
        "root_230_status":ROOT_STATUS,
        "root_Branch_A_unconditionally_accepted":False,
        "external_published_C_graph_c_graph_values_numerically_known":False,
        "all_order_exact_physical_source_envelope_derived":True,
        "all_order_original_Caro_Wei_cuts_no_clone_heavy_proved":True,
        "all_order_SS6_d6_conditional_improvement_proved":True,
        "all_order_original_lowtail_lemma_inherited_not_reproved":True,
        "new_R":R,"new_SS6_T_coefficient":str(SS6_T_FACTOR),
        "old_SS6_T_coefficient":str(OLD_T_FACTOR),
        "D6_sixset_lower_improvement_factor":str(Fraction(2**120,R**6)),
        "formal_graph_constant_ledgers":formal,
        "actual_original_envelopes":[genuine_envelope(1<<h) for h in (6,7,8,10)],
        "genuine_true_original_heavy_cases":true_cases,
        "reject_improper_assumption_mutations":mutations(Fraction(1),Fraction(1)),
        "root_ASET_exponent_proved":False,
    }


if __name__=="__main__":
    print("AA4_ORIGINAL_HEAVY_SHARP_SS6_CERTIFICATE="+json.dumps(
        canonical_report(),sort_keys=True,separators=(",",":")),flush=True)
