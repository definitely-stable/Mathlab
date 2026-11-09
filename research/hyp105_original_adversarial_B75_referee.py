"""HYP-105 AA4-ADV: fail-closed deterministic adversarial ORIGINAL W(3,2) f/g survey.

New mathematical gate: endpoint-bin Motzkin risk-tail necessity. If the
total true weighted incompatible mass B/M can reach >=3/4 for an actual
source, at least one same-ordered-physical-endpoint bin with positive
mass MUST have an actual incompatibility clique of size >=5: every
bin with clique <=4 has B_bin/M_bin <=3/4 by weighted Motzkin-Straus.
For each exact candidate, the stronger source-certified sufficient
criterion for B/M<3/4 is
   (sum_bins M_bin / omega_bin) / (sum_bins M_bin) > 1/4.
Unlike a finite stress search, these conclusions are ALL-h.

The genuine source experiment below searches permutations of the COMPLETE
15 pair labels on each of 15 original points and 15 original lines of
true W(3,2), with fixed arbitrary correlations and no cloned source.
It does NOT establish a universal upper bound, disprove an all-h
ASYMPTOTIC theorem from finite W32, or sample W34.

Ranking uses an expressly non-proof, degree-product FLOAT heuristic.
Shortlisted candidates are independently audited with exact Fraction
probabilities from ONE shared ORIGINAL source priority rank integral.
The exact source test checks real original point/line pencils, named
incidence-ID ownership of both physical flag diagonals, true physical
proper P3, source J and opposite-depth x/y conflicts, the complete
same-endpoint tensor and actual weighted graph clique certificates.
No earlier AA4 source algorithm is imported in the MAIN search code.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial
import json
import random

from hyp105_original_defect_factor_referee import genuine_symplectic_source

SCHEMA="mathlab.hyp105.original-adversarial-B75-exact-source.v1"
ROOT_STATUS="OPEN_WITH_FORMAL_BLOCKER"
SEED=230756
PAIR_ALPHABET=tuple(combinations(range(6),2))
FLAGS=tuple(map(tuple,genuine_symplectic_source(2)))
ALL_FLAGS=tuple(range(len(FLAGS)))
IDENTITY=tuple(range(15))
REVERSE=tuple(reversed(IDENTITY))
P3_SOURCE_J_K=64
TARGET=Fraction(3,4)


def genuine_source_for_assignment(f_perm,g_perm,retained=None):
    """Each assignment bijects actual 15 points or lines to ALL 15 physical pairs."""
    if (len(f_perm)!=15 or len(g_perm)!=15 or
        tuple(sorted(f_perm))!=IDENTITY or
        tuple(sorted(g_perm))!=IDENTITY):
        raise ValueError("all 15 true ORIGINAL point/line label pairs must be globally injected")
    if len(FLAGS)!=45 or len(set(FLAGS))!=45:
        raise AssertionError("wrong original symplectic W(3,2) incidence source")
    ids=ALL_FLAGS if retained is None else tuple(sorted(set(retained)))
    if any(i not in ALL_FLAGS for i in ids):
        raise ValueError("named deleted ORIGINAL incidence-ID range")
    f=tuple(PAIR_ALPHABET[i] for i in f_perm)
    g=tuple(PAIR_ALPHABET[i] for i in g_perm)
    bypoint=defaultdict(list)
    byline=defaultdict(list)
    for i in ids:
        p,l=FLAGS[i]
        bypoint[p].append(i)
        byline[l].append(i)
    J=[set() for _ in FLAGS]
    for side,books in (("point",bypoint),("line",byline)):
        for group in books.values():
            for i,j in combinations(group,2):
                p1,l1=FLAGS[i];p2,l2=FLAGS[j]
                A=g[l1] if side=="point" else f[p1]
                B=g[l2] if side=="point" else f[p2]
                if set(A)&set(B):
                    J[i].add(j);J[j].add(i)
    edges={}
    adj=defaultdict(set)
    for i in ids:
        p,l=FLAGS[i]
        x0,x1=f[p];y0,y1=g[l]
        for u,v in (((x0,y0),(x1,y1)),((x0,y1),(x1,y0))):
            e=tuple(sorted((u,v)))
            if e in edges:raise AssertionError("true physical edge duplicate ORIGINAL owner")
            edges[e]=i
            adj[u].add(v)
            adj[v].add(u)
    if len(edges)!=2*len(ids):
        raise AssertionError("true original whole source has two real diagonals per flag")
    if max((len(J[i]) for i in ids),default=0)>P3_SOURCE_J_K:
        raise AssertionError("LOW original J-degree cap invalid")
    return {"f_perm":tuple(f_perm),"g_perm":tuple(g_perm),
        "f":f,"g":g,"ids":ids,"J":J,"edges":edges,"adj":adj,
        "deleted_original_IDs":tuple(i for i in ALL_FLAGS if i not in ids),
        "source_max_J":max((len(J[i]) for i in ids),default=0)}


def all_genuine_proper_p3(source):
    """All actual ORIGINAL coordinate-proper physical directed length-3 paths."""
    adj=source["adj"]
    owner=source["edges"]
    results=[]
    for a in sorted(adj):
        for b in sorted(adj[a]):
            for c in sorted(adj[b]):
                if c[0] in (a[0],b[0]) or c[1] in (a[1],b[1]):continue
                for d in sorted(adj[c]):
                    path=(a,b,c,d)
                    if len({v[0] for v in path})!=4 or len({v[1] for v in path})!=4:
                        continue
                    ids=tuple(owner[tuple(sorted((path[i],path[i+1])))] for i in range(3))
                    if len(set(ids))!=3 or any(j in source["J"][i]
                            for i,j in combinations(ids,2)):
                        raise AssertionError("coordinate-proper ORIGINAL path source owners clash")
                    results.append((path,ids))
    return results


def original_incompatibility(a,b,J):
    """Real same endpoints; four cross-depth tests, true named J source conflict."""
    p,os=a
    q,ot=b
    if p[0]!=q[0] or p[-1]!=q[-1]:
        raise ValueError("same directed physical endpoints required")
    union=tuple(sorted(set(os+ot)))
    if any(j in J[i] for i,j in combinations(union,2)):
        return "original_J"
    if p[1][0]==q[2][0] or p[2][0]==q[1][0]:
        return "first_physical_coordinate"
    if p[1][1]==q[2][1] or p[2][1]==q[1][1]:
        return "second_physical_coordinate"
    return "compatible"


def _path_groups(paths):
    byend=defaultdict(list)
    for path in paths:
        byend[(path[0][0],path[0][-1])].append(path)
    return byend


def _proxy_weight(ids,J):
    """FLOAT search heuristic ONLY; exact scientific proofs use Fraction."""
    p=1.0
    for i in ids:p/=1+len(J[i])
    return p


def fast_screen(f_perm,g_perm,retained=None):
    """Entire real W32 source exact PATHS and conflict classes, heuristic weights."""
    src=genuine_source_for_assignment(f_perm,g_perm,retained)
    paths=all_genuine_proper_p3(src)
    byend=_path_groups(paths)
    M=0.0;B=0.0
    for group in byend.values():
        weights=[_proxy_weight(os,src["J"]) for path,os in group]
        W=sum(weights)
        M+=W*W
        for i in range(len(group)):
            for j in range(i+1,len(group)):
                if original_incompatibility(group[i],group[j],src["J"])!="compatible":
                    B+=2*weights[i]*weights[j]
    return {"screening_proxy_B_over_M":B/M if M else 0.0,
        "screening_path_count":len(paths),
        "screening_endpoint_bins":len(byend),
        "no_synthetic_source_geometry":True}


def _exact_original_local_priority(os,J):
    """Independent true ORIGINAL priority 3! simplex integral, no path independence."""
    owner=tuple(sorted(set(os)))
    if len(owner)!=3 or any(j in J[i] for i,j in combinations(owner,2)):
        raise AssertionError("true physical proper path should have J-free owners")
    outer=set().union(*(J[i] for i in owner))-set(owner)
    depend={z:tuple(i for i in owner if z in J[i]) for z in outer}
    value=Fraction(0)
    for order in permutations(owner):
        loc={i:j for j,i in enumerate(order)}
        c=[0,0,0]
        for d in depend.values():
            c[max(loc[i] for i in d)]+=1
        suffix=0;den=1
        for i in (2,1,0):
            suffix+=1+c[i]
            den*=suffix
        value+=Fraction(1,den)
    if not Fraction(1,65**3)<=value<=1:
        raise AssertionError("Harris original priority source lower violated")
    return value


def _exact_original_P3_weights(paths,J):
    cache={}
    result=[]
    for path,os in paths:
        S=tuple(sorted(os))
        if S not in cache:
            cache[S]=_exact_original_local_priority(S,J)/64
        result.append(cache[S])
    return result


def _independent_clique_number(adj):
    """Independent set-intersection branch-and-bound, not prior PR #755 routine."""
    n=len(adj)
    if n==0:return 0
    ordered=sorted(range(n),key=lambda i:len(adj[i]),reverse=True)
    best=0
    def grow(pool,depth):
        nonlocal best
        if not pool:
            best=max(best,depth)
            return
        if depth+len(pool)<=best:return
        while pool:
            v=pool.pop()
            grow([i for i in pool if i in adj[v]],depth+1)
            if depth+len(pool)<=best:return
    grow(ordered,0)
    return best


