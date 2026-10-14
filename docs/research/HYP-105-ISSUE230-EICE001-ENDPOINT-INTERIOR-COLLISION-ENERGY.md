# EICE-001 — exact original endpoint/interior collision energy

Status: RESTRICTED_THEOREM_C / OPEN_WITH_FORMAL_BLOCKER. Research only; stacked on PR #394. No Branch A/B claim.

## Exact all-h inequality

Let s=2^h, V=(s+1)(s^2+1), N=V(s+1), f and g arbitrary complete globally injective ORIGINAL W(3,s) pair maps. On any physical graph assembled from whole incidence-diagonal pairs use a reversible normalized length-three non-backtracking path law mu. In particular, with minimum non-isolated degree >=2 the stationary law has mass

    mu(z0,z1,z2,z3) = 1/[2m(d(z1)-1)(d(z2)-1)].

If degree-one vertices exist, this expression sums to less than 1; the module renormalizes by surviving mass and EXPLICITLY labels its different conditional law. None of the full-graph computations are claimed to be the accepted regularized G* of Opus.

Let r and q denote existing ORIGINAL line and point labels of physical endpoints, and x1,y1 the first internal physical coordinates. Define subprobability nu_f(r,x)=Pr_mu[g(r)={y0,y3},x1=x], nu_g(q,y)=Pr_mu[f(q)={x0,x3},y1=y], energies E_f=sum nu_f^2 and E_g=sum nu_g^2. The exact original carrier supports are C_f={(r,x):exists p incident r, x in f(p)}, and C_g={(q,y):exists line l incident q,y in g(l)}; both have size <=2N.

For the mu-mass theta_I of coordinate-proper original nonincident endpoint paths whose unique GQ projection q--l--p--r has end-clean labels and internally blocked f(p) or g(l), Opus' W inclusion and reversal symmetry prove:

    theta_I <= 2nu_f(C_f)+2nu_g(C_g)
            <= 2sqrt(|C_f| E_f)+2sqrt(|C_g| E_g)
            <= 4sqrt(N(E_f+E_g)),

hence the exact universal necessary inequality

    theta_I^2 <=16N(E_f+E_g).  (E1)

The counting is ORIGINAL incidence-aware. No independence, probabilistic g, or selected GF5 motif is assumed. This inequality alone proves NO lower bound on S.

## Conditional Branch A gate

If the Opus theorem R is independently validated including coherent G* existence and uniform m*=Omega(s^4), dmin*=Omega(s), and all improper/non-internal bad path mass=o(1), then S=o(s^6) forces theta_I(G*)=1-o(1), and E1 implies N(E_f+E_g)>=(1-o(1))/16. A sufficient FUTURE statement would prove the existence, for every f,g, of at least one valid G* with 16N(E_f+E_g)<=(1-eta)^2 for fixed eta>0. That upper bound is NOT established.

## Execution and falsifiers

- Complete genuine original W32 lex/reverse/S68/S72 inputs from PR #394; 45 incidence identities and all 90 diagonals on full G.
- Exact Fraction normalizations, independently enumerated weighted ordered walk-pair collision products, exact carrier capacity Cauchy inequalities, exact GQ anchors.
- Fail closed on illegal input maps, original ID duplication, insufficient walk budgets, missing properness and minimum active degree in strict G* mode.
- Full graph G is a finite diagnostic only; it cannot be promoted to G* or the asymptotic theorem R. No ASET exponent or GF5 S lower is inferred.
- The Python report says universal_S_lower_proved=False.

## Next allowed research

EICE-002: construct and PROVE a whole-incidence-paired coherent G* regularizer (point/line matchings, bichromatic coordinate labeling, and paired low-degree peeling); recompute explicit uniform density/minimum-degree constants. EICE-003: attempt the spectral collision-energy upper bound on that G*, or give an admissible high-energy witness. EICE-004: independently study exact source-identity C/B-transversal switching on the same maps if EICE-003 fails. All theorem status transitions demand math audit and GitHub-hosted CI; no changes to main.
