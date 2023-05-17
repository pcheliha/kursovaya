# импортируем библиотеку jsonimport json
import json
from datetime import datetime

with open("C:/Users/Pchel/PycharmProjects/kursovaya/utils/operations.json", 'r', encoding='utf-8') as f:
    operations = json.load(f)


def sort_operations():
    for i in operations:
        if i == {}:
           operations.remove(i)
    q = sorted(operations, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)
    new_operations = []
    for i in q:
        if i["state"] == 'EXECUTED':
            new_operations.append(i)
    return new_operations[0:5]

print(sort_operations())