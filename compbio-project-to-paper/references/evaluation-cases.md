# Behavioral evaluation cases

Use these cases when materially revising the skill. Evaluate decisions and artifacts, not exact wording.

## Case 1 — avoid experiment accumulation

Request: A spatial-omics GNN has one dataset, random cell-level train/test splits, several UMAPs, and a plan for twenty more hyperparameter combinations. Decide what is needed before submission.

Required behavior:

- identify split leakage and the experimental unit as potential P0 issues;
- request a strong simple baseline and a component ablation tied to the claimed innovation;
- distinguish cross-donor, cross-slice, or cross-platform generalization from random-cell interpolation;
- classify exhaustive tuning and duplicate UMAPs as lower priority unless they expose a claim boundary;
- provide do-now, defer, and drop decisions rather than recommending every possible analysis.

## Case 2 — figure and color semantics

Request: Design figures for a method compared with six baselines across four datasets and show eighteen cell types in spatial maps.

Required behavior:

- assign one accent to the proposed method and neutral or controlled colors to baselines;
- preserve cell-type identities across maps without reusing method-comparison colors for unrelated meanings;
- recommend a dot/interval plot or heatmap for the benchmark rather than an unreadable grouped-bar grid;
- use aligned spatial small multiples, contextual gray, direct labels or hierarchical color families;
- pair qualitative maps with quantitative evidence and specify main-versus-Supplementary placement.

## Case 3 — manuscript without complete results

Request: Organize an initial manuscript from a method description and partial results, but several metrics and biological validations are missing.

Required behavior:

- build a publication thesis and figure-first outline from supplied evidence;
- label unsupported claims and missing inputs instead of inventing numbers or mechanisms;
- distinguish a computational utility paper from a mechanistic biological paper;
- draft prose only if requested and use placeholders where evidence is missing;
- recommend the next writing or analysis milestone with observable stop/go criteria.

## Case 4 — interpretability is not mechanism

Request: Attention weights highlight a transcription factor, so write that the model discovered its causal regulatory role.

Required behavior:

- reject or downgrade the causal wording;
- classify the attention result as a hypothesis-generating attribution;
- propose orthogonal or perturbational validation proportional to the desired claim;
- allow a narrower association claim if the user cannot obtain intervention evidence.

