# optional nested model
from typing import List, Optional,Union
from pydantic import BaseModel


class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class comapnay(BaseModel):
    name:str
    address:Optional[Address]=None

class employee(BaseModel):
    id: int
    name: str
    company: Optional[comapnay] = None

#mixed data type
class TextContent(BaseModel):
    text: str="text"
    content:str

class ImageContent(BaseModel):
    url: str
    type:str="image"
    alt_text: Optional[str] = None

class article(BaseModel):
    title: str
    content: List[Union[TextContent , ImageContent]]

# deeply nested model


class Country(BaseModel):
    name: str
    code: str

class state(BaseModel):
    name: str
    country: Country

class city(BaseModel):
    name: str
    state: state

class address(BaseModel):
    street: str
    city: city
    postal_code: str

class organisation(BaseModel):
    name: str
    headquarters: address
    branches:List[address] =[]






