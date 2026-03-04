import hashlib


class User:
    def __init__(self, user_id, username, password, role="student", cleared=False):
        self.id = user_id
        self.username = username
        self.role = role
        self.cleared = cleared
        self.__password = self.__hash_password(password)

    # Encapsulation: private password
    def __hash_password(self, password):
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

    @classmethod
    def from_dict(cls, data):
        user = cls(
            data["id"],
            data["username"],
            "",                          # placeholder — we set the hash directly below
            data.get("role", "student"),
            data.get("cleared", False)
        )
        user._User__password = data["password"]  # restore stored hash directly
        return user