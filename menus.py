
def main_login():
    return input("""
---===---===---===---===---===---===---===---===---
---===---==Hello! U're welcome to here!!==---===---
---===---===---===---===---===---===---===---===---
                 
<L> - Login in a Account
<C> - Create a Account
<E> - Exit
-> """).upper()

def tasks_menu(user_name):
    
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
