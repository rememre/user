import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Postgres:
    user     = os.getenv("POSTGRES_USER","postgres")
    password = os.getenv("POSTGRES_PASSWORD","password")
    host     = os.getenv("POSTGRES_HOST", "localhost")
    port     = os.getenv("POSTGRES_PORT", 5432)
    database = os.getenv("POSTGRES_DB", "postgres")
    
    @property
    def url(self):
        return f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"

engine = create_engine(Postgres().url, connect_args={})
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
