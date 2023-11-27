from typing import List

from sqlalchemy.orm import Session

from ..db import request
from ..models import Factory, Review

@request
def select_reviews(factory_id: int, session: Session = None) -> List[Review]:
    """Select reviews by id_"""
    reviews = session.query(Review).where(Review.factory_id == factory_id)
    return reviews.all()

@request
def select_all_reviews(session: Session = None) -> List[Review]:
    """Выбрать все фабрики из базы"""
    reviews = session.query(Review).all()
    return reviews

@request
def add_review(
    rating: int,
    feedback: str,
    status: str,
    factory_id: int | Factory,
    session: Session = None) -> bool:
    """Add new review"""

    new_factory = Review(rating=rating, feedback=feedback, status=status, factory_id=factory_id)
    session.add(new_factory)
    session.commit()


@request
def update_review(id_: int, new_rating: int, new_feedback: str, new_status: str, session: Session = None) -> None:
    """Update review by id_"""
    review = session.query(Review).where(Review.id == id_).first()
    if new_rating:
        review.rating = new_rating
    if new_feedback:
        review.feedback = new_feedback
    if new_status:
        review.status = new_status

    session.commit()

@request
def delete_review(id_: int, session: Session = None) -> None:
    """Delete review by name"""
    review = session.query(Review).where(Review.id == id_).first()
    session.delete(review)
    session.commit()