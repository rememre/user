from typing import Annotated, Dict, Literal

from fastapi import APIRouter, Body, Depends, Path, status
from sqlalchemy.orm import Session

from ..dependencies import get_db
from ..exceptions import SomethingWentWrong, Unauthorized
from ..models.user import UserModel
from ..schemas.user import UserForm, UserSchema
from ..services.user import UserService

router = APIRouter(prefix="/users")


@router.post("", status_code=status.HTTP_201_CREATED, response_model=Dict[Literal['data'], UserSchema])
def create_user(user_form: Annotated[UserForm, Body()], db: Annotated[Session, Depends(get_db)]):
    data: UserModel = UserService(db).create(user_form)
    if not data:
        raise SomethingWentWrong
    return {'data': data}


@router.get("/{user_id}", status_code=status.HTTP_200_OK, response_model=Dict[Literal['data'], UserSchema])
def get_user_by_id(user_id: Annotated[str, Path()], db: Annotated[Session, Depends(get_db)]):
    data = UserService(db).get(user_id)
    if not data:
        return Unauthorized
    return {'data': data}
