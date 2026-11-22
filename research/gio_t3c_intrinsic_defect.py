"""GIO-003/G6-C1: intrinsic defect-matrix and typed-label spectral gates.

Only typed, simple, (s,t)-biregular original incidence with girth>=8.
NO GQ/template/full-projection axiom. A1 conflict + Gram for fixed linear
line-excess, and A2 proper physical C6 -> historical D6 are proved here.
A4/A5/A6 full produced-BBo supersaturation remain OPEN.

Every finite assertion is an independent exact falsifier, not an all-order
proof or a numeric published graph-supersaturation certificate.
"""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import combinations
from math import comb, isqrt
from pathlib import Path
import argparse
import json
import random

from gio_generalized_gq import geometry, min_labels
from hyp105_aa4_branch_a_integrated_referee import physical_d6
from gio_resilience import source_first_d6

SCHEMA = "mathlab.gio003.g6c1.intrinsic-defect.v1"
BASE_MAIN = "f42aa108a2f9e15dadebf5c45fa4923cc435742b"


def ceil_sqrt(n):
    if type(n) is not int or n < 0:
        raise ValueError("nonnegative exact integer required")
    k = isqrt(n)
    return k + (k*k < n)


def source_graph(lines, point_count, s, t):
    """Independent incidence-first oracle; detect any C4 or C6, no GQ use."""
    if any(type(x) is not int or x < 2 for x in (s, t)):
        raise ValueError("thick positive integer (s,t) required")
    if type(point_count) is not int or point_count < 1:
        raise ValueError("explicit point count required")
    if not lines:
        raise ValueError("nonempty original lines required")
    lines = tuple(tuple(sorted(x)) for x in lines)
    for ell, line in enumerate(lines):
        if len(line) != s+1 or len(set(line)) != s+1:
            raise ValueError(("line degree failure", ell))
        if any(type(p) is not int or not 0 <= p < point_count for p in line):
            raise ValueError("point outside literal source range")
    on = [set() for _ in range(point_count)]
    owner = {}
    for ell, line in enumerate(lines):
        for p in line:
            on[p].add(ell)
        for p, q in combinations(line, 2):
            if (p, q) in owner:
                raise ValueError("source 4-cycle or repeated point pair")
            owner[p, q] = ell
    if any(len(z) != t+1 for z in on):
        raise ValueError("point biregularity failure")
    nbr_p = [set() for _ in range(point_count)]
    for p, q in owner:
        nbr_p[p].add(q)
        nbr_p[q].add(p)
    nbr_l = [set() for _ in lines]
    for around in on:
        for ell in around:
            nbr_l[ell].update(around-{ell})
    for p in range(point_count):
        assert len(nbr_p[p]) == s*(t+1)
    for ell in range(len(lines)):
        assert len(nbr_l[ell]) == t*(s+1)

    projections, missing = {}, []
    for q in range(point_count):
        for ell, line in enumerate(lines):
            if ell in on[q]:
                continue
            feet = nbr_p[q].intersection(line)
            if len(feet) > 1:
                raise ValueError(("source 6-cycle / multiple 3paths", q, ell,
                                  tuple(sorted(feet))))
            if not feet:
                missing.append((q, ell))
                continue
            foot = next(iter(feet))
            join = owner[(min(q, foot), max(q, foot))]
            anchors = ((q, join), (foot, join), (foot, ell))
            assert len(set(anchors)) == 3
            assert all(y in lines[l] for y,l in anchors)
            projections[q, ell] = anchors

    dp = point_count-(s+1)*(s*t+1)
    dl = len(lines)-(t+1)*(s*t+1)
    if dp < 0 or dl < 0:
        raise AssertionError("Moore bound violated by supposed girth>=8")
    assert dp*(t+1) == dl*(s+1)
    assert len(missing) == point_count*dl
    assert len(projections) == point_count*(t+1)*s*t
    flags = tuple(sorted((p,l) for l,line in enumerate(lines) for p in line))
    assert len(flags) == point_count*(t+1) == len(lines)*(s+1)
    load = Counter(flag for path in projections.values() for flag in path)
    assert len(load) == len(flags) and all(load[x] == 3*s*t for x in flags)
    return dict(lines=lines, points=point_count, s=s, t=t, on=on, flags=flags,
                neighbors_point=nbr_p, neighbors_line=nbr_l,
                projected=projections, missing=tuple(missing),
                excess_points=dp, excess_lines=dl, projection_load=load)


