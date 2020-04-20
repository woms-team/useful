from src.core import config
from src.db.session import db_session
from src.app.user.service import user
from src.app.user.schemas import UserCreate


def main():
    """ Создание супер юзера """
    super_user = user.get_by_username(db_session, username=config.SUPERUSER_NAME)
    if not super_user:
        user_in = UserCreate(
            username=config.SUPERUSER_NAME,
            email=config.SUPERUSER_EMAIL,
            password=config.SUPERUSER_PASSWORD,
            is_superuser=True,
            is_active=True
        )
        user.create(db_session, obj_in=user_in)


main()
