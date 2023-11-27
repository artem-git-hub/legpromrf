"""
    Модуль взаимодействия с БД
"""
import logging

import sqlite3
from sqlalchemy import create_engine, Column, DateTime, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config import config


logger = logging.getLogger(__name__)

Base = declarative_base()

class TimedModel(Base):
    """
        Модель для добавления всем таблицам двух колонок:
        created_at - дата создания записи
        updated_at - дата обновления записи
    """

    __abstract__ = True

    created_at = Column(DateTime(True), server_default=func.now())
    updated_at = Column(
        DateTime(True),
        default=func.now(),
        onupdate=func.now(),
        server_default=func.now(),
    )


def request(func):
    """
        Декоратор передающий экземпляр сессии в функции взаимодействующие с базой данных
    """

    def interaction(*args, **kwargs):

        try:
            # Начало явной транзакции
            config.db.session.begin()

            # Операции с базой данных
            result = func(session=config.db.session, *args, **kwargs)

            # Закрыть сессию
            config.db.session.close()


            return result

        except Exception as e:
            # Откат транзакции в случае ошибки
            config.db.session.rollback()
            logger.error(f"Transaction error: {e}")
            raise
    return interaction



def on_startapp():
    """
        Функция создания подключения к БД и создания сессии 
    """

    try:
        # Create an SQLite database (you can replace this with a file path)
        engine = create_engine(f'mysql+pymysql://{config.db.username}:{config.db.password}@{config.db.host}:{config.db.port}/{config.db.name}', echo=True)

        #Create class Session
        session = sessionmaker(bind=engine)

        #Write Session to config
        config.db.session = session()

        logger.info("Successful connection to MySQL")
    except sqlite3.OperationalError as e:
        logger.error("Failed to establish connection with MySQL.")
        logger.error(str(e))
        exit(1)



    if config.db.debug:
        # Если DEBUG = True то удалятся и создадутся все таблицы
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)



def on_shutdown():
    """
        Закрытие сессии
    """

    # Close the session
    config.db.session.close()
