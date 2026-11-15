
from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="SecureBank API",
    version="0.1.0",
    description="SecureBank educational banking API",
)


@app.get("/health")
def health_check():
    return {"status": "ok", "service": "securebank-api"}


@app.get("/api/v1/accounts")
def list_accounts():
    raise HTTPException(
        status_code=501,
        detail="Accounts API is not implemented yet",
    )

