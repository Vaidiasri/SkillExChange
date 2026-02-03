# Now we make  the database connection for our app
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Database URL configuration from .env
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./test.db")

# Enable echo only in development
ECHO_SQL = os.getenv("ECHO_SQL", "False").lower() == "true"

# Create async engine with best practices
engine = create_async_engine(
    DATABASE_URL,
    echo=ECHO_SQL,
    future=True,
    pool_pre_ping=True,  # Verify connections before using them
    pool_recycle=3600,   # Recycle connections every hour
)

# Declarative base for models
class Base(DeclarativeBase):
    pass

# Create async session factory with best practices
AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
    autocommit=False,
)

# Dependency to get database session
async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        except Exception as e:
            await session.rollback()
            raise
        finally:
            await session.close()

# Create all tables on startup
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)