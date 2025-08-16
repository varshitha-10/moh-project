# Security Documentation

## Threat Model
- SQL injection, NoSQL injection, XSS, CSRF, privilege escalation, data exfiltration.
- Mitigations: parameterized queries, RBAC, approval workflow, data masking, audit logging, JWT auth.

## Compliance
- GDPR: Data masking, audit logs, user access controls.
- SOC2: Audit trails, access management, monitoring.
- HIPAA (optional): Data encryption, PII masking, access controls.

## Secure Development
- All queries parameterized.
- RBAC enforced per user/table/column.
- All access and queries logged.
- Sensitive data masked in responses.
