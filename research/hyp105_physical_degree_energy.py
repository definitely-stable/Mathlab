"""HYP-105 #230 AA4-DEG: exact physical coordinate-degree spectral transfer.

A rigorously scoped all-h statement. Unlike the physical N3 endpoint
variance chi^2, this bounds Frobenius energy of the a-by-a *degree matrix*
D(u,x) = # genuine original incidence flags with u in f(point) and
x in g(line). It does NOT prove P=O(s^6) or chi^2=O(1).
"""
from math import isqrt


def minimal_alphabet(V):
    if type(V) is not int or V < 1:
        raise ValueError("positive integer V required")
    a = (1 + isqrt(1 + 8 * V)) // 2
    while a * (a - 1) // 2 < V:
        a += 1
    while (a - 1) * (a - 2) // 2 >= V:
        a -= 1
    return a


def _verify_typed_injections(a, V, point_pairs, line_pairs):
    for images in (point_pairs, line_pairs):
        if len(images) != V:
            raise ValueError("incomplete original typed point/line pair mapping")
        pairs = []
        for edge in images:
            if (len(edge) != 2 or type(edge[0]) is not int
                    or type(edge[1]) is not int
                    or not 0 <= edge[0] < edge[1] < a):
                raise ValueError("physical images must be ordered K_a edges")
            pairs.append(tuple(edge))
        if len(set(pairs)) != V:
            raise ValueError("physical image maps must be globally injective")


def _verified_source(s, flags, V):
    degree = s + 1
    fset = set(flags)
    if (len(flags) != V * degree or len(fset) != len(flags)
            or any(type(q) is not int or type(l) is not int
                   or not (0 <= q < V and 0 <= l < V)
                   for q, l in flags)):
        raise ValueError("invalid original GQ incidence flags")
    points = [set() for _ in range(V)]
    lines = [set() for _ in range(V)]
    for q, l in flags:
        points[q].add(l)
        lines[l].add(q)
    if any(len(x) != degree for x in points + lines):
        raise ValueError("not (s+1)-regular typed source incidence")
    return points, lines


def source_spectral_projector_identity(s, flags):
    """Independent exact integer audit: X^2 = 2*s*V*X.

    X = V*(M M^T)-(s+1)^2*J. For the genuine W(3,s) source,
    MM^T has spectrum {(s+1)^2, 2s, 0} and X/(2s V)
    is the orthogonal spectral projector of the centered incidence.
    Computational verification is cubic in V: use s=2 and s=4.
    """
    if type(s) is not int or s < 2 or s & (s - 1):
        raise ValueError("s must be dyadic and >=2")
    V = (s + 1) * (s * s + 1)
    point_lines, _ = _verified_source(s, flags, V)
    degree = s + 1
    X = [
        [V * len(point_lines[i].intersection(point_lines[j]))
         - degree * degree for j in range(V)]
        for i in range(V)
    ]
    for i in range(V):
        if sum(X[i]) != 0:
            raise AssertionError("centered incidence does not annihilate ones")
    for i in range(V):
        for j in range(V):
            v = sum(X[i][k] * X[k][j] for k in range(V))
            if v != 2 * s * V * X[i][j]:
                raise AssertionError("original symplectic GQ spectral polynomial fails")
    return {
        "s": s, "V": V,
        "tr_projector_times_2sV": sum(X[i][i] for i in range(V)),
        "spectral_identity_verified": True,
    }


def physical_degree_energy(s, point_pairs, line_pairs, flags,
                           *, verify_spectral=False):
    """Exact integer certificate of coordinate-degree centered energy.

    Let f_u/g_x be the two coordinate degrees and
    D[u,x]=sum_{(q,l) incidence}1[u in f(q)]1[x in g(l)].
    E[u,x]=D[u,x]-(s+1)f_u*g_x/V.

    PROVED all-h:
      ||E||_F^2 <=
       2*s*(a-2)*min(2V - sum_u f_u^2/V, 2V - sum_x g_x^2/V).
    And pointwise centered expander mixing:
      (V D[u,x]-(s+1)f_u*g_x)^2
       <=2s*f_u*(V-f_u)*g_x*(V-g_x).
    These are UPPER bounds using sqrt(2s) source incidence singular
    spectrum, not assumptions of independence between f and g.

    The finite spectrum oracle requires O(V^3), so skip it for s>=8.
    """
    if type(s) is not int or s < 2 or (s & (s-1)):
        raise ValueError("s must be dyadic and >=2")
    V = (s+1)*(s*s+1)
    a = minimal_alphabet(V)
    _verify_typed_injections(a, V, point_pairs, line_pairs)
    _verified_source(s, flags, V)
    if verify_spectral:
        source_spectral_projector_identity(s, flags)
    left = [0] * a
    right = [0] * a
    D = [[0] * a for _ in range(a)]
    for edge in point_pairs:
        for u in edge:
            left[u] += 1
    for edge in line_pairs:
        for x in edge:
            right[x] += 1
    for q, l in flags:
        for u in point_pairs[q]:
            for x in line_pairs[l]:
                D[u][x] += 1
    if sum(sum(row) for row in D) != 4 * V * (s+1):
        raise AssertionError("incorrect physical graph degree sum")
    residual_numerator = [
        [V * D[u][x] - (s+1)*left[u]*right[x]
         for x in range(a)]
        for u in range(a)
    ]
    energy_numerator = sum(z*z for row in residual_numerator for z in row)
    left_square = sum(k*k for k in left)
    right_square = sum(k*k for k in right)
    # 2s(a-2) * [2V - sum(df^2)/V] * V^2.
    each_guide = [
        2*s*(a-2)*V*(2*V*V - k)
        for k in (left_square, right_square)
    ]
    bound_num = min(each_guide)
    if energy_numerator > bound_num:
        raise AssertionError("global centered degree-energy theorem violated")

    pointwise_slacks = []
    for u in range(a):
        for x in range(a):
            rhs = 2*s*left[u]*(V-left[u])*right[x]*(V-right[x])
            diff = rhs - residual_numerator[u][x]**2
            if diff < 0:
                raise AssertionError("pointwise expander mixing inequality violated")
            pointwise_slacks.append(diff)

    max_degree = max(map(max, D))
    total_three_walks_envelope = max_degree * sum(z*z for row in D for z in row)
    # Any proper and nonincident-endpoint directed 3-walk is a 3-walk.
    # For simple undirected H, # of all directed 3-walks
    # =d^T A d <= lambda_max(A)||d||^2<=Delta sum d_v^2.
    if energy_numerator < 0 or max_degree < 0:
        raise AssertionError("negative structural statistic")
    return {
        "s": s, "V": V, "a": a, "flags": len(flags),
        "left_coordinate_degrees": tuple(left),
        "right_coordinate_degrees": tuple(right),
        "degree_matrix": tuple(tuple(row) for row in D),
        "degree_sum": 4*V*(s+1),
        "degree_square_sum": sum(z*z for row in D for z in row),
        "residual_energy_num_over_V2": energy_numerator,
        "residual_energy_upper_num_over_V2": bound_num,
        "separate_upper_numerators": tuple(each_guide),
        "pointwise_min_slack": min(pointwise_slacks),
        "max_corner_degree": max_degree,
        "all_three_walk_upper": total_three_walks_envelope,
        "all_h_sixth_order_bound_proved": False,
        "path_chi_square_bound_proved": False,
    }
