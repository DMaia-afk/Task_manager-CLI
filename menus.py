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
    for user_id, (name, password) in users.items():
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
    # Definir um código para verificar se há repetido
    user_id = random.randrange(1, 100, 1)
    user_name = input("*Input your name.\n-> ").upper()
    user_password = input("*Input your password.\n-> ")
    users[user_id] = [user_name, user_password]
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
<E> - Exit

-> """).upper()

def add_new_task(user_id, tasks):
    new_task = input("*Input your new task:\n-> ")
    situation = "pending"
    if user_id not in tasks:
        tasks[user_id] = []
    tasks[user_id].append([new_task, situation])
    print(f"Task created: {new_task} (Situation: {situation}) id: {user_id}")

def list_all_tasks(user_id, tasks): 
    if user_id in tasks and tasks[user_id]:
        print("|"+21*"="+"TASKS"+21*"="+"|")
        for idx, (task, status) in enumerate(tasks[user_id], 1):
            print(f"{idx}. {task} - {status}")
        print("|" + 47*"=" + "|")
    else:
        print("No tasks found for this user.")

def mark_task():
    pass

def remove_task():
    pass

def question_verification():
    return input("Do you want to continue?[Y/N}\n-> ").upper()


save_menu = """

"""

remove_menu = """

"""

