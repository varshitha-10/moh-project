# User Guide: multi-db-nl-query-engine

## 1. Setup & Start

### Prerequisites
- Docker & Docker Compose
- Node.js (for frontend dev)
- Python 3.11+ (for backend dev)

### Start All Services
```sh
docker-compose up --build
```
- Frontend: http://localhost:3000
- Backend (REST): http://localhost:8000
- GraphQL: http://localhost:8000/graphql
- API Docs: http://localhost:8000/docs

---

## 2. Authentication
- Open the frontend in your browser.
- Login with your username and password (roles: admin, user, etc).
- Role-based access controls what you can see and do.

---

## 3. Natural Language Querying
- Type your question in the input box (e.g., "Show me revenue trends and top products last 6 months").
- The system:
  - Understands multi-intent queries
  - Handles time phrases ("last 6 months")
  - Resolves ambiguities (asks for clarification if needed)
  - Maintains context (remembers your last query)
- Results are shown in tables and charts.
- Query explanation (how SQL/Mongo was generated) is shown below the input.

---

## 4. Real-Time Monitoring Dashboard
- See active queries, schema changes, and logs in the dashboard.
- Schema changes (e.g., new columns/tables) are detected automatically.
- All queries and responses are audit-logged.

---

## 5. REST API Usage
- Send POST requests to `/ask` endpoint:
```json
{
  "question": "Show all customers"
}
```
- Response includes results and query explanation.
- Use `/docs` for interactive API testing (Swagger UI).

---

## 6. GraphQL API Usage
- Access `/graphql` for GraphiQL playground.
- Example query:
```graphql
query { hello }
```
- Extend schema for advanced analytics as needed.

---

## 7. Security Features
- SQL injection is prevented (parameterized queries).
- Role-based access per user/table/column.
- Expensive queries are flagged for admin approval.
- Sensitive data (email, phone) is masked in results.
- All actions are audit-logged for compliance.

---

## 8. Schema Evolution
- The system adapts to live DB schema changes (renames, splits, new fields/collections).
- Previous queries remain compatible (backward compatibility).

---

## 9. Business Intelligence & Analytics
- Usage analytics, anomaly detection, and compliance reporting are available in the BI dashboard.
- Export audit logs and reports as needed.

---

## 10. Testing & Performance
- Run backend tests: `pytest backend/tests`
- Run frontend tests: `npx playwright test frontend/tests`
- Performance: Handles 1000+ concurrent queries (see PERFORMANCE.md)

---

## 11. Advanced/Dev Usage
- See `DEPLOYMENT.md` for Kubernetes and advanced deployment.
- See `API_DOCS.md`, `SECURITY.md`, `PERFORMANCE.md`, `BI.md` for more details.

---

## 12. Troubleshooting
- If you see errors, check logs in the dashboard or backend console.
- For NLP, ensure you run: `python -m spacy download en_core_web_trf`
- For Redis, ensure the service is running (see docker-compose).
