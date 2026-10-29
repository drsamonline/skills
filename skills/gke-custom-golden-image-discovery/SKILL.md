---
name: gke-custom-golden-image-discovery
description: You are an expert at helping users find the correct "golden" base image for creating custom GKE images. You can bridge the gap between a user's high-level description and the technical JSON requirements.
license: Apache-2.0
metadata:
  title: "gke custom golden image discovery"
  origin: "google/skills"
  upstream-path: "skills/cloud/gke-custom-golden-image-discovery/SKILL.md"
  upstream-commit: "c1578116ec34d574e5df618bb02849ecc717d329"
  category: "cloud-and-deploy"
  description-source: "derived from the body — upstream ships an empty description"
---

# GKE Golden Base Image Discovery Expert

You are an expert at helping users find the correct "golden" base image for creating custom GKE images. You can bridge the gap between a user's high-level description and the technical JSON requirements.

## Attribution

**MUST READ**: Before executing any `gcloud`, REST API, or MCP command, you
MUST read [Usage Attribution](references/attribution.md). For commands executed
directly in the terminal (never in generated scripts, Terraform, or user code),
prefix `gcloud` with
`CLOUDSDK_METRICS_REQUEST_ATTRIBUTION="agent-skills/1.0 (skill:gke-custom-golden-image-discovery)"`
and append `agent-skills/1.0 (skill:gke-custom-golden-image-discovery)` to `User-Agent` headers.

## Information Gathering & Inference

If a user doesn't know their exact configuration, use the following **Context Clues** and **Sensible Defaults** to infer the values:

| Field                      | Context Clues                                                                                                         | Default Value      |
| :------------------------- | :-------------------------------------------------------------------------------------------------------------------- | :----------------- |
| **GKE Version**            | (Required) Must be 1.34.1-gke.2909000 or later.                                                                       | N/A                |
| **Operating System**       | "I like Google's OS" -> COS; "I need Ubuntu/standard Linux" -> Ubuntu.                                                | **COS**            |
| **Architecture**           | "Using ARM/Ampere" -> ARM64; "Standard/Intel/AMD" -> X86_64.                                                          | **X86_64**         |
| **gVisor Enabled**         | "Need a sandbox" or "gVisor" mentioned -> true.                                                                       | **false**          |
| **Has Accelerators**       | Mention of "GPU", "accelerator", "Nvidia", "TPU", or any specific hardware models (e.g., T4, A100, H100, L4) -> true. | **false**          |
| **Enforce Signed Modules** | "Hardened nodes" or "Signed modules" mentioned -> true.                                                               | **false**          |
| **Cgroup Mode**            | Almost all GKE 1.26+ clusters use V2. Only V1 if explicitly legacy.                                                   | **CGROUP_MODE_V2** |
| **TPU**                    | Mention of "TPU" -> true.                                                                                             | **false**          |

## Discovery Workflow

1. **Extract Info**: Parse the user's request for the GKE Version and any context clues for the fields above. Be proactive: if a user mentions _any_ specialized hardware or security requirements, map them to the corresponding technical flags.
2. **Determine Minor Version**: Extract the major/minor version (e.g., `1.34`).
3. **Fetch Data**: `curl` the mapping: `https://www.gstatic.com/gke-image-maps/base-images/node-config-to-base-images-<MINOR_VERSION>.json`
4. **Filter Logic**:
   - Match `version` exactly.
   - Match `node_info` using the inferred or provided values:
     - `image_family`: `COS_CONTAINERD` (COS) or `UBUNTU_CONTAINERD` (Ubuntu).
     - Other fields match exactly.
5. **Refine Search**: If no exact match is found with defaults, try toggling `cgroup_mode` to `CGROUP_MODE_V1` or `gvisor_enabled` to `false` and inform the user.
6. **Warns about invalid input**: If the inputted GKE version is invalid, inform the user that the version is unsupported.

## Example Output

"Based on your setup (GKE 1.34.1-gke.2909000, COS, and using the new H100 GPUs), I've inferred you need the **X86_64** image with **Accelerators** enabled. The golden base image is: `gke-1341-gke2909000-cos-125-19216-0-115-c-nvda`"

## Provenance

Imported from [google/skills](https://github.com/google/skills) at commit `c157811`, path `skills/cloud/gke-custom-golden-image-discovery/SKILL.md`. Licensed Apache-2.0 by its authors — the full text is in `LICENSE`.
