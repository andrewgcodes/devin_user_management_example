import random
import string

class User:
    def __init__(self, username, roles=None):
        self.username = username
        self.roles = roles if roles is not None else []

    def add_role(self, role):
        self.roles.append(role)

def generate_username(prefix="user", taken_usernames=None):
    if taken_usernames is None:
        taken_usernames = []
    username = None
    while username is None or username in taken_usernames:
        suffix = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
        username = f"{prefix}_{suffix}"
    return username

def create_user(prefix="user", roles=None, existing_users=None):
    if existing_users is None:
        existing_users = []
    username = generate_username(prefix=prefix, taken_usernames=[u.username for u in existing_users])
    user = User(username, roles)
    existing_users.append(user)
    return user

def batch_create_users(prefix="user", roles=None, count=5, existing_users=[]):
    new_users = []
    for _ in range(count):
        user = create_user(prefix=prefix, roles=roles, existing_users=existing_users)
        new_users.append(user)
    return new_users

def main():
    user_list = []

    first = create_user(prefix="admin", roles=["admin"], existing_users=user_list)
    second = create_user(prefix="admin", roles=["user"], existing_users=user_list)

    batch1 = batch_create_users(prefix="guest", roles=["guest"], count=3)
    batch2 = batch_create_users(prefix="guest", roles=["guest"], count=2)

    print("Single users:", [u.username for u in user_list])
    print("Batch1 users:", [u.username for u in batch1])
    print("Batch2 users:", [u.username for u in batch2])

if __name__ == "__main__":
    main()
