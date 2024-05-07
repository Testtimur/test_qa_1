from dataclasses import dataclass

"""Почитать поподробнее"""


@dataclass
class Person:
    full_name: str = None
    age: int = None
    first_name: str = None
    last_name: str = None
    salary: int = None
    department: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None
