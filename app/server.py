import logging
import os
import sys
import json
from socket import socket
import log.server_log_config
from messenger.server import Server


def main():
    logger = logging.getLogger('server')

    server = Server()

    if server.start():
        logger.info('Server started!')
    else:
        logger.critical('Server did not start!')

    while True:
        logger.info('Server waiting for client')
        client = server.get_client()
        if client is not None
            logger.info('Server waiting for message from client')
        else:
            logger.error('Client is None')
        message = server.get_message_from_client(client)
        print(message)


if __name__ == '__main__':
    main()
