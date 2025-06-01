from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class TicketBase(BaseModel):
    title: str
    description: Optional[str] = None
    user_id: str
    status: Optional[str] = "open"  # open, in_progress, closed

class TicketCreate(TicketBase):
    pass

class TicketOut(TicketBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

