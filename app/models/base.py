import datetime
from typing import Any

from sqlalchemy.orm import declarative_base

Base = declarative_base()

def create_timestamp(a,b, target: Any) -> None:
    ts = datetime.datetime.now(datetime.UTC)
    target.created_at  = ts
    target.updated_at  = ts


def update_timestamp(a,b, target: Any) -> None:
    ts = datetime.datetime.now(datetime.UTC)
    target.updated_at  = ts
