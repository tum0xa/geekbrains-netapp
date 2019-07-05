formatter = logging.Formatter("%(asctime)s: %(levelname)s - %(module)s: %(message)s ")

critical_handler.setFormatter(formatter)
error_handler.setFormatter(formatter)
action_handler.setFormatter(formatter)