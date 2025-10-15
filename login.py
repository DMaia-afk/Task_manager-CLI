import random

def login_menu(users):
    user_name = input("*Input your name.\n-> ").upper()
    for user_id,(name,password) in users.items():
        if user_name == name:
            user_password = input("*Input your password: ")
            if user_password == password:
                print("Login successful!")
                return user_id, user_name
            else:
                print("Incorrect password.")
                return "O", False
    print("\nUser not found.")
    return "O", False

def create_user_menu(users):
    while True:
        user_id = random.randrange(1, 101, 1)
        if user_id not in users:
            break  
    user_name = input("*Input your name.\n-> ").upper()
    user_password = input("*Input your password.\n-> ")
    users[user_id] = [user_name, user_password]
    print(f"User created: {user_name} (ID: {user_id})")
    return users
