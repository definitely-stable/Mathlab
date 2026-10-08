# Preprints

This directory is intentionally empty of research claims at the LENT-001 G0 stage.

A Mathlab result is promoted here only after:

1. statement freeze;
2. complete reviewable proof;
3. prior-art classification sufficient for an honest novelty statement;
4. reproducible verification instructions;
5. explicit Lean status.

Expected per-preprint layout, following the useful separation pattern in `openai/math`:

```text
preprints/<result-family>/
  README.md          # title, version, citation, verification instructions
  manuscript/        # source
  verification/      # exact/checker artifacts specific to the manuscript
  paper.pdf          # only when reproducibly built
```

Historical versions should remain traceable after corrections.
