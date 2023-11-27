"""
    Файл конфигурации
"""
from dataclasses import dataclass
from environs import Env
from sqlalchemy.orm import Session


@dataclass
class DbData:
    """
        Класс данных для базы данных
    """
    name: str
    username: str
    password: str
    host: str
    port: str

    debug: str
    session: Session = None


@dataclass
class Config:
    """
        Основной класс конфигурации
    """
    db: DbData


def load_config(path: str = None):
    """
        Загрузка конфигурации из переменных окружения
    """

    env = Env()
    env.read_env(path)

    return Config(
        db=DbData(name=env.str("DB_NAME"),
                  username=env.str("DB_USERNAME"),
                  password=env.str("DB_PASSWORD"),
                  host=env.str("DB_HOST"),
                  port=env.str("DB_PORT"),
                  debug=env.bool("DB_DEBUG")
        )
    )

config = load_config(".env")
