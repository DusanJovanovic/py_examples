import hashlib

users = {
    'Miki': '51c62d69a62c78d9a8335b92025008fb49c7aea47a92271f07b54a6590820e25',
    'Paja': '2883bc2c9893cc73d29d7841b3085a08fa46b2bd5cdb29f5cb3f07e5211dfcbb',
    'Dzontra': 'eaea120fe93f43de2ea2c99b6d3880248cac2f425ce3ddfd7daf6f9442727ecb',
}

test_data_good = {
    'Paja': 'Patak',
    'Miki': 'Maus',
    'Dzontra': 'Volta',
}

test_data_bad = {
    'Paja': 'wrong',
    'Miki': 'fake_news',
    'Dzontra': 'rocket_man',
}


def authenticate(func):
    def decorated_function(*args, **kwargs):

        password = kwargs.get('password')
        user = kwargs.get('user')

        if not password or not user:
            user, password = args
        if users[user] != hashlib.sha256(password.encode()).hexdigest():
            return 'Wrong password!!!'

        return func(*args, **kwargs)

    return decorated_function


@authenticate
def check_credentials(user, password):
    return f'Welcome {user}!'


def test_users():
    for user, password in test_data_good.items():
        assert check_credentials(user, password) == f'Welcome {user}!'
    print('Test succesful, test_data_good.')
    for user, password in test_data_bad.items():
        assert check_credentials(user, password) == f'Wrong password!!!'
    print('Test succesful, test_data_bad.')

test_users()