import sys


def main():
    try:
        n, m = int(sys.argv[1]), int(sys.argv[2])
    except:
        print("Ожидаемый ввод: python task1.py n m (n и m должны быть больше 1)")
        sys.exit(1)

    circ_arr = [x for x in range(1, n+1)]
    res_arr = []
    step = m-1
    element = 1
    ind = 0
    while element not in res_arr:
        res_arr.append(element)
        ind = ind + step
        element = circ_arr[ind % n]

    print("".join(map(str, res_arr)))


if __name__ == "__main__":
    main()
