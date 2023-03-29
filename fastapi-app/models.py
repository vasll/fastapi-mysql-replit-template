from pydantic import BaseModel
from typing import Optional


class Item(BaseModel):
    """ Data model representation of an item in the database. For demonstration purposes """
    id: Optional[int] = None    # Default is autoincrement
    name: str
    description: str