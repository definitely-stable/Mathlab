"""AA4-SS6GATE: independent ordinary C6 theorem hypotheses + explicit spectral branch.

TRUE input: simple bipartite graph (not a hypergraph, homomorphism
or a cloned graph); published Simonovits / Jiang-Yepremyan ordinary
C6 supersaturation requires e>=C_graph v^(4/3) with unknown C_graph.

NEW standalone graph theorem without external constants:
if d=2e/v, Delta=max degree and d^5 >=144*v*Delta^2 then
  C6(unoriented, simple) >= d^6/24.
Proof: tr A6>=d^6 (Rayleigh); tr A6<=12 C6+6Delta tr A4;
tr A4 <=sqrt(2e tr A6). Since X=tr A6 and
sqrt(X)>=d^3>=12Delta*sqrt(v*d),
  12 C6 >= X-6Delta sqrt(v*d*X)>=X/2>=d^6/2.
NO hypothesis that every original W(3,s) chunk passes this branch.
Exact Fraction/integer arithmetic; NO guessed published constants.
"""
from collections import Counter,defaultdict
from fractions import Fraction
from itertools import combinations

from hyp105_full_physical_degree_tail import genuine_source


def _simple_bipartite_graph(graph,left,right):
    if type(graph) is not dict:
        raise ValueError("explicit undirected adjacency dict required")
    L=tuple(left);R=tuple(right)
    if len(set(L))!=len(L) or len(set(R))!=len(R) or set(L)&set(R):
        raise ValueError("bipartition must be disjoint and without repetitions")
    vertices=set(L)|set(R)
    if vertices!=set(graph):
        raise ValueError("every actual graph vertex, including isolates, required")
    for u,ns in graph.items():
        if u in ns or any(v not in vertices or u not in graph[v] for v in ns):
            raise ValueError("simple symmetric graph only")
        if any((v in R)!=(u in L) for v in ns):
            raise ValueError("edge does not cross chosen bipartition")
    return L,R,{u:set(ns) for u,ns in graph.items()}


def exact_c6_gate(graph,left,right,*,trial_C_graph=None):
    """External hypothesis EXACT integer cube, not an invented C_graph.

    The actual unknown published value C_graph is NEVER assigned.
    trial_C_graph allows FALSE-IF-CONSTANT historical algebra tests,
    which do not certify the published theorem's numerical C.
    """
    L,R,g=_simple_bipartite_graph(graph,left,right)
    n=len(g)
    e=sum(map(len,g.values()))//2
    delta=max(map(len,g.values()),default=0)
    d=Fraction(2*e,n) if n else Fraction()
    # Completely direct COMMON NEIGHBOR cycle census, independent of
    # any historical #680 / #691 sixth-walk/C6 code.
    C6=0
    for x,y,z in combinations(L,3):
        cxy=g[x]&g[y]
        cyz=g[y]&g[z]
        czx=g[z]&g[x]
        t=cxy&cyz
        C6+=len(cxy)*len(cyz)*len(czx)-len(t)*(len(cxy)+len(cyz)+len(czx))+2*len(t)
    # Independent A^2 neighbor-join / A^3 adjacency contractions.
    a2={}
    for u in g:
        row=Counter()
        for v in g[u]:row.update(g[v])
        a2[u]=row
    tr4=sum(c*c for row in a2.values() for c in row.values())
    a3={}
    for u in g:
        row=Counter()
        for v in g[u]:row.update(a2[v])
        a3[u]=row
    tr6=sum(c*c for row in a3.values() for c in row.values())
    if C6<0 or not (tr6>=d**6 if n else tr6==0):
        raise AssertionError("C6 codegree or spectral lower invalid")
    if tr6>12*C6+6*delta*tr4:
        raise AssertionError("six-walk noninjective/backtrack bound invalid")
    if tr4*tr4>2*e*tr6:
        raise AssertionError("four/six trace Cauchy invalid")
    # d^5>=144*n*Delta^2, EXACT integer condition, no rounding:
    # (2e)^5 >=144*n^6*Delta^2.
    spectral=(n>0 and e>0 and
              (2*e)**5 >=144*n**6*delta**2)
    lower= d**6/24 if spectral else None
    if spectral and C6<lower:
        raise AssertionError("NEW self-contained explicit C6 floor failed")
    trial=None
    if trial_C_graph is not None:
        if type(trial_C_graph) not in (int,Fraction) or Fraction(trial_C_graph)<=0:
            raise ValueError("trial C must be an exact positive rational only")
        C=Fraction(trial_C_graph)
        trial={
            "hypothetical_C_test_only":C,
            "trial_density_condition_e_ge_C_v_4_over_3":
                (n>0 and e**3>=C**3*n**4),
            "exact_cubed_e_over_v_fourthird":
                Fraction(e**3,n**4) if n else Fraction(),
            "NOT_verified_published_C_value":True,
        }
    return {
        "v":n,"e":e,"delta":delta,"average_degree":d,
        "ordinary_unoriented_simple_C6":C6,
        "trA4":tr4,"trA6":tr6,
        "spectral_direct_condition_met":spectral,
        "spectral_direct_C6_lower":lower,
        "degree_cap_condition_exact_fraction_ratio":
            (Fraction((2*e)**5,144*n**6*delta**2)
             if n and delta else None),
        "published_ordinary_C6_theorem_conditional_statement":
            "For some absolute C_graph,c_graph>0, if e^3>=C_graph^3*v^4 then C6>=c_graph*(e/v)^6.",
        "published_graph_constants_NUMERICALLY_UNKNOWN":True,
        "external_statement_is_ordinary_SIMPLE_graphs_not_homomorphisms":True,
        "trial_graph_hypothesis":trial,
    }


