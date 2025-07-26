# app/routes.py
from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from models import Expense
from database import engine

router = APIRouter()

@router.post("/expenses/")
def add_expense(expense: Expense):
    with Session(engine) as session:
        session.add(expense)
        session.commit()
        session.refresh(expense)
        return expense

@router.get("/expenses/")
def get_expenses():
    with Session(engine) as session:
        return session.exec(select(Expense)).all()
    
@router.put("/expenses/{expense_id}")
def update_expense(expense_id: int, updated_expense: Expense):
    with Session(engine) as session:
        expense = session.get(Expense, expense_id)
        if not expense:
            raise HTTPException(status_code=404, detail="Expense not found")

        # Update fields
        expense.title = updated_expense.title
        expense.amount = updated_expense.amount
        expense.category = updated_expense.category
        expense.date = updated_expense.date

        session.add(expense)
        session.commit()
        session.refresh(expense)
        return expense

@router.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):
    with Session(engine) as session:
        expense = session.get(Expense, expense_id)
        if not expense:
            raise HTTPException(status_code=404, detail="Expense not found")

        session.delete(expense)
        session.commit()
        return {"message": f"Expense with ID {expense_id} deleted successfully"}