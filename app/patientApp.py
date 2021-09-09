from fastapi import FastAPI
from app import patientRoutes

app = FastAPI()
app.include_router(patientRoutes.router, tags=["Patient"], prefix="/patient")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}