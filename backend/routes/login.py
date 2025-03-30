from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from routes.signup import registered_users


router = APIRouter()

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/login")
async def login(request: LoginRequest):
    if request.email in registered_users and registered_users[request.email] == request.password:
        return {"message": "Login successful"}
    raise HTTPException(status_code=401, detail="Invalid credentials")
