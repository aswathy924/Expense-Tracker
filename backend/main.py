# app/main.py
from fastapi import FastAPI
from database import create_db_and_tables
from routes import router

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(router)
