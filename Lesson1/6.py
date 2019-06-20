# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет»,
# «декоратор». Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести
# его содержимое.

with open('test_file.txt', 'w') as out_file:
    out_file.write('сетевое программирование\n')
    out_file.write('сокет\n')
    out_file.write('декоратор\n')

with open('test_file.txt', 'r') as check_file:
    print(f'test_file.txt encoding={check_file.encoding}')

with open('test_file.txt', 'r', encoding='utf-8') as uni_file:
    print(f'test_file.txt:')
    for line in uni_file.readlines():
        print(line)
