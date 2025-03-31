import sys


def main():
    try:
        numbers_file = sys.argv[1]
    except:
        print("Ожидаемый ввод: python task4.py numbers.txt")
        sys.exit(1)

    nums = []

    try:
        with open(numbers_file, "r", encoding="utf-8") as file:
            for line in file:
                n = int(line.strip())
                nums.append(n)
    except:
        print("Ошибка при работе с файлом numbers.txt")
        sys.exit(1)

    nums.sort()
    middle_element = nums[len(nums) // 2]
    res_sum = 0
    for num in nums:
        res_sum += abs(middle_element - num)

    print(res_sum)


if __name__ == "__main__":
    main()

