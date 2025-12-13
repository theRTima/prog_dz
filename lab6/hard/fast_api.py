from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session, Mapped, mapped_column
from fastapi import FastAPI, HTTPException, Depends
import uvicorn

postgresql_database = "postgresql://postgres:856156@localhost/test"
engine = create_engine(postgresql_database)
SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):pass

class Game(Base):
    __tablename__ = "games"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String)
    size: Mapped[int]

Base.metadata.create_all(bind=engine)

def init_db():
    session = SessionLocal()
    if session.query(Game).count() == 0:
        games = [
            Game(title="The Witcher 3", size=50000),
            Game(title="Cyberpunk 2077", size=70000),
            Game(title="Red Dead Redemption 2", size=150000)
        ]
        session.add_all(games)
        session.commit()
        print("3 игры добавлены")
    session.close()

init_db()

app = FastAPI(title="test api")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/games")
def get_games(db: Session = Depends(get_db)):
    games = db.query(Game).all()
    return games

@app.get("/games/count")
def get_games_count(db: Session = Depends(get_db)):
    count = db.query(Game).count()
    return {"count": count}

@app.get("/games/{game_id}")
def get_game(game_id: int, db: Session = Depends(get_db)):
    game = db.query(Game).filter(Game.id == game_id).first()
    if not game:
        raise HTTPException(status_code=404, detail="no game")
    return game

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)