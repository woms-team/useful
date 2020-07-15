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

##### 3) Установить pyenv

[pyenv installer](https://github.com/pyenv/pyenv-installer)
    
[help docs](https://github.com/pyenv/pyenv)
    
##### 4) Установить poetry

    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
    
[help docs](https://python-poetry.org/docs/)
    
##### 5) Устанавливить зависимости
    
    poetry install

##### 6) В папке `src.core` файл `local_config.py-example` переименовать в `local_config.py` и прописать конект к базе

##### 7) Активировать виртуальное окружение

    poetry shell
       
##### 8) Создание миграций

    alembic revision --autogenerate -m "Your comment"

##### 9) Выполнить команду для выполнения миграций

    alembic upgrade head
    
##### 10) Создать суперпользователя

    в разработке
    
##### 11) Запустить сервер

    python main.py
    
##### 12) Перейти по адресу

    http://127.0.0.1:8000/docs
 
## License

[BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause)

Copyright (c) 2020-present, DJWOMS - Omelchenko Michael