def exact_source_risk(f_perm,g_perm,retained=None,full_clique=True):
    """True exact rational B/M and exact endpoint-local Motzkin certificate."""
    src=genuine_source_for_assignment(f_perm,g_perm,retained)
    paths=all_genuine_proper_p3(src)
    if not paths:
        raise AssertionError("empty REAL original CORE proper 3path tensor")
    byend=_path_groups(paths)
    M=Fraction(0);B=Fraction(0);G=Fraction(0)
    BJ=Fraction(0);BX=Fraction(0);BY=Fraction(0)
    motzkin_good=Fraction(0)
    risk_M_omega5=Fraction(0)
    counts=Counter()
    bins_by_omega=Counter()
    max_omega=0
    weights_cache={}
    priority_ints=0
    best_bin=None
    ordered_pair_count=0
    for key,group in sorted(byend.items()):
        ws=[]
        for _,os in group:
            S=tuple(sorted(os))
            if S not in weights_cache:
                weights_cache[S]=_exact_original_local_priority(S,src["J"])/64
                priority_ints+=1
            ws.append(weights_cache[S])
        W=sum(ws,Fraction(0))
        mass=W*W
        bad=Fraction(0)
        good=sum((w*w for w in ws),Fraction(0))
        local_J=local_X=local_Y=Fraction(0)
        n=len(group)
        adj=[set() for _ in range(n)]
        for i in range(n):
            for j in range(i+1,n):
                reason=original_incompatibility(group[i],group[j],src["J"])
                counts[reason]+=2
                ordered_pair_count+=2
                amount=2*ws[i]*ws[j]
                if reason=="compatible":
                    good+=amount
                else:
                    bad+=amount
                    adj[i].add(j);adj[j].add(i)
                # INDEPENDENT decomposed edge predicates, overlap allowed.
                U=tuple(sorted(set(group[i][1]+group[j][1])))
                if any(v in src["J"][u] for u,v in combinations(U,2)):
                    local_J+=amount
                p=group[i][0];q=group[j][0]
                if p[1][0]==q[2][0] or p[2][0]==q[1][0]:
                    local_X+=amount
                if p[1][1]==q[2][1] or p[2][1]==q[1][1]:
                    local_Y+=amount
        counts["compatible"]+=n
        ordered_pair_count+=n
        if good+bad!=mass:
            raise AssertionError("all REAL original same-endpoint weighted pair mass not conserved")
        if full_clique:
            omega=_independent_clique_number(adj)
            if omega<1 or good*omega<mass:
                raise AssertionError("weighted Motzkin-Straus violated for actual source bin")
            motzkin_good+=mass/omega
            bins_by_omega[omega]+=1
            max_omega=max(max_omega,omega)
            if omega>=5:risk_M_omega5+=mass
            if best_bin is None or (bad/mass)>best_bin["B_over_M"]:
                best_bin={"endpoint":[list(key[0]),list(key[1])],
                    "B_over_M":bad/mass,"path_count":n,"clique":omega}
        M+=mass
        B+=bad
        G+=good
        BJ+=local_J;BX+=local_X;BY+=local_Y
    if not M or G+B!=M or sum(counts.values())!=ordered_pair_count:
        raise AssertionError("source exact full 3path risk mass invalid")
    if not (BJ<=M and BX<=M and BY<=M and B<=M):
        raise AssertionError("individual true source conflict weight > all pairs")
    if full_clique and not (G>=motzkin_good>=M/Fraction(16*65**3)):
        raise AssertionError("source weighted Motzkin graph certificate invalid")
    if full_clique and B/M>=TARGET and max_omega<=4:
        raise AssertionError("mathematical all-h critical clique-five necessity violated")
    result={
        "s":2,"label_map_point_f_perm":list(f_perm),
        "label_map_line_g_perm":list(g_perm),
        "original_named_deletions":list(src["deleted_original_IDs"]),
        "original_pair_injection":True,
        "named_original_source_flag_count":len(FLAGS),
        "paired_CORE_original_source_flags":len(src["ids"]),
        "true_actual_physical_edges":len(src["edges"]),
        "max_original_source_J_degree":src["source_max_J"],
        "full_original_proper_directed_P3":len(paths),
        "physical_ordered_endpoint_bins":len(byend),
        "ordered_same_end_path_pair_count":ordered_pair_count,
        "disjoint_joint_incompatibility_class_counts":dict(sorted(counts.items())),
        "distinct_exact_original_priority_owner_integrals":priority_ints,
        "exact_weighted_M":str(M),
        "exact_weighted_G":str(G),
        "exact_weighted_B":str(B),
        "exact_ratio_B_over_M":str(B/M),
        "exact_ratio_G_over_M":str(G/M),
        "exact_J_only_weighted_B":str(BJ),
        "exact_x_only_weighted_B":str(BX),
        "exact_y_only_weighted_B":str(BY),
        "exact_B_over_M_below_three_quarters":B/M<TARGET,
        "counterexample_at_3_over_4_for_THIS_finite_W32":B/M>=TARGET,
        "all_h_asymptotic_counterexample_claimed":False,
        "root_PROVED_A":False,
    }
    if full_clique:
        result.update({
            "actual_max_original_incompatibility_clique":max_omega,
            "bin_clique_histogram":dict(sorted(bins_by_omega.items())),
            "exact_Motzkin_G_floor":str(motzkin_good),
            "exact_Motzkin_bound_on_B_over_M":str(1-motzkin_good/M),
            "actual_mass_share_bins_omega_at_least_5":str(risk_M_omega5/M),
            "weighted_Motzkin_alone_proves_B_over_M_below_three_quarters":
                motzkin_good/M>Fraction(1,4),
            "highest_local_bad_ratio_endpoint_bin":{
                "physical_ordered_endpoints":best_bin["endpoint"],
                "exact_local_B_over_M":str(best_bin["B_over_M"]),
                "true_proper_path_count":best_bin["path_count"],
                "incompatible_clique_size":best_bin["clique"]},
        })
    return result


