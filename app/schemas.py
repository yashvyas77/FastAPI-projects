from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class PostCreate(BaseModel):
    title: str
    content: str

class PostResponse(BaseModel):
    id: UUID
    caption: str
    url: str
    file_name: str
    file_type: str
    created_at: datetime

    class Config:
        from_attributes = True