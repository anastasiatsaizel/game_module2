import json
from datetime import datetime

def save_result(name, rounds, score):
    result = {
        "Дата": str(datetime.now().strftime("%d-%m-%Y %H:%M:%S")),
        "Игрок": name,
        "Количество раундов": rounds,
        "Итоговый счет": score
    }

    try:
        with open("game_results.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    #         превращает json файл в python словарь, без него старые результаты сотрутся
    except FileNotFoundError:
        data = []

    data.append(result)

    with open("game_results.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
#          записать питон в json


def get_results():
    try:
        with open("game_results.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            for item in data:
                print(item)
    except FileNotFoundError:
        print("Нет результатов")