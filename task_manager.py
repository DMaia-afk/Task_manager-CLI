from menus import *

users = {}
start_form = "yes"
print(users)

option = main_login()

while start_form == "yes" and option=="L"or option=="C":
    if option=="L":
        login_menu(users)
        if login_menu == False:
            print("Unespected error!!!")
        else:
            main_login(users['user_name'])



    elif option=="C":
        create_menu(users=users)
        print(users)  
        option = main_login()

    
    
    ## Continuar com a lógica
    else:
        break



