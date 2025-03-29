import sys


def circular_array(n, m):
    path = []
    start = 1
    while start not in path:
        path.append(start)
        start = (start + m -1) % n
        if start == 0:
            start = n
    return path


def main():
    if len(sys.argv) != 3:
        print("Использование: python task1.py n m")
        sys.exit(1)

    n, m = int(sys.argv[1]), int(sys.argv[2])

    res = circular_array(n, m)
    print("".join(map(str, res)))


if __name__ == "__main__":
    main()

