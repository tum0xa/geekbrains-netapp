# 1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание
# соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление в формат
# Unicode и также проверить тип и содержимое переменных.

str_developing = "разработка"
str_socket = "сокет"
str_decorator = "декоратор"

print(f'"разработка" - {type(str_developing)}, {str_developing}')
print(f'"сокет" - {type(str_socket)}, {str_socket}')
print(f'"декоратор" - {type(str_decorator)}, {str_decorator}')

uni_developing = "\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430"
uni_socket = "\u0441\u043e\u043a\u0435\u0442"
uni_decorator = "\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440"

print(f'"разработка" - {type(uni_decorator)}, {uni_developing}')
print(f'"сокет" - {type(uni_socket)}, {uni_socket}')
print(f'"декоратор" - {type(uni_decorator)}, {uni_decorator}')
