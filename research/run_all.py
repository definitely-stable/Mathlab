#!/usr/bin/env python3
"""Run G0/G1A evidence and the active G2A exact-extremal lab."""

from lent_exact import self_check
from lent_exhaustive import run_frozen_grid, run_g1a_grid
from lent_extremal import run_g2a


def main() -> None:
    self_check()
    run_frozen_grid()
    print("FOUNDATION_PASS")
    run_g1a_grid()
    run_g2a()


if __name__ == "__main__":
    main()
