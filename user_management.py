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

def batch_create_users(prefix="user", roles=None, count=5, existing_users=None):
    """Create multiple users with the same prefix and roles.
    
    Args:
        prefix (str): Prefix for usernames
        roles (list): List of roles to assign
        count (int): Number of users to create
        existing_users (list): List to append new users to
    
    Returns:
        list: List of newly created users
    """
    if existing_users is None:
        existing_users = []
    new_users = []
    for _ in range(count):
        user = create_user(prefix=prefix, roles=roles, existing_users=existing_users)
        new_users.append(user)
    return new_users

def main():
    user_list = []
    first = create_user(prefix="admin", roles=["admin"], existing_users=user_list)
    second = create_user(prefix="admin", roles=["user"], existing_users=user_list)
    
    batch1 = batch_create_users(prefix="guest", roles=["guest"], count=3, existing_users=user_list)
    batch2 = batch_create_users(prefix="guest", roles=["guest"], count=2, existing_users=user_list)
    
    print("All users:", [u.username for u in user_list])

if __name__ == "__main__":
    main()
