from fastapi import FastAPI
from routes import signup, login

app = FastAPI()

# Routes
app.include_router(signup.router, prefix="/auth")
app.include_router(login.router, prefix="/auth")
