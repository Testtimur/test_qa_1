from dataclasses import dataclass

"""Почитать поподробнее"""


@dataclass
class Person:
    full_name: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None
