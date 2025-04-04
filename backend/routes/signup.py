from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from db import users_collection

router = APIRouter()

class SignupRequest(BaseModel):
    email: str
    password: str

@router.post("/signup")
async def signup(request: SignupRequest):
  
    existing_user = await users_collection.find_one({"email": request.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    user_data = {"email": request.email, "password": request.password}
    await users_collection.insert_one(user_data)
    return {"message": "User registered successfully"}
