from pydantic import BaseModel


class Token(BaseModel):
    id: str
    username: str
    email: str
