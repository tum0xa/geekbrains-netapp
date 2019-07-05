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
import time

DEFAULT_PORT = 7777
DEFAULT_SERVER = 'localhost'

DEFAULT_USER = 'guest'
DEFAULT_PASS = 'quest'
DEFAULT_USER_STATUS = "I'm guest!"

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
    server = DEFAULT_SERVER
    user_name = DEFAULT_USER
    user_pass = DEFAULT_PASS
    user_status = 'Hello!'

    if len(sys.argv) > 2:
        print("Too many parameters!")
        quit()
    else:

        try:
            server = sys.argv[1]
        except IndexError:
            print('IP address or name of server required!')
            quit()
        finally:
            arg_dict['server_ip'] = server

        try:
            port = sys.argv[2]
        except IndexError:
            port = DEFAULT_PORT
        finally:
            if re.match(PORT_PATTERN, str(port)):
                if 0 < int(port) < 65536:
                    port = int(port)
                else:
                    port = DEFAULT_PORT
            else:
                port = DEFAULT_PORT
            port = int(port)
            arg_dict['port'] = port

    msg = test_msg

    auth_msg = json.dumps({
        "action": "authenticate",
        "time": str(time.time()),
        "user": {
            "account_name": user_name,
            "password": user_pass
        }
    })

    presense_msg = str({"action": "presence",
                        "time": str(time.time()),
                        "type": "status",
                        "user": {
                            "account_name": user_name,
                            "status": user_status
                        }
                        })

    s = socket(AF_INET, SOCK_STREAM)
    s.connect((server, port))

    s.send(auth_msg.encode('utf-8'))
    data = s.recv(640)
    response_code = data['response']

    if response_code == 200:
        print(f'{data["alert"]}')
    elif: response_code = 409
        print(f'')
    print('Сообщение от сервера: ', data.decode('utf-8'), ', длиной ', len(data), ' байт')

    # s.send(presense_msg.encode('utf-8'))

    # # print('Сообщение от сервера: ', data.decode('utf-8'), ', длиной ', len(data), ' байт')
    s.close()


if __name__ == '__main__':
    main()