def defect_matrices(m):
    """Exact symmetric missing-threepath defect from named original flags."""
    P,L=m["points"],len(m["lines"])
    Dp=[[0]*P for _ in range(P)]
    Dl=[[0]*L for _ in range(L)]
    for q,ell in m["missing"]:
        for y in m["lines"][ell]:
            Dp[q][y] += 1
        for other in m["on"][q]:
            Dl[ell][other] += 1
    s,t=m["s"],m["t"]
    d=(s+1)*m["excess_lines"]
    assert d==(t+1)*m["excess_points"]
    for D in (Dp,Dl):
        assert all(D[i][i] == 0 for i in range(len(D)))
        assert all(sum(row) == d for row in D)
        assert all(D[i][j] == D[j][i] for i in range(len(D))
                   for j in range(i+1,len(D)))
    return Dp,Dl,d


def exact_second_walk_identity(neighbors, D, s, t):
    """M^2=(k-mu)I+(lambda-mu)M+mu*11^T-D for true C4/C6-free source."""
    V=len(neighbors)
    k=s*(t+1); lam=s-1; mu=t+1; theta=lam-mu
    assert len(D)==V and all(len(row)==V for row in D)
    for x in range(V):
        assert len(neighbors[x])==k
        for y in range(V):
            lhs=len(neighbors[x] & neighbors[y])
            rhs=(k-mu)*(x==y)+theta*(y in neighbors[x])+mu-D[x][y]
            if lhs!=rhs:
                raise AssertionError(("defect matrix identity failed",x,y,lhs,rhs))
    return dict(vertices=V,degree=k,lambda_adjacent=lam,mu_nominal=mu,
                theta=theta,k_minus_mu=k-mu,
                exact_identity=True)


def typed_maps(m, scheme="lex"):
    """Minimal independent source factor pair alphabets, no geometry restriction."""
    vp,vl=m["points"],len(m["lines"])
    aP,fs=min_labels(vp)
    aL,gs=min_labels(vl)
    if scheme=="correlated":
        # Adversarial fixed complete maps; no f/g independence assumption.
        rs=random.Random(793+vp+3*vl)
        fp=list(fs); gp=list(gs)
        rs.shuffle(fp); rs.shuffle(gp)
        fs,gs=tuple(fp),tuple(gp)
    elif scheme!="lex":
        raise ValueError("unknown typed label arrangement")
    assert len(set(fs))==vp and len(set(gs))==vl
    assert comb(aP-1,2)<vp<=comb(aP,2)
    assert comb(aL-1,2)<vl<=comb(aL,2)
    return dict(flags=m["flags"],f=fs,g=gs,aP=aP,aL=aL,
                point_by_pair={p:i for i,p in enumerate(fs)},
                line_by_pair={p:i for i,p in enumerate(gs)})


def typed_conflicts_and_gram(m, labels, neighbor, defect, s, t):
    """Two independent exact censuses for each source collinearity type."""
    V=len(labels);a=max(max(pair) for pair in labels)+1
    assert len(labels)==V and len(set(labels))==V
    fibers=defaultdict(set)
    for i,pair in enumerate(labels):
        assert len(pair)==2 and pair[0]!=pair[1]
        for x in pair:
            fibers[x].add(i)
    occupancy=sum(len(z)**2 for z in fibers.values())
    assert sum(map(len,fibers.values()))==2*V
    assert all(len(z)<=a-1 for z in fibers.values())
    e_col=0
    for i in range(V):
        for j in neighbor[i]:
            if j>i and set(labels[i])&set(labels[j]):
                e_col+=1
    # Independent symbol-first direct point-graph conflict census.
    e_sym=sum(sum(1 for x,y in combinations(sorted(fiber),2)
                  if y in neighbor[x]) for fiber in fibers.values())
    assert e_sym==e_col
    k=s*(t+1);mu=t+1;theta=s-t-2
    q_direct=sum(sum(len(neighbor[i]&fiber)**2 for i in range(V))
                 for fiber in fibers.values())
    corr=sum(sum(defect[i][j] for i in fiber for j in fiber)
             for fiber in fibers.values())
    formula=2*V*(k-mu)+2*theta*e_col+mu*occupancy-corr
    assert formula==q_direct
    assert corr>=0
    return dict(vertices=V,alphabet=a,degree=k,e_col=e_col,
                source_fiber_square=occupancy,
                defect_correction=corr,gram=q_direct,
                repaired_gram_formula=True,
                symbol_first_conflicts_checked=True)


