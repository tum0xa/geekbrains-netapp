import sys
import json
from socket import socket, AF_INET, SOCK_STREAM
from tools.checkers import *

DEFAULT_PORT = '8888'
MAX_SIZE = 640

test_msg = json.dumps({
    "action": "test",
    "time": "time",
    "user": {
        "account_name": "test_user",
        "password": "test_password"
    }
})


class User:
    _is_active = False

    def __init__(self, username, password, email):
        self.username = username
        self._password = password
        self.email = check_email(email)

    @property
    def is_active(self):
        return self._is_active

    def activate(self):
        self._is_active = True


class Client:
    addresses = ['localhost']
    is_online = False
    room = None
    user = None

    def __init__(self, client_socket=None, address=None):
        if isinstance(client_socket, socket):
            self.client = client_socket

        else:
            self.client = None

        self.address = address
        if address not in self.addresses:
            self.addresses.append(address)

    def connect_to_server(self, address, port=DEFAULT_PORT):
        try:
            self.client = socket(AF_INET, SOCK_STREAM)
            self.client.connect((address, port))
        except Exception:
            return False
        else:
            return True

    def send_hello(self):
        self.client.send(test_msg.encode('utf-8'))

    def authenticate(self):

