import logging
import logging.handlers
import os

LOG_FOLDER_PATH = os.path.dirname(__file__)

CLIENT_LOG_FILE_PATH = os.path.join(LOG_FOLDER_PATH, 'client.log')

client_logger = logging.getLogger('client')

client_handler = logging.FileHandler(CLIENT_LOG_FILE_PATH, encoding='utf-8')

formatter = logging.Formatter("%(asctime)s: %(levelname)s - %(module)s: %(message)s ")

client_handler.setFormatter(formatter)

client_logger.addHandler(client_handler)
client_logger.setLevel(logging.INFO)
