from pydantic import BaseModel


class product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True



product_one =product(id=1,name='pc',price=8999.90,in_stock=True)


product_two =product(id=2,name='c cable',price=1999.90)