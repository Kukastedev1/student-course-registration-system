import json
import os
from models.user import User

DATA_FILE = "data/users.json"


class AuthService:

    @staticmethod
    def load_users():
        """Load users from JSON file."""
        if not os.path.exists(DATA_FILE):
            return []

        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            # convert each dictionary to a User object
            return [User.from_dict(user) for user in data]

    @staticmethod
    def save_users(users):
        """Save list of User objects to JSON file."""
        with open(DATA_FILE, "w") as file:
            json.dump([user.to_dict() for user in users], file, indent=4)

    @staticmethod
    def register(username, password):
        """Register a new user. Default cleared=False."""
        users = AuthService.load_users()

        # check if username already exists
        for user in users:
            if user.username == username:
                return "Username already exists!"

        new_id = len(users) + 1
        new_user = User(new_id, username, password, cleared=False)
        users.append(new_user)
        AuthService.save_users(users)
        return "User registered successfully! Awaiting admin clearance."

    @staticmethod
    def login(username, password):
        """Login a user if credentials match and user is cleared."""
        users = AuthService.load_users()

        for user in users:
            if user.username == username and user.check_password(password):
                if not user.cleared:
                    return "Access denied. Awaiting admin clearance."
                return user

        return "Invalid username or password!"

    @staticmethod
    def clear_student(username):
        """Admin can clear a student to allow login and enrollment."""
        users = AuthService.load_users()

        for user in users:
            if user.username == username:
                user.cleared = True
                AuthService.save_users(users)
                return f"Student '{username}' cleared successfully."

        return "Student not found."