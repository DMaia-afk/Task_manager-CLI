from menus import * 
from tasks import *
from login import *
from data import *

users = load_users()
print(users)
tasks = load_tasks()


main_option = main_login()

while True:
    if main_option=="L":
        user_id, user_name = login_menu(users)
        if user_name == False:
            print("\nUnespected error!!!")
            main_option = main_login()
        else:
            option = tasks_menu(user_name=user_name)
            menu_2 = True
            while menu_2:
                if option == "A":
                    add_new_task(user_id, tasks=tasks)
                    print(tasks)
                    verification = question_verification()
                    save_tasks(tasks=tasks)
                    while verification == "Y":
                        add_new_task(user_id, tasks=tasks)
                        verification = question_verification()
                    else:
                        option = tasks_menu(user_name=user_name)
                elif option == "L":
                    list_all_tasks(user_id, tasks=tasks)
                    save_tasks(tasks=tasks)
                    option = tasks_menu(user_name=user_name)
                elif option == "M":
                    mark_task(user_id, tasks=tasks)
                    verification = question_verification()
                    while verification == "Y":
                        mark_task(user_id, tasks=tasks)
                        save_tasks(tasks=tasks)
                        verification = question_verification()
                    else:
                        option = tasks_menu(user_name=user_name)
                elif option == "R":
                    remove_task(user_id, tasks=tasks)
                    save_tasks(tasks=tasks)
                    verification = question_verification()
                    while verification == "Y":
                        remove_task(user_id, tasks=tasks)
                        verification = question_verification()
                    else:
                        option = tasks_menu(user_name=user_name)
                        
                elif option == "E":
                    menu_2 = False
                    save_tasks(tasks=tasks)
                    main_option = main_login()
                    
                else:
                    print("Please! Choose a correctly option")
                    option = tasks_menu(user_name=user_name)

    elif main_option=="C":
        if create_user_menu(users=users):
            save_users(users=users)
            
        main_option = main_login()

    elif main_option=="E":
        break
        
    else:
        print("Please, send again!")
        main_option = main_login()


