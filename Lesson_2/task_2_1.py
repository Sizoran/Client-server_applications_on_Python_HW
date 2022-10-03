'''
Task 1: Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку
определенных данных из файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный»
файл в формате CSV. Для этого:
Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными,
их открытие и считывание данных. В этой функции из считанных данных необходимо с помощью
регулярных выражений извлечь значения параметров «Изготовитель системы», «Название ОС»,
«Код продукта», «Тип системы». Значения каждого параметра поместить в соответствующий список.
Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list,
os_type_list. В этой же функции создать главный список для хранения данных отчета — например,
main_data — и поместить в него названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих столбцов также оформить в виде
списка и поместить в файл main_data (также для каждого файла);
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции
реализовать получение данных через вызов функции get_data(), а также сохранение подготовленных
данных в соответствующий CSV-файл;
Проверить работу программы через вызов функции write_to_csv().
'''

import chardet
import re
import csv



def get_data():
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    pattern_prod = re.compile('Изготовитель системы')
    pattern_name = re.compile('Название ОС')
    pattern_code = re.compile('Код продукта')
    pattern_type = re.compile('Тип системы')
    headers_arr = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    main_data = []
    rotated_mane_data = []
    for i in range(3):
        name_file = f'info_{i+1}.txt'
        with open(name_file, 'rb') as file:
            temp_data = file.read()
            charset = chardet.detect(temp_data)
            temp_data = temp_data.decode(charset['encoding'])
            temp_data_arr = temp_data.split('\n')

            for el in temp_data_arr:
                if len(pattern_prod.split(el)) > 1:
                    os_prod_list.extend(pattern_prod.split(el)[1].strip().strip(':').split())

                if len(pattern_name.split(el)) > 1:
                    os_name_list.append(pattern_name.split(el)[1].strip().strip(':').strip())

                if len(pattern_code.split(el)) > 1:
                    os_code_list.extend(pattern_code.split(el)[1].strip().strip(':').split())

                if len(pattern_type.split(el)) > 1:
                    os_type_list.extend(pattern_type.split(el)[1].strip().strip(':').strip('PC').split())

    rotated_mane_data.append(headers_arr)

    main_data.append(os_prod_list)
    main_data.append(os_name_list)
    main_data.append(os_code_list)
    main_data.append(os_type_list)
    rotated_mane_data.extend((zip(*main_data)))

    def write_to_csv():
        with open('data_report.csv', 'w', encoding='utf-8') as file_report:
            F_N_WRITER = csv.writer(file_report, lineterminator='\r')
            F_N_WRITER.writerows(rotated_mane_data)

    write_to_csv()
get_data()

