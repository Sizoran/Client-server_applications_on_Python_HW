"""
Task 2: Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON
с информацией о заказах. Написать скрипт, автоматизирующий его заполнение данными. Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item),
количество (quantity), цена (price), покупатель (buyer), дата (date). Функция должна
предусматривать запись данных в виде словаря в файл orders.json. При записи данных указать
величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее
значений каждого параметра.
"""

import json

order_1 = {'item': 1, 'quantity': 1, 'price': 500, 'buyer': 'Alex', 'date': '10.05.2021'}
order_2 = {'item': 2, 'quantity': 2, 'price': 1000, 'buyer': 'Ben', 'date': '02.03.2021'}
order_3 = {'item': 3, 'quantity': 8, 'price': 800, 'buyer': 'Alisa', 'date': '30.01.2020'}
order_4 = {'item': 4, 'quantity': 2, 'price': 5500, 'buyer': 'Cavin', 'date': '09.02.2022'}
order_5 = {'item': 5, 'quantity': 10, 'price': 20, 'buyer': 'Pol', 'date': '21.12.2022'}

def write_order_to_json(order):
    data_orders = json.load(open('orders.json'))
    data_velue = data_orders.get('orders')
    data_velue.append(order)
    data_orders.clear()
    data_orders = {'orders': data_velue}

    with open('orders.json', 'w', encoding='utf-8') as f_n:
        json.dump(data_orders, f_n, indent=4, ensure_ascii=False)

write_order_to_json(order_1)
write_order_to_json(order_2)
write_order_to_json(order_3)
write_order_to_json(order_4)
write_order_to_json(order_5)
