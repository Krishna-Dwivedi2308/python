from pydantic import BaseModel, field_validator, model_validator


class User(BaseModel):
    username: str

    @field_validator("username")
    def username_length(
        cls, v
    ):  # cls is the class being passed to it , and then v is the value that is being passed to validate
        if len(v) < 4:
            raise ValueError("Username must be at least 4 char")
        return v  # this step is important , if you don't return the value , it won't get passed further to the next validations etc


class SignupData(BaseModel):
    password: str
    confirmpassword: str

    @model_validator(mode="after")
    def password_match(cls, values):
        try:
            if values.password != values.confirmpassword:
                raise ValueError("Password do not match")
        except Exception as e:
            print(e)
        return values


password = input("Enter the password")
cpass = input("Confirm the password")
user = SignupData(**{"password": password, "confirmpassword": cpass})
