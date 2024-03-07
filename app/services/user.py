from uuid import uuid4

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from ..config.logger import logger
from ..exceptions import BadRequest
from ..models.user import UserModel
from ..models.user_pass import UserPass
from ..schemas.user import UserForm
from ..services.auth import AuthService


class UserService:
    def __init__(self, db: Session) -> None:
        self.__db = db

    def __generate_id(self, prefix: str = "usr") -> str:
        uid = str(uuid4()).replace("-","")
        return prefix + "_" + uid

    def _test(self) -> bool:
        try:
            self.__db.query(UserModel).count()
            return True
        except Exception as e:
            print(repr(e))
            return False

    def create(self, user_form: UserForm) -> UserModel | None:
        user_id = self.__generate_id()
        user = UserModel(id=user_id, username=user_form.username, email=user_form.email)
        salt = self.__generate_id("salt")
        logger.debug(salt)
        logger.debug(user_form.password)
        hash = AuthService.hash(salt + user_form.password)
        user_pass = UserPass(user_id=user_id, salt=salt, password=hash)
        try:
            self.__db.add(user)
            self.__db.add(user_pass)
            self.__db.commit()
            return user
        except IntegrityError as e:
            self.__db.rollback()
            logger.error(e._sql_message())
            raise BadRequest
        except Exception as e:
            self.__db.rollback()
            logger.error(repr(e))
            return None

    def get(self, user_id: str):
        return self.__db.query(UserModel).filter(UserModel.id == user_id).first()
