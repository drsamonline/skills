---
name: gke-cost-analysis
description: This skill provides guidance on answering natural language questions about GKE-related costs, billing reports, and utilization analysis.
license: Apache-2.0
metadata:
  title: "gke cost analysis"
  origin: "google/skills"
  upstream-path: "skills/cloud/gke-cost-analysis/SKILL.md"
  upstream-commit: "c1578116ec34d574e5df618bb02849ecc717d329"
  category: "cloud-and-deploy"
  description-source: "derived from the body — upstream ships an empty description"
---

# GKE Cost Analysis

This skill provides guidance on answering natural language questions about
GKE-related costs, billing reports, and utilization analysis.

## Attribution

**MUST READ**: Before executing any `gcloud`, REST API, or MCP command, you
MUST read [Usage Attribution](references/attribution.md). For commands executed
directly in the terminal (never in generated scripts, Terraform, or user code),
prefix `gcloud` with
`CLOUDSDK_METRICS_REQUEST_ATTRIBUTION="agent-skills/1.0 (skill:gke-cost-analysis)"`
and append `agent-skills/1.0 (skill:gke-cost-analysis)` to `User-Agent` headers.

## Overview

When users ask about GKE costs (e.g., "What are my costs across projects?",
"What's my most expensive namespace?", "Why is my cluster cost spiking?"), use
this skill to provide a structured and expert response using BigQuery billing
exports, cost allocation metadata, and live cluster metrics.

## Instructions

When handling a cost-related question:

1.  **Provide a Direct Answer**: Address the specific cost question or
    analytical request clearly and concisely.
2.  **Explain BigQuery Integration**: Explain how to query BigQuery for
    historical cost breakdown. Note that GKE costs originate from the GCP
    Billing Detailed BigQuery Export (`gcp_billing_export_resource_v1_*`).
3.  **Check & Verify Cost Allocation**: Explain that GKE Cost Allocation must be
    enabled on the cluster (`--enable-cost-allocation`) for namespace, label,
    and workload-level billing granularity. If queries return empty labels,
    provide the `gcloud` command to enable it.
4.  **Analyze Pricing Drivers & Utilization**: When diagnosing cost drivers,
    explain whether the cluster is in Autopilot (billed by requested pod
    CPU/memory) or Standard mode (billed by underlying VM node size + control
    plane fees), and compare live utilization (`kubectl top`) against
    provisioned requests.
5.  **Provide Actionable Commands/Queries**: Provide concrete BigQuery CLI (`bq
    query`) commands or read-only `gcloud`/`kubectl` inspection commands. Prefer
    `bq` over BigQuery Studio when available.

## Key Points & Pricing Drivers

-   **Data Source**: GKE costs come from GCP Billing Detailed BigQuery Export.
    The user must provide the full path to their BigQuery table (dataset name
    and table name containing the Billing Account ID).
-   **Granularity Requirement**: GKE Cost Allocation
    (`--enable-cost-allocation`) must be enabled on the cluster to populate
    `goog-k8s-cluster-name`, `k8s-namespace`, `k8s-workload-name`, and
    `k8s-workload-type` labels in BigQuery.
-   **Autopilot vs. Standard Cost Drivers**:
    -   **Autopilot Pricing**: Billed directly on pod resource requests
        (`requests.cpu`, `requests.memory`, ephemeral storage). Over-requested
        pods drive up billing regardless of whether the pod actively uses those
        CPU cycles or memory.
    -   **Standard Pricing**: Billed on provisioned node pool VMs (`e2`, `n4`,
        `c3`, etc.). Idle nodes or multiple low-utilization dev clusters drive
        excess infrastructure costs.
    -   **Cluster Management Fee**: ~$0.10/hour per cluster applies to BOTH
        Standard and Autopilot modes. The free tier waives it for one eligible
        cluster per billing account.
-   **Credits & Discounts Impact**: When analyzing `cost` versus
    `cost_before_credits`, note that Committed Use Discounts (CUDs) and Spot VMs
    appear as credits or reduced rate charges in the billing export.
-   **Tools & Syntax**: BigQuery CLI (`bq`) is preferred. When writing Standard
    SQL queries, use a dot (`.`) instead of a colon (`:`) to separate the
    project ID and dataset name (`{project_id}.{dataset_name}.{table_name}`).
-   **Defaults**: Assume last 30 days, row limit 10, ordering by cost descending
    (`ORDER BY cost DESC`), unless specified otherwise.

## Live Cluster & Cost Monitoring

Use read-only CLI commands to inspect current cluster budgets, node utilization,
and pod resource consumption vs. requests:

```bash
# View billing budgets for an account (requires Cost Management API)
gcloud billing budgets list --billing-account={billing_account} --quiet

# View live node resource utilization across the cluster
kubectl top nodes

# View pod resource usage across namespaces (compare against requested limits to diagnose waste)
kubectl top pods --all-namespaces --containers
```

> **Warning — cluster mutation, not read-only:** Enabling GKE cost allocation
> modifies the cluster. Get explicit user confirmation before running it, and
> note that namespace/workload labels populate in the billing export only from
> enablement onward (no historical backfill).
>
> ```bash
> gcloud container clusters update {cluster_name} \
>     --enable-cost-allocation \
>     --region {region}
> ```

## Applying Cost Optimizations

To apply rightsizing changes based on analysis (such as setting up `VPA`
recommendation mode, adjusting CPU/memory to `P95 * 1.2`, configuring Spot VMs
via `nodeSelector` or `ComputeClass`, enforcing `ResourceQuotas`, or selecting
machine types and CUDs), use the **`gke-cost-optimization`** skill.

## BigQuery Query Templates

Ready-to-adapt `bq query` templates — single workload cost, per-workload
per-cluster breakdown, per-namespace breakdown — with the placeholder policy
and defaults (30 days, `LIMIT 10`, `ORDER BY cost DESC`) are in
[references/billing-queries.md](references/billing-queries.md). All parameters
(dataset, table, project, cluster, etc.) must be replaced with user values.

Note: Checking that the `goog-k8s-cluster-name` label exists scopes the total
billing data specifically to GKE costs.

## Provenance

Imported from [google/skills](https://github.com/google/skills) at commit `c157811`, path `skills/cloud/gke-cost-analysis/SKILL.md`. Licensed Apache-2.0 by its authors — the full text is in `LICENSE`.
