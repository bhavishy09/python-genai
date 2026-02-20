from pydantic import BaseModel
from typing import Optional,List,Dict

class Carts(BaseModel):
    user_id: int
    items: List[str]
    quantity: dict[str,int]



class Blogpost(BaseModel):
        title: str
        content: str
        image_url: Optional[str] = None  # Optional field with default value None

    
    
car_data = {

        "user_id": 123,
        "items": ["laptop","mouse","keyboard"],
        "quantity": {"laptop": 1, "mouse": 2, "keyboard": 1}      
            
    }

carts = Carts(**car_data)