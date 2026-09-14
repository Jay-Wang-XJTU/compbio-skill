# Benchmark and evidence design for computational biology

Load this reference when project or manuscript decisions depend on the adequacy of benchmarks, validation, generalization, robustness, interpretability, or reproducibility.

## Universal checks

- Define the biological or computational experimental unit before significance testing. Cells from one donor are not independent donors.
- Match data splitting to the generalization claim: unseen cells, donors, batches, studies, tissues, species, platforms, perturbations, or combinations are different tests.
- Identify leakage through preprocessing, feature selection, normalization, graph construction, label transfer, pretrained corpora, and hyperparameter selection.
- Include strong simple baselines and representative state-of-the-art methods. Apply comparable inputs, tuning budgets, and stopping criteria.
- Use metrics that expose complementary failure modes; do not multiply correlated metrics to simulate evidence breadth.
- Report variability across the unit that was resampled, not only across random seeds on a fixed dataset.
- Separate interpolation from extrapolation and in-domain accuracy from out-of-domain generalization.
- Preserve failures, resource constraints, and non-applicable methods in the comparison record.

## Claim-specific evidence

### Prediction and perturbation response

Use held-out regimes that match the advertised use: unseen perturbation, cell type, donor, dose, combination, or dataset. Compare with mean/control and linear baselines. Examine direction, magnitude, distributional fidelity, calibration or uncertainty, and downstream biological conclusions rather than only global correlation.

### Representation learning, integration, and foundation models

Test whether representations improve a defined task over PCA or a task-specific baseline. Separate batch mixing from biological conservation. Evaluate rare populations, zero/few-shot claims, frozen versus fine-tuned representations, data-scale ablations, and overlap between pretraining and evaluation corpora.

### Spatial omics

Use ground truth where available, plus anatomical or experimental validation. Test across slices, donors, resolutions, panels, and platforms when claimed. Guard against spatial leakage from nearby cells or registered sections. Pair spatial maps with quantitative metrics and a biological interpretation that can be independently checked.

### Trajectory and dynamics

Address identifiability and model assumptions. Test terminal-state recovery, directionality, time ordering, kinetic parameters, lineage drivers, or perturbation effects using time-resolved, lineage-tracing, metabolic-labeling, CRISPR, or other orthogonal evidence when the claim requires it.

### Deconvolution

Use synthetic or pseudo-bulk mixtures with known proportions, mismatched-reference and unknown-cell-type scenarios, batch and noise stress tests, cross-cohort evaluation, and real-tissue plausibility. Distinguish performance on proportions from downstream biological utility.

### Interpretability and mechanism

Attention, latent dimensions, gradients, or feature rankings are hypotheses, not validation. Stronger evidence includes component ablation, perturbation consistency, orthogonal measurements, known regulatory relationships, prospective prediction, and experimental intervention. Use causal language only when the design licenses it.

### Scalability

Measure wall time and peak memory at relevant sizes, with hardware and preprocessing scope stated. Include failure or out-of-memory outcomes fairly. A theoretical complexity statement does not replace measured behavior.

## Main versus Supplementary placement

Keep in main figures the decisive comparison, the generalization test needed by the headline claim, one meaningful robustness boundary, and the biological or user-facing payoff. Put exhaustive seeds, alternative preprocessing, secondary metrics, extended ablations, extra datasets with duplicate evidence functions, and implementation diagnostics in Supplementary material unless they change the conclusion.

## Warning signs

- random cell splits presented as donor-level generalization;
- many UMAPs without a quantitative decision criterion;
- a new deep model compared only with older complex methods but not a linear or non-neural baseline;
- cherry-picked datasets, cell types, genes, or perturbations;
- significance computed over cells when the claim concerns samples or patients;
- interpretability asserted from attractive feature maps alone;
- biological discovery that is only a restatement of known marker expression;
- a broad framework claim supported by one modality or one cohort;
- reproducibility artifacts promised but not sufficient to regenerate decisive figures.

