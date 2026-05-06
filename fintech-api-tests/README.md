# 🏦 Fintech API Test Automation Suite

> A production-grade API testing portfolio project simulating a neobank/payments platform.
> Built with Python · Pytest · Newman · k6 · GitHub Actions · Allure Reports.

[![CI Pipeline](https://github.com/YOUR_USERNAME/fintech-api-tests/actions/workflows/ci.yml/badge.svg)](https://github.com/YOUR_USERNAME/fintech-api-tests/actions/workflows/ci.yml)
[![Allure Report](https://img.shields.io/badge/Allure-Report-orange)](https://YOUR_USERNAME.github.io/fintech-api-tests/)
[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📋 Project Overview

This project demonstrates end-to-end API test automation for a fintech banking platform covering:

| Domain | Coverage |
|---|---|
| Authentication | Login, logout, token refresh, invalid credentials |
| User Accounts | Create, read, balance checks, status validation |
| Transactions | List, filter, pagination, schema validation |
| Payments | Initiate, status tracking, cancellation, error handling |
| Performance | Load testing, stress testing, response time thresholds |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| **Pytest + Requests** | Functional API test framework |
| **jsonschema / pydantic** | JSON contract / schema validation |
| **Newman (Postman CLI)** | Runs Postman collections in CI |
| **k6** | Performance and load testing |
| **Allure** | Rich HTML test reports |
| **GitHub Actions** | CI/CD pipeline — runs on every push and PR |
| **python-dotenv** | Local secret management |
| **Faker** | Realistic test data generation |

---

## 📁 Project Structure

```
fintech-api-tests/
├── tests/
│   ├── conftest.py          # Shared fixtures (api_client, auth_token, fake data)
│   ├── schemas.py           # JSON Schema definitions for contract testing
│   ├── test_health.py       # Smoke tests — API liveness & readiness
│   ├── test_auth.py         # Authentication tests
│   ├── test_accounts.py     # Account management tests
│   ├── test_transactions.py # Transaction history tests
│   └── test_payments.py     # Payment processing tests
├── postman/
│   ├── collection.json              # Postman collection (sanitized)
│   ├── environment.example.json     # Environment template (no real secrets)
│   └── reports/                     # Newman HTML reports
├── performance/
│   ├── load_test.js         # k6 load test (normal traffic simulation)
│   └── stress_test.js       # k6 stress test (breaking point)
├── config/
│   ├── settings.py          # Central config — loads from .env / GitHub Secrets
│   └── endpoints.py         # All API endpoint paths as constants
├── .github/
│   └── workflows/
│       ├── ci.yml           # Main CI pipeline (push / PR)
│       └── nightly.yml      # Nightly regression + performance run
├── docs/
│   └── SECURITY.md          # Secret management documentation
├── .env.example             # Environment variable template
├── .gitignore               # Excludes .env, real tokens, caches
├── pytest.ini               # Pytest configuration & markers
└── requirements.txt         # Python dependencies
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- Node.js 18+ (for Newman)
- k6 ([install guide](https://k6.io/docs/getting-started/installation/))

### Local Setup

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/fintech-api-tests.git
cd fintech-api-tests

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment
cp .env.example .env
# Edit .env with your real API credentials

# 5. Install Newman
npm install -g newman newman-reporter-htmlextra
```

### Running Tests

```bash
# Run all tests
pytest

# Run smoke tests only (fast, ~30 seconds)
pytest -m smoke

# Run a specific module
pytest tests/test_payments.py -v

# Run with markers
pytest -m "regression and not slow"

# Run in parallel (4 workers)
pytest -n 4

# Generate Allure report
pytest --alluredir=reports/allure-results
allure serve reports/allure-results
```

### Running Newman (Postman)

```bash
newman run postman/collection.json \
  --env-var "base_url=$BASE_URL" \
  --env-var "api_key=$API_KEY" \
  --reporters htmlextra \
  --reporter-htmlextra-export postman/reports/report.html
```

### Running k6 Performance Tests

```bash
# Load test (100 virtual users, 5 minutes)
k6 run performance/load_test.js

# Stress test
k6 run performance/stress_test.js
```

---

## 📊 Test Coverage

| Module | Happy Path | Negative | Schema | Total |
|---|---|---|---|---|
| Health | 4 | 0 | 1 | 4 |
| Auth | 5 | 6 | 2 | 13 |
| Accounts | 6 | 4 | 2 | 12 |
| Transactions | 5 | 3 | 2 | 10 |
| Payments | 6 | 7 | 2 | 15 |
| **Total** | **26** | **20** | **9** | **54** |

---

## 🔐 Security

All sensitive values (API keys, tokens, credentials) are managed via:
- **GitHub Secrets** in CI/CD
- **Local `.env` file** (git-ignored) for development

See [docs/SECURITY.md](docs/SECURITY.md) for full details.

---

## 📈 CI/CD Pipeline

Every push and pull request triggers:

1. **Setup** — Python 3.11 + Node.js 18 environment
2. **Install** — pip + Newman
3. **Pytest** — Full functional test suite with Allure results
4. **Newman** — Postman collection runner
5. **k6** — Performance tests (nightly only)
6. **Allure Publish** — Report deployed to GitHub Pages

---

## 👤 Author

**Your Name** · QA Automation Engineer  
[LinkedIn](https://linkedin.com/in/yourprofile) · [GitHub](https://github.com/YOUR_USERNAME)
