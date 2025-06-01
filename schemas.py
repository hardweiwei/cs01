from pydantic import BaseModel

class TicketCreate(BaseModel):
    title: str
    description: str
    user_id: str

class TicketOut(TicketCreate):
    id: int
    status: str

    class Config:
        orm_mode = True
