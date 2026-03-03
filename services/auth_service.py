import json
import os
from models.user import User

DATA_FILE = "data/users.json"


class AuthService:

    @staticmethod
    def load_users():
        """Load users from JSON and convert to User objects."""
        if not os.path.exists(DATA_FILE):
            return []

        with open(DATA_FILE, "r") as file:
            try:
                data = json.load(file)
                return [User.from_dict(user) for user in data]
            except json.JSONDecodeError:
                return []

    @staticmethod
    def save_users(users):
        """Save list of User objects to JSON."""
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

        with open(DATA_FILE, "w") as file:
            json.dump([user.to_dict() for user in users], file, indent=4)

    @staticmethod
    def register(username, password):
        """Register a new user with auto-generated student ID."""
        users = AuthService.load_users()

        # Prevent duplicate usernames
        for user in users:
            if user.username == username:
                return "Username already exists!"

        new_id = len(users) + 1

        # Generate student ID like ST001, ST002, ST003...
        student_id = f"ST{str(new_id).zfill(3)}"

        new_user = User(new_id, username, password, student_id)
        users.append(new_user)

        AuthService.save_users(users)

        return f"User registered successfully! Your student ID is {student_id}"

    @staticmethod
    def login(username, password):
        """Authenticate user and return User object if valid."""
        users = AuthService.load_users()

        for user in users:
            if user.username == username and user.check_password(password):
                return user   # return User object

        return None  # return None instead of string