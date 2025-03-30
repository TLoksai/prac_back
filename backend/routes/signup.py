from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict

router = APIRouter()

# Temporary storage for registered users
registered_users: Dict[str, str] = {}  # {email: password}

class SignupRequest(BaseModel):
    name: str
    email: str
    password: str
    confirm_password: str

@router.post("/signup")
async def signup(request: SignupRequest):
    if request.email in registered_users:
        raise HTTPException(status_code=400, detail="Email already registered")

    if request.password != request.confirm_password:
        raise HTTPException(status_code=400, detail="Passwords do not match")

    # Store user credentials
    registered_users[request.email] = request.password
    return {"message": "Signup successful"}
