# 1. Реализовать простое клиент-серверное взаимодействие по протоколу JIM (JSON instant messaging):
# клиент отправляет запрос серверу;
# сервер отвечает соответствующим кодом результата. Клиент и сервер должны быть реализованы в виде отдельных
# скриптов, содержащих соответствующие функции.

# Функции клиента:
# сформировать presence-сообщение;
# отправить сообщение серверу;
# получить ответ сервера;
# разобрать сообщение сервера;
# параметры командной строки скрипта client.py
# <addr> [<port>]:
# addr — ip-адрес сервера;
# port — tcp-порт на сервере, по умолчанию 7777.


from socket import *
import sys
import re
import json

DEFAULT_PORT = '7777'
DEFAULT_SERVER_IP = 'localhost'
MAX_CLIENTS = 5
PORT_PATTERN = r'^[0-9]{,5}$'
IP_PATTERN = r'^((25[0-5])|(2[0-4][0-9])|(1[0-9][0-9])|([1-9][0-9])|([0-9]))[.]((25[0-5])|(2[0-4][0-9])|(1[0-9][0-9])' \
             r'|([1-9][0-9])|([0-9]))[.]((25[0-5])|(2[0-4][0-9])|(1[0-9][0-9])|([1-9][0-9])|([0-9]))[.]((25[0-5])|(2' \
             r'[0-4][0-9])|(1[0-9][0-9])|([1-9][0-9])|([0-9]))$'

test_msg = """{
           "action": "presence",
           "time": "12",
                         "type": "status",
            "user": {
            "account_name":  "C0deMaver1ck",
            "status":      "Yep, I am here!"
                    }
    }"""

def main():
    arg_dict = {}
    port = DEFAULT_PORT
    server_ip = DEFAULT_SERVER_IP
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
                param = DEFAULT_SERVER_IP
            else:
                if param.startswith('-'):
                    param = DEFAULT_SERVER_IP
            finally:

                if re.match(IP_PATTERN, param):
                    ip_listen = param
                else:
                    ip_listen = DEFAULT_SERVER_IP

                arg_dict['server_ip'] = server_ip

        elif arg not in arg_dict.keys() and arg not in arg_dict.values():
            if arg.startswith('-'):
                print(f'Wrong argument "{arg}"!')
            else:
                print(f'Parameter "{arg}" is wrong!')
    msg = test_msg
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((server_ip, int(port)))
    s.send(msg.encode('utf-8'))
    # data = s.recv(640)
    # # print('Сообщение от сервера: ', data.decode('utf-8'), ', длиной ', len(data), ' байт')
    s.close()


if __name__ == '__main__':
    main()