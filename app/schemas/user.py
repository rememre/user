from string import ascii_lowercase, ascii_uppercase, digits

from pydantic import BaseModel, EmailStr, field_validator

from ..constants import SPECIAL


class UserForm(BaseModel):
    username: str
    email: EmailStr
    password: str

    @classmethod
    def __contains_lowercase(cls, password:str):
        return any(c in password for c in ascii_lowercase)

    @classmethod
    def __contains_uppercase(cls, password:str):
        return any(c in password for c in ascii_uppercase)

    @classmethod
    def __contains_digits(cls, password:str):
        return any(c in password for c in digits)

    @classmethod
    def __contains_special(cls, password:str):
        return any(c in password for c in SPECIAL)

    @field_validator('password')
    def valid_password(cls, v):
        if (
            cls.__contains_special(v)
            and cls.__contains_digits(v)
            and cls.__contains_lowercase(v)
            and cls.__contains_uppercase(v)
        ):
            return v
        else:
            raise ValueError('Password must contain at least one lowercase letter, one uppercase letter, one number and on special symbol')



class UserSchema(BaseModel):
    id: str
    username: str
    email: EmailStr

    class Config:
        from_attributes = True

