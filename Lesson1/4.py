# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в
# байтовое и выполнить обратное преобразование (используя методы encode и decode).

str_developing = "разработка"
str_administration = "администрирование"
str_protocol = "protocol"
str_standard = "standard"

print(str_developing, str_administration, str_protocol, str_standard)

byte_developing = str_developing.encode()
byte_administration = str_administration.encode()
byte_protocol = str_protocol.encode()
byte_standard = str_standard.encode()

print(byte_developing, byte_administration, byte_protocol, byte_standard)

str_developing = byte_developing.decode()
str_administration = byte_administration.decode()
str_protocol = byte_protocol.decode()
str_standard = byte_standard.decode()

print(str_developing, str_administration, str_protocol, str_standard)
