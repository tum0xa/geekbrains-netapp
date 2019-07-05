import re

PATTERN_EMAIL = r'^([a-z0-9_\.-]+\@[\da-z\.-]+\.[a-z\.]{2,6})$'


def check_email(email):
    if re.match(PATTERN_EMAIL, email):
        return email
    else:
        return None