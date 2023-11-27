"""
    Модели для роутов в FastAPI приложении
"""

from pydantic import BaseModel

class FactoryBase(BaseModel):
    """
        Модель для демонстрации фабрики
    """

    id: int
    name: str
    address: str

class ReviewsBase(BaseModel):
    """
        Модель для демонстрации отзыва
    """

    id: int
    rating: int
    feedback: str
    status: str
    factory_id: int


class ReviewCreate(BaseModel):
    """
        Модель для создания отзыва
    """

    rating: int
    feedback: str
    status: str
