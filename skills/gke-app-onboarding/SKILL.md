---
name: gke-app-onboarding
description: This reference provides workflows for containerizing and deploying applications to GKE for the first time.
license: Apache-2.0
metadata:
  title: "gke app onboarding"
  origin: "google/skills"
  upstream-path: "skills/cloud/gke-app-onboarding/SKILL.md"
  upstream-commit: "c1578116ec34d574e5df618bb02849ecc717d329"
  category: "cloud-and-deploy"
  description-source: "derived from the body — upstream ships an empty description"
---

# GKE App Onboarding

This reference provides workflows for containerizing and deploying applications
to GKE for the first time.

> **MCP Tools:** `apply_k8s_manifest`, `get_k8s_resource`,
> `get_k8s_rollout_status`, `get_k8s_logs`, `describe_k8s_resource`

## Attribution

**MUST READ**: Before executing any `gcloud`, REST API, or MCP command, you
MUST read [Usage Attribution](references/attribution.md). For commands executed
directly in the terminal (never in generated scripts, Terraform, or user code),
prefix `gcloud` with
`CLOUDSDK_METRICS_REQUEST_ATTRIBUTION="agent-skills/1.0 (skill:gke-app-onboarding)"`
and append `agent-skills/1.0 (skill:gke-app-onboarding)` to `User-Agent` headers.

## Workflow

### 1. App Assessment

Before containerizing, assess the application:

-   **Language & Framework**: Identify the tech stack
-   **Dependencies**: List required libraries and external services
-   **Configuration**: How is the app configured? (env vars, config files,
    secrets)
-   **Statefulness**: Does it need persistent storage? (databases, file storage)
-   **Networking**: Port mapping and protocol (HTTP, gRPC, TCP)
-   **Health endpoints**: Does the app expose health check endpoints?

### 2. Containerization

Create a container image. A Dockerfile with a multi-stage build is recommended
for most apps — see the Go Dockerfile in
[`references/go-example.md`](./references/go-example.md) for a worked example.

**Best practices:**

-   Use multi-stage builds to keep production images small
-   Use distroless or minimal base images to reduce attack surface
-   Run as non-root user
-   Log to `stdout` and `stderr` for Cloud Logging collection

A complete worked Node.js example is provided in [`assets/`](./assets/):
[`Dockerfile`](./assets/Dockerfile) (non-root `node` user),
[`index.js`](./assets/index.js) (implements distinct `/healthz` and `/readyz`
endpoints), [`package.json`](./assets/package.json), and
[`deployment.yaml`](./assets/deployment.yaml) (hardened Deployment plus
ClusterIP Service, probes wired to `/healthz` and `/readyz`).

For applications where writing a Dockerfile is not preferred, you can use
[**Cloud Native Buildpacks**](https://buildpacks.io/) to automatically detect
the language and build a container image:

```bash
pack build <image> --builder gcr.io/buildpacks/builder:latest
```

### 3. Image Management

Build and store the container image:

```bash
# Configure Docker for Artifact Registry
gcloud auth configure-docker <REGION>-docker.pkg.dev --quiet

# Build and push
docker build -t <REGION>-docker.pkg.dev/<PROJECT>/<REPO>/<IMAGE>:<TAG> .
docker push <REGION>-docker.pkg.dev/<PROJECT>/<REPO>/<IMAGE>:<TAG>
```

**Vulnerability scanning**: Enable automatic scanning in Artifact Registry to
detect issues in base images and dependencies.

```bash
# Check scan results
gcloud artifacts docker images describe \
  <REGION>-docker.pkg.dev/<PROJECT>/<REPO>/<IMAGE>:<TAG> \
  --show-package-vulnerability \
  --quiet
```

### 4. Manifest Generation

Generate Kubernetes manifests for the application. A baseline Deployment +
ClusterIP Service manifest (probes, resource requests/limits, 2 replicas) is in
[`references/go-example.md`](./references/go-example.md).

**Checklist for manifests:**

-   Resource requests and limits set
-   Liveness and readiness probes configured
-   At least 2 replicas for production
-   Service type appropriate (ClusterIP for internal, use Gateway API for
    external)

See [`assets/deployment.yaml`](./assets/deployment.yaml) for a hardened worked
example. A production-hardened pod spec must include ALL of: `runAsNonRoot:
true`, `readOnlyRootFilesystem: true`, `allowPrivilegeEscalation: false`,
`capabilities.drop: ["ALL"]`, `seccompProfile: {type: RuntimeDefault}`,
`automountServiceAccountToken: false` (unless the pod needs the token — then say
why), resource requests, digest-pinned image, and a ClusterIP Service.

That checklist is the baseline for any pod spec produced here. For manifest work
beyond it — Gateway API routes, GCS FUSE and secret volume mounting, `subPath`
overlays, Spot VM targeting, or AI/inference serving specs — see
`gke-manifest-generation`.

### 5. Deploy

```
# MCP (preferred)
apply_k8s_manifest(parent="projects/<PROJECT>/locations/<REGION>/clusters/<CLUSTER>", yamlManifest="<manifest>")

# Verify
get_k8s_rollout_status(parent="...", resourceType="deployment", name="my-app")
get_k8s_resource(parent="...", resourceType="pod", labelSelector="app=my-app")
```

**kubectl fallback:**

```bash
kubectl apply -f manifests/
kubectl rollout status deployment/my-app
kubectl get pods -l app=my-app
```

## Golden Path Onboarding Checklist

For every production application onboarding to GKE:

1.  **Container Security**: Non-root user (`runAsNonRoot: true`), lockfile
    install, minimal/distroless base image.
2.  **Resource Requests**: Explicit CPU and memory requests (mandatory for GKE
    Autopilot).
3.  **Health Probes**: Both liveness (`livenessProbe`) and readiness
    (`readinessProbe`) probes configured.
4.  **Reliability & Availability**: At least 2 replicas and a
    `PodDisruptionBudget` (`minAvailable: 1` or `2`).
5.  **IAM & Workload Identity**: Workload Identity
    (`iam.gke.io/gcp-service-account`) instead of static service account keys.

## Next Steps

Once the application is running on GKE:

-   Configure autoscaling — see the `gke-workload-scaling` skill
-   Set up observability — see the `gke-observability` skill
-   Harden security — see the `gke-workload-security` skill
-   Configure reliability (PDBs, topology spread) — see the `gke-reliability`
    skill

## Provenance

Imported from [google/skills](https://github.com/google/skills) at commit `c157811`, path `skills/cloud/gke-app-onboarding/SKILL.md`. Licensed Apache-2.0 by its authors — the full text is in `LICENSE`.
