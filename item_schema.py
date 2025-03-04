from pydantic import BaseModel, Field

class ItemSchema(BaseModel):
    name: str = Field(min_length=3, max_length=30)
    description: str = Field(min_length=3, max_length=300)