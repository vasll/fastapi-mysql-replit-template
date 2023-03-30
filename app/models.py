from pydantic import BaseModel
from typing import Optional

# This file contains classes that represent entries in a table in the database
# These models are for data validation and can be used as a parameter in API route functions to tell the endpoint how the input should be structured,
# if the input has a different structure it will raise an exception. These models can also be used as a response_model in the API routes annotations
# to tell the user what they can expect as a response

# For example, this Item class is a representation of an entry in the 'items' schema in the database
class Item(BaseModel):
    """ Data model representation of an item in the database. (For demonstration purposes) """
    id: Optional[int] = None    # Default is autoincrement
    name: str
    description: str