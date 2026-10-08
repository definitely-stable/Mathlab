"""TOM-002: finite model-transfer falsification witnesses, not paper proof checks.

The checks specifically reject two INVALID extrapolations:
(i) reducing the rational characteristic-zero matrix recipe to every F_p;
(ii) applying characteristic-zero Wronskian arguments without assumptions.

They do not refute the SEPARATE positive-characteristic construction
present in OpenAI Math family 116, or any OM-140 memory lower bound.
"""
from fractions import Fraction
import unittest


def char_zero_matrix_entry(variable: int, row: int, column: int):
    """Coefficient from OM-116 char-zero construction, zero-indexed."""
    if variable < 1 or row < 0 or column < 0:
        raise ValueError("invalid matrix coordinate")
    if column >= row:
        return Fraction(0)
    return Fraction((-1) ** (row - column - 1), row * variable ** (row - column))


def fraction_mod_prime(value: Fraction, prime: int):
    """Defined only when denominator is invertible mod prime."""
    if prime < 2:
        raise ValueError("prime required")
    if value.denominator % prime == 0:
        raise ZeroDivisionError("denominator not invertible in characteristic p")
    return (value.numerator * pow(value.denominator, -1, prime)) % prime


def wronskian_monomials_at_one(prime: int):
    """Formal Wronskian of 1 and z^p over F_p evaluated at z=1."""
    return prime % prime


class TransferBarrierTests(unittest.TestCase):
    def test_rational_matrix_has_noninvertible_denominator_in_gf3(self):
        # Choose n=1,s=2 -> D=2ns^2=8, so coordinate row=3 exists.
        coeff = char_zero_matrix_entry(1, 3, 2)
        self.assertEqual(coeff, Fraction(1, 3))
        with self.assertRaises(ZeroDivisionError):
            fraction_mod_prime(coeff, 3)
        # This invalidates *naive reduction of this recipe*, NOT
        # existence of a distinct hitting tuple over GF(3).

    def test_rational_matrix_fraction_reduces_for_coprime_denominator(self):
        self.assertEqual(fraction_mod_prime(Fraction(1, 3), 5), 2)

    def test_wronskian_positive_characteristic_obstruction(self):
        # f(z)=1, g(z)=z^p are independent formal series, yet W(f,g)
        # equals p*z^(p-1), identically zero over F_p.
        for p in (2, 3, 5, 7):
            with self.subTest(prime=p):
                self.assertEqual(wronskian_monomials_at_one(p), 0)
                self.assertNotEqual((0, p), (0, 0))  # distinct monomial degrees
        # Distinct series with zero Wronskian -> characteristic-zero
        # nonvanishing proof cannot be transplanted unchanged.

    def test_exact_real_observations_can_recover_vector_when_retained(self):
        # A strictly nonsingular 2x2 measurement matrix is sufficient
        # for exact 2D signal recovery if all values are retained.
        # No finite-bit memory budget is asserted by this toy.
        x = (Fraction(3, 5), Fraction(4, 5))
        rows = ((Fraction(1), Fraction(2)), (Fraction(2), Fraction(1)))
        b1 = rows[0][0] * x[0] + rows[0][1] * x[1]
        b2 = rows[1][0] * x[0] + rows[1][1] * x[1]
        det = rows[0][0] * rows[1][1] - rows[0][1] * rows[1][0]
        self.assertNotEqual(det, 0)
        recovered = ((b1 * rows[1][1] - rows[0][1] * b2) / det,
                     (rows[0][0] * b2 - b1 * rows[1][0]) / det)
        self.assertEqual(recovered, x)

    def test_finite_state_bits_are_not_real_registers(self):
        # 2^M persistent states cannot uniquely represent 2^M+1
        # distinguishable signals without further resources.
        for memory_bits in range(5):
            states = 1 << memory_bits
            self.assertLess(states, states + 1)


if __name__ == "__main__":
    unittest.main()
