from typing import List

from sqlalchemy.orm import Session

from ..db import request
from ..models import Factory

@request
def select_factory(id: int, session: Session = None) -> Factory:
    """Select factory by id"""
    factory = session.query(Factory).where(Factory.id == id).first()
    return factory

@request
def select_all_factories(session: Session = None) -> List[Factory]:
    """Выбрать все фабрики из базы"""
    factories = session.query(Factory).all()
    return factories

@request
def add_factory(address: str, name: str, session: Session = None) -> bool:
    """Add new factory"""
    new_factory = Factory(address=address, name=name)
    session.add(new_factory)
    session.commit()


@request
def update_factory(id: int, new_name: str, new_address: str, session: Session = None) -> None:
    """Update factory by id"""
    factory = session.query(Factory).where(Factory.id == id).first()
    if new_name:
        factory.name = new_name
    if new_address:
        factory.address = new_address

    session.commit()

@request
def delete_factory(id: int, session: Session = None) -> None:
    """Delete factory by name"""
    factory = session.query(Factory).where(Factory.id == id).first()
    session.delete(factory)
    session.commit()
