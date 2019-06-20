# 3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.

byte_attribute = b'attribute'
byte_class = b'класс' # SyntaxError: bytes can only contain ASCII literal characters.
byte_function = b'функция' # SyntaxError: bytes can only contain ASCII literal characters.
byte_type = b'type'

print(byte_attribute)
print(byte_class)
print(byte_function)
print(byte_type)