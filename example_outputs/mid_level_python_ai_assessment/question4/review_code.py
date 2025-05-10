def login_user(db, username, password):
    user = db.get(username)
    if not user:
        return False
    if user.password == password:
       db.record_login(username)
       return True
    else:
       return False


def handle_request(request, db):
    token = request.get("auth_token")
    username, password = decrypt(token)
    if login_user(db, username, password):
        return {"status": 200, "data": "Welcome"}
    else:
        return {"status": 401, "data": "Unauthorized"}
