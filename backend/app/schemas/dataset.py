import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class DatasetCreate(BaseModel):
    name: str
    description: str | None = None


class DatasetRead(BaseModel):
    id: uuid.UUID
    name: str
    description: str | None
    source: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
