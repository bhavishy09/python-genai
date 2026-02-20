from pydantic import BaseModel,field_validator,model_validator
from datetime import datetime

class Person(BaseModel):
    first_name:str
    last_name:str


    @field_validator('first_name','last_name')
    def names_must_be_capatilize(cls,v):
        if not v.istitle():
            raise ValueError('names must be capitalized')
        return v
    


# names = Person(
#         first_name='John',
#         last_name='Doe'
        
#         )
# print(names)
    

class User(BaseModel):
    email:str

    @field_validator('email') 
    def normalize_email(cls,v):
        return v.lower().strip()


class product(BaseModel):
  
    price:str
# we use mode='before' to specify that the validator should be applied before any other validation checks are performed on the price field.
    @field_validator('price',mode='before')
    def parse_price(cls,v):
        if instance(v,str):
            return float(v.replace('$',''))
        return v
    

class daterange(BaseModel):
    start_date:datetime
    end_date:datetime

    @model_validator(mode='after')
    def vaildate_date_range(cls,values):
        start_date = values.get('start_date')
        end_date = values.get('end_date')
        if start_date and end_date and start_date > end_date:
            raise ValueError('start date must be before end date')
        return values
