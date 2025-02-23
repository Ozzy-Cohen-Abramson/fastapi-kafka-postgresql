# from pydantic import BaseModel, Field

# class ItemSchema(BaseModel):
#     name: str = Field(min_length=3, max_length=30)
#     description: str = Field(min_length=3, max_length=300)

from utils.database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text


class ItemSchema(Base):
    __tablename__ = "items"

    id = Column(Integer,primary_key=True,nullable=False)
    name = Column(String,nullable=False)
    description = Column(String,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))