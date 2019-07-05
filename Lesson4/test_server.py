import re
import unittest


PATTERN_EMAIL = r'^([a-z0-9_\.-]+\@[\da-z\.-]+\.[a-z\.]{2,6})$'


def check_email(email):
    if re.match(PATTERN_EMAIL, email):
        return email
    else:
        return None


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


class Client(User):

    addresses = ['localhost']
    is_online = False
    room = None


class Room:

    participants = []
    black_list = []
    event = ''

    def __init__(self, uid, name, admin, **settings):
        self._uid = uid
        self.name = name
        self.admin = admin
        self.event = f'Room {self.name} is created'

    def add_participant(self, participant):
        if participant not in self.participants and participant not in self.black_list:
            participant.room = self
            self.participants.append(participant)
            self.event = f'{participant.username} enter to the room!'
            return True
        elif participant in self.participants:
            self.event = f'{participant.username} already here!'
            return False
        elif participant in self.black_list:
            self.event = f'{participant.username} has a permanent ban!'
        else:
            self.event = f"{participant.username} can't enter to the room!"
            return False

    def permanent_ban_by_participant(self, participant):
        try:
            self.participants.remove(participant)
            self.black_list.append(participant)
        except Exception:
            return False
        else:
            return True


class Lobby:

    clients = []
    rooms = []

    def __init__(self, name, **settings):
        self.name = name


def authenticate_client(username, password):
    response_code = 200
    return response_code


class TestServer(unittest.TestCase):
    def test_authenticate_success(self):

        self.assertEqual(authenticate_client('User1', '123456'), 200)