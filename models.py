from sqlalchemy import Column, Integer, String
from database import Base

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    description = Column(String(255))
    status = Column(String(20), default="已提交")
    user_id = Column(String(50))
