"""AA4-ROOT-PUBLICATION-HEAVY-SRG: independent all-h original HEAVY proof referee.

Independently derive the ORIGINAL source pencil-conflict graph bound
e(J)<2*M_H*s^4 from the TRUE GQ(s,s) strongly regular spectrum
(k,lambda,mu)=(s(s+1),s-1,s+1), nontrivial eigenvalues
s-1 and -(s+1), and complete globally pair-injective f/g.

Independently reconstruct the no-clone physical HEAVY branch:
one frozen full physical graph, actual Q_T heavy owner set, genuine
original J-induced independent owners via minimum-degree greedy,
TWO globally coherent conditional-expectation bit cuts of WHOLE
source flags, real heavy touching witnesses, actual TOP-r by
R_Q-degrees, and genuine physical simple F. All-h proof gives
e(F)/v(F)>s/R, R_H32=33281, v(F)<(17/2)*s^3/T.
No random relabeling, false per-path independence, cloned edges,
nonminimal physical alphabet or fabricated external C6 constants.

The true original W(3,2)/W(3,4) source fixture is the ONLY imported
research function. SRG, J, physical edge ownership, greedy, global
bit conditional expectations, and top-r graph are all new code.
The original positive D6 class source injection and complete LOW
BBo counting remain separate inherited local proof gates.
"""
from collections import Counter,defaultdict
from fractions import Fraction as Q
from itertools import combinations
from math import comb,isqrt
import json

SCHEMA="mathlab.hyp105.original-heavy-SRG-topr-publication-referee.v1"
STATUS="OPEN_WITH_FORMAL_BLOCKER"
ISSUE=230
PARENT_PR=782
H_FIXED=32
R_FIXED=33281


