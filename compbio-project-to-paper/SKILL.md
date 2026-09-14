---
name: compbio-project-to-paper
description: Assess and shape computational-biology projects into publishable evidence stories. Use for project-stage experiment prioritization, single-cell or spatial-omics method-paper figure strategy and color design, and figure-first manuscript planning. Do not use for routine pipeline execution, statistics-only analysis, or language-only polishing.
---

# Computational Biology Project to Paper

Turn an evolving computational-biology project into the shortest defensible evidence chain for a paper. Optimize for scientific credibility and narrative leverage, not experiment count. Never imply that a checklist guarantees acceptance.

## Routing

Read [manifest.yaml](manifest.yaml), detect one or more task values, and load only the matching references:

- `project-triage` — decide what must be done before submission, what can wait for review, and what should be dropped.
- `figure-story` — design the figure sequence, panel roles, plot forms, and semantic color system.
- `manuscript-architecture` — build the paper thesis, claim-evidence map, Results logic, and section outline.

Use multiple values for an integrated request. State the selected values in one short progress line and continue; this is a cheap correction point, not an approval gate.

## Core stance

- Start with the intended claim and contribution type, then evaluate analyses by the evidence function they serve.
- Separate a submission blocker from useful reviewer insurance. Do not recommend work merely because it is customary or possible.
- Treat UMAPs, spatial maps, attention weights, and attractive biological examples as context or interpretation unless paired with evidence that tests the claimed advantage.
- Calibrate the evidence bar to the claim. A predictive claim needs leakage-safe generalization; a mechanistic claim needs intervention or strong orthogonal support; a scalability claim needs measured runtime or memory behavior.
- Prefer strong simple baselines, fair tuning, explicit data splits, meaningful experimental units, uncertainty, and reproducibility over a larger collection of favorable metrics.
- Do not invent results, citations, biological mechanisms, sample sizes, or reviewer expectations. Mark missing evidence and distinguish author claims, observed results, and strategic recommendations.
- Use the supplied paper corpus as design evidence, not as a mandatory template. Verify current competitors, journal requirements, and recent benchmarks from primary sources when they could have changed.

## Shared workflow

1. Establish the project contract from available material: project stage, intended paper type, target venue or venue band, central claim, users, data modalities, current evidence, constraints, and desired submission horizon.
2. Write a one-sentence publication thesis: `For [biological/computational problem], we show [advance] using [approach], supported by [decisive evidence], within [boundary].`
3. Build a claim-evidence inventory before proposing more work. For each result, record the claim served, evidence function, current strength, source, and likely main/Supplementary destination.
4. Apply the matching route references. If a material choice cannot be inferred, pause only the dependent recommendation and continue independent work with a labeled assumption.
5. Return the requested artifact and run the route-specific QA below.

## Source and precedent handling

When the user supplies papers or a local corpus:

- Use the PDF workflow for text extraction and rendered-page inspection; do not infer layout from extracted text alone.
- Run `scripts/extract_paper_structure.py` when a compact index of titles, headings, caption pages, or candidate figure pages would reduce repeated inspection.
- Study evidence order, panel function, visual encoding, and claim language. Paraphrase patterns; do not copy prose or distinctive figure compositions.
- For online research, prefer official journal pages, publisher records, paper repositories, and authors' code/data repositories. Label preprints and record the search date.

Read [references/paper-patterns.md](references/paper-patterns.md) when the user asks for precedent, paper comparisons, publication norms, or lessons from the supplied corpus.

## Output contracts

### Project triage

Return:

1. `Publication thesis`
2. `Current evidence map`
3. `Priority table` using `P0 / P1 / P2 / P3` and `do now / prepare / defer / drop`
4. `Minimum submission package`
5. `Reviewer-risk register`
6. `Next milestone` with explicit stop/go criteria

Every proposed task must name the claim it serves, omission risk, approximate cost or dependency, figure destination, and trigger for revisiting it.

### Figure story

Return:

1. one-sentence conclusion for each figure;
2. panel map with each panel's evidence job;
3. recommended plot form and statistical unit;
4. semantic color ledger with hex values;
5. main-versus-Supplementary allocation;
6. accessibility and consistency checks.

### Manuscript architecture

Return:

1. publication thesis and contribution hierarchy;
2. figure-first Results outline;
3. section and paragraph jobs;
4. claim-evidence map;
5. assumptions, unsupported claims, and missing inputs;
6. targeted next writing step.

Draft prose only when requested. Preserve supplied facts and terminology, use placeholders for missing evidence, and revise locally rather than rewriting unaffected sections.

## Final QA

- Every recommended experiment or analysis has a unique evidence function.
- P0 items are genuine credibility or inference gates, not preferences.
- Deferred work has a concrete reviewer trigger and a preservation plan for adding it later.
- Main figures form a claim-escalating sequence; repeated robustness and secondary views move to Supplementary material.
- Proposed colors encode stable meanings across all panels and remain distinguishable without relying on red-versus-green.
- Claims do not outrun the data split, biological validation, statistical unit, or source material.
- Current literature statements are cited and distinguish published articles from preprints.

## Boundaries

This skill may specify analyses, controls, plots, and manuscript structure. It does not silently execute a full bioinformatics pipeline, fabricate missing results, choose a target journal with false certainty, or optimize findings through selective reporting. Use dedicated analysis, statistics, figure-generation, document, or language-editing capabilities when the user asks to execute those deliverables.
