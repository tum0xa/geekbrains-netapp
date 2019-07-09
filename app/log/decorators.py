from functools import wraps


class Log:

    def __init__(self, logger):
        self.logger = logger

    @staticmethod
    def _create_message(result=None, *args, **kwargs):

        message = ''
        if result:
            message = f'result: {result}'
        if args:
            message = f'args: {args} '
        if kwargs:
            message = f'kwargs: {kwargs} '

        return message

    def __call__(self, func):

        @wraps(func)
        def decorated(*args, **kwargs):
            result = func(*args, **kwargs)
            message = Log._create_message(result, *args, **kwargs)
            self.logger.info(f'{message} - {decorated.__name__} - {decorated.__module__}')
            return result

        return decorated