def independent_closed_six_walk_oracle(graph):
    """Independent naive closed-6-walk and injective-6-vertex DFS.

    TEST ONLY for small graphs, no historical cycle enumerator.
    """
    total_walks=0
    injective_walks=0
    for start in graph:
        def walk(v,path):
            nonlocal total_walks,injective_walks
            if len(path)==6:
                if start in graph[v]:
                    total_walks+=1
                    injective_walks+=len(set(path))==6
                return
            for w in graph[v]:
                walk(w,path+(w,))
        walk(start,(start,))
    if injective_walks%12:
        raise AssertionError("unoriented C6 has 12 rooted/oriented representatives")
    return {"trA6_direct_walks":total_walks,"C6_direct_12fold":injective_walks//12}


def exact_balanced_chunk_parameter_gate(epsilon,C_graph,s,T):
    """Exact symbolic bridge, NO assumption numeric published C_graph.

    Input graph theorem constants are hypothetical symbolic RATIOS.
    Validates only the CONDITIONAL algebra in #684 at any actual s.
    """
    for val in (epsilon,C_graph,T):
        if type(val) not in (int,Fraction) or Fraction(val)<=0:
            raise ValueError("positive exact rational inputs required")
    if type(s) is not int or s<64 or s&(s-1):
        raise ValueError("dyadic original GQ parameter s>=64 required")
    eps,C,t=map(Fraction,(epsilon,C_graph,T))
    beta=eps*eps/128
    threshold=(2**19)*C**3/beta**3
    if threshold!=(2**40)*C**3/eps**6:
        raise AssertionError("source heavy-tail constant bridge incorrect")
    # If m/v>=beta*s/32 and v<=16*s^3/T,
    # sufficient for e>=C*v^(4/3) iff t>=threshold.
    meets=t>=threshold
    return {
        "s":s,"epsilon":eps,"trial_symbolic_C_graph":C,
        "T":t,"beta_original_source_flag_fraction":beta,
        "symbolic_sufficient_T":threshold,
        "conditional_theorem_hypothesis_certified_if_all_chunk_bounds_hold":meets,
        "conditional_C6_floor_as_coefficient_of_s6_for_c_graph_equal_1":
            eps**12/Fraction(2**72),
        "published_C_graph_NOT_assigned_a_real_numeric_value":True,
        "source_D6_transfer_and_real_chunk_properties_are_SEPARATE_OBLIGATIONS":True,
    }


def _original_pair_maps(power,f,g):
    s,V,flags=genuine_source(power)
    a=2
    while a*(a-1)//2<V:a+=1
    legal=set(combinations(range(a),2))
    try:f=tuple(tuple(x) for x in f);g=tuple(tuple(y) for y in g)
    except (ValueError,TypeError):raise ValueError("typed maps missing")
    if (len(f)!=V or len(g)!=V or len(set(f))!=V or len(set(g))!=V
        or any(x not in legal for x in f+g)):
        raise ValueError("complete globally injected f,g on MINIMAL pair alphabet required")
    return s,V,flags,a,f,g


def true_original_selected_graph_ss6_gate(power,f,g,ids,lc,rc):
    """Independently prove selected G conditions on actual original W32/W34.

    Require ORIGINAL source conflict independence and both full-flag
    typed cuts; verify BOTH original flag diagonals, all simple C6
    coordinate-proper with SIX distinct original flags/factors, and
    injective original D6 sixsets. Does not assert graph C constants.
    """
    if type(power) is not int or power not in (1,2):
        raise ValueError("finite true original GQ W32/W34 only")
    s,V,flags,a,f,g=_original_pair_maps(power,f,g)
    I=tuple(ids)
    if len(set(I))!=len(I) or any(type(i) is not int or i<0 or i>=len(flags) for i in I):
        raise ValueError("distinct actual retained ORIGINAL flag IDs required")
    if (len(lc)!=a or len(rc)!=a or
        any(type(c) is not int or c not in (0,1) for c in tuple(lc)+tuple(rc))):
        raise ValueError("complete 0/1 typed physical alphabet color cuts required")
    ff=list(map(set,f));gg=list(map(set,g))
    for i,j in combinations(I,2):
        p,l=flags[i];q,m=flags[j]
        if (p==q and gg[l]&gg[m]) or (l==m and ff[p]&ff[q]):
            raise ValueError("source selected original flags contain pencil conflict")
    graph={}
    owner={}
    for i in I:
        p,l=flags[i]
        x,z=f[p];y,w=g[l]
        if lc[x]==lc[z] or rc[y]==rc[w]:
            raise ValueError("source flag not bichromatic on BOTH typed cuts")
        for u,v in (((x,y),(z,w)),((x,w),(z,y))):
            edge=frozenset((u,v))
            if len(edge)!=2 or edge in owner:
                raise AssertionError("ORIGINAL physical paired edges not unique")
            owner[edge]=i
            graph.setdefault(u,set()).add(v)
            graph.setdefault(v,set()).add(u)
    if len(owner)!=2*len(I):raise AssertionError("source physical paired edge lost")
    left=tuple(sorted((v for v in graph if lc[v[0]]==0)))
    right=tuple(sorted((v for v in graph if lc[v[0]]==1)))
    audit=exact_c6_gate(graph,left,right)
    source_sixsets=set()
    # Entire graph C6 census using LEFT triples and DISTINCT RIGHT
    # common-neighbor choices, no historical original D6 oracle.
    for x,y,z in combinations(left,3):
        xy=graph[x]&graph[y]
        yz=graph[y]&graph[z]
        zx=graph[z]&graph[x]
        for a1 in xy:
            for b1 in yz:
                if b1==a1:continue
                for c1 in zx:
                    if c1 in (a1,b1):continue
                    cyc=(x,a1,y,b1,z,c1)
                    if len({v[0] for v in cyc})!=6 or len({v[1] for v in cyc})!=6:
                        raise AssertionError("coherent original C6 repeats physical coordinate")
                    originals=tuple(owner[frozenset((cyc[k],cyc[(k+1)%6]))] for k in range(6))
                    if (len(set(originals))!=6 or
                        len({flags[i][0] for i in originals})!=6 or
                        len({flags[i][1] for i in originals})!=6):
                        raise AssertionError("selected ordinary C6 is not six distinct genuine D6 flags")
                    six=frozenset(originals)
                    if six in source_sixsets:
                        raise AssertionError("one original source D6 sixset counts physical cycles twice")
                    source_sixsets.add(six)
    if len(source_sixsets)!=audit["ordinary_unoriented_simple_C6"]:
        raise AssertionError("independent original D6 sixsets != exact ordinary cycles")
    return {
        "s":s,"actual_ORIGINAL_selected_IDs":len(I),
        "actual_original_paired_diagonal_edges":len(owner),
        "actual_selected_graph_bipartite":True,
        "actual_selected_graph_no_coordinate_cherries":True,
        "ordinary_graph_audit":audit,
        "injected_distinct_original_D6_sixsets":len(source_sixsets),
        "source_sixID_flag_injection":True,
        "this_finite_audit_does_NOT_derive_external_C_graph":True,
    }
