# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union
import doctest
class Planet:
    def __init__(self, name: str, size: float, distance_from_sun: float):
        """
        Создание и подготовка к работе объекта "Планета"

        :param name: Название планеты
        :param size: Размер планеты в километрах
        :param distance_from_sun: Расстояние от планеты до Солнца в миллионах километров

        Примеры:
        >>> planet = Planet("Марс", 6779, 227.9)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Name should be a string.")
        self.name = name

        if not isinstance(size, (int, float)) or size <= 0:
            raise ValueError("Size should be a positive number.")
        self.size = size

        if not isinstance(distance_from_sun, (int, float)):
            raise TypeError("Distance from sun should be a number.")
        self.distance_from_sun = distance_from_sun

    def rotate(self, days: int) -> None:
        """
        Имитация вращения планеты вокруг своей оси

        :param days: Количество дней для имитации вращения

        Пример:
        >>> planet = Planet("Венера", 12104, 108.2)
        >>> planet.rotate(30)
        """
        if not isinstance(days, (int, float)) or days <= 0:
            raise ValueError("Days should be a positive number.")

        if not isinstance(days, (int, float)):
            raise TypeError("Days should be a number.")
        ...

    def orbit_around_sun(self, years: float) -> None:
        """
        Имитация обращения планеты вокруг Солнца

        :param years: Количество лет для имитации обращения

        Пример:
        >>> planet = Planet("Юпитер", 139820, 778.3)
        >>> planet.orbit_around_sun(5)
        """
        if not isinstance(years, (int, float)) or years <= 0:
            raise ValueError("years should be a positive number.")
        if not isinstance(years, (int, float)):
            raise TypeError("years should be a number.")
        ...

    def generate_magnetic_field(self) -> str:
        """
        Генерация магнитного поля планеты

        :return: Информация о сгенерированном магнитном поле

        Пример:
        >>> planet = Planet("Земля", 12742, 149.6)
        >>> planet.generate_magnetic_field()
        """
        ...


class Spaceship:
    def __init__(self, model: str, max_speed: float, crew_capacity: int):
        """
        Создание и подготовка к работе объекта "Космический корабль"

        :param model: Модель корабля
        :param max_speed: Максимальная скорость корабля в км/ч
        :param crew_capacity: Вместимость экипажа

        Примеры:
        >>> spaceship = Spaceship("Старшип", 50000, 100)  # инициализация экземпляра класса
        """
        if not isinstance(model, str):
            raise TypeError("Model should be a string.")
        self.model = model

        if not isinstance(max_speed, (int, float)) or max_speed <= 0:
            raise ValueError("Max speed should be a positive number.")
        self.max_speed = max_speed

        if not isinstance(crew_capacity, int) or crew_capacity <= 0:
            raise ValueError("Crew capacity should be a positive integer.")
        self.crew_capacity = crew_capacity

    def launch(self, destination: str, distance: float) -> str:
        """
        Запуск корабля в путешествие к указанному объекту в космосе

        :param destination: Название объекта, к которому направляется корабль
        :param distance: Расстояние до объекта в космосе в миллионах километров

        :return: Сообщение о результате запуска корабля

        Пример:
        >>> spaceship = Spaceship("Вояджер", 60000, 50)
        >>> spaceship.launch(destination="Проксима Центавра", distance=4.24)
        """
        if not isinstance(distance, (int, float)):
            raise TypeError("The distance must be of type int or float")
        if distance < 0:
            raise ValueError("The distance should be a positive number")
        ...

    def land(self) -> str:
        """
        Имитация посадки корабля на поверхность планеты или космической станции

        :return: Сообщение о результате посадки корабля

        Пример:
        >>> spaceship = Spaceship("Фалькон 9", 20000, 20)
        >>> spaceship.land()
        """
        ...


class BlackHole:
    def __init__(self, mass: float, radius: float, rotation_speed: float):
        """
        Создание и подготовка к работе объекта "Черная дыра"

        :param mass: Масса черной дыры в кг
        :param radius: Радиус черной дыры в км
        :param rotation_speed: Скорость вращения черной дыры в рад/с

        Примеры:
        >>> black_hole = BlackHole(5e31, 1000, 0.2)  # инициализация экземпляра класса
        """
        if not isinstance(mass, (int, float)) or mass <= 0:
            raise ValueError("Mass should be a positive number.")
        self.mass = mass

        if not isinstance(radius, (int, float)) or radius <= 0:
            raise ValueError("Radius should be a positive number.")
        self.radius = radius

        if not isinstance(rotation_speed, (int, float)):
            raise TypeError("Rotation speed should be a number.")
        self.rotation_speed = rotation_speed

    def evaporate(self) -> None:
        """
        Имитация испарения черной дыры из-за излучения Хокинга
        """
        ...

    def generate_gravitational_field(self) -> str:
        """
        Генерация гравитационного поля черной дыры

        :return: Информация о сгенерированном гравитационном поле

        Пример:
        >>> black_hole = BlackHole(3e32, 1500, 0.4)
        >>> black_hole.generate_gravitational_field()
        """
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
