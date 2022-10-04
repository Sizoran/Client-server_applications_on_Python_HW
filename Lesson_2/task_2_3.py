"""
Task 3:Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий
сохранение данных в файле YAML-формата. Для этого:
Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список,
второму — целое число, третьему — вложенный словарь, где значение каждого ключа — это целое
число с юникод-символом, отсутствующим в кодировке ASCII (например, €);
Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. При этом
обеспечить стилизацию файла с помощью параметра default_flow_style, а также установить
возможность работы с юникодом: allow_unicode = True;
ВАЖНО: Реализовать считывание данных из созданного файла и проверить, совпадают ли они с
исходными.
"""
import yaml
from yaml import SafeLoader

data_items_list = ['Notebook', 'ipad', 'mouse', 'monitor', 'coffee']
data_items_price_dict = {'Notebook': '1000$ - 3000$', 'ipad': '300€ - 1000€',
                         'mouse': '50€', 'monitor': '760€', 'coffee': '5€'}
data_to_yaml = {'items': data_items_list, 'items_price': data_items_price_dict,
                'items_quantity': 5}


def format_to_yaml(file):
    with open('file.yaml', 'w', encoding='utf-8') as data_f_n:
        yaml.dump(file, data_f_n, default_flow_style=False, allow_unicode=True)


def check_yaml(file):
    with open('file.yaml', encoding='utf-8') as f_n:
        f_n_content = yaml.load(f_n, Loader=SafeLoader)  # Открываем и сверяем данные с оригиналом
        if f_n_content == file:
            print('Данные совпадают')
        else:
            print('Данные не совпадают')


format_to_yaml(data_to_yaml)
check_yaml(data_to_yaml)
