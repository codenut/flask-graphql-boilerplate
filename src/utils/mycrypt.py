from app import bcrypt


def hashstr(s):
    return bcrypt.generate_password_hash(s).decode('utf-8')


def checkstr(s, h):
    return bcrypt.check_password_hash(s.encode('utf-8'), h.encode('utf-8'))
