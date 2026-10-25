# HYP-105 / #230 — AA4-BC: GOOD completions after adversarially pinned original LINE images

**Strict partial research theorem.** Scientific Draft child of [AA4-BB PR #563](https://github.com/definitely-stable/Mathlab/pull/563), pinned parent HEAD 94bb67c5f9c603cda08245f12dc848928e7de6d8. Not a root A/B/C proof. The entire model is the actual symplectic W(3,2^h), with one original incidence ID for each genuine incident point-line pair, typed globally injected physical unordered pairs, and one globally coherent right-line mapping. We count true-original threeflag physically opposite GOOD wedges, **not** selected historical seven-GF(5) six-ID motifs.

## Main theorem and quantifiers

For every dyadic s=2^h with h>=5, set d=s+1, V=(s+1)(s²+1), and choose minimal a with binom(a,2)>=V, t=a-2. Let f be ANY complete globally injected original point-factor map to K_a physical pair edges. Fix ANY complete V-edge right physical support E. Fix ANY k distinct ACTUAL original LINE factors J and ANY injection phi:J→E, provided

\[
0\le k\le\lfloor V/1024\rfloor.
\]

Complete phi by sampling ONE uniformly random bijection of the N=V−k remaining original LINE factors onto E\phi(J). All completions extend the SAME adversarially prescribed original source line-to-physical images; all point f labels and all right occupied physical support E are unchanged. Physical AA4-AO BAD coordinates are determined by the two ORIGINAL FULL supports im(f) and E, and do NOT get recomputed after removing pinned labels from the free subproblem.

Let R_free be the number of TRUE original GOOD physically opposite centered three-incidence-flag configurations (p,l),(q0,k0),(q1,k1), having three distinct actual source POINT factors and three distinct actual source LINE factors, such that NONE of the three source line factors is in J. The full legal R_GOOD satisfies R_GOOD>=R_free for every completed globally injected map.

**BC-1 (uniform partial-map extension):**

\[
\boxed{\mathbb E_{g\supset\phi}R_{\rm free}\ge s^6/512,\qquad
\exists g\supset\phi\text{ legal complete}:\ R_{\rm GOOD}(f,g)\ge s^6/512.}
\]

This is a deterministic existence theorem for EVERY given legal partial original line map, but not for EVERY complete given line map.

**BC-2 (uniform conditional concentration):** If η(s,k) is the explicit exact rational bound below, then

\[
\boxed{\frac{\operatorname{Var}_{g\supset\phi}R_{\rm free}}
{(\mathbb E_{g\supset\phi}R_{\rm free})^2}
\le\eta(s,k)\le30\,000\,000\,000/V=O(s^{-3}).}
\]

Therefore

\[
\boxed{\Pr_{g\supset\phi}\{R_{\rm GOOD}<s^6/1024\}
\le\min(1,4\eta(s,k)).}
\]

The latter probability upper tends to zero with s uniformly in the given f,E,J,phi; it can be vacuous for moderate s. Neither theorem applies when all V line labels are locked.

## Source-deletion lemma on actual W(3,s)

Let F° denote the AA4-AO induced CLEAN occupied point physical support (based on the FULL F=im f). Source weights w(l,k0,k1) count actual centered original physically point-opposite and point-CLEAN threeflag events. They are nonnegative and use three distinct ACTUAL original line-factor IDs. The previous #561/#562 theorem, for all h>=5 and all genuine f, proves

\[
B:=\sum w\ge B_0=d(d-1)(d-2)T_\circ(F)
\ge d(d-1)(d-2)V^2/16.
\]

The genuine-original source overlap bound from #562 is

\[
M_1=\max_j\sum_{\{l,k_0,k_1\}\ni j}w(l,k_0,k_1)
\le5d^3t^2.
\]

Remove every original source event whose triple uses ANY pinned source LINE ID. A union bound over actual source IDs gives

\[
B_{\rm free}\ge B-kM_1\ge B_0-k(5d^3t^2)\ge B_0/2.\tag{BC-S}
\]

Proof of last inequality for ALL dyadic h>=5: minimal physical K_a implies t²<2V, genuine d=s+1>=33 implies (d−1)(d−2)>=d²/2, thus B0>=d³V²/32. Since k<=V/1024, the lost weight is strictly below 10d³V²/1024 < d³V²/64 <=B0/2. This uses neither independence nor an invented source geometry.

## Physical image-deletion lemma on the ORIGINAL FULL right support

Let E° be the induced CLEAN occupied right support using the BAD coordinates of the FULL E. Parent #561 proves the rooted physical port energy

\[
T_\circ(E)=\sum_{\{u,v\}\in E^\circ}
(\deg_{E^\circ}u-1)(\deg_{E^\circ}v-1)\ge V^2/16.
\]

Thus 2T°(E)>=V²/8 is the number of ordered physically opposite and CLEAN triples of three distinct occupied right physical edges. For any given physical edge e, at most H=2t² ordered opposite-port completions use e in each specified center/outer slot, by elementary K_a endpoint geometry; in all three slots at most 3H=6t². Deleting ANY k pinned occupied physical edges from the available triple images can therefore kill at most 6kt² favorable ordered triples. With E_free=E\phi(J) and its CLEAN subset defined using ORIGINAL Bad(E),

\[
A_{\rm free}:=2T(E^\circ\setminus\phi(J))
\ge V^2/8-6kt^2\ge V^2/16.\tag{BC-P}
\]

The last inequality follows from t²<2V and k<=V/1024, giving loss <12V²/1024<V²/16. In particular no physical pair image is reused and the full original support still determines BAD coordinates. Reclassifying E_free as a new support would be mathematically WRONG.

## Exact conditional expectation and existence

Conditional on the given k original source LINE images, ONE uniform complete global permutation assigns the N remaining source factors to the N distinct free physical edges. Every prescribed triple of three DISTINCT unpinned source line IDs therefore has exactly the same probability

\[
p_{\rm free}=\frac{A_{\rm free}}{N(N-1)(N-2)}
\]

of CLEAN physically opposite right physical images. There is no independence across source triples. Linearity yields the exact equality

\[
\mathbb E_{g\supset\phi}R_{\rm free}=B_{\rm free}p_{\rm free}.
\]

Combining BC-S and BC-P,

\[
\mathbb E R_{\rm free}\ge \frac{B_0}{2}
\frac{V^2/16}{(N)_3}
\ge \frac14\left(\frac{2B_0(V^2/16)}{(V)_3}\right)
\ge s^6/512,
\]

using the parent #561 true-original h>=5 uniform GOOD expectation floor >=s^6/128. Some COMPLETE legal extension has at least its average count. Since full R_GOOD includes every unpinned eligible original source wedge, the same extension has R_GOOD>=s^6/512. This proves BC-1.

## Conditional variance, exact rational envelope and explicit polynomial rate

The #563 zero/one/exactly-two/three shared-original-LINE-ID second-moment argument applies to unpinned source weights without changing its geometric proof. Restriction only DECREASES each original source multiplicity overlap bound M1<=5d³t², M2<=8d³t, M3<=6d³. Put

\[
\begin{aligned}
&N=V-k,\quad
B_*=d(d-1)(d-2)V^2/16-k(5d^3t^2),\\
&A_*=V^2/8-6kt^2,\quad p_*=A_* /(N)_3,\quad
q_N=(N-3)_3/(N)_3,\\
&P_{1,N}=4t^4/(N-1)_4,\quad P_{2,N}=16Nt^3/(N)_4.
\end{aligned}
\]

Then the exact certificate is

\[
\boxed{\eta(s,k)=q_N^{-1}-1+
\frac{15d^3t^2P_{1,N}}{B_*p_*^2}+
\frac{24d^3tP_{2,N}}{B_*p_*^2}+
\frac{6d^3}{B_*p_*}.}\tag{BC-V}
\]

Each algebraic denominator is positive in the all-h domain. A conservative analytic universal bound follows from N>=V/2, N>=8, B_*>=d³V²/64, p_*>=1/(16V), t²<2V, t<=2sqrt(V), and q_N^{-1}-1<=60/V. The separate factors satisfy

\[
M_1/B_*\le640/V,\quad M_2/B_*\le1024/V^{3/2},
\quad M_3/B_*\le384/V^2,
\]
\[
P_{1,N}\le4096/V^2,\quad P_{2,N}\le32768/V^{3/2},
\quad 1/p_*\le16V.
\]

Substitution yields

\[
\eta(s,k)\le
[60+3(640)(4096)(256)+3(1024)(32768)(256)+384(16)]/V
=27\,783\,075\,900/V < 30\,000\,000\,000/V.
\]

The exact rational BC-V is normally much tighter; this inequality is simply a completely explicit all-dyadic proof of conditional O(s^-3). Chebyshev at half the guaranteed expected value gives BC-2. No random-sample independence of six-source-ID GF5 charges has been introduced.

## Evidence, nonimplications and next frontier

Added: versioned original partial-pins source and exact-rational certificate, six independent test groups, this full proof, dedicated two-job GitHub-hosted workflow. The tests compare genuine original W32 full-source physically point-CLEAN threeflag triples to a completely independent literal original threeflag enumeration after locking one source LINE ID; original W32/W34 right free CLEAN ordered triples to a separate independent physical triple enumerator; actual W34 GF4 with nononto K14 and six physical missing edges; all h=5..34,40,48,64,80 exact integer worst-case k=0,1,floor(V/1024); reject malformed pinned injections and unproved domain. A separate small abstract six-line example exhaustively checks all 5!=120 complete global right extensions after one locked original line image. The small abstract test checks permutation probability alone and is NOT presented as a fake high-order source W3.

This theorem is a robust **partially prescribed** legal original LINE-map extension, not a fixed complete map anti-alignment theorem. It does NOT prove R_GOOD>0 for EVERY complete adversarial f,g, any accepted historical GF5 SIX-DISTINCT-ORIGINAL-ID selected motif lower, source Hall sixflag lift, root A/B/C, R3 or ASET exponents. Earlier #547/#548 five-swap D6 repair theorems concern another six-ID statistic and are not prior proof of this partial locking result. The probabilistic and bounded deletion ideas are elementary; novelty is explicitly restricted to the real source and original CLEAN support application, subject to independent review.

**Next important mathematical frontier:** push the lockable fraction toward 1 using JOINT original incidence/physical anti-alignment information rather than source-only and physical-only union bounds. Locking all V is the unresolved root adversarial case. Independently bridge three true original GOOD flags through actual residual 3×3 source Hall and all seven selected GF(5) six-original-ID acceptance. Retain Draft; require exact-final-SHA CI, ancestor integrity and independent mathematical proof review before integration.
