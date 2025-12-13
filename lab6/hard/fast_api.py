from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uvicorn

DATABASE_URL = "sqlite:///./books.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

Base = declarative_base()

class Book(Base):
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

if db.query(Book).count() == 0:
    test_books = [
        Book(title="test book", author="Рощин Т.М"),
        Book(title="Война и мир", author="Л.Н. Толстой"),
        Book(title="Мастер и Маргарита", author="М.А. Булгаков"),
    ]
    db.add_all(test_books)
    db.commit()

app = FastAPI(title="datadabase")

@app.get("/books")
def get_books():
    books = db.query(Book).all()
    return books

@app.get("/books/{book_id}")
def get_book(book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return book

@app.get("/count")
def get_count():
    count = db.query(Book).count()
    return {"count": count}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)