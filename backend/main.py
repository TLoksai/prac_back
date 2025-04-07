from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import login, signup
import uvicorn


app = FastAPI()

# CORS middleware to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(signup.router, prefix="/auth", tags=["Signup"])
app.include_router(login.router, prefix="/auth", tags=["Login"])


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)