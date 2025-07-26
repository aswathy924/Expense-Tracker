# app/database.py
from sqlmodel import create_engine, SQLModel
from models import Expense  

postgres_url = "postgresql://postgres:postgres@localhost:5433/expense_tracker"
engine = create_engine(postgres_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
