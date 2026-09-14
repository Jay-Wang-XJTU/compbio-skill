# Figure-first manuscript architecture

Use this route to organize a computational-biology paper before or during initial drafting.

## 1. Build the argument before sentences

Write:

- one central claim;
- up to three supporting claims;
- the decisive evidence for each claim;
- the boundary that prevents overclaiming;
- the contribution type: algorithmic, representational, resource, biological, or hybrid.

If a claim has no decisive evidence, mark it as a hypothesis or remove it from the headline story.

## 2. Use a figure-first Results outline

Map one Results subsection to one evidence question and normally one main figure. A useful progression is:

`problem and method -> controlled validation -> fair benchmark -> generalization/robustness -> biological application -> interpretation/validation`

Do not narrate the chronological order in which analyses were performed. Start each subsection with the question or claim, place decisive evidence early, then explain the boundary and transition to the next question.

Each paragraph should perform one job: `context`, `gap`, `approach`, `result`, `comparison`, `interpretation`, `boundary`, or `transition`.

## 3. Section logic

### Title

Name the central capability or biological advance. Avoid stacking architecture buzzwords unless the architecture itself is the contribution.

### Abstract

Use five moves: problem, exact gap, approach, decisive evidence, bounded payoff. Include representative quantitative evidence only when verified and central.

### Introduction

Move from the biological/computational problem to the exact unmet requirement, explain why existing method classes do not meet it, state the design response, and preview the evidence. Literature should establish the gap, not decorate every sentence.

### Results

Use claim-led subsection headings. Keep the method detail needed to interpret a result near that result; move implementation detail to Methods. Pair performance with failure analysis and biological interpretation where appropriate.

### Discussion

Synthesize what the evidence establishes, position the advance against prior work, distinguish technical performance from biological insight, state claim-specific limitations, and derive future work from those limitations. Do not repeat Results figure by figure.

### Methods and availability

Make data splits, preprocessing, baselines, tuning, seeds, hardware, software versions, statistical units, code, and data routes sufficient to reproduce decisive figures.

## 4. Claim language

- `outperforms` requires fair, representative comparisons and uncertainty.
- `generalizes` requires a genuinely held-out context matching the claim.
- `robust` requires defined perturbations or alternative specifications.
- `interpretable` requires a biological meaning and a validation route.
- `mechanistic` or causal language requires intervention or a design that supports causality.
- `scalable` requires measured resource behavior over relevant sizes.
- `framework` should denote a reusable interface or family of tasks, not a single model evaluated once.

## 5. Revision discipline

When a user redirects a draft, preserve correct sections and revise only the affected claim, paragraph, figure transition, or terminology. Any new paragraph should either replace weaker text or serve a previously missing evidence function. Maintain a compact terminology ledger for methods, datasets, cell types, metrics, modalities, and abbreviations.

## 6. Output map

Use:

| Section/Figure | Question | Claim | Evidence | Boundary | Paragraph jobs | Status |
|---|---|---|---|---|---|---|

Status values: `supported`, `partially supported`, `hypothesis`, `missing evidence`, or `remove`.