def direct_original_owner_conflicts(m, maps):
    """Independent original-flag-pair J census; neither spectrum nor Gram."""
    original_flags=m["flags"]
    points=defaultdict(list)
    lines=defaultdict(list)
    for i,(p,l) in enumerate(original_flags):
        points[p].append(i)
        lines[l].append(i)
    point_shared=0
    for at in points.values():
        for i,j in combinations(at,2):
            li,lj=original_flags[i][1],original_flags[j][1]
            if set(maps["g"][li]) & set(maps["g"][lj]):
                point_shared+=1
    line_shared=0
    for at in lines.values():
        for i,j in combinations(at,2):
            pi,pj=original_flags[i][0],original_flags[j][0]
            if set(maps["f"][pi]) & set(maps["f"][pj]):
                line_shared+=1
    return dict(J=point_shared+line_shared,via_point=point_shared,
                via_line=line_shared)


def spectral_cap(k, theta, mu, d):
    """Exact integer eigenvalue ceiling on 1-perp from defect identity.

    For any eigenvalue x of collinearity adjacency on the 1-perp subspace,
    x^2 <= |theta| |x| + (k-mu)+d, since the missing-defect matrix is
    symmetric, entrywise nonnegative and d-regular.
    Therefore |x|<=|theta|+ceil_sqrt(k-mu+d).
    """
    assert k>=mu>0 and d>=0
    L=abs(theta)+ceil_sqrt(k-mu+d)
    assert L*L-abs(theta)*L>=k-mu+d
    return L


def coarse_linear_excess_ledger(m, maps, P, L, point_data, line_data,
                                balance, line_excess_multiplier):
    """Rigorous all-order intrinsic A1 bound when Delta_L<=C*r.

    b and C are fixed before the family; finite fixture examples may
    instantiate C=ceil(Delta/r) only as *individual falsifiers*.
    """
    if any(type(x) is not int for x in (balance,line_excess_multiplier)):
        raise ValueError("b,C must be fixed integers")
    b=balance;C=line_excess_multiplier
    if b<1 or C<0:
        raise ValueError("b>=1, C>=0")
    s,t=m["s"],m["t"]
    r=min(s,t)
    if max(s,t)>b*r or m["excess_lines"]>C*r:
        raise ValueError("outside fixed balance/linear Moore-excess gate")
    Dp,Dl,d=defect_matrices(m)
    k0=b*(b+1)
    theta0=b+2
    v0=(b+1)*(b*b+1+C)
    a0=2*v0+3
    lambda0=theta0+(b+1)*(b+C)
    j0=k0*a0+lambda0*v0
    J0=2*j0
    G0=2*v0*k0+2*theta0*j0+2*(b+1)*v0*a0
    assert m["points"]<=v0*r**3 and len(m["lines"])<=v0*r**3
    for x,k,theta,mu,dat in (
        (P,m["s"]*(m["t"]+1),s-t-2,t+1,point_data),
        (L,m["t"]*(m["s"]+1),t-s-2,s+1,line_data)):
        V=dat["vertices"]
        a=dat["alphabet"]
        assert a*a<=a0*a0*r**3
        assert k<=k0*r*r and abs(theta)<=theta0*r and mu<=(b+1)*r
        cap=spectral_cap(k,theta,mu,d)
        assert cap<=lambda0*r
        assert dat["e_col"]<=k*(a-1)+cap*V
        assert dat["e_col"]<=j0*r**4
        assert dat["gram"]**2<=G0*G0*r**11
    j=direct_original_owner_conflicts(m,maps)["J"]
    assert j==point_data["e_col"]+line_data["e_col"]
    assert j<=J0*r**4
    return dict(balance=b,excess_multiplier=C,source_min_order=r,
                point_excess=m["excess_points"],line_excess=m["excess_lines"],
                common_defect_row_degree=d,
                constants=dict(V0=v0,A0=a0,K0=k0,theta0=theta0,
                               Lambda0=lambda0,conflict_each_J0=j0,
                               combined_J0=J0,pencil_square_G0=G0),
                exact_one_sided_point_and_line_spectral_bound=True,
                exact_conflict_J_upper=J0*r**4,
                exact_pencil_square_squared_upper=G0*G0*r**11,
                no_GQ_spectrum_assumed=True,
                no_external_C6_input_used=True)


