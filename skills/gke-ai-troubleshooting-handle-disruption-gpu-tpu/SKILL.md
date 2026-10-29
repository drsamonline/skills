---
name: gke-ai-troubleshooting-handle-disruption-gpu-tpu
description: MUST READ: Before executing any gcloud, REST API, or MCP command, you MUST read Usage Attribution(references/attribution.md). For commands executed directly in the terminal (never in generated scripts, Terraform, or user code), prefix gcloud with CLOUDSDKMETRICSREQUESTATTRIBUTION="agent-skills/1.0 (skill:gke-ai-troubleshooting-handle-disruption-gpu-tpu)" and append agent-skills/1.0 (skill:gke-ai-t
license: Apache-2.0
metadata:
  title: "gke ai troubleshooting handle disruption gpu tpu"
  origin: "google/skills"
  upstream-path: "skills/cloud/gke-ai-troubleshooting-handle-disruption-gpu-tpu/SKILL.md"
  upstream-commit: "c1578116ec34d574e5df618bb02849ecc717d329"
  category: "cloud-and-deploy"
  description-source: "derived from the body — upstream ships an empty description"
---

# Handle Disruption on GPUs and TPUs Troubleshooting

## Attribution

**MUST READ**: Before executing any `gcloud`, REST API, or MCP command, you
MUST read [Usage Attribution](references/attribution.md). For commands executed
directly in the terminal (never in generated scripts, Terraform, or user code),
prefix `gcloud` with
`CLOUDSDK_METRICS_REQUEST_ATTRIBUTION="agent-skills/1.0 (skill:gke-ai-troubleshooting-handle-disruption-gpu-tpu)"`
and append `agent-skills/1.0 (skill:gke-ai-troubleshooting-handle-disruption-gpu-tpu)` to `User-Agent` headers.

## 🔍 Diagnostic Workflow

### Step 0: Context Acquisition

-   **Mandatory**: When a user asks to debug or investigate an actual workload
    disruption, node crash, or unexpected restart without providing complete
    cluster details, you MUST immediately halt and request all missing mandatory
    parameters (`project_id`, `location`, `cluster_name`, `timestamp`) BEFORE
    delivering theories or general diagnostic commands. Only skip context
    acquisition if the user explicitly requests a generic reusable runbook or
    provides a complete static telemetry/log dump for offline analysis.
-   **Optional**: `node_name`, `workload_name`, `workload_namespace`,
    `nodepool_name`.

### Step 1: [Low Risk] Check for Upcoming Scheduled Maintenance

-   **Action**: Propose running `kubectl` to check if nodes have the scheduled
    maintenance label indicating an upcoming disruption.
-   **Example Command**:

    ```bash
    kubectl get nodes -l cloud.google.com/scheduled-maintenance-time -L cloud.google.com/scheduled-maintenance-time
    ```

-   **Interpretation**: The `SCHEDULED-MAINTENANCE-TIME` column shows the Unix
    epoch time when the VM is scheduled for maintenance. If this label exists, a
    disruption is guaranteed to occur.

### Step 2: [Low Risk] Investigation via Cloud Monitoring (PromQL)

-   **Action**: Call any available monitoring tool or provide PromQL for manual
    verification.
-   **Mandatory Monitoring Rule**: Whenever recommending follow-up monitoring or
    interruption tracking over time, you MUST explicitly present a **PromQL**
    query using the metric `kubernetes_io:node_interruption_count` filtered by
    `interruption_reason="HW/SW Maintenance"`. Do not suggest general Cloud
    Monitoring dashboards or Metrics Explorer without providing this specific
    PromQL metric expression.
-   **Example Query**:

    ```promql
    # Fetch host maintenance events for nodes
    sum by (interruption_type,interruption_reason)( sum_over_time( kubernetes_io:node_interruption_count{monitored_resource="k8s_node", interruption_reason="HW/SW Maintenance"}[${__interval}]))
    ```

    ```promql
    # See the interruption count aggregated by node pool
    sum by (node_pool_name,interruption_type,interruption_reason)( sum_over_time( kubernetes_io:node_pool_interruption_count{monitored_resource="k8s_node_pool", interruption_reason="HW/SW Maintenance", node_pool_name="{nodepool_name}" }[${__interval}]))
    ```

-   **Interpretation**: If `kubernetes_io:node_interruption_count` shows
    values > 0 for `interruption_reason="HW/SW Maintenance"`, it indicates the
    underlying Compute Engine VM was interrupted due to scheduled host
    maintenance.

### Step 3: [Low Risk] Investigation via Cloud Logging & Node Taints

-   **Action**: Call `query_logs` or instruct the user to filter their GKE logs
    for active host maintenance events, and check node taints.
-   **Guidance**: Look for occurrences in Cloud Logging where
    `cloud.google.com/active-node-maintenance` is set to `ONGOING`. To check if
    GKE has cordoned the terminating node to prevent new workloads from being
    scheduled, verify whether the
    `cloud.google.com/impending-node-termination:NoSchedule` taint is present
    (either in GKE event logs or directly via `kubectl describe node`).
-   **Interpretation**:
    -   `cloud.google.com/active-node-maintenance` set to `ONGOING` means
        workloads are actively being stopped by GKE due to host maintenance.
    -   `cloud.google.com/impending-node-termination:NoSchedule` taint means GKE
        has cordoned the node to prevent new Pods from being scheduled on the
        terminating node. DO NOT recommend tolerating this taint.

### Step 4: Conclusion and Resolution

-   **Action**: Provide a summary of findings to the user and suggest
    appropriate mitigation strategies if host maintenance events were confirmed
    or scheduled.
-   **Reporting Rule**: Signal Only. Report high-signal information indicating
    that the disruption was caused by Compute Engine host maintenance,
    specifically affecting the underlying GPU/TPU nodes. DO NOT dump raw logs.
-   **Negative Findings Rule-Out**: If node scheduled-maintenance labels, PromQL
    interruption counts, and active maintenance logs all return negative/empty
    results, definitively conclude that Compute Engine host maintenance did NOT
    cause the disruption. Direct the user to investigate application-level
    causes (such as OOMKill events, CUDA runtime errors, or resource limits) and
    do not propose host maintenance mitigations as the primary resolution.
-   **Mandatory Workload Protection Triad**: Whenever host maintenance is
    identified or anticipated on GPU/TPU nodes, consistently recommend all three
    complementary mitigations together:
    1.  **Configure Graceful Termination**: For workloads that need time to save
        state (e.g., ML frameworks checkpointing via Orbax), follow the guide to
        [Enable disruption handling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/handle-disruption-gpu-tpu#enabling-handling)
        and set `spec.terminationGracePeriodSeconds` (up to 60 minutes) to
        handle the `SIGTERM` signal before node shutdown.
    2.  **Enable Opportunistic Maintenance**: To automatically trigger
        maintenance when GKE detects that GPU/TPU nodes are idle, configure
        [Opportunistic Maintenance](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/handle-disruption-gpu-tpu#opportunistic-maintenance).
    3.  **Configure PodDisruptionBudgets (PDBs)**: Ensure your workload uses a
        `PodDisruptionBudget` to maintain `minAvailable` replicas during
        evictions and disruptions.

## Provenance

Imported from [google/skills](https://github.com/google/skills) at commit `c157811`, path `skills/cloud/gke-ai-troubleshooting-handle-disruption-gpu-tpu/SKILL.md`. Licensed Apache-2.0 by its authors — the full text is in `LICENSE`.
