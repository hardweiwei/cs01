from models import Ticket
from sqlalchemy.orm import Session
from schemas import TicketCreate

def create_ticket(db: Session, ticket: TicketCreate):
    db_ticket = Ticket(**ticket.dict())
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket

def get_tickets_by_user(db: Session, user_id: str):
    return db.query(Ticket).filter(Ticket.user_id == user_id).all()

def get_ticket_by_id(db: Session, ticket_id: int):
    return db.query(Ticket).filter(Ticket.id == ticket_id).first()
