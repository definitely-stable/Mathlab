"""HYP-105 Option 2: Inter-Class Motif Compensation and Partial Spread Investigation on W(3,4).

Investigates:
1. Exact 7-class motif distribution S = D6 + (BA + AB) + ... on W(3,4).
2. Trajectory of (D6, BA, AB) across lex, spread, random, and adversarial certificate (BBo = 5261).
3. Test whether total S remains strictly positive even when D6 or BBo is minimized.
4. Partial spread bound on W(3,4): partial spread size s^2 + 1 = 17.
"""
import json
from hyp105_issue230_projection import fixture, ProjectionClosure
from hyp105_issue230_d5_retained_energy import true_spread_global_model
from hyp105_g5e2b3e1b0_seven_signature import seven_census
from hyp105_issue230_proof_audit import _geometry


def get_seven_class_breakdown(model):
    census = seven_census(model)
    counts = census["seven_class_motif_counts"]
    d6 = counts.get("D6", 0)
    ba = counts.get("B-left/A-right", 0)
    ab = counts.get("A-left/B-right", 0)
    core = d6 + ba + ab
    total_s = census["S_seven"]
    return {
        "D6": d6,
        "BA": ba,
        "AB": ab,
        "core_sum": core,
        "total_S": total_s,
        "all_counts": counts,
    }


def run_option2_audit():
    print("=== HYP-105 OPTION 2: INTER-CLASS MOTIF COMPENSATION AUDIT ===")

    # 1. Lexicographic W(3,4)
    m_lex = fixture(2, "lex")
    lex_res = get_seven_class_breakdown(m_lex)
    print("\nW(3,4) Lexicographic:")
    print(f"  D6: {lex_res['D6']}, BA: {lex_res['BA']}, AB: {lex_res['AB']}")
    print(f"  Core (D6 + BA + AB): {lex_res['core_sum']}, Total S: {lex_res['total_S']}")

    # 2. Spread W(3,4)
    m_spread, _, _, _ = true_spread_global_model(2, 'balanced')
    spread_res = get_seven_class_breakdown(m_spread)
    print("\nW(3,4) Spread-Aligned:")
    print(f"  D6: {spread_res['D6']}, BA: {spread_res['BA']}, AB: {spread_res['AB']}")
    print(f"  Core (D6 + BA + AB): {spread_res['core_sum']}, Total S: {spread_res['total_S']}")

    # 3. Random W(3,4)
    m_rand = fixture(2, "random")
    rand_res = get_seven_class_breakdown(m_rand)
    print("\nW(3,4) Random:")
    print(f"  D6: {rand_res['D6']}, BA: {rand_res['BA']}, AB: {rand_res['AB']}")
    print(f"  Core (D6 + BA + AB): {rand_res['core_sum']}, Total S: {rand_res['total_S']}")

    # 4. Adversarial Certificate (BBo = 5261 / 5400)
    with open("research/hyp105_w34_adversarial_certificate.json", "r", encoding="utf-8") as f:
        cert = json.load(f)

    _, points, lines, incidences = _geometry(2)
    m_cert = {
        "s": 4,
        "a": 14,
        "left_labels": [tuple(p) for p in cert["f"]],
        "right_labels": [tuple(p) for p in cert["g"]],
        "incidences": incidences,
    }
    cert_res = get_seven_class_breakdown(m_cert)
    print("\nW(3,4) Adversarial Certificate (BBo = 5261):")
    print(f"  D6: {cert_res['D6']}, BA: {cert_res['BA']}, AB: {cert_res['AB']}")
    print(f"  Core (D6 + BA + AB): {cert_res['core_sum']}, Total S: {cert_res['total_S']}")

    # Compensation Comparison:
    print("\n--- Cross-Class Compensation Analysis ---")
    models = [("lex", lex_res), ("spread", spread_res), ("random", rand_res), ("cert", cert_res)]
    for name, r in models:
        ratio_core = r['core_sum'] / 4096.0
        ratio_s = r['total_S'] / 4096.0
        print(f"  {name:8s}: D6={r['D6']:5d}, BA+AB={r['BA']+r['AB']:5d}, Total S={r['total_S']:5d} ({ratio_s:.3f} s^6)")


if __name__ == "__main__":
    run_option2_audit()
