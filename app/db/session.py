#database engine


# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from app.core.config import get_settings

# settings = get_settings()
# engine = create_engine(
#         settings.database_url,
#         echo=settings.debug,
# )

# SessionLocal = sessionmaker(
#     autocommit=False,
#     autoflush=False,
#     bind=engine,
# )

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import (
      create_async_engine,
      AsyncSession,
      async_sessionmaker,
)

from app.core.config import get_settings

settings = get_settings()

engine = create_async_engine(
    settings.database_url,
    echo=settings.debug,
    pool_pre_ping=True,
)

SessionLocal = async_sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False 
)

async def get_db()-> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session

