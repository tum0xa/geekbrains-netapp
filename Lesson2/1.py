# 1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов
# info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV.
# Для этого:
# Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и
# считывание данных. В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь
# значения параметров «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого
# параметра поместить в соответствующий список. Должно получиться четыре списка — например, os_prod_list,
# os_name_list, os_code_list, os_type_list. В этой же функции создать главный список для хранения данных отчета
# — например, main_data — и поместить в него названия столбцов отчета в виде списка: «Изготовитель системы»,
# «Название ОС», «Код продукта», «Тип системы». Значения для этих столбцов также оформить в виде списка и поместить
# в файл main_data (также для каждого файла);
# Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение
# данных через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
# Проверить работу программы через вызов функции write_to_csv().

import csv

MAX_FILES = 3


def get_data():
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    header_data = ["Изготовитель системы", "Название ОС", "Код продукта", "Тип системы"]

    for filename in [f'info_{num}.txt' for num in range(1, MAX_FILES + 1)]:

        with open(filename, 'r', encoding='windows-1251') as f_n:

            f_n_reader = csv.reader(f_n)

            for row in f_n_reader:
                try:
                    title, content, *_ = row[0].split(":")
                except Exception:
                    pass

                if title == header_data[0]:
                    os_prod_list.append(content.strip())
                elif title == header_data[1]:
                    os_name_list.append(content.strip())
                elif title == header_data[2]:
                    os_code_list.append(content.strip())
                elif title == header_data[3]:
                    os_type_list.append(content.strip())

    return [header_data, os_name_list, os_code_list, os_type_list]


def write_to_csv(file_pointer):
    f_n_writer = csv.writer(file_pointer)

    for row in get_data():
        f_n_writer.writerow(row)


with open('result.csv', 'w') as f_n:
    write_to_csv(f_n)
