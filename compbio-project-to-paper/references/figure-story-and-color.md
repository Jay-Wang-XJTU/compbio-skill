# Figure story, plot choice, and color system

Design figures as an evidence sequence. A figure is not a storage bin for completed analyses.

## 1. Figure contract

For every main figure, write:

- the question it answers;
- one-sentence conclusion;
- the decisive panel;
- the evidence role of every other panel;
- the next question created by the figure;
- what moves to Supplementary material if the figure becomes crowded.

Typical roles are `problem context`, `method contract`, `controlled validation`, `decisive comparison`, `generalization`, `robustness`, `interpretation`, `biological discovery`, and `orthogonal validation`.

An often effective sequence for a new computational method is:

1. problem, data, and method contract;
2. controlled validation and decisive benchmark;
3. generalization, robustness, or scale required by the main claim;
4. real biological application;
5. interpretable or experimentally validated discovery.

Use the sequence as a diagnostic, not a mandatory five-figure template. Modular frameworks may devote one figure to each supported data view; discovery-led papers may lead with biology and place architecture later.

## 2. Plot selection

| Evidence question | Preferred forms | Caution |
|---|---|---|
| Performance across methods and datasets | dot/interval plot, rank plot, compact heatmap | Avoid crowded grouped bars and averages that hide dataset failures. |
| Distribution or group difference | box/violin plus points, ECDF, estimation plot | Show sample unit, n, uncertainty, and paired structure. |
| Embedding quality | UMAP/spatial map plus quantitative metric | Embeddings are context, not standalone proof. |
| Spatial organization | aligned small multiples, tissue map, enrichment dot plot | Keep coordinates, crop, scale, and labels comparable. |
| Composition | stacked bars for composition; dot plot for enrichment | Do not use stacked bars for precise small differences. |
| Robustness | line or interval plots across perturbation levels | Mark failure regions and missing runs. |
| Trajectory or fate | vector/streamline map plus time/fate validation | Avoid relying on direction arrows alone. |
| Cell-cell communication | matrix/heatmap for complete comparison; network for selected relationships | Dense hairball networks obscure evidence. |
| Attribution or regulators | ranked dot/bar plot plus expression, spatial, or perturbation validation | Feature importance alone is hypothesis generation. |
| Model architecture | left-to-right schematic with inputs, transformations, losses, and outputs | Show biological meaning, not every implementation layer. |

## 3. Semantic color ledger

Choose color by meaning and keep the mapping fixed across figures.

Default color-blind-aware starting points:

| Role | Hex | Use |
|---|---|---|
| focal method / primary claim | `#0072B2` | Proposed method, main trajectory, or primary condition |
| biological confirmation | `#009E73` | Validated or concordant biological signal |
| contrasting condition | `#D55E00` | Perturbation or comparison requiring emphasis |
| warning / uncertainty | `#E69F00` | Caution, ambiguous region, or intermediate state |
| secondary emphasis | `#CC79A7` | A distinct secondary mechanism or modality |
| supporting category | `#56B4E9` | Non-primary supportive series |
| comparator neutral | `#7A7A7A` | Baselines and non-focal methods |
| background cells / context | `#D9D9D9` | Non-focal observations |
| text / axes | `#2F2F2F` | Labels and structural marks |

Do not use all colors merely because they are available.

- Categorical variables: use distinct hues and preserve identity everywhere. For more than about eight categories, use hierarchical color families, direct labels, grouping, or separate panels rather than an unreadable flat palette.
- Ordered quantities: use a perceptually uniform sequential scale.
- Signed effects: use a diverging scale centered on the scientifically meaningful zero or null.
- Conditions: make the focal contrast visually strongest; use neutrals for context.
- Proposed method versus baselines: one accent for the method and neutral or lightly differentiated baselines unless individual competitors matter.
- Avoid rainbow scales, red-green-only distinctions, and encoding two unrelated meanings with the same color.

## 4. Panel discipline

- Make the decisive panel largest or visually first.
- Keep repeated axes, category order, spatial crop, and legend mapping identical.
- Prefer direct labels when they reduce legend lookup.
- Use typography and line weight for hierarchy before adding color.
- Show individual biological replicates when feasible; do not imply precision through decorative error bars.
- Put exhaustive alternative metrics, hyperparameters, seeds, and duplicate applications in Supplementary material.

## 5. QA

Check the complete figure at final physical size, then inspect every panel. Verify grayscale legibility, color-vision robustness, font size, panel-label order, statistical unit, n, uncertainty definition, repeated-category consistency, legend completeness, and whether each panel advances the figure conclusion.

