# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet
import numpy as np

def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            if object_type == "planet":
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
    return objects


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
      0           1            2       3     4   5    6    7
    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """
    params = line.split()
    star.R = params[1]
    star.color = params[2]
    star.m = params[3]
    star.x = params[4]
    star.x = params[5]
    star.Vx = params[6]
    star.Vy = params[7]
    return 

def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
        0           1             2       3    4   5    6    7 
    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    params = line.split()
    planet.R = params[1]
    planet.color = params[2]
    planet.m = params[3]
    planet.x = params[4]
    planet.x = params[5]
    planet.Vx = params[6]
    planet.Vy = params[7]
    return 


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    0                1            2      3     4   5    6    7
    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            print(out_file, '{0}, {1:f}, {2}, {3:f}, {4:f}, {5:f}, {6:f}, {7:f}'.format(obj.type.capitalize(), obj.R, obj.color, obj.m, obj.x, obj.y, obj.Vx, obj.Vy))

def write_space_objects_statistics_to_file(output_filename, space_objects):
    pass

if __name__ == "__main__":
    print("This module is not for direct call!")
