from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import Base, Ticket
from database import engine, SessionLocal
from schemas import TicketCreate, TicketOut
from crud import create_ticket, get_tickets_by_user, get_ticket_by_id
from typing import List

# 创建数据库表
Base.metadata.create_all(bind=engine)

app = FastAPI()

# 允许跨域访问
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 新建工单
@app.post("/tickets/", response_model=TicketOut)
def create(ticket: TicketCreate):
    db = SessionLocal()
    try:
        db_ticket = create_ticket(db, ticket)
        return db_ticket
    finally:
        db.close()

# 查询某个用户的工单列表
@app.get("/tickets/", response_model=List[TicketOut])
def list(user_id: str):
    db = SessionLocal()
    try:
        tickets = get_tickets_by_user(db, user_id)
        return tickets
    finally:
        db.close()

# 查询单个工单详情
@app.get("/tickets/{ticket_id}", response_model=TicketOut)
def detail(ticket_id: int):
    db = SessionLocal()
    try:
        ticket = get_ticket_by_id(db, ticket_id)
        if ticket is None:
            raise HTTPException(status_code=404, detail="Ticket not found")
        return ticket
    finally:
        db.close()

