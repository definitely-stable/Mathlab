"""Genuine W(3,4) paired-subfield witness with an end posting of 28.

The infinite s=t^2 construction is proved in the accompanying note;
this finite witness uses two GF(2) subgeometries of the true GF(4) host.
It falsifies a constant-four end cap, not the root seven-class conjecture.
"""
from itertools import combinations

from hyp105_b1_symplectic import normalized, symplectic, symplectic_gq
from hyp105_physical_degree_energy import _verify_typed_injections


TRANSVECTIONS = (
    ((0,1,3,3),2), ((1,1,2,2),3),
    ((0,0,1,3),2), ((0,1,0,0),1),
)


def paired_subfield_w34_witness():
    """Return full deterministic typed injections and actual source provenance.

    Transvections x -> x + lambda B(x,v)v preserve the alternating
    form in characteristic two. All choices and the remaining K14
    pair assignments are fixed; no optimization or random labels.
    """
    field,points,lines,flags = symplectic_gq(2)
    point_index = {p:i for i,p in enumerate(points)}
    line_index = {tuple(line):l for l,line in enumerate(lines)}
    point_permutation = []
    for point in points:
        image = point
        for vector,coefficient in TRANSVECTIONS:
            c = field.mul(coefficient,symplectic(image,vector,field))
            image = tuple(x ^ field.mul(c,y) for x,y in zip(image,vector))
        point_permutation.append(point_index[normalized(image,field)])
    line_permutation = [
        line_index[tuple(sorted(point_permutation[p] for p in line))]
        for line in lines
    ]
    P0 = {p for p,point in enumerate(points) if set(point) <= {0,1}}
    L0 = {l for l,line in enumerate(lines) if len(set(line)&P0) == 3}
    AP0 = {point_permutation[p] for p in P0}
    AL0 = {line_permutation[l] for l in L0}
    # At s=4 only 11 free coordinates fit. The infinite construction
    # needs no truncation for its stated subsequence t>=4, s=t^2.
    P = sorted(P0-AP0)[:11]
    L = sorted(L0-AL0)[:11]
    used_points = set(P)|{point_permutation[p] for p in P}
    used_lines = set(L)|{line_permutation[l] for l in L}
    p0,l0 = next((p,l) for p,l in flags
                 if p not in used_points and l not in used_lines)
    q = next(p for p in range(85) if p not in used_points|{p0})
    r = next(l for l in range(85)
             if l not in used_lines|{l0} and q not in lines[l])
    f,g = [None]*85,[None]*85
    f[p0] = g[l0] = (0,1)
    f[q] = g[r] = (0,2)
    for labels,support,permutation in (
        (f,P,point_permutation),(g,L,line_permutation),
    ):
        for z,source_id in enumerate(support,3):
            labels[source_id] = (1,z)
            labels[permutation[source_id]] = (2,z)
        used = {edge for edge in labels if edge is not None}
        remaining = iter(edge for edge in combinations(range(14),2)
                         if edge not in used)
        for source_id in range(85):
            if labels[source_id] is None:
                labels[source_id] = next(remaining)
    _verify_typed_injections(14,85,f,g)
    return tuple(f),tuple(g),{
        "alpha":(p0,l0),"endpoint":(q,r),
        "subfield_points":P,"subfield_lines":L,
        "source_overlap":(len(P0&AP0),len(L0&AL0)),
        "retained_subfield_flags":sum(p in P and l in L for p,l in flags),
        "point_permutation":tuple(point_permutation),
        "line_permutation":tuple(line_permutation),
    }
