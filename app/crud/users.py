import uuid

# Dummy database local in-memory
DUMMY_DATABASE = {
    uuid.UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"): {
        "id": uuid.UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"),
        "username": "john",
        "role_type": "admin",
        "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$41tsWCGMyVDgd6NYC2FlPg$FjKVdCFEpHGiFpYAzMfrexEKbxHuCkYc23p91LrMxiU" # secret123
    }
}

class CRUDUser:
    def get_user_by_username(self, username: str) -> dict | None:
        # Search user by username in dummy database
        for user in DUMMY_DATABASE.values():
            if user["username"] == username:
                return user
        return None