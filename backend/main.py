from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import login, signup  # Import login and signup separately

app = FastAPI()

# CORS middleware to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Adjust for frontend port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes separately
app.include_router(signup.router, prefix="/auth", tags=["Signup"])
app.include_router(login.router, prefix="/auth", tags=["Login"])
