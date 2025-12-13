from sqlalchemy import  Column, Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
   
postgresql_database = "postgresql://postgres:856156@localhost/test"

engine = create_engine(postgresql_database)
Session = sessionmaker(bind=engine)

class Base(DeclarativeBase): pass

class Game(Base):
    __tablename__ = "games"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    size = Column(Integer,)
  
Base.metadata.create_all(bind=engine)

session = Session()
games = [
    Game(title="The Witcher 3", size=50000),
    Game(title="Cyberpunk 2077", size=70000),
    Game(title="Red Dead Redemption 2", size=150000)
]

session.add_all(games)
session.commit()
session.close()

print("3 games added")
