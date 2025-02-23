from pydantic import BaseModel
from datetime import datetime

class ItemBase(BaseModel):
    description: str
    name: str
    
    class Config:
        orm_mode = True


class CreateItem(ItemBase):
    class Config:
        orm_mode = True
        
class ItemResponse(ItemBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True  # Ensures compatibility with SQLAlchemy models