import logging
import os
import sys
import json
from socket import socket
import log.server_log_config
from log.decorators import Log
from messenger.server import Server


def main():
    server = Server()
    server.start()
    while True:
        client = server.get_client()
        message = server.get_message_from_client(client)
        print(message)


if __name__ == '__main__':
    main()
