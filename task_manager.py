from menus import *

start = True
users = {}
tasks = {}
print(users)

main_option = main_login()

while True:
    if main_option=="L":
        user_id, user_name = login_menu(users)
        if user_name == False:
            print("\nUnespected error!!!")
            main_option = main_login()
        else:
            option = main_menu(user_name=user_name)
            while True:
                if option == "A":
                    add_new_task(user_id, tasks=tasks)
                    print(tasks)
                    verification = question_verification()
                    while verification == "Y":
                        add_new_task(user_id, tasks=tasks)
                        verification = question_verification()
                    else:
                        option = main_menu(user_name=user_name)
                elif option == "L":
                    list_all_tasks(user_id, tasks=tasks)
                    option = main_menu(user_name=user_name)
                elif option == "M":
                    pass
                elif option == "R":
                    pass
                elif option == "E":
                    break
                else:
                    print("Pls! Choose a correctly option")




    elif main_option=="C":
        create_user_menu(users=users)
        print(users)  
        main_option = main_login()

    
    
    ## Continuar com a lógica
    elif main_option=="E":
        break
        
    else:
        print("Pls, send again!")
        main_option = main_login()


