import hashlib


class User:
    def __init__(self, username, password, role="student", cleared=False):
        self.username = username
        self.password = password
        self.role = role
        self.cleared = cleared

    def __init__(self, user_id, username, password):
        self.id = user_id
        self.username = username
        self.__password = self.__hash_password(password)

    # Encapsulation: private password
    def __hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password):
        return self.__password == hashlib.sha256(password.encode()).hexdigest()

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "role": self.role,
            "cleared": self.cleared
        }

    @staticmethod
    def from_dict(data):
        user = User(data["username"], data["password"], data["role"], data["cleared"])
        user._User__password = data["password"]
        return user