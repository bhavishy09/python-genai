from pydantic import BaseModel, field_validator,model_validator

class User(BaseModel):
    username: str

    @field_validator('username')
    def username_length(cls,v):
        if len(v) < 4:
            raise ValueError('username must be at least 4 characters long')
        return v


class signup_data(BaseModel):
    password: str
    confirm_password: str

    ## model_validator is used to validate the entire model after all field validators have been executed. 
    # It allows you to perform cross-field validation, 
    #ensuring that the values of multiple fields are consistent with each other.
    # In this case, we use it to check if the password and confirm_password fields match.
    @model_validator(mode='after')
    def passwords_match(cls, values):
        password = values.get('password')
        confirm_password = values.get('confirm_password')
        if password != confirm_password:
            raise ValueError('passwords do not match')
        return values