def _initial_labelings():
    return (
        ("lex-lex",IDENTITY,IDENTITY),
        ("lex-reverse",IDENTITY,REVERSE),
        ("point-reverse-line-lex",REVERSE,IDENTITY),
        ("reverse-reverse",REVERSE,REVERSE),
        ("point-shift3-line-shift7",IDENTITY[3:]+IDENTITY[:3],
             IDENTITY[7:]+IDENTITY[:7]),
    )


def _mutate_labels(rng,f,g):
    a=list(f);b=list(g)
    for i in range(rng.choice((1,1,1,2,3))):
        seq=a if rng.randrange(2)==0 else b
        u=rng.randrange(15)
        v=rng.randrange(15)
        while v==u:v=rng.randrange(15)
        seq[u],seq[v]=seq[v],seq[u]
    return tuple(a),tuple(b)


def deterministic_adversarial_scan(trials=320,seed=SEED,shortlist=5):
    """Reproducible structural full-source search; heuristic ranking NOT a proof."""
    if type(trials) is not int or trials<20 or trials>2000:
        raise ValueError("bounded deterministic trial budget [20,2000]")
    if type(seed) is not int:
        raise ValueError("explicit reproducible integer seed required")
    rng=random.Random(seed)
    visited=set()
    ranking=[]
    proxy_max=0.0
    eligible=0
    best_candidate=None
    current=IDENTITY,IDENTITY
    current_score=-1
    categories=Counter()
    def evaluate(f,g,kind):
        nonlocal proxy_max,eligible,best_candidate
        if (f,g) in visited:return None
        visited.add((f,g))
        row=fast_screen(f,g)
        score=row["screening_proxy_B_over_M"]
        eligible+=1
        categories[kind]+=1
        record=(score,tuple(f),tuple(g),kind,row["screening_path_count"])
        ranking.append(record)
        if score>proxy_max:
            proxy_max=score
            best_candidate=(f,g)
        return score
    for name,f,g in _initial_labelings():
        evaluate(f,g,"seed:"+name)
    top=(IDENTITY,IDENTITY)
    for i in range(trials):
        if i%43==0:
            f=list(IDENTITY);g=list(IDENTITY)
            rng.shuffle(f);rng.shuffle(g)
            f=tuple(f);g=tuple(g)
            kind="global-random-restart"
        elif i%17==0 and ranking:
            row=sorted(ranking,key=lambda z:z[0],reverse=True)[:8]
            base=rng.choice(row)
            f,g=_mutate_labels(rng,base[1],base[2])
            kind="elite-recombination"
        elif i%5==0:
            f,g=_mutate_labels(rng,*top)
            kind="global-best-neighbor"
        else:
            f,g=_mutate_labels(rng,*current)
            kind="local-mutation"
        v=evaluate(f,g,kind)
        if v is None:continue
        # Simulated annealing, seeded and deterministic.
        temp=.015*(.25+.75*((trials-i)/trials))
        if v>=current_score or rng.random() < min(1,(temp/(temp+max(0,current_score-v)))**3):
            current=(f,g);current_score=v
        if v>=(ranking[-1][0] if len(ranking)==1 else max(z[0] for z in ranking[:-1])):
            top=(f,g)
    ranking.sort(key=lambda row:(-row[0],row[1],row[2]))
    selected=[(score,f,g,kind,count) for score,f,g,kind,count in ranking[:shortlist]]
    # Mandatory verify exact source, not degree-product proxy.
    exact=[]
    for _,f,g,kind,proper in selected:
        x=exact_source_risk(f,g)
        x["search_proposal_type"]=kind
        x["screening_proxy_only_B_over_M"]=_proxy_ratio_string(
            fast_screen(f,g)["screening_proxy_B_over_M"])
        exact.append(x)
    exact.sort(key=lambda row:Fraction(row["exact_ratio_B_over_M"]),reverse=True)
    baselines=[]
    for name,f,g in _initial_labelings()[:2]:
        x=exact_source_risk(f,g)
        x["baseline_name"]=name
        baselines.append(x)
    all_exact=exact+baselines
    highest=max(all_exact,key=lambda row:Fraction(row["exact_ratio_B_over_M"]))
    max_real=Fraction(highest["exact_ratio_B_over_M"])
    if not max_real>0 or not all(x["named_original_source_flag_count"]==45 and
        x["true_actual_physical_edges"]==90 for x in all_exact):
        raise AssertionError("adversarial search not genuine original whole W32 source")
    return {
        "schema":SCHEMA,"issue":230,"status":ROOT_STATUS,
        "root_PROVED_A":False,
        "all_h_B_over_M_less_3_over_4_PROVED":False,
        "counterexample_to_asymptotic_B75_claimed":False,
        "finite_exact_W32_B75_witness_found":any(x["counterexample_at_3_over_4_for_THIS_finite_W32"] for x in all_exact),
        "true_original_symplectic_order":2,
        "global_pair_alphabet":6,
        "label_pairs_per_side":15,
        "original_f_and_g_separately_permuted":True,
        "source_original_Z_deleted_in_search":False,
        "random_seed":seed,"proposal_budget":trials,
        "unique_completed_proxy_trials":eligible,
        "seeded_proposal_categories":dict(categories),
        "nonproof_fast_degree_product_proxy_max":_proxy_ratio_string(proxy_max),
        "exact_fraction_top_candidate_shortlist":exact,
        "predeclared_exact_true_source_baselines":baselines,
        "best_exact_original_W32_full_source_witness":highest,
        "best_exact_original_W32_ratio":str(max_real),
        "strict_no_universal_extrapolation_from_finite_witness":True,
        "mathematical_all_h_clique_five_necessary_for_B_over_M_ge_3_4":True,
        "mathematical_weighted_clique_bin_certifies_strict_B_below_3_4_when_sum_M_over_omega_gt_M_over_4":True,
        "numerical_external_graph_C6_constants_claimed":False,
    }


def _proxy_ratio_string(z):
    return format(z,".12g")


def canonical_report():
    return deterministic_adversarial_scan()


if __name__=="__main__":
    print("AA4_ADV_B75_CERTIFICATE="+json.dumps(canonical_report(),sort_keys=True,separators=(",",":")))
