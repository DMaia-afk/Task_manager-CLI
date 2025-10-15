import json
from pathlib import Path


_archive_users = "users.json"
_archive_tasks = "tasks.json"
data_folder = Path("data")
data_path_users = data_folder / _archive_users
data_path_tasks = data_folder / _archive_tasks


def load_users():
    with open(data_path_users, 'r') as file:
        data = json.load(file)
    return data

def save_users(users):
    with open(data_path_users,'w') as file:
        data_save = json.dump(users, file)
    return data_save

def load_tasks():
    with open(data_path_tasks, 'r') as file:
        data = json.load(file)
    return data

def save_tasks(tasks):
    with open(data_path_tasks, "w") as file:
        data_save = json.dump(tasks, file)
    return data_save