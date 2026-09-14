# Publication-oriented project triage

Use this route to decide what earns scarce development time before submission.

## 1. Define the claim contract

Record:

- intended paper type: method, resource, benchmark, biological discovery, or hybrid;
- central claim and no more than three supporting claims;
- target users and the decision or analysis the method improves;
- target venue or realistic venue band;
- submission horizon, compute, data, wet-lab, and personnel constraints;
- boundary: what the project will not claim.

If the venue is unspecified, use a conservative high-quality computational-method paper baseline and label it as an assumption. Do not infer that adding more datasets automatically raises the venue tier.

## 2. Classify current and proposed work

Assign one evidence function to each item:

- `problem validity` — establishes that the problem is real and not solved by a trivial alternative;
- `method correctness` — tests whether the implementation realizes the claimed mechanism;
- `decisive comparison` — compares against strong and simple baselines under fair conditions;
- `generalization` — tests an unseen donor, dataset, platform, species, perturbation, modality, or domain required by the claim;
- `robustness` — tests seeds, hyperparameters, noise, missing features, preprocessing, or alternative specifications;
- `ablation` — isolates the contribution of a claimed component;
- `scalability` — measures runtime, memory, or sample-size behavior;
- `interpretability` — connects model representations to a verifiable biological quantity;
- `biological discovery` — reveals a nontrivial biological pattern beyond method performance;
- `orthogonal validation` — supports the finding with another assay, cohort, database, perturbation, or experiment;
- `reproducibility` — code, environment, data access, deterministic seeds, documentation, and figure provenance.

If two proposed items serve the same function for the same claim, prefer the cheaper or stronger one unless heterogeneity itself is part of the claim.

## 3. Priority and action

### P0 — submission blocker

Without this item, the central claim is not credible, fair, reproducible, or interpretable at the claimed level. Typical P0 cases include leakage-safe splits, appropriate experimental units, a credible simple baseline, an ablation for the named innovation, external validation required by a generalization claim, and intervention evidence required by a causal or mechanistic claim.

Action: `do now`.

### P1 — claim advancer

Materially strengthens or broadens a central claim and is likely to earn main-figure space. It may turn a technical improvement into biological utility, establish cross-platform value, or show that an interpretable component leads to a verified insight.

Action: normally `do now`; defer only when cost is high and the narrower claim remains publishable.

### P2 — reviewer insurance

Answers a plausible challenge but does not change the paper's main conclusion. Examples include secondary clustering choices, additional seeds after stability is established, another closely related dataset, or extended sensitivity ranges.

Action: `prepare` when cheap or when results take a long time to generate; otherwise `defer` with code paths, cached inputs, and a precise trigger.

### P3 — low-yield extension

Duplicates an existing evidence function, adds a weakly related modality, produces a decorative analysis, or creates more failure surface than claim leverage.

Action: `drop` unless it replaces weaker evidence.

## 4. Decision dimensions

Judge priority using qualitative evidence, not a false-precision score:

| Dimension | Question |
|---|---|
| Claim leverage | Would the result establish, advance, or materially bound a central claim? |
| Omission risk | Could a careful reviewer reject the inference without it? |
| Evidence uniqueness | Does another existing result already perform the same job? |
| Cost and dependency | What compute, data, wet-lab work, or engineering blocks it? |
| Failure informativeness | Would a negative result improve the claim boundary or reveal a fatal weakness? |
| Figure value | Does it earn a main-panel role, a Supplementary role, or no paper role? |
| Scope risk | Does it introduce a new claim that requires its own validation chain? |

## 5. What usually cannot wait

- train/test or donor/platform leakage checks aligned to the claim;
- fair baseline selection and tuning, including strong simple baselines;
- correct statistical unit and uncertainty across biological or dataset-level replicates;
- ablations for components named as the reason the method works;
- external or out-of-distribution validation when generalization is claimed;
- biological validation proportional to the strength of biological language;
- measured scalability when scale is advertised;
- accessible code/data/environment sufficient to reproduce decisive figures;
- an honest limitations boundary.

## 6. What can often wait

- every published baseline rather than a representative, strong set;
- datasets that repeat the same domain, scale, and evidence function;
- exhaustive hyperparameter sweeps after a defensible stability region is shown;
- additional biological narratives that do not test a distinct claim;
- expensive validation for a claim the manuscript can explicitly narrow without it.

Deferral is not omission by neglect. Preserve the runnable analysis, input manifest, expected output, figure slot, estimated turnaround, and reviewer trigger.

## 7. Output table

Use this schema:

| Item | Claim served | Evidence function | Priority | Action | Omission risk | Cost/dependency | Main/SI destination | Revisit trigger |
|---|---|---|---|---|---|---|---|---|

End with a minimum submission package and one next milestone whose stop/go criteria can be checked from observable results.

