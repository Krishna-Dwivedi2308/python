from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True


product_one = Product(id=101, name="chaicode", price=100.00)
print(product_one)

product_two = Product(id=102, name="chaicode", price=100.00, in_stock=False)
print(product_two)

product_three = Product(
    id=103
)  # this is a required field and is missing so this will throw an error
print(product_three)
