from pydantic import BaseModel, computed_field,Field


class product(BaseModel):
    price: float
    quantity: int

# computed field to calculate total price and
# return it as a property
  #  computed filed uses the @computed_field decorator to indicate that
    # the method is a computed field.

    @computed_field
 #property decorator is used to make the total_price method accessible as an attribute of the product instance
#, allowing us to access it like product_instance.total_price instead of calling it as a method.
    @property
    def total_price(self) -> float:
        return self.price * self.quantity
   

class booking(BaseModel):
    user_id:int
    room_id:int
    nights:int =Field(..., ge=1)
    rate_per_night:float

    @computed_field
    @property
    def total_amount(self) -> float:
        return self.nights * self.rate_per_night
    

bookings=booking(
    user_id=123,
    room_id=456,
    nights=3,
    rate_per_night=150.0
)

print(bookings.total_amount)


#model dump is serialization method that converts the model instance into a dictionary format
#, making it easier to work with and manipulate the data. It is useful for debugging, logging,
# or when you need to convert the model instance into a format that can be easily serialized (e.g., JSON).
print(bookings.model_dump())