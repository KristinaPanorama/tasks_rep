import math
import sys


def read_center_radius(circle_path):
    try:
        with open(circle_path, encoding="utf-8") as file:
            center_x, center_y = map(float, file.readline().split())
            radius = float(file.readline().strip())
        return center_x, center_y, radius

    except FileNotFoundError:
        print("Невозможно открыть файл")
        sys.exit(1)
    except Exception as e:
        print("Ошибка при работе с файлом: ", str(e))
        sys.exit(1)


def read_dots(dot_path):
    try:
        with open(dot_path, encoding="utf-8") as file:
            dots = []
            for line in file:
                dots.append(tuple(map(int, line.split())))
        return dots

    except FileNotFoundError:
        print("Невозможно открыть файл")
        sys.exit(1)
    except Exception as e:
        print("Ошибка при работе с файлом:", str(e))
        sys.exit(1)


def check_points(x, y, center_x, center_y, radius):
    d = math.sqrt(((center_x - x) ** 2 + (center_y - y) ** 2))

    if math.isclose(d, radius, rel_tol=1e-6):
        return 0
    if d < radius:
        return 1
    if d > radius:
        return 2


def main():
    if len(sys.argv) != 3:
        print("Использование: python task2 circle.txt dot.txt")
        sys.exit(1)

    circle_path = sys.argv[1]
    dot_path = sys.argv[2]

    center_x, center_y, r = read_center_radius(circle_path)
    dots = read_dots(dot_path)

    for d in dots:
        print(check_points(*d, center_x, center_y, r))


if __name__ == "__main__":
    main()
