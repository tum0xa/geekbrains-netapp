# 2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность
# кодов (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.

byte_class = b'class'
byte_function = b'function'
byte_method = b'method'

print(f'"class" - {type(byte_class)}, {byte_class}, {len(byte_class)}')
print(f'"function" - {type(byte_function)}, {byte_function}, {len(byte_function)}')
print(f'"method" - {type(byte_method)}, {byte_method}, {len(byte_method)}')

