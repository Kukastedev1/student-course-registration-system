import json
import os
from models.user import User


DATA_FILE = "data/users.json"


class AuthService:

    @staticmethod
    def load_users():
        if not os.path.exists(DATA_FILE):
            return []

        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            return [User.from_dict(user) for user in data]

    @staticmethod
    def save_users(users):
        with open(DATA_FILE, "w") as file:
            json.dump([user.to_dict() for user in users], file, indent=4)

    @staticmethod
    def register(username, password):
        users = AuthService.load_users()

        # check if username already exists
        for user in users:
            if user.username == username:
                return "Username already exists!"

        new_id = len(users) + 1
        new_user = User(new_id, username, password)
        users.append(new_user)

        AuthService.save_users(users)
        return "User registered successfully!"

    @staticmethod
    def login(username, password):
        users = AuthService.load_users()

        for user in users:
            if user.username == username and user.check_password(password):
                return user

        return "Invalid username or password!"