def doubled_gq(kind="W32", switched=False):
    """Adversarial non-GQ regular girth-8 source, with Moore excess."""
    base=geometry(kind)
    s,t=base["s"],base["t"]
    n=(s+1)*(s*t+1)
    orig=tuple(base["lines"])
    plus=tuple(tuple(p+n for p in line) for line in orig)
    rows=[list(x) for x in orig+plus]
    if switched:
        p=rows[0][0]
        L=len(orig)
        assert p+n in rows[L]
        rows[0].remove(p)
        rows[L].remove(p+n)
        rows[0].append(p+n)
        rows[L].append(p)
    return tuple(tuple(x) for x in rows),2*n,s,t


def shortcycle_edit_from_gq(kind="W32"):
    """True non-GQ source for the universal physical C6 inverse witness."""
    g=geometry(kind)
    s,t=g["s"],g["t"]
    old=source_graph(g["lines"],(s+1)*(s*t+1),s,t)
    for p in range(old["points"]):
        for q in range(old["points"]):
            if q==p or q in old["neighbors_point"][p]:
                continue
            for lq in sorted(old["on"][q]):
                if (p,lq) not in old["projected"]:
                    continue
                anchors=old["projected"][p,lq]
                join=anchors[0][1]
                for lp in sorted(old["on"][p]-{join}):
                    prior=set(old["flags"])
                    removed={(p,lp),(q,lq)}
                    added={(p,lq),(q,lp)}
                    if not removed<=prior or added&prior:
                        continue
                    edited=(prior-removed)|added
                    foot=anchors[1][0]
                    assert {(p,join),(foot,join),(foot,lq),(p,lq)}<=edited
                    return tuple(sorted(edited)),old,dict(
                        removed=tuple(sorted(removed)),
                        added=tuple(sorted(added)),
                        four_cycle=((p,join),(foot,join),(foot,lq),(p,lq)))
    raise AssertionError("no permitted GQ two-edge switch")


def rainbow_c6_universal_source_inverse():
    """Physical-first and source-first exact bijection on a NON-GQ C4 source.

    The actual graph can have short source cycles; physical *proper*
    six-cycles still possess six distinct original factor point/line
    owners by injectivity of factor-label pair maps.
    """
    edited,old,switch=shortcycle_edit_from_gq("W32")
    maps=typed_maps(old,"correlated")
    source=dict(flags=edited,f=maps["f"],g=maps["g"])
    ids=frozenset(range(len(edited)))
    direct=physical_d6(source,ids)
    other=source_first_d6(source,ids)
    assert direct==other
    assert len(direct)>0
    assert all(len(key)==len(set(key))==6 for key in direct)
    return dict(kind="switched_W32_non_GQ",non_GQ_C4=True,
                real_physical_rainbow_C6=len(direct),
                source_original_six_ID_D6=len(other),
                physical_first_equals_source_first=True,
                no_projection_or_GQ_hypothesis=True,
                edited_source_flags=len(edited),
                physical_factor_alphabets=(maps["aP"],maps["aL"]))


