# nested models
from typing import List, Optional
from pydantic import BaseModel



#example 1 {  user-> address}
class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

# nested model  -> user model has address as a field which is of type Address
# This allows us to represent complex data structures where a user can have an associated address with multiple fields.
class user(BaseModel):
    id: int
    name: str
    
    
    address: Address



address=Address(

    street="123 Main St",
    city="New York",
    state="NY",
    zip_code="10001"

)

user_data = {
    "id": 1,
    "name": "John Doe",
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "state": "NY",
        "zip_code": "10001"
    }
}

users= user(**user_data)
print(users)


