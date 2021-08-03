import hashlib

users = {
    '8C6976E5B5410415BDE908BD4DEE15DFB167A9C873FC4BB8A81F6F2AB448A918':
        'A665A45920422F9D417E4867EFDC4FB8A04A1F3FFF1FA07E998E86F7F7A27AE3',  # admin
    '04F8996DA763B7A969B1028EE3007569EAF3A635486DDAB211D512C85B9DF8FB':  # user
        'A665A45920422F9D417E4867EFDC4FB8A04A1F3FFF1FA07E998E86F7F7A27AE3'}


def authentication_user(login, password):
    user_exists = False

    login_byte = login.encode('utf-8')
    login_hash = hashlib.sha256(login_byte).hexdigest()

    password_byte = password.encode('utf-8')
    password_hash = hashlib.sha256(password_byte).hexdigest()

    access_data = 0

    for login in users:
        if access_data == 1:
            break

        if login_hash in login:
            access_data += 1
            if access_data == 1 and password_hash == users[login]:
                user_exists = True  # Доступ получен данные верны

    return user_exists
