

from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker


DATABASE_URL = 'postgresql+psycopg2://postgres:postgres@localhost:5677/trading'

engine = create_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True
)


LocalSession = sessionmaker(bind=engine, autoflush=False)