import json
import sys


def insert_values(l_tests, vals):
    for t in l_tests:
        if "values" in t and isinstance(t["values"], list):
            insert_values(t["values"], vals)

        if "value" in t and t.get("id") in vals:
            t["value"] = vals[t["id"]]


def read_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        print("Невозможно открыть файл")
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка при работе с файлом, {str(e)}")
        sys.exit(1)


def main():
    if len(sys.argv) != 4:
        print("Использование: python script.py tests.json values.json report.json")
        sys.exit(1)

    tests_path, values_path, report_path = sys.argv[1:4]

    tests = read_file(tests_path)
    values = read_file(values_path)

    try:
        id_val_dict = {item["id"]: item["value"] for item in values["values"]}
    except TypeError:
        print("Неправильная структура массива values")
        sys.exit(1)

    insert_values(tests["tests"], id_val_dict)

    try:
        with open(report_path, "w", encoding="utf-8") as file:
            json.dump(tests, file, indent=3)
    except Exception as e:
        print(f"Ошибка при работе с файлом, {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
