from sqlmodel import SQLModel, Field
from pydantic import field_validator, ValidationError
from typing import Optional
from datetime import date

class Expense(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    amount: float
    category: str
    date: date


    @field_validator("amount")
    def amount_must_be_positive(cls, v):
        if v < 0:
            raise ValueError("Amount must be non-negative")
        return v