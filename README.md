<h2 align="center">Useful</h2>


### Описание проекта:
Скоро

### Инструменты разработки

**Стек:**
- Python >= 3.7
- FastAPI == 0.52.0
- PostgreSQL

**Ссылки**:

## Разработка

##### 1) Сделать форк репозитория и поставить звездочку)

##### 2) Клонировать репозиторий

    git clone ссылка_сгенерированная_в_вашем_репозитории

##### 3) Установить pipenv

    pip install pipenv
    
##### 4) Устанавливить зависимости
    
    pipenv install

##### 5) В корне проекта создать файл .env
    
    SECRET_KEY=66a57bc62d00874ff566b46b4946b4ef4c6334a3a1d6d102c147ee83d538f23b
    FIRST_SUPERUSER=Имя юзера
    FIRST_SUPERUSER_PASSWORD=Пароль юзера
    DB_NAME=Имя бд
    DB_USER=Имя пользователя бд
    DB_PASSWORD=Пароль бд
    DB_HOST=localhost
    USERS_OPEN_REGISTRATION=True
    BACKEND_CORS_ORIGIN=http://localhost, http://localhost:4200, http://localhost:3000, http://localhost:8080
    SMTP_PORT=587
    SMTP_HOST=
    SMTP_USER=
    SMTP_PASSWORD=
    SMTP_EMAILS_FROME_MAIL=

##### 6) Создание миграций

    скоро

##### 7) Выполнить команду для выполнения миграций

    alembic upgrade head - не сейчас
    
##### 8) Создать суперпользователя

    в разработке
    
##### 9) Запустить сервер

    python main.py
    
##### 10) Перейти по адресу

    http://127.0.0.1:8000/docs
    
## License

[BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause)

Copyright (c) 2020-present, DJWOMS - Omelchenko Michael



