def password(length):
    return ''.join([random_char() for i in range(length)])

def random_char():
    return 'a'
