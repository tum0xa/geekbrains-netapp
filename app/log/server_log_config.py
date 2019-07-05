import logging
import logging.handlers
import os

LOG_FOLDER_PATH = os.path.dirname(__file__)

SERVER_LOG_FILE_PATH = os.path.join(LOG_FOLDER_PATH, 'server.log')

server_logger = logging.getLogger('server')

server_handler = logging.handlers.TimedRotatingFileHandler(SERVER_LOG_FILE_PATH, when='d')

formatter = logging.Formatter("%(asctime)s: %(levelname)s - %(module)s: %(message)s ")

server_handler.setFormatter(formatter)

server_logger.addHandler(server_handler)
server_logger.setLevel(logging.INFO)
