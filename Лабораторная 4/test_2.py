# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    ...  # TODO считать содержимое csv файла

    ...  # TODO Сериализовать в файл с отступами равными 4
    data = []
    with open(INPUT_FILENAME, 'r', newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=',')
        for row in csvreader:
            data.append(row)

    with open(OUTPUT_FILENAME, 'w') as jsonfile:
        json.dump(data, jsonfile, indent= 4)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
