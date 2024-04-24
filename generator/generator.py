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
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
    )
