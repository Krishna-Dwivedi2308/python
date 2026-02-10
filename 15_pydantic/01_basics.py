from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    is_active: bool


input_data = {"id": 101, "name": "Chaicode", "is_active": True}
user = User(
    **input_data
)  # ** means the dict must be unpacked before validaing against the model
print(user)
# now this data will be validated against the User model.
# -------------------------------------------------------
# now , in the following example , we see that 101 is passed as a string but still this won't throw an error because pydantic tries to convert the string into an integer and successfully manages to do so .
# it would give an error if the values passed were difficult to convert into int implicitly. Like : "101a"


input2 = {"id": "101", "name": "Chaicode", "is_active": True}
user2 = User(**input2)
print(user2)  # no error
