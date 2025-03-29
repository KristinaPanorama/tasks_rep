import sys


def calculate_min_movies(nums):
    if not nums:
        return 0
    nums.sort()
    m = nums[len(nums) // 2]
    return sum([abs(m-num) for num in nums])


def read_numbers(path):
    nums = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                nums.append(int(line.strip()))
            return nums

    except Exception as e:
        print(f"Ошибка при работе с файлом: {str(e)}")
        sys.exit(1)


def main():
    if len(sys.argv) != 2:
        print("Использование: python task4.py numbers.txt")
        sys.exit(1)

    numbers_path = sys.argv[1]

    numbers = read_numbers(numbers_path)
    movies = calculate_min_movies(numbers)
    print(movies)


if __name__ == "__main__":
    main()

