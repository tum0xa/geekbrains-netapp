# 1. Реализовать простое клиент-серверное взаимодействие по протоколу JIM (JSON instant messaging):
# клиент отправляет запрос серверу;
# сервер отвечает соответствующим кодом результата. Клиент и сервер должны быть реализованы в виде отдельных
# скриптов, содержащих соответствующие функции.


#
# Функции сервера:
# принимает сообщение клиента;
# формирует ответ клиенту;
# отправляет ответ клиенту;
# имеет параметры командной строки: -p <port> — TCP-порт для работы (по умолчанию использует 7777);
# -a <addr> — IP-адрес для прослушивания (по умолчанию слушает все доступные адреса).


from socket import *
import sys
import re
import json

DEFAULT_PORT = '7777'
DEFAULT_IP = ''
MAX_CLIENTS = 5
PORT_PATTERN = r'^[0-9]{,5}$'
IP_PATTERN = r'^((25[0-5])|(2[0-4][0-9])|(1[0-9][0-9])|([1-9][0-9])|([0-9]))[.]((25[0-5])|(2[0-4][0-9])|(1[0-9][0-9])' \
             r'|([1-9][0-9])|([0-9]))[.]((25[0-5])|(2[0-4][0-9])|(1[0-9][0-9])|([1-9][0-9])|([0-9]))[.]((25[0-5])|(2' \
             r'[0-4][0-9])|(1[0-9][0-9])|([1-9][0-9])|([0-9]))$'


def main():
    arg_dict = {}
    port = DEFAULT_PORT
    ip_listen = DEFAULT_IP
    param = ''

    for n in range(1, len(sys.argv)):
        arg = sys.argv[n]
        if arg == '-p':
            try:
                param = sys.argv[n + 1]
            except IndexError:
                param = DEFAULT_PORT
            else:
                if param.startswith('-'):
                    param = DEFAULT_PORT
            finally:
                if re.match(PORT_PATTERN, param):
                    if 0 < int(param) < 65536:
                        port = param
                    else:
                        port = DEFAULT_PORT
                else:
                    port = DEFAULT_PORT

                arg_dict['port'] = port

        elif arg == '-a':
            try:
                param = sys.argv[n + 1]

            except IndexError:
                param = DEFAULT_IP
            else:
                if param.startswith('-'):
                    param = DEFAULT_IP
            finally:

                if re.match(IP_PATTERN, param):
                    ip_listen = param
                else:
                    ip_listen = DEFAULT_IP

                arg_dict['ip_listen'] = ip_listen

        elif arg not in arg_dict.keys() and arg not in arg_dict.values():
            if arg.startswith('-'):
                print(f'Wrong argument "{arg}"!')
            else:
                print(f'Parameter "{arg}" is wrong!')

    s = socket(AF_INET, SOCK_STREAM)

    s.bind((ip_listen, int(port)))
    s.listen(MAX_CLIENTS)

    while True:
        print(port, ip_listen)
        client, addr = s.accept()
        data = client.recv(640)
        print(json.loads(data.decode()))

        client.send("Hello!".encode('ascii'))
        client.close()


if __name__ == '__main__':
    main()
