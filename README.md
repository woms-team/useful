<h2 align="center">Useful</h2>


### Описание проекта:
Скоро

### Инструменты разработки

**Стек:**
- Python >= 3.8
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

##### 5) В папке `src.core` файл `local_config.py-example` переименовать в `local_config.py` и прописать конект к базе

##### 6) Создание миграций

    alembic revision --autogenerate -m "Your comment"

##### 7) Выполнить команду для выполнения миграций

    alembic upgrade head
    
##### 8) Создать суперпользователя

    в разработке
    
##### 9) Запустить сервер

    python main.py
    
##### 10) Перейти по адресу

    http://127.0.0.1:8000/docs
    
## License

[BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause)

Copyright (c) 2020-present, DJWOMS - Omelchenko Michael



