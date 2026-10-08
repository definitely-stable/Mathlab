#!/usr/bin/env python3
"""Run frozen G0 evidence plus the active G1A exact-oracle evidence."""

from lent_exact import self_check
from lent_exhaustive import run_frozen_grid, run_g1a_grid


def main() -> None:
    self_check()
    run_frozen_grid()
    print("FOUNDATION_PASS")
    run_g1a_grid()


if __name__ == "__main__":
    main()