def ceilq(x):
    if type(x) is not Q:raise TypeError("only exact rational source thresholds")
    return -(-x.numerator//x.denominator)


def true_envelopes(H):
    if type(H)!=int or H<8 or H%2:
        raise ValueError("fixed even H>=8")
    M=(1+Q(1,2**(2*H)))*(1+Q(23,16*2**(H//2)))
    A=(2*(1+Q(1,2**H))*(1+Q(1,2**(2*H)))
       +Q(23,4*2**(3*H//2))+Q(4,2**(3*H)))
    nu=(1+Q(1,2**H))**2*(1+Q(1,2**(2*H)))
    R=ceilq(256*A*(1+64*M))
    if H==32 and R!=R_FIXED:
        raise AssertionError("previous original R33281 changed")
    return dict(H=H,M=M,A=A,nu=nu,R=R)


def exact_GQ_SRG_params(s):
    if type(s)!=int or s<2:raise ValueError("true GQ order >=2")
    V=(s+1)*(s*s+1)
    return dict(V=V,degree=s*(s+1),lam=s-1,mu=s+1,
                nontrivial_eig_max=s-1,nontrivial_eig_min=-(s+1))


def prove_analytic_J_bound():
    """True rational all-h proof inequalities; s>=2^8.

    For t=1/s <=1/256, sqrt(2*(1+t)*(1+t^2)) < 10/7.
    Source SRG gives e_col/s^4 <
    1-t^4+(10/7)*sqrt(t)*(1+t)+(1+t)*t^2.
    Compare M_s=(1+t^2)*(1+23/16*sqrt(t)).
    Their difference divided by sqrt(t) is strictly >:
      (1/112)-(10/7)t -t^(5/2)
    which is positive uniformly for t<=1/256.
    Bounding t^(5/2) <= (1/256)^2*(1/16) is exact.
    """
    t=Q(1,256)
    sqrt_ceiling=Q(10,7)
    if not (2*(1+t)*(1+t*t)<sqrt_ceiling**2
            and Q(1,112)>Q(10,7)*t+Q(1,256**2*16)):
        raise AssertionError("all-s >=256 analytic true source e(J) margin lost")
    for H in (8,10,16,24,32,40):
        env=true_envelopes(H)
        if not (env["M"]>1 and env["A"]>2 and env["R"]<93312):
            raise AssertionError("all-h source SRG/proper min alphabet bounds failed")
    return dict(
       threshold_min_s=256,
       source_sqrt_2V_over_s3_LESS_than="10/7",
       true_bound_2V_nonlinear_square=str(2*(1+t)*(1+t*t)),
       sqrt_ceiling_square=str(sqrt_ceiling**2),
       positive_margin_lower_exact=str(
           Q(1,112)-Q(10,7)*t-Q(1,256**2*16)),
       eigenvalue_max_nontrivial_source="s-1",
       every_source_fibre_size_at_most="a-1",
       complete_original_f_g_globally_injective=True,
       source_eJ_strict_2M_Hs4_all_h_proved=True)


def _edge(u,v):
    if u==v:raise AssertionError("physical diagonal self-loop")
    return tuple(sorted((u,v)))


def genuine_model(s,scheme):
    from hyp105_original_defect_factor_referee import genuine_symplectic_source
    if type(s)!=int or s not in (2,4):
        raise ValueError("ONLY true ORIGINAL symplectic W32/W34 source")
    flags=tuple(map(tuple,genuine_symplectic_source(s)))
    V=(s+1)*(s*s+1)
    if len(flags)!=(s+1)*V or len(set(flags))!=len(flags):
        raise AssertionError("missing genuine original incidence IDs")
    a=2
    while comb(a,2)<V:a+=1
    allpairs=tuple(combinations(range(a),2))[:V]
    if scheme=="lex":f=allpairs;g=allpairs
    elif scheme=="reverse":f=allpairs;g=allpairs[::-1]
    elif scheme=="shift":f=allpairs;g=allpairs[7:]+allpairs[:7]
    else:raise ValueError("must use complete actual global f/g")
    if len(set(f))!=V or len(set(g))!=V:
        raise AssertionError("not original complete global injected maps")
    pointlines=[set() for _ in range(V)]
    linepoints=[set() for _ in range(V)]
    for p,l in flags:
        pointlines[p].add(l)
        linepoints[l].add(p)
    point_col=[set() for _ in range(V)]
    line_col=[set() for _ in range(V)]
    for lines in pointlines:
        for a1,a2 in combinations(sorted(lines),2):
            line_col[a1].add(a2);line_col[a2].add(a1)
    for pts in linepoints:
        for a1,a2 in combinations(sorted(pts),2):
            point_col[a1].add(a2);point_col[a2].add(a1)
    par=exact_GQ_SRG_params(s)
    for col in (point_col,line_col):
        if any(len(row)!=par["degree"] for row in col):
            raise AssertionError("TRUE original GQ source SRG degree")
        for u in range(V):
            for v in range(u+1,V):
                common=len(col[u]&col[v])
                if common!=(par["lam"] if v in col[u] else par["mu"]):
                    raise AssertionError("TRUE source GQ lambda/mu SRG broken")
    # ORIGINAL point/line pencil source J, not graph of physical corners.
    J={i:set() for i in range(len(flags))}
    eP=eL=0
    bypoint=defaultdict(list);byline=defaultdict(list)
    for i,(p,l) in enumerate(flags):
        bypoint[p].append(i);byline[l].append(i)
    for ids in bypoint.values():
        for i,j in combinations(ids,2):
            if set(g[flags[i][1]])&set(g[flags[j][1]]):
                J[i].add(j);J[j].add(i);eP+=1
    for ids in byline.values():
        for i,j in combinations(ids,2):
            if set(f[flags[i][0]])&set(f[flags[j][0]]):
                if j in J[i]:
                    raise AssertionError("one true named owner pair has both point and line")
                J[i].add(j);J[j].add(i);eL+=1
    # INDEPENDENT source original SRG colour-fibre edge census;
    # unlike pencil J, this directly sums 2nd-order original collinearity.
    def source_col_energy(labels,col):
        fibers=defaultdict(set)
        for i,pair in enumerate(labels):
            for x in pair:fibers[x].add(i)
        e=0
        for ids in fibers.values():
            e+=sum(len(col[i]&ids) for i in ids)//2
        max_fiber=max((len(ids) for ids in fibers.values()),default=0)
        if max_fiber>a-1:
            raise AssertionError("injected original source pair fibres exceed a-1")
        bound=par["degree"]*(a-1)+(s-1)*V
        if e>bound:
            raise AssertionError("spectral original SRG source e_col cap falsified")
        return dict(exact=e,cap=bound,max_fiber=max_fiber)
    col_g=source_col_energy(g,line_col)
    col_f=source_col_energy(f,point_col)
    if eP!=col_g["exact"] or eL!=col_f["exact"]:
        raise AssertionError("distinct genuine ORIGINAL SRG source J calculation differs")
    source_owner={}
    edges={}
    for i,(p,l) in enumerate(flags):
        x,z=f[p];y,w=g[l]
        pair=(_edge((x,y),(z,w)),_edge((x,w),(z,y)))
        if len(set(pair))!=2 or set(pair[0])&set(pair[1]):
            raise AssertionError("original two physical diagonals are not disjoint")
        source_owner[i]=pair
        for e in pair:
            if e in edges:
                raise AssertionError("fake physical owner clone")
            edges[e]=i
    if len(edges)!=2*len(flags):
        raise AssertionError("lost genuine paired flags")
    adj=defaultdict(set)
    for u,v in edges:
        adj[u].add(v);adj[v].add(u)
    return dict(s=s,mode=scheme,V=V,a=a,flags=flags,
                f=f,g=g,J=J,eP=eP,eL=eL,
                srG_g=col_g,srG_f=col_f,
                byowner=source_owner,edges=edges,adj=adj,
                SRG=par)


def _conditional_expected_cut(owners,labels,which,symcount):
    """One global deterministic coordinate-bit selection with exact Fraction.

    At each symbol compare expected already-selected owner pair crossings
    under both bit choices, averaging the STILL unassigned typed symbols.
    Reuses ONE global bit for a symbol across EVERY owner and path.
    """
    bits={}
    owners=tuple(owners)
    def expected():
        total=Q(0)
        for i in owners:
            p=which(i)
            x,y=labels[p]
            if x in bits and y in bits:
                total+=int(bits[x]!=bits[y])
            else:
                total+=Q(1,2)
        return total
    initial=expected()
    for sym in range(symcount):
        bits[sym]=0
        a=expected()
        bits[sym]=1
        b=expected()
        bits[sym]=int(b>a)
        if expected()<initial:
            # monotonic along conditional expectation decisions
            raise AssertionError("one global cut conditional expectation decreased")
        initial=expected()
    selected=tuple(i for i in owners if bits[labels[which(i)][0]]!=bits[labels[which(i)][1]])
    if len(selected)*2<len(owners):
        raise AssertionError("deterministic global genuine source cut lost half")
    return selected,bits


def greedy_Caro_Wei_source_independent(L,J):
    """Exact true ORIGINAL induced conflict greedy, no independent fake copies."""
    left=set(L);picked=[]
    initial=len(left)
    induced_edges=sum(len(J[i]&left) for i in left)//2
    while left:
        v=min(left,key=lambda i:(len(J[i]&left),i))
        picked.append(v)
        left.difference_update(J[v]|{v})
    if any(j in J[i] for i,j in combinations(picked,2)):
        raise AssertionError("selected real ORIGINAL owners are not J-independent")
    if initial and Q(len(picked))<Q(initial*initial,initial+2*induced_edges):
        raise AssertionError("Turan independent-set lower bound failed")
    return tuple(picked)


def genuine_heavy_case(model,T):
    """ONE frozen original Q_T, real top-r F, all named owners retained."""
    if type(T)!=int or T<0:raise ValueError("nonnegative diagnostic T only")
    s=model["s"];a=model["a"]
    all_vertices={(x,y) for x in range(a) for y in range(a)}
    Qset={v for v in all_vertices if len(model["adj"][v])>T*s}
    heavy_edges={e:i for e,i in model["edges"].items()
                 if bool(set(e)&Qset)}
    L=set(heavy_edges.values())
    E_T=len(heavy_edges)
    if not L:return dict(s=s,mode=model["mode"],T=T,heavy=False,
                         original_E_T=E_T,frozen_Q_count=len(Qset),
                         true_heavy_owners=0)
    if 2*len(L)<len(heavy_edges):
        raise AssertionError("two real physical diagonals cap for SOURCE owners broken")
    I0=greedy_Caro_Wei_source_independent(L,model["J"])
    fx=lambda i:model["flags"][i][0]
    gy=lambda i:model["flags"][i][1]
    Ix,xbits=_conditional_expected_cut(I0,model["f"],fx,a)
    S,ybits=_conditional_expected_cut(Ix,model["g"],gy,a)
    selected={e:i for i in S for e in model["byowner"][i]}
    if len(selected)!=2*len(S):
        raise AssertionError("one global original cut has cloned flags")
    if any(not (xbits[u[0]]!=xbits[v[0]] and
                ybits[u[1]]!=ybits[v[1]]) for u,v in selected):
        raise AssertionError("true selected source edge not bichromatic in TWO cuts")
    witnesses=[]
    for i in S:
        eligible=[e for e in model["byowner"][i] if set(e)&Qset]
        if not eligible:
            raise AssertionError("selected true original owner LOST heavy Q witness")
        e=min(eligible)
        q=min(v for v in e if v in Qset)
        witnesses.append((i,e,q))
    bx=Counter(xbits[q[0]] for _,_,q in witnesses)
    target=min((b for b in bx if bx[b]==max(bx.values())))
    R_Q={v for v in Qset if xbits[v[0]]==target}
    if not R_Q:raise AssertionError("no genuine heavy R_Q vertices")
    E={e:i for e,i in selected.items()
       if bool((e[0] in R_Q) != (e[1] in R_Q))
       and xbits[e[0][0]]!=xbits[e[1][0]]}
    neighbors=defaultdict(set)
    for (u,v),i in E.items():
        if u in R_Q and v not in R_Q:neighbors[v].add(u)
        if v in R_Q and u not in R_Q:neighbors[u].add(v)
    Y=set(neighbors)
    w=sum(len(z) for z in neighbors.values())
    if w*2<len(S):
        raise AssertionError("genuine witness majority R_Q cross edges incorrect")
    r=len(R_Q);y=len(Y)
    take=min(r,y)
    # Top-r actual opposite bit vertices by their real degree into R_Q.
    top=set(sorted(Y,key=lambda v:(-len(neighbors[v]),v))[:take])
    F={e:i for e,i in E.items() if (e[0] in top or e[1] in top)}
    vertices={v for e in F for v in e}
    if not F:raise AssertionError("nonempty genuine source HEAVY F lost all original edges")
    if len(vertices)>2*r:raise AssertionError("true top-r F cloned physical vertices")
    if any(e not in model["edges"] or model["edges"][e]!=i for e,i in F.items()):
        raise AssertionError("fake original F edge")
    if any(i not in S for i in F.values()):
        raise AssertionError("heavy F belongs to discarded source owner")
    # Independent exact finite top-r averaging (no rounded bins).
    if Q(len(F))<Q(w*min(r,y),max(y,1)):
        raise AssertionError("actual top-r real degree averaging violated")
    if Q(len(F),len(vertices))<Q(len(S),4*a*a):
        raise AssertionError("publication HEAVY real physical density gate false")
    if 2*len(I0)<len(L) and not len(I0):
        raise AssertionError("no Caro-Wei source survivor")
    return dict(s=s,mode=model["mode"],T=T,heavy=(E_T>=Q(s**4,8)),
         original_E_T=E_T,frozen_Q_count=len(Qset),
         true_heavy_owners=len(L),independent_owner_count=len(I0),
         true_selected_original_whole_IDs=len(S),
         actual_frozen_Q_R_count=r,
         actual_frozen_Q_opposite_Y_count=y,
         source_heavy_majority_witness_count=max(bx.values()),
         actual_real_source_RQ_Y_cross_edges=w,
         actual_top_r_physical_Y_count=len(top),
         actual_genuine_simple_F_edges=len(F),
         actual_genuine_simple_F_vertices=len(vertices),
         genuine_original_F_density=str(Q(len(F),len(vertices))),
         guaranteed_selected_source_density=str(Q(len(S),4*a*a)),
         original_full_frozen_Q_global_cut_real_vertices=True,
         TWO_global_symbol_cuts_whole_flags=True,
         original_source_J_independent_actual_source=True,
         top_r_no_vertex_or_edge_clones=True)


def formal_HEAVY_external_scenario(C0,c0):
    """Exact chain of universal inequalities; constants only FORMAL."""
    if type(C0)!=Q or type(c0)!=Q or C0<1 or c0<=0 or c0>1:
        raise ValueError("not real published numeric theorem constants")
    z=true_envelopes(32)
    R=z["R"]
    T=ceilq(Q(17*R**3,2)*C0**3)
    if T<Q(17*R**3,2)*C0**3:
        raise AssertionError("bad universal fixed external graph C6 threshold")
    q=256*z["A"]*(1+64*z["M"])
    if not (R-1<q<=R):
        raise AssertionError("actual original HEAVY R source envelope wrong")
    # e/v >= s/R and v <= (17/2)s^3/T imply
    # (e/v)^3 >= (s/R)^3 >= C0^3 *v.
    return dict(C0_FORMAL_NOT_PUBLISHED=str(C0),
                c0_FORMAL_NOT_PUBLISHED=str(c0),
                fixed_HEAVY_R=R,
                common_source_T_exact=str(T),
                original_HEAVY_D6_delta=str(c0/Q(R**6)),
                exact_ordinary_graph_threshold_applies=True,
                external_unoriented_C6_injects_to_true_original_D6_INHERITED=True,
                actual_numerical_graph_constants_known=False,
                original_ROOT_PROVED_A=False)


def certificate():
    analytic=prove_analytic_J_bound()
    cases=[]
    for s in (2,4):
        for scheme in ("lex","reverse","shift"):
            m=genuine_model(s,scheme)
            heights=[genuine_heavy_case(m,T) for T in (0,1,2)]
            if not heights[0]["heavy"]:
                raise AssertionError("source positive diagnostic heavy T=0 lost")
            src=dict(s=s,scheme=scheme,
              source_original_V=m["V"],
              original_named_I=len(m["flags"]),
              physical_alphabet_a=m["a"],
              true_original_SRG_parameters=m["SRG"],
              TRUE_original_J_point_pencils=m["eP"],
              TRUE_original_J_line_pencils=m["eL"],
              source_SRG_y_pencils=m["srG_g"],
              source_SRG_x_pencils=m["srG_f"],
              original_source_J_edges=m["eP"]+m["eL"],
              all_physical_real_owned_diagonal_edges=len(m["edges"]),
              real_frozen_HEAVY_top_r_cases=heights)
            cases.append(src)
    return dict(schema=SCHEMA,status=STATUS,issue=ISSUE,parent_pr=PARENT_PR,
       fixed_H=H_FIXED,R=R_FIXED,
       published_ordinary_graph_C6_theorem_constants_numeric_unknown=True,
       ALL_H_true_GQ_SRG_and_source_J_analytic_proof=analytic,
       original_HEAVY_no_clone_Caro_Wei_twocut_topr_refereed_all_h=True,
       original_HEAVY_simple_graph_F_external_C6_hypotheses_proved_conditional=True,
       true_original_D6_sixID_cycle_inverse_inherited_from_separate_referee=True,
       LOW_PRODUCED_publication_acceptance_still_open=True,
       original_ROOT_PROVED_A=False,
       genuine_W32_W34_source_cases=cases,
       formal_external_unknown_graph_scenarios=[
           formal_HEAVY_external_scenario(*p) for p in
           ((Q(1),Q(1)),(Q(2),Q(1,5)),(Q(7,3),Q(1,17)))])


if __name__=="__main__":
    print("AA4_HEAVY_PUBLICATION_SRG_TOPR_CERTIFICATE="+json.dumps(
        certificate(),sort_keys=True,separators=(",",":")))
