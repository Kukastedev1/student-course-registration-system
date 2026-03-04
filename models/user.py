import hashlib


class User:
    def __init__(self, user_id, username, password, role="student", cleared=False):
        self.id = user_id
        self.username = username
        self.role = role
        self.cleared = cleared
        self.__password = self._hash_password(password)

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password):
        return self.__password == hashlib.sha256(password.encode()).hexdigest()

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.__password,
            "role": self.role,
            "cleared": self.cleared
        }

    @staticmethod
    def from_dict(data):
        user = User(
            data.get("id"),
            data.get("username"),
            data.get("password"),
            data.get("role", "student"),
            data.get("cleared", False)
        )
        # Prevent re-hashing password
        user._User__password = data.get("password")
        return user