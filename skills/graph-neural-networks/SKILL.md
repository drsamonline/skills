---
name: graph-neural-networks
description: "Build graph neural networks with PyTorch Geometric: node, link and graph classification; message passing with GCN, GAT, GraphSAGE, GIN; heterogeneous graphs; neighbour sampling for large graphs; custom datasets and transforms. Use when working with `torch_geometric`, not for general NetworkX analytics or non-graph PyTorch models."
license: "per source — see references/*/LICENSE"
metadata:
  title: "Graph neural networks with PyTorch Geometric"
  category: "ai-and-ml"
  origin: "merged pack, imported 2026-11-07"
  merged-from: "torch-geometric"
---

# Graph neural networks with PyTorch Geometric

Almost every PyG bug is a shape or an orientation: `edge_index` is `[2, num_edges]`, seed nodes come first in a loader batch, and heterogeneous graphs change which conveniences are legal. Learn the data contract before the model.

## When to use

- The data is a graph and the task is node, edge or graph level prediction.
- A heterogeneous schema (multiple node and edge types) needs modelling.
- A graph is too large for GPU memory and needs neighbour sampling.

## Method

1. Install the PyTorch build for the platform first, then PyG; neighbour sampling needs `pyg-lib` or `torch-sparse`, and spatial k-NN needs `pyg-lib`.
2. Build the data correctly: `edge_index` shaped `[2, num_edges]` (transpose if you have a list of pairs), features aligned to node order, and explicit splits.
3. For heterogeneous data use `HeteroData` with node and edge types, and a conv layer that takes the metadata (for example HGT with a head count that divides the hidden size).
4. Choose the conv layer by task and graph: GCN for homophilous citation-style graphs, GAT where edge-level attention helps, GraphSAGE for inductive neighbourhood aggregation, GIN for expressive graph-level tasks.
5. Apply transforms deliberately: `pre_transform` is computed once and cached, `transform` runs on every access. Confirm weight semantics before `ToUndirected` (it reduces duplicate edge attributes, default sum) and remember self-loops can duplicate existing ones.
6. Do not use `add_self_loops=True` on a heterogeneous bipartite graph where source and destination types differ — use skip connections instead.
7. For graphs that do not fit in memory, use `NeighborLoader` with a compatible sampling backend and remember the seed nodes are the first `batch.batch_size` rows of the output.
8. Preserve the dataset version, split and preprocessing when comparing against published numbers; OGB benchmarks use their own package and evaluator.
9. Sanity-check with a tiny graph and an overfit-one-batch run before scaling up.

## Sources merged here

Each row is one skill that went into this one. The full original text, scripts and assets live in
`references/<id>/` — read the row first, then that folder.

| Source skill | What it adds |
|---|---|
| [`torch-geometric`](references/torch-geometric/) | The PyG reference: data contracts, datasets, transforms, layers, custom message passing, task patterns, neighbour sampling. |

## Key files / entry points

- `references/torch-geometric/` — installation, `Data`/`HeteroData`, datasets, transforms, built-in layers, custom `MessagePassing`, task patterns, sampling.

## Gotchas

- `edge_index` with shape `[num_edges, 2]` trains silently and badly.
- Seed nodes are the first rows of a loader batch, not the whole batch.
- `ToUndirected` can merge edge attributes and change their meaning.
- Dataset classes download from providers; they are not API search endpoints.
- Extension requirements differ by PyG minor version — check the installed release.

## Licence & attribution

The merged text above is © 2026 Dr. Sohil Momin. Each merged source keeps its own licence and
attribution inside its folder under `references/`; where a source shipped a `LICENSE`, that file is
preserved verbatim next to it.

- `torch-geometric` — no licence file shipped with the source