def finite_case(name,scheme="lex"):
    if name in ("doubleW32","switchedDoubleW32"):
        lines,P,s,t=doubled_gq("W32",name=="switchedDoubleW32")
    else:
        g=geometry(name)
        lines,s,t=g["lines"],g["s"],g["t"]
        P=(s+1)*(s*t+1)
    m=source_graph(lines,P,s,t)
    Dp,Dl,d=defect_matrices(m)
    pmat=exact_second_walk_identity(m["neighbors_point"],Dp,s,t)
    lmat=exact_second_walk_identity(m["neighbors_line"],Dl,t,s)
    maps=typed_maps(m,scheme)
    pdata=typed_conflicts_and_gram(m,maps["f"],m["neighbors_point"],Dp,s,t)
    ldata=typed_conflicts_and_gram(m,maps["g"],m["neighbors_line"],Dl,t,s)
    owner_conflicts=direct_original_owner_conflicts(m,maps)
    assert owner_conflicts["J"]==pdata["e_col"]+ldata["e_col"]
    r=min(s,t)
    b=(max(s,t)+r-1)//r
    C=(m["excess_lines"]+r-1)//r
    led=coarse_linear_excess_ledger(m,maps,pmat,lmat,pdata,ldata,b,C)
    return dict(kind=name,scheme=scheme,s=s,t=t,points=P,lines=len(lines),
                flags=len(m["flags"]),source_excess_points=m["excess_points"],
                source_excess_lines=m["excess_lines"],missing=len(m["missing"]),
                unique_projections=len(m["projected"]),
                point_matrix=pmat,line_matrix=lmat,
                point_spectrum_upper=spectral_cap(pmat["degree"],pmat["theta"],
                      pmat["mu_nominal"],d),
                line_spectrum_upper=spectral_cap(lmat["degree"],lmat["theta"],
                      lmat["mu_nominal"],d),
                exact_common_defect_row=d,
                point_label=pdata,line_label=ldata,
                owner_conflicts=owner_conflicts,
                spectral_and_conflict_ledger=led,
                finite_falsifier_only=True)


def certificate():
    kinds=("W32","W33","Qminus24","dualQminus42",
           "doubleW32","switchedDoubleW32")
    rows=[finite_case(name) for name in kinds]
    correlated=[finite_case("Qminus24","correlated"),
                finite_case("switchedDoubleW32","correlated")]
    inverse=rainbow_c6_universal_source_inverse()
    return dict(schema=SCHEMA,issue=793,meta_issue=790,root_issue=230,
        frozen_base_main_sha=BASE_MAIN,
        claim="PROVED_CONDITIONAL_INTRINSIC_A1_A2_A3_NOT_FULL_T3",
        finite_cases=rows+correlated,
        physical_rainbow_C6_inverse=inverse,
        structural_lemmas=[
            "exact_biregular_girth8_Moore_projection_defect",
            "point_and_dual_exact_missing_projection_matrix",
            "symmetric_nonnegative_regular_D_defect",
            "one_perp_spectral_cap_from_D_row_bound",
            "minimal_typed_pair_conflicts_O_bc(r^4)_if_DeltaL_le_Cr",
            "pencil_squares_O_bc(r^11_over_2)",
            "rainbow_physical_C6_historical_D6_inverse_universal"],
        fixed_balance_and_linear_excess_constants_must_precede_family=True,
        existence_of_infinite_non_GQ_small_excess_family_not_claimed=True,
        no_intrinsic_A4_A5_A6_mixed_book_or_BBo_supersaturation=True,
        no_full_abstract_T3_theorem=True,no_unrestricted_ASET_exponent=True,
        no_external_referee_or_Lean_certificate=True)


if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--out",default="gio003-g6c1-intrinsic-defect.json")
    args=ap.parse_args()
    x=certificate()
    Path(args.out).write_text(json.dumps(x,sort_keys=True,indent=2)+"\n",
                              encoding="utf-8")
    print("PASS_GIO003_G6C1_INTRINSIC_DEFECT_CERTIFICATE")
