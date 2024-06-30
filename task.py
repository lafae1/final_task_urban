import csv
from collections import Counter


def read_file(filename: str) -> list[dict]:
    """
    Читает данные из CSV файла и преобразует их в список словарей.

    :param filename: Название файла, содержащего данные.
    :return: Список словарей с данными о домах.
    """
    trans_list = []
    with open(filename) as file:
        read = csv.DictReader(file)
        for row in read:
            row["floor_count"] = int(row["floor_count"])
            row["heating_value"] = float(row["heating_value"])
            row["area_residential"] = float(row["area_residential"])
            row["population"] = int(row["population"])
            trans_list.append(row)
    return trans_list


def classify_house(floor_count: int) -> str:
    """
    Классифицирует дом на основе количества этажей.

    Проверяет, является ли количество этажей целым числом и положительным значением.
    Возвращает категорию дома в зависимости от количества этажей.

    :param floor_count: Количество этажей в доме.
    :return: Категория дома в виде строки: "Малоэтажный", "Среднеэтажный" или
    "Многоэтажный".
    """
    first_treshold = 1
    second_treshold = 5
    last_treshold = 16
    if type(floor_count) is not int:
        msg = "Необходимо ввести целое число"
        raise TypeError(msg)
    if floor_count <= 0:
        msg = "Необходимо ввести положительное число"
        raise ValueError(msg)

    if first_treshold <= floor_count <= second_treshold:
        return "Малоэтажный"
    if second_treshold < floor_count <= last_treshold:
        return "Среднеэтажный"
    return "Многоэтажный"


def get_classify_houses(houses: list[dict]) -> list[str]:
    """
    Классифицирует дома на основе количества этажей.

    :param houses: Список словарей с данными о домах.
    :return: Список категорий домов.
    """
    return [classify_house(house["floor_count"]) for house in houses]


def get_count_house_categories(categories: list[str]) -> dict[str, int]:
    """
    Подсчитывает количество домов в каждой категории.

    :param categories: Список категорий домов.
    :return: Словарь с количеством домов в каждой категории.
    """
    return Counter(categories)


def min_area_residential(houses: list[dict]) -> str:
    """
    Находит адрес дома с наименьшим средним метров жилой площади на одного жильца.

    :param houses: Список словарей с данными о домах.
    :return: Адрес дома с наименьшим средним количеством квадратных
    метров жилой площади на одного жильца.
    """
    res = min(houses, key=lambda x: x["area_residential"] / x["population"])
    return res["house_address"]


if __name__ == "__main__":
    dict_ = read_file("housing_data.csv")
    classified_houses = get_classify_houses(dict_)
    get_count_house_categories(classified_houses)
    minimal_area = min_area_residential(dict_)
