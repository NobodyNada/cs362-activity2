import secrets

def password(length):
    return secrets.token_urlsafe(length)
