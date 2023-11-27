"""
    Модуль запуска FastAPI
"""
from typing import List
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from db.db import on_shutdown, on_startapp
from db.iteraction.factory import select_all_factories, select_factory
from db.iteraction.review import add_review, select_reviews
from misc import upload_to_database_if_clear
from pydamtic_models import FactoryBase, ReviewCreate, ReviewsBase

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/factories/{factory_id}/reviews")
def create_review(factory_id: int, review: ReviewCreate):
    """
        Эндпоинт для добавления отзыва на фабрику
    """

    factory =  select_factory(factory_id)
    if factory is None:
        raise HTTPException(status_code=404, detail="Factory not found")
    add_review(**review.dict(), factory_id=factory_id)
    return {"message": "Review created successfully"}


# Реализуйте API-маршруты
@app.get("/reviews/{factory_id}/", response_model=List[ReviewsBase])
def get_reviews(factory_id: int):
    """
        Эндпоинт для выборки всех отзывов на определенную фабрику
    """

    reviews = select_reviews(factory_id)
    return reviews



@app.get("/factories/", response_model=List[FactoryBase])
def get_all_factories():
    """
        Эндпоинт для выборки всех фабрик
    """

    factories = select_all_factories()
    return factories


def startup_event():
    """
        Функция срабатывающая при запуске FastAPI приложения
    """
    on_startapp()
    upload_to_database_if_clear()
    print("FastAPI is starting up!")


def shutdown_event():
    """
        Функция срабатывающая при выключении FastAPI приложения
    """
    on_shutdown()
    print("FastAPI is shutting down!")


app.add_event_handler("startup", startup_event)
app.add_event_handler("shutdown", shutdown_event)
