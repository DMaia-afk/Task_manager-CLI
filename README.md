# Task Manager CLI

A simple and interactive Command Line Interface (CLI) Task Manager built with Python. This application allows you to manage your daily tasks and user accounts, storing all data securely in JSON files.

## Features

- **User Registration & Login:**  
  Create a new account or log in with your credentials. Each user has a unique ID.

- **Task Management:**  
  - **Add Tasks:** Create new tasks with a default status of "pending".
  - **List Tasks:** View all your tasks and their statuses.
  - **Mark Tasks:** Change the status of a task from "pending" to "completed".
  - **Remove Tasks:** Delete tasks you no longer need.

- **Persistent Storage:**  
  All users and tasks are saved in JSON files, so your data is preserved between sessions.

## How to Use

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/task_manager_cli.git
   cd task_manager_cli
   ```

2. **Install Python (if not already installed):**  
   Make sure you have Python 3.7+.

3. **Run the Application:**
   ```bash
   python task_manager.py
   ```

4. **Main Menu Options:**
   - `<L>`: Login to your account
   - `<C>`: Create a new account
   - `<E>`: Exit the application

5. **Task Menu Options (after login):**
   - `<A>`: Add a new task
   - `<L>`: List all your tasks
   - `<M>`: Mark a task as completed
   - `<R>`: Remove a task
   - `<E>`: Exit to the main menu

## File Structure

- `task_manager.py` — Main entry point for the application.
- `menus.py` — Handles menu displays and user prompts.
- `login.py` — User authentication and registration logic.
- `tasks.py` — Functions for adding, listing, marking, and removing tasks.
- `data.py` — Functions for loading and saving data to JSON files.

## Data Storage

- **Users:** Stored in `users.json`
- **Tasks:** Stored in `tasks.json`

## Example

```
---===---===Hello! JOHN!--===---===---===---                 
---===---===Welcome to CLI Task Manager===---===---
<A> - Add a new
<L> - List 
<M> - Mark
<R> - Remove
<E> - Exit
-> 
```

## License

This project is licensed under the MIT License.

---

Feel free to contribute or suggest improvements!
