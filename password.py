import random

def password(length):
    return ''.join([random_char() for i in range(length)])

def random_char():
    # Characters to use in passwords.
    CHARS = "abcdefghijklmnopqrstuvwxyz" + \
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + \
            "1234567890!@#$%^&*()"
    return CHARS[random.randrange(0, len(CHARS))]
