# Security & Secret Management

This document explains how sensitive data is handled in this project. Hiring managers and reviewers: this section demonstrates security-conscious QA engineering practices.

## What is kept secret

| Data | Storage |
|---|---|
| API base URLs | GitHub Secrets + local `.env` |
| API keys | GitHub Secrets + local `.env` |
| Auth tokens | GitHub Secrets (never hardcoded) |
| Test user credentials | GitHub Secrets + local `.env` |
| Postman environment values | Local only — never committed |

## Local development

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
2. Fill in your real values in `.env`.
3. The `.env` file is listed in `.gitignore` and will never be committed.

## CI/CD (GitHub Actions)

All secrets are stored in **GitHub Repository Secrets**:
- Settings → Secrets and variables → Actions → New repository secret

They are injected into the workflow as environment variables:
```yaml
env:
  BASE_URL: ${{ secrets.BASE_URL }}
  API_KEY: ${{ secrets.API_KEY }}
  AUTH_TOKEN: ${{ secrets.AUTH_TOKEN }}
```

GitHub masks secret values in all workflow logs automatically.

## Postman collections

- Only `environment.example.json` (with placeholder values) is committed.
- Real environment files with live tokens stay local and are excluded by `.gitignore`.
- Newman in CI reads secrets from environment variables, not from committed files.

## What NOT to do

- Never hardcode credentials in test files
- Never commit `.env` files
- Never log or print secret values in test output
- Never use production credentials for testing — always use dedicated test accounts
