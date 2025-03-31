import math
import sys


def find_point_position(point_x, point_y, center_x, center_y, radius):
    vector_len = math.sqrt(((center_x - point_x) ** 2 + (center_y - point_y) ** 2))

    if vector_len == radius:
        return 0
    if vector_len < radius:
        return 1
    if vector_len > radius:
        return 2


def main():
    try:
        file_circle = sys.argv[1]
        file_dot = sys.argv[2]
    except:
        print("Ожидаемый ввод: python task2.py circle.txt dot.txt")
        sys.exit(1)

    try:
        with open(file_circle, "r") as file:
            circle_arr = file.read().split()
            center_x = float(circle_arr[0].strip())
            center_y = float(circle_arr[1].strip())
            radius = float(circle_arr[2].strip())

        with open(file_dot, "r") as file:
            dots = []
            for line in file:
                coords = tuple(map(float, line.split()))
                dots.append(coords)
    except:
        print("Ошибка при работе с файлом dot.txt или circle.txt")
        sys.exit(1)

    for d in dots:
        print(find_point_position(*d, center_x, center_y, radius))


if __name__ == "__main__":
    main()
