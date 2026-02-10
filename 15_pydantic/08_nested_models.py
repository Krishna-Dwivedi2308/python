from typing import List, Optional
from pydantic import BaseModel


class Address(BaseModel):
    street: str
    city: str
    postal_code: str


class User(BaseModel):
    id: int
    name: str
    address: Address  # this ingerits the definitions from the Address model(class)


# Method-1 of usage
address = Address(street="123", city="Jaipur", postal_code="100001")

user = User(id=1, name="Hitesh", address=address)
# Method-2 of usage:
user_data = {
    "id": 1,
    "name": "Krishna",
    "address": {"street": "123", "city": "Jaipur", "postal_code": "100001"},
}
user2 = User(**user_data)
print(user2.address)
