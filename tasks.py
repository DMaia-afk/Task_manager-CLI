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

def mark_task(user_id, tasks):
    if user_id in tasks and tasks[user_id]:
        print("Tasks: ")
        print("|"+21*"="+"TASKS"+21*"="+"|")
        for idx, (task, status) in enumerate(tasks[user_id], 1):
            print(f"{idx}. {task} - {status}")
        print("|" + 47*"=" + "|")
        choice = int(input("Enter the task number to mark as completed: "))
        if 1 <= choice <= len(tasks[user_id]):
            tasks[user_id][choice - 1][1] = "completed"
            print(f'Task "{tasks[user_id][choice - 1][0]}" marked as completed!')
        else:
            print("Invalid option.")
    else:
        print("No tasks found for this user.")

def remove_task(user_id, tasks):
    if user_id in tasks and tasks[user_id]:
        print("Tasks:")
        for idx, (task, status) in enumerate(tasks[user_id], 1):
            print(f"{idx}. {task} - {status}")
        try:
            choice = int(input("Enter the task number to remove:"))
            if 1 <= choice <= len(tasks[user_id]):
                removed = tasks[user_id].pop(choice - 1)
                print(f'Task "{removed[0]}" successfully removed!')
                if not tasks[user_id]:
                    del tasks[user_id]
            else:
                print("Invalid option.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("No tasks found for this user.")

def question_verification():
    return input("Do you want to continue?[Y/N}\n-> ").upper()
