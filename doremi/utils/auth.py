import random
import string


def make_random_string(length=32):
    return "".join(random.sample(string.ascii_letters + string.digits, length))


def make_vcode(length=6):
    return "".join(random.sample(string.digits, length))


def make_token(length=32):
    token = make_random_string(length)
