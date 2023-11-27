"""
    Модуль дополнительных функций
"""
from db.iteraction.factory import add_factory, select_all_factories


def upload_to_database_if_clear() -> None:
    """
        Если БД пустая то записываем в нее эти значения фабрик
    """
    if not select_all_factories():
        add_factory("г. Киров ул. Ленина 33", "Фабрика номер 1")
        add_factory("г. Москва ул. Пушкина 444", "Мария")
        add_factory("г. Саратов ул. Весенняя 12", "Виктория")
