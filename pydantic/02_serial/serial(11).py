# serialzation is process converting complex data structures into a format 
#that can be easily stored or transmitted, such as JSON or XML.


#we take pydantic model convert to easiy storable format like json or dict,
# this process is called serialization.


from pydantic import BaseModel,ConfigDict
from typing import List, Optional

from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool
    address: Address
    created_at: datetime
    tages: List[str] = []

    model_config=ConfigDict(
        json_encoders={
            datetime: lambda v: v.strftime('%d-%m-%y %H-%M-%S')
        }
    )



user= User(
    id=1,
    name="John Doe",
    email="h@hitesh.ai",
    address=Address(
        street="123 Main St",
        city="New York",
        state="NY",
        zip_code="10001"
    ),
    is_active=True,
    created_at=datetime.now(),
    tages=["admin","user"]
)

print(user)

print("="*20)

#model dump is a method provided by pydantic models that allows you to convert the model instance into a dictionary 
# representation.
pydict=user.model_dump()
print(pydict)

# almoest same but typeof is json string
json_str=user.model_dump_json()
print("="*50)
print(json_str)