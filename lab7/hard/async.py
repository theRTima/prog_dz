import asyncio
import databases
import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, Float, MetaData

DATABASE_URL = "sqlite:///async_games.db"
database = databases.Database(DATABASE_URL)
metadata = MetaData()

games = Table(
    "async_games",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String, nullable=False),
    Column("genre", String),
    Column("release_year", Integer),
    Column("price", Float)
)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

class AsyncManager:
    async def connect(self):
        await database.connect()
    async def disconnect(self):
        await database.disconnect()
    async def create_game(self, title, genre, release_year, price):
        query = games.insert().values(title=title, genre=genre, release_year=release_year, price=price)
        return await database.execute(query)
    async def get_all_games(self):
        query = games.select()
        return await database.fetch_all(query)

async def main():
    manager = AsyncManager()
    await manager.connect()
    await manager.create_game("Dark Souls III", "RPG", 2016, 60)
    all_games = await manager.get_all_games()
    for game in all_games:
        print(game["id"], game["title"], game["price"])
    await manager.disconnect()


asyncio.run(main())