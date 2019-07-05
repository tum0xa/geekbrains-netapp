# Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
# Написать скрипт, автоматизирующий его заполнение данными.

# Для этого:
# Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
# цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря
# в файл orders.json. При записи данных указать величину отступа в 4 пробельных символа;

# Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.

import json
from datetime import datetime


def write_to_json(item, quantity=0, price=0, buyer='', date=''):
    oreder_n = 0

    data = {'item': item,
            'quantity': quantity,
            'price': price,
            'buyer': buyer,
            'date': date}
    orders = {}
    with open("orders.json", 'r') as f_n:
        orders = json.load(f_n)
    oreder_n = len(orders['orders']) + 1
    orders['orders'].append({'order_number': oreder_n,
                             'order': data})

    with open("orders.json", 'w') as f_n:
        json.dump(orders, f_n, indent=4)


write_to_json('Button', 22, 50, "Petr", date=str(datetime.now()))
