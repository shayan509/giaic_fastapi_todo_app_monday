from sqlmodel import SQLModel, create_engine, Session
import os

# Use SQLite for local development
DATABASE_URL = "sqlite:///./todo.db"

engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False}  # Required for SQLite
)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session