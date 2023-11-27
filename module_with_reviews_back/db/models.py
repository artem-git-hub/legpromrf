from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey

from .db import TimedModel

class Factory(TimedModel):
    """
        модель для фабрик
    """

    __tablename__ = 'factories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    address = Column(String(255))
    reviews = relationship("Review", back_populates="factory")

class Review(TimedModel):
    """
        модель для отзывов
    """

    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True, index=True)
    rating = Column(Integer)
    feedback = Column(String(255))
    status = Column(String(50))
    factory_id = Column(Integer, ForeignKey("factories.id"))
    factory = relationship("Factory", back_populates="reviews")
