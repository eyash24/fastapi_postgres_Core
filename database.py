# from sqlalchemy import create_engine
# from sqlalchemy.orm import DeclarativeBase, sessionmaker

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from config import settings


'''
# SQLite database settings
SQLALCHEMY_DATABASE_URL = 'sqlite+aiosqlite:///./blog.db' # SQLite database 
engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)
'''
# SessionLocal = sessionmaker(
#     autocommit=False, 
#     autoflush = False,
#     bind=engine
# )


# Postgres
engine = create_async_engine(
    settings.database_url
)

AsycnSessionLocal = async_sessionmaker(
    engine,
    class_ = AsyncSession,
    expire_on_commit=False,
)

class Base(DeclarativeBase):
    pass


async def get_db():
    async with AsycnSessionLocal() as session:
        yield session

