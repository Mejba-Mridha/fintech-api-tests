"""
tests/schemas.py
────────────────
JSON Schema definitions for all API response objects.
Used with jsonschema.validate() in test assertions.

Validating the schema — not just the status code — is what separates
a senior QA from a junior one. It proves the API contract is intact.
"""


# ─── Auth ─────────────────────────────────────────────────────────────────────

LOGIN_RESPONSE_SCHEMA = {
    "type": "object",
    "required": ["access_token", "token_type", "expires_in"],
    "properties": {
        "access_token": {"type": "string", "minLength": 10},
        "token_type": {"type": "string", "enum": ["Bearer", "bearer"]},
        "expires_in": {"type": "integer", "minimum": 1},
        "refresh_token": {"type": "string"},
    },
    "additionalProperties": True,
}


# ─── User ─────────────────────────────────────────────────────────────────────

USER_SCHEMA = {
    "type": "object",
    "required": ["id", "email", "first_name", "last_name", "created_at"],
    "properties": {
        "id": {"type": "string"},
        "email": {"type": "string", "format": "email"},
        "first_name": {"type": "string"},
        "last_name": {"type": "string"},
        "phone": {"type": ["string", "null"]},
        "created_at": {"type": "string"},
        "status": {"type": "string", "enum": ["active", "inactive", "suspended"]},
    },
    "additionalProperties": True,
}


# ─── Account ──────────────────────────────────────────────────────────────────

ACCOUNT_SCHEMA = {
    "type": "object",
    "required": ["id", "user_id", "currency", "balance", "status", "created_at"],
    "properties": {
        "id": {"type": "string"},
        "user_id": {"type": "string"},
        "account_number": {"type": "string"},
        "currency": {"type": "string", "minLength": 3, "maxLength": 3},
        "balance": {"type": "number", "minimum": 0},
        "status": {"type": "string", "enum": ["active", "frozen", "closed"]},
        "created_at": {"type": "string"},
    },
    "additionalProperties": True,
}

ACCOUNT_BALANCE_SCHEMA = {
    "type": "object",
    "required": ["account_id", "available_balance", "currency"],
    "properties": {
        "account_id": {"type": "string"},
        "available_balance": {"type": "number"},
        "pending_balance": {"type": "number"},
        "currency": {"type": "string"},
        "last_updated": {"type": "string"},
    },
    "additionalProperties": True,
}


# ─── Transaction ──────────────────────────────────────────────────────────────

TRANSACTION_SCHEMA = {
    "type": "object",
    "required": ["id", "account_id", "amount", "currency", "type", "status", "created_at"],
    "properties": {
        "id": {"type": "string"},
        "account_id": {"type": "string"},
        "amount": {"type": "number"},
        "currency": {"type": "string"},
        "type": {"type": "string", "enum": ["credit", "debit", "transfer", "fee", "refund"]},
        "status": {"type": "string", "enum": ["pending", "completed", "failed", "reversed"]},
        "description": {"type": ["string", "null"]},
        "reference": {"type": ["string", "null"]},
        "created_at": {"type": "string"},
    },
    "additionalProperties": True,
}

TRANSACTION_LIST_SCHEMA = {
    "type": "object",
    "required": ["data", "total", "page", "per_page"],
    "properties": {
        "data": {
            "type": "array",
            "items": TRANSACTION_SCHEMA,
        },
        "total": {"type": "integer", "minimum": 0},
        "page": {"type": "integer", "minimum": 1},
        "per_page": {"type": "integer", "minimum": 1},
    },
}


# ─── Payment ──────────────────────────────────────────────────────────────────

PAYMENT_SCHEMA = {
    "type": "object",
    "required": ["id", "amount", "currency", "status", "created_at"],
    "properties": {
        "id": {"type": "string"},
        "amount": {"type": "number", "minimum": 0.01},
        "currency": {"type": "string"},
        "source_account_id": {"type": "string"},
        "destination_account_id": {"type": "string"},
        "status": {
            "type": "string",
            "enum": ["initiated", "pending", "processing", "completed", "failed", "cancelled"],
        },
        "description": {"type": ["string", "null"]},
        "reference": {"type": ["string", "null"]},
        "created_at": {"type": "string"},
        "completed_at": {"type": ["string", "null"]},
    },
    "additionalProperties": True,
}


# ─── Error ────────────────────────────────────────────────────────────────────

ERROR_RESPONSE_SCHEMA = {
    "type": "object",
    "required": ["error"],
    "properties": {
        "error": {
            "type": "object",
            "required": ["code", "message"],
            "properties": {
                "code": {"type": "string"},
                "message": {"type": "string"},
                "details": {"type": ["string", "null", "object"]},
            },
        }
    },
    "additionalProperties": True,
}
