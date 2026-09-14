# Paper-derived design patterns

This synthesis was prepared on 2026-09-14 from ten user-supplied PDFs in `D:\Work\paper`, targeted rendered-page inspection, and primary online paper pages. It records reusable evidence and presentation patterns, not prose or figure templates to copy. Re-check current competitors and journal requirements for live projects.

`local-corpus-index.json` is a local-only extraction audit containing source paths and candidate caption pages. Do not load it for ordinary project advice; use it only to locate pages for renewed inspection of the original PDFs.

## Local corpus

| Paper | Evidence and presentation logic | Reusable lesson |
|---|---|---|
| [scGen](https://doi.org/10.1038/s41592-019-0494-8) | Method schematic, held-out perturbation prediction, then transfer across cell types, studies, and species. | A compact paper can succeed when every application tests a distinct generalization axis. Modern submissions need stronger simple baselines and leakage controls than this 2019 precedent alone supplies. |
| [scVelo](https://doi.org/10.1038/s41587-020-0591-3) | Starts from a violated modeling assumption, introduces a dynamical alternative, then links kinetic fits to latent time and developmental biology. | Method novelty is clearest when the failure mode, mathematical response, and biological consequence are visibly connected. |
| [CytoCommunity](https://doi.org/10.1038/s41592-023-02124-2) | One framework supports unsupervised and supervised questions; controlled spatial benchmarks precede risk-associated tumor-neighborhood discoveries. | Multiple modes belong in one paper only when each has an explicit task and biological payoff. |
| [CellRank 2](https://doi.org/10.1038/s41592-024-02303-9) | A modular kernel abstraction unifies pseudotime, velocity, time-series, and metabolic-labeling views; each view receives a distinct application. | Breadth is persuasive when a shared interface connects otherwise different data views and each application proves that modularity. |
| [NicheCompass](https://doi.org/10.1038/s41588-025-02120-6) | Architecture and interpretable signaling programs lead to developmental biology, broad benchmarking, cancer niches, reference mapping, multi-omics, and atlas scale. | A strong deep-learning paper pairs benchmark superiority with interpretable biology, domain transfer, and measured scale; robustness repetition moves to extended material. |
| [CellFlow](https://doi.org/10.1101/2025.04.11.648220) — preprint | Generative perturbation framework, scale and interpretability, diverse benchmarks, then condition prioritization and virtual protocol screening. | Connect model performance to an experimental decision; the strongest application changes what should be tested next. |
| [RegVelo](https://doi.org/10.1016/j.cell.2026.04.022) | Couples gene regulation with dynamics, benchmarks fate and network inference, makes perturbation predictions, then validates regulators with CRISPR/Perturb-seq and in vivo evidence. | Experimental validation can elevate a method paper into a mechanistic discovery paper, but it becomes a submission gate once mechanistic language is central. |
| [CellNiche](https://doi.org/10.1038/s41467-026-71759-4) | Places atlas-scale efficiency in the opening contract, benchmarks across spatial transcriptomics and proteomics, then shows tumor and cross-platform atlas applications. | Scalability should be measured early and followed by a use case that is only possible at that scale. |
| [DECODE](https://doi.org/10.1038/s41592-026-03007-y) | Four-stage common deconvolution framework, cross-omics benchmark breadth, explicit noise/batch/unknown-type stress tests, and real-cohort application. | A broad `common framework` claim needs controlled scenario coverage and robustness tests, not only one real dataset. |
| [NicheTrans](https://doi.org/10.1038/s41592-026-03153-3) | Separates problem motivation from model architecture, evaluates paired translation quantitatively and qualitatively, then uses translated modalities for domains, programs, and disease interpretation. | For cross-omics translation, show both reconstruction fidelity and biological information unavailable from the measured modality alone. |

## Recent external signals

- [scGPT](https://doi.org/10.1038/s41592-024-02201-0) demonstrates the broad-task foundation-model narrative, but breadth should not substitute for matched task-specific baselines.
- [Deeper evaluation of a single-cell foundation model](https://doi.org/10.1038/s42256-024-00949-w) shows that reproductions, ablations, and logistic-regression baselines can overturn an architectural narrative.
- [Deep-learning perturbation prediction does not yet outperform simple linear baselines](https://doi.org/10.1038/s41592-025-02772-6) makes the simple-baseline requirement a central design constraint for new perturbation models.
- [Benchmarking generalizable single-cell perturbation prediction](https://doi.org/10.1038/s41592-025-02980-0) evaluates 27 methods on 29 datasets with complementary metrics, illustrating the current expectation for scenario-level generalization rather than one aggregate score.
- [Nicheformer](https://doi.org/10.1038/s41592-025-02814-z) uses a large mixed single-cell/spatial corpus, spatially defined downstream tasks, uncertainty, and data-subset analyses to support a spatial foundation-model claim.
- [Open Problems in Single-Cell Analysis](https://doi.org/10.1038/s41587-025-02694-w) emphasizes living, community-guided task definitions and reproducible benchmarks as the field grows beyond one-off comparisons.
- [A foundation model of transcription across human cell types](https://doi.org/10.1038/s41586-024-08391-z) illustrates a stronger biological endpoint for foundation models: extrapolation to unseen cell types tied to regulatory prediction.

## Cross-paper synthesis

The recurring main-text evidence ladder is:

1. establish the unmet biological or computational requirement;
2. state the method contract and assumptions;
3. validate under a controlled or ground-truth setting;
4. compare fairly with strong simple and state-of-the-art baselines;
5. test the exact generalization, robustness, or scale in the headline claim;
6. show a real biological or experimental-decision payoff;
7. add orthogonal or experimental validation when interpretation becomes mechanistic;
8. make decisive figures reproducible.

Common visual patterns include a schematic-led first figure, stable colors for cell identities across embeddings and tissue maps, one accent color for the proposed method, gray contextual cells, aligned small multiples, quantitative panels beside qualitative maps, and movement of exhaustive robustness to Supplementary or Extended Data.
