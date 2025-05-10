import json
import os

DATA_FILE = 'users.json'

def load_users():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE) as f:
        return json.load(f)

def save_users(users):
    with open(DATA_FILE, 'w') as f:
        json.dump(users, f)

def add_user(username, password):
    users = load_users()
    if username in users:
        raise ValueError('User already exists')
    users[username] = password
    save_users(users)
    return True