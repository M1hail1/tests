import json

def task() -> float:
    filename = 'input.json'
    with open(filename) as file:
        data = json.load(file)
    summ = 0
    for i in data:
        summ += i['score'] * i['weight']
    return round(summ, 3)


print(task())
