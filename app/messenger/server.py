import json
import logging
import os
import sys
from socket import socket, AF_INET, SOCK_STREAM

from tools.checkers import *
from client import Client
from log.decorators import Log

logger = logging.getLogger('server')
log = Log(logger)

DEFAULT_PORT = '8888'
MAX_CLIENTS = 5
MAX_SIZE = 640


class Server:
    users = []
    guests = []
    rooms = []
    socket = None

    def __init__(self, host='', port=DEFAULT_PORT):
        self.port = port
        self.host = host

    @log
    def start(self):
        try:
            self.socket = socket(AF_INET, SOCK_STREAM)
            self.socket.bind((self.host, int(self.port)))
            self.socket.listen(MAX_CLIENTS)
        except Exception:
            return False
        else:
            return True

    def get_client(self):
        client_socket, address = self.socket.accept()
        client = Client(client_socket, address)
        self.guests.append(client)
        return client

    @log
    def get_message_from_client(self, client):
        data = client.client.recv(MAX_SIZE)
        message = json.loads(data.decode())
        return message

    def msg_handler(self, client, msg):
        pass
