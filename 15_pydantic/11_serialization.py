from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime


class Address(BaseModel):
    street: str
    city: str
    zip_code: str


class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    created_At: datetime
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(  # this is extremely important to parse datetime
        json_encoders={datetime: lambda v: v.strftime("%d-%m-%Y %H:%M:%S")}
    )


user = User(
    id=1,
    name="Hitesh",
    email="hiyesh@ai",
    created_At=datetime(2024, 3, 15, 14, 30),
    address=Address(street="something", city="something", zip_code="111111"),
    is_active=False,
    tags=["premium", "general"],
)
print(user)
# id=1 name='Hitesh' email='hiyesh@ai' is_active=False created_At=datetime.datetime(2024, 3, 15, 14, 30) address=Address(street='something', city='something', zip_code='111111') tags=['premium', 'general']
print("=" * 30)
python_dict = (
    user.model_dump()
)  # this model dump converted the nested address object(submodels) into a dictionary that is directly usable
print(python_dict)
# {'id': 1, 'name': 'Hitesh', 'email': 'hiyesh@ai', 'is_active': False, 'created_At': datetime.datetime(2024, 3, 15, 14, 30), 'address': {'street': 'something', 'city': 'something', 'zip_code': '111111'}, 'tags': ['premium', 'general']}
print("-" * 30)
print(user.model_dump_json())  # this will convert into json-encoded string

# {"id":1,"name":"Hitesh","email":"hiyesh@ai","is_active":false,"created_At":"15-03-2024 14:30:00","address":{"street":"something","city":"something","zip_code":"111111"},"tags":["premium","general"]}
