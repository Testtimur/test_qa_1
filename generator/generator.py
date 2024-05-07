import random

from data.data import Person
from faker import Faker

#yield - нам возвращает генератор (итерируемый генеренератор), class у нас называется Person
#Faker - нам позволяет работать с большим количеством данных


faker_ru = Faker('ru_Ru')  # Для того чтобы Faker был русским мы пишем 'ru_RU'
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        email=faker_ru.email(),
        age=random.randint(18, 80),
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        salary=random.randint(13700, 120000),
        department=faker_ru.job(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
    )
