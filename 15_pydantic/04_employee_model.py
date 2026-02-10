from typing import Optional
from pydantic import BaseModel, Field
import re


class Employees(BaseModel):
    id: int
    name: str = Field(
        ...,  # this means this field is required
        min_length=3,
        max_length=50,
        # this following part is just for providing documentaion
        description="Employee name",
        examples="Hitesh Chaudhary",
    )
    department: Optional[str] = "genera"
    salary: float = Field(
        ...,
        ge=10000,
        le=100000000,
        description="This is to enter the annual salary",
        examples=123333,
    )


class User(BaseModel):
    email: str = Field(..., regex=r"")
    phone: str = Field(..., regex=r"")
    age: int = Field(..., ge=0, le=150, description="age in years")
    discount: float = Field(..., ge=0, le=100, description="Discount Percentage")
