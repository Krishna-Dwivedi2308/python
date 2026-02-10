from typing import List, Dict, Optional
from pydantic import BaseModel


class Cart(BaseModel):
    user_id: int
    items: List[str]  # List comes from typing and str comes from pydantic
    quantities: Dict[str, int]  # Dict comes from typing and int comes from pydantic


class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None


cart_data = {
    "user_id": 123,
    "items": ["Laptop", "Mouse", "Keyboard"],
    "quantities": {"Laptop": 1, "mouse": 2, "Keyboard": 3},
}
cart = Cart(**cart_data)
