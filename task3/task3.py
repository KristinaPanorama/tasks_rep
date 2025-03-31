import json
import sys


def make_report_file(tests, id_values):
    for t in tests:
        if "values" in t and isinstance(t["values"], list):
            make_report_file(t["values"], id_values)

        if "value" in t and t.get("id") in id_values:
            t["value"] = id_values[t["id"]]


def main():
    try:
        file_values, file_tests, file_report = sys.argv[1:4]
    except:
        print("Ожидаемый ввод: python task3.py values.json tests.json report.json")
        sys.exit(1)

    try:
        with open(file_values, "r", encoding="utf-8") as file:
            values_list = json.load(file)["values"]

        with open(file_tests, "r", encoding="utf-8") as file:
            tests = json.load(file)

    except:
        print("Ошибка при работе с файлами values.json или tests.json")
        sys.exit(1)

    id_val_dict = {item["id"]: item["value"] for item in values_list}

    make_report_file(tests["tests"], id_val_dict)

    try:
        with open(file_report, "w", encoding="utf-8") as file:
            json.dump(tests, file, indent=3)
    except:
        print("Ошибка при работе с файлом report.json")
        sys.exit(1)


if __name__ == "__main__":
    main()
