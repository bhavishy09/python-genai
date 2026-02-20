from pydantic import Base_model, Field
from typing import Optional
import re

class emoyee(Base_model):
    id: int
    name: str = Field(

        ...,
        min_length=3,
        max_length=50,
        description="employee's name",
        examples="bhavishya katariya"

    )
    department: Optional[str] = 'general'
    salary : float = Field(

        ...,
        ge=10000,
        le=1000000,
        description="annual  salary in rupees"

    )

class User(Base_model):
    id: int
    name: str
    email: str = Field(
        ...,
     regex=r'',
     description="User's email address"
     )
    age: Optional[int] = Field(
       ...,
       ge=0,
       le=100,
       description="age in years"

    )

    discount: Optional[float] = Field(
        
        ...,
        ge=0.0,
        le=100.0,
        description="discount percentage"

    )