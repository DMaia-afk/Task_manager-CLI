import random


def main_login():
    return input("""
---===---===---===---===---===---===---===---===---
---===---==Hello! U're welcome to here!!==---===---
---===---===---===---===---===---===---===---===---
                 
<L> - Login in a Account
<C> - Create a Account
<E> - Exit
-> """).upper()

def login_menu(users):
    user_name = input("*Input your name.\n-> ").upper()
    if user_name in users:
        user_password = input("*Input your password: ").upper()
        if user_password == users[user_name][1]:
            print("Login successful!")
            return True and user_name
        else:
            print("Incorrect password.")
            return False
    else:
        print("User not found.")
        return False

def create_menu(users):
    user_id = random.randrange(1, 100, 1)
    user_name = input("*Input your name.\n-> ").upper()
    user_password = input("*Input your password.\n-> ").upper()
    users[user_name] = [user_id, user_password]
    print(f"Usuário criado: {user_name} (ID: {user_id})")
    return users


def main_menu(user_name):
    
    return input(f"""
---===---===---===---===---===---===---===---===---
---===---===Hello! {user_name}!--===---===---===---                 
---===---===Welcome to CLI Task Manager===---===---
---===---===---===---===---===---===---===---===---
<A> - Add a new
<L> - List 
<M> - Mark
<R> - Remove
<S> - Save
<Lo> - Load

-> """).upper()
    

save_menu = """

"""

remove_menu = """

"""

