---
name: api-compliance-checker
description: Design compliant API patterns for GDPR, PCI-DSS, HIPAA, SOC2, and other regulatory frameworks.
license: MIT
metadata:
  title: "api compliance checker"
  origin: "LambdaTest/agent-skills"
  upstream-path: "api-skill/api-compliance/SKILL.md"
  upstream-commit: "992638bccbc311f42c0bd8b2b3387a0d1ce6288d"
  category: "testing-qa"
  description-source: "derived from the body — upstream ships no usable description"
---

# API Compliance & Audit Skill

Design compliant API patterns for GDPR, PCI-DSS, HIPAA, SOC2, and other regulatory frameworks.

---

## GDPR Data Subject Rights Endpoints

```
POST /api/v1/privacy/data-export-request   — user requests copy of their data (Art. 20)
GET  /api/v1/privacy/data-export/{token}   — download export (after processing)
POST /api/v1/privacy/deletion-request      — right to erasure (Art. 17)
GET  /api/v1/privacy/deletion-status/{id}  — track deletion progress
POST /api/v1/privacy/rectification         — correct inaccurate personal data (Art. 16)
GET  /api/v1/privacy/consent               — get user's consent records
POST /api/v1/privacy/consent               — record/update consent
DELETE /api/v1/privacy/consent/{purpose}   — withdraw consent for a purpose
POST /api/v1/privacy/portability           — export data in machine-readable format
```

### Data Export Response
```json
{
  "request_id": "uuid",
  "status": "processing",
  "estimated_completion": "2024-01-02T00:00:00Z",
  "download_url": null,
  "expires_at": null
}
```

### Consent Record
```json
{
  "user_id": "uuid",
  "consents": [
    {
      "purpose": "marketing_email",
      "granted": true,
      "granted_at": "2023-06-01T00:00:00Z",
      "ip_address": "1.2.3.x",
      "method": "explicit_checkbox"
    },
    {
      "purpose": "analytics",
      "granted": false,
      "withdrawn_at": "2023-12-01T00:00:00Z"
    }
  ]
}
```

---

## PCI-DSS Field Masking Rules

| Field | Storage | API Response | Logs |
|-------|---------|-------------|------|
| Card number (PAN) | Tokenised only | `**** **** **** 4242` | Never log |
| CVV/CVC | Never store | Never return | Never log |
| Expiry date | Encrypted | `MM/YY` only | Never log |
| Cardholder name | Encrypted | Masked `A*** S***` | Never log |
| Bank account number | Tokenised | Last 4 digits only | Never log |

```json
{
  "payment_method": {
    "type": "card",
    "last4": "4242",
    "brand": "visa",
    "exp_month": 12,
    "exp_year": 2027,
    "token": "tok_abc123"
  }
}
```

---

## HIPAA — Health Data Endpoints

PHI (Protected Health Information) rules:
- Minimum necessary data principle: return only fields required for the stated purpose
- All endpoints carrying PHI must require MFA-backed auth
- Audit log every access to PHI — who accessed what, when

```
GET /api/v1/patients/{id}/records     — requires: HIPAA BAA, audit logged
GET /api/v1/patients/{id}/medications — minimum necessary: only active prescriptions
POST /api/v1/access-log/query         — compliance officer audit log query
```

PHI fields requiring special handling: `name`, `dob`, `ssn`, `address`, `phone`, `email`, `mrn`, `diagnosis`, `treatment`.

---

## SOC2 Audit Log Schema

Every state-changing action must produce an immutable audit log entry:

```json
{
  "id": "evt_uuid",
  "timestamp": "ISO8601",
  "actor": {
    "type": "user|service|system",
    "id": "uuid",
    "ip_address": "1.2.3.x",
    "user_agent": "Mozilla/5.0..."
  },
  "action": "user.deleted",
  "resource": {
    "type": "user",
    "id": "uuid"
  },
  "changes": {
    "before": { "status": "active" },
    "after": { "status": "deleted" }
  },
  "result": "success|failure",
  "request_id": "uuid",
  "tenant_id": "uuid"
}
```

### Audit Log Query Endpoint
```
GET /api/v1/audit-logs
Query params: actor_id, resource_type, action, from, to, result
Response: paginated list of audit events
```

**Audit log requirements:**
- Immutable: no DELETE or UPDATE on audit records
- Retention: minimum 1 year online, 7 years archived (SOC2)
- Integrity: hash-chain or WORM storage to prevent tampering
- Export: CSV/JSON export for compliance officer review

---

## Data Retention Policy Endpoints

```
GET  /api/v1/admin/retention-policies        — list policies by data type
POST /api/v1/admin/retention-policies        — define new policy
POST /api/v1/admin/retention/purge-dry-run   — preview what would be deleted
POST /api/v1/admin/retention/purge           — execute purge (requires 2-person auth)
GET  /api/v1/admin/retention/purge/{id}      — track purge job progress
```

### Retention Policy
```json
{
  "data_type": "user_activity_logs",
  "retention_days": 90,
  "action_on_expiry": "anonymise",
  "legal_hold": false,
  "regulation": "GDPR"
}
```

---

## Compliance Response Headers

```http
X-Data-Classification: public|internal|confidential|restricted
X-Data-Residency: EU
X-Retention-Policy: 90d
X-Audit-Logged: true
```

---

## Compliance Checklist

- [ ] All PII fields documented in a data map
- [ ] Data subject rights endpoints implemented
- [ ] Consent captured and stored with timestamp + method
- [ ] PCI fields tokenised — never stored in plaintext
- [ ] Audit log on every state-changing operation
- [ ] Audit logs immutable and retained per regulation
- [ ] Data residency enforced at routing layer
- [ ] Encryption at rest (AES-256) and in transit (TLS 1.2+)
- [ ] Breach notification workflow documented
- [ ] Third-party API data sharing documented (Art. 28 GDPR)


---

## After Completing the API output

Once the API output is delivered, ask the user:

"Would you like me to generate SDKs for API for this design? (yes/no)"

If the user says **yes**:
- Check if the api-sdk-generator on skill is available in the installed skills list
- If the skill **is available**:
  - Read and follow the instructions in the api-sdk-generator skill
  - Use the API output above as the input
- If the skill **is NOT available**:
  - Inform the user: "It looks like the api-sdk-generator skill isn't installed. 
    You can install it and re-run.

If the user says **no**:
- End the task here

---

## Provenance

Imported from [LambdaTest/agent-skills](https://github.com/LambdaTest/agent-skills) at commit `992638b`, path `api-skill/api-compliance/SKILL.md`. Licensed MIT — the full text is in `LICENSE`.
