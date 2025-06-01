from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import Base, Ticket
from database import engine, SessionLocal
from schemas import TicketCreate, TicketOut
from crud import create_ticket, get_tickets_by_user, get_ticket_by_id

Base.metadata.create_all(bind=engine)

app = FastAPI()

# 允许跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/tickets/", response_model=TicketOut)
def create(ticket: TicketCreate):
    db = SessionLocal()
    db_ticket = create_ticket(db, ticket)
    db.close()
    return db_ticket

@app.get("/tickets/", response_model=list[TicketOut])
def list(user_id: str):
    db = SessionLocal()
    tickets = get_tickets_by_user(db, user_id)
    db.close()
    return tickets

@app.get("/tickets/{ticket_id}", response_model=TicketOut)
def detail(ticket_id: int):
    db = SessionLocal()
    ticket = get_ticket_by_id(db, ticket_id)
    db.close()
    if ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket
