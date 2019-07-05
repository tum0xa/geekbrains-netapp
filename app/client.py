import logging
import os
import sys
import json

from messenger.client import Client

import log.client_log_config

def main():
    logger = logging.getLogger('client')
    client = Client()
    if client.connect_to_server('localhost', 8888):
        logger.info('Client connected to server!')
        client.send_hello()
    else:
        logger.info('Client did not connect to server!')


if __name__ == '__main__':
    main()
