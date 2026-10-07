#!/usr/bin/env python3
"""Run the frozen LENT-001 G0 executable evidence."""

from lent_exact import self_check
from lent_exhaustive import run_frozen_grid


def main() -> None:
    self_check()
    run_frozen_grid()
    print("FOUNDATION_PASS")


if __name__ == "__main__":
    main()
