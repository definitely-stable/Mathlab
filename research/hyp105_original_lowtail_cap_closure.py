"""AA4-CAPCLOSE: independent exact original-source collinearity and moment caps.

See docs/research/HYP-105-AA4-ORIGINAL-LOWTAIL-CAP-CLOSURE.md.
Finite source replay is a falsifier; it is NOT an all-h root proof.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb, isqrt


def ceil_sqrt(n):
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("square-root input must be a nonnegative integer")
    q = isqrt(n)
    return q + (q*q < n)


def source_energy(s, flags, labels, a):
    """Genuine ORIGINAL GQ point-collinearity SRG identity; dualize flags for lines."""
    labels = tuple(tuple(z) for z in labels)
    flags = tuple(tuple(z) for z in flags)
    V = len(labels)
    if V != (s+1)*(s*s+1) or len(set(flags)) != len(flags):
        raise ValueError("not a complete original GQ(s,s) incidence source")
    if len(flags) != V*(s+1) or len(set(labels)) != V:
        raise ValueError("source or pair labels incomplete/noninjective")
    legal = set(combinations(range(a), 2))
    if any(z not in legal for z in labels):
        raise ValueError("invalid typed globally injected physical pairs")
    lines = defaultdict(set)
    for p, ell in flags:
        lines[ell].add(p)
    if len(lines) != V or any(len(ps) != s+1 for ps in lines.values()):
        raise ValueError("original line degree invalid")
    adj = [set() for _ in range(V)]
    for ps in lines.values():
        for p in ps:
            adj[p].update(ps-{p})
    if any(len(ns) != s*(s+1) for ns in adj):
        raise ValueError("original GQ point collinearity degrees invalid")
    for p in range(V):
        for q in range(p+1,V):
            expected = s-1 if q in adj[p] else s+1
            if len(adj[p]&adj[q]) != expected:
                raise ValueError("source fails genuine GQ(s,s) collinearity")
    S=[set() for _ in range(a)]
    for p,pair in enumerate(labels):
        for x in pair:
            S[x].add(p)
    d2=sum(len(group)**2 for group in S)
    induced=sum(sum(len(adj[p]&group) for p in group)//2 for group in S)
    observed=sum(sum(len(adj[p]&group)**2 for p in range(V)) for group in S)
    exact=2*V*(s*s-1)+(s+1)*d2-4*induced
    if observed!=exact:
        raise AssertionError("exact original collinearity C^2 identity failed")
    spectral=Fraction(2*(s+1)**2*V,1)+Fraction(
        (s+1)**2*(s*s-1)*d2,V)
    if observed>spectral or d2>2*V*(a-1):
        raise AssertionError("original GQ spectral/occupancy cap failed")
    return {"G":observed,"symbol_degree_squares":d2,
            "collinear_symbol_pairs":induced,"exact_srg_rhs":exact,
            "spectral_ceiling":(spectral.numerator+spectral.denominator-1)//spectral.denominator,
            "F1_ceiling":2*observed}


def core_conflict_max(flags, f, g, core):
    """Actual ORIGINAL source pencil conflict graph; not physical graph degree."""
    buckets=defaultdict(list)
    for i in core:
        p,ell=flags[i]
        for y in g[ell]:
            buckets[(0,p,y)].append(i)
        for x in f[p]:
            buckets[(1,ell,x)].append(i)
    adj={i:set() for i in core}
    for ids in buckets.values():
        for u,v in combinations(ids,2):
            adj[u].add(v)
            adj[v].add(u)
    return max((len(x) for x in adj.values()),default=0)


def cap_closure(s,V,a,total_flags,core_count,allowed_count,
                delta,K,qsum,ebad,D6_cap,Gx,Gy):
    """Conditional all-N original BBo LOWER, given a verified original D6_cap.

    The caller must establish D6_original_avoid(Z)<=D6_cap.
    The finite fixture uses a TRIVIAL valid binomial upper, not an assumed
    unverified s^6 bound. No claim of unconditional root Branch A.
    """
    args=(s,V,a,total_flags,core_count,allowed_count,delta,K,qsum,
          ebad,D6_cap,Gx,Gy)
    if (not all(type(z) is int and z>=0 for z in args) or s<2 or
        V!=(s+1)*(s*s+1) or total_flags!=V*(s+1) or
        not 0<=core_count<=allowed_count<=total_flags or a<2 or
        comb(a-1,2)>=V or comb(a,2)<V):
        raise ValueError("invalid genuine source cap inputs")
    m=2*core_count
    kap=K+1
    inv2=16*comb(2*kap,2)
    inv3=64*comb(3*kap,3)
    sixth=24*D6_cap+72*m*delta*delta
    proper3_norm2=inv3*inv3*sixth
    fourth=2*inv2*inv2*ceil_sqrt(2*m*sixth)+2*delta*qsum
    f2=8*(s+1)*kap*allowed_count*delta
    bx=ceil_sqrt(2*Gx*f2)
    by=ceil_sqrt(2*Gy*f2)
    bad=ceil_sqrt(ebad*proper3_norm2)
    blocks=2*ceil_sqrt(bx*delta*fourth)+2*ceil_sqrt(by*delta*fourth)
    density=Fraction((4*core_count)**3,a**4)
    lower=density-3*delta*qsum-bad-blocks
    return {"sigma2_inverse":inv2,"sigma3_inverse":inv3,
            "sixth_moment_cap":sixth,
            "proper3_Frobenius2_cap":proper3_norm2,
            "physical_fourth_moment_cap":fourth,"original_dual_F2_cap":f2,
            "original_Bx_cap":bx,"original_By_cap":by,
            "bad_endpoint_path_cap":bad,"four_internal_blockers_cap":blocks,
            "density":str(density),"two_BBo_lower_raw":str(lower),
            "allh_root_A_accepted":False}



def uniform_projection_mask_radius(K,T):
    """Exact improved deletion-mask absorption budget, CONDITIONAL on caps.

    For m<=4*s^4, Delta<=T*s, D6_original_avoid<=s^6,
    ||P3||_F^2<=q3^2*(24+288*T^2)*s^6.  If |Z|<=rho*s^4
    then the deleted-original-anchor mask contributes <=s^6/8
    at rho=1/(768*q3^2*(24+288*T^2)).
    This does NOT prove existence of such a core or root Branch A.
    """
    if type(K) is not int or K<0 or type(T) is not int or T<1:
        raise ValueError("formal integer conflict/physical caps required")
    k=K+1
    q3=64*comb(3*k,3)
    old_q3=64*27*k**3
    L6=24+288*T*T
    old_L6=24+576*T*T
    rho=Fraction(1,768*q3*q3*L6)
    old_rho=Fraction(1,768*old_q3*old_q3*old_L6)
    if rho<=old_rho:
        raise AssertionError("new original mask budget failed to improve")
    return {"selector3_inverse":q3,"L6_tight":L6,
            "rho_mask":str(rho),"prior_rho_mask":str(old_rho),
            "improves_historical_mask_budget":True,
            "root_A_claim":False}


def replay_frozen_original_lowtail():
    """Independent four-case exact ORIGINAL W32/W34 source / LOWCERT oracle."""
    import json
    from pathlib import Path
    from hyp105_full_physical_degree_tail import genuine_source
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic

    path=Path(__file__).with_name("hyp105_original_lowtail_alln_energy_certificates.json")
    corpus=json.loads(path.read_text(encoding="utf8"))
    if len(corpus["genuine_true_original_cases"])!=4:
        raise AssertionError("frozen true ORIGINAL W32/W34 cases missing")
    rows=[]
    for row in corpus["genuine_true_original_cases"]:
        s=row["s"]
        h={2:1,4:2}.get(s)
        if h is None:
            raise AssertionError("unexpected original GQ order")
        s2,V,flags=genuine_source(h)
        if s2!=s:
            raise AssertionError("source order mismatch")
        mapping=pair_labeled_symplectic(h,row["scheme"])
        f=tuple(map(tuple,mapping["left_labels"]))
        g=tuple(map(tuple,mapping["right_labels"]))
        a=row["physical_alphabet"]
        Z=set(row["deleted_original_flag_IDs"])
        C=tuple(row["original_core_source_IDs"])
        if not set(C).isdisjoint(Z):
            raise AssertionError("original ID deletion/core collision")
        x=source_energy(s,flags,f,a)
        y=source_energy(s,[(ell,p) for p,ell in flags],g,a)
        K=core_conflict_max(flags,f,g,C)
        # Every sixset is a six-element subset of the surviving ORIGINAL flags.
        # This is loose but indisputably valid, unlike an unverified s^6 claim.
        dcap=comb(len(flags)-len(Z),6)
        cap=cap_closure(s,V,a,len(flags),len(C),len(flags)-len(Z),
                        row["physical_original_core_max_Delta"],K,
                        row["original_source_Qx"]+row["original_source_Qy"],
                        row["original_bad_endpoint_union_size"],dcap,
                        x["G"],y["G"])
        px=row["original_masked_POINT_source_B"]
        py=row["original_masked_LINE_dual_source_B"]
        assert px["F1"]<=x["F1_ceiling"]
        assert py["F1"]<=y["F1_ceiling"]
        assert px["F2"]<=cap["original_dual_F2_cap"]
        assert py["F2"]<=cap["original_dual_F2_cap"]
        assert px["B"]<=cap["original_Bx_cap"]
        assert py["B"]<=cap["original_By_cap"]
        assert (row["exact_original_proper3_endpoint_Frobenius_square"]
                <=cap["proper3_Frobenius2_cap"])
        assert row["physical_trace_A4"]<=cap["physical_fourth_moment_cap"]
        assert Fraction(cap["two_BBo_lower_raw"])<=2*row["real_positive_original_BBo_sixsets"]
        rows.append({"s":s,"scheme":row["scheme"],"conflict_K":K,
                     "G_point":x["G"],"G_line":y["G"],
                     "F1_point_cap":x["F1_ceiling"],
                     "F1_line_cap":y["F1_ceiling"],
                     "source_induced_collinear_point_pairs":x["collinear_symbol_pairs"],
                     "source_induced_collinear_line_pairs":y["collinear_symbol_pairs"],
                     "actual_Bx":px["B"],"actual_By":py["B"],
                     "observed_BBo":row["real_positive_original_BBo_sixsets"],
                     "exact_caps_pass":True})
    return {"schema":"mathlab.hyp105.original-cap-closure.v1",
            "allh_root_A_accepted":False,"cases":rows}


if __name__=="__main__":
    import json
    print("AA4_ORIGINAL_CAP_CLOSURE_CERTIFICATE="+json.dumps(
        replay_frozen_original_lowtail(),sort_keys=True,separators=(",",":")),
        flush=True)
