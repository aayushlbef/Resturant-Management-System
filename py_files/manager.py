from py_files.functions import *

def manager_to_do(username, password):
    print("\n\tWelcome to Manager Panel")
    print("\nWhat You Want to Do:\n")
    to_do = input("Enter '1' to Manage Customer,\nEnter '2' to Manage Menu Categories and Pricing,\nEnter '3' to View Ingreadients list requested,\nEnter '4' to Update own Profile,\nEnter '5' to go to login Page,\nEnter '6' to exit from code.\n\n")
    if to_do == "1":
        manage_customer(username, password)
    elif to_do == "2":
        manage_menu(username, password)
    elif to_do == "3":
        view_ingredients(username, password)
    elif to_do == "4":
        print(update_own_profile(username, password, file_location="./txt_files/Manager.txt"))
        wait_for_enter_and_redirect(lambda: manager_to_do(username, password))
    elif to_do == "5":
        from py_files.login_register import login_roles
        login_roles()
    elif to_do == "6":
        exit("\tThank You! for Using our Program")
    else:
        print("Invlaid Number! Please Input Number (1 - 6)")
        manager_to_do(username, password)

def manage_customer(username, password):
    n = input("\nEnter '1' for add,\nEnter '2' for edit,\nEnter '3' for delete: ")
    if n=="1":
        print(add_role(file_location="./txt_files/Customer.txt"))
    elif n=="2":
        print(edit_role(file_location="./txt_files/Customer.txt"))
    elif n=="3":
        print(delete_role(file_location="./txt_files/Customer.txt"))
    else:
        print("\nInvalid Number!  Please Input Number (1 - 3)")
        manage_customer(username, password)
    wait_for_enter_and_redirect(lambda: manager_to_do(username, password))

def manage_menu(username, password):
    n = input("\nEnter '1' for add menu,\nEnter '2' for edit menu,\nEnter '3' for delete menu:\n\n")
    if n=="1":
        add_menu(username, password)
    elif n=="2":
        edit_menu(username, password)
    elif n=="3":
        delete_menu(username, password)
    else:
        print("\nInvalid Number! Please Input Number (1 - 3)")
        manage_menu(username, password)

def add_menu(username, password):
    category = input("Enter category (e.g., Drinks, Main Course): ")
    item_name = input("Enter item name: ")
    price = input("Enter price: ")
    if category.isalpha():
        if item_name.isalpha():
            if price.isdigit():
                with open("./txt_files/Menu.txt", "a") as f:
                    dict_menu = {"Category":category, "Item": item_name, "Price": price}
                    f.write(str(dict_menu))
                    f.write("\n")
                print("Menu item added.")
            else:
                print("Invalid Price! Pleaase Input valid Price")
                add_menu(username, password)
        else:
            print("Invalid Iteam Name! Please Input only alphabets")
            add_menu(username, password)
    else:
        print("Invalid Category name! Please Input only alphabets")
        add_menu(username, password)
    wait_for_enter_and_redirect(lambda: manager_to_do(username, password))

def edit_menu(username, password):
    category = input("Enter category to edit (e.g., Drinks, Main Course): ")
    item_name = input("Enter item name to edit: ")
    
    if category.isalpha():
        if item_name.isalpha():
            with open("./txt_files/Menu.txt", "r") as f_r:
                stored_menus = [eval(line.strip()) for line in f_r]
            
            menu_found = False
            for menu in stored_menus:
                if menu["Category"] == category and menu["Item"] == item_name:
                    while True:
                        new_category = input("Enter new Category: ")
                        new_item_name = input("Enter new Item: ")
                        new_price = input("Enter new Price: ")
                    
                        if new_category.isalpha() and new_item_name.isalpha() and new_price.isdigit():
                            if new_item_name.isalpha():
                                if new_price.isdigit():
                                    menu["Category"] = new_category
                                    menu["Item"] = new_item_name
                                    menu["Price"] = new_price
                                    menu_found = True
                                    break
                                else:
                                    print("Invalid Price! Pleaase Input valid Price")
                            else:
                                print("Invalid Iteam Name! Please Input only alphabets")
                        else:
                            print("Invalid Category name! Please Input only alphabets")

            if not menu_found:
                print("Menu is not found.")
                edit_menu(username, password)

            # Write the updated list back to the file
            with open("./txt_files/Menu.txt", "w") as f_w:
                for menu in stored_menus:
                    f_w.write(str(menu) + "\n")
            print("Menu updated successfully!")
        else:
            print("Invalid Iteam Name! Please Input only alphabets")
            edit_menu(username, password)
    else:
        print("Invalid Category name! Please Input only alphabets")
        edit_menu(username, password)

    wait_for_enter_and_redirect(lambda: manager_to_do(username, password))

def delete_menu(username, password):
    category = input("Enter category to delete (e.g., Drinks, Main Course): ")
    item_name = input("Enter item name to delete: ")
    
    if category.isalpha():
        if item_name.isalpha():
            with open("./txt_files/Menu.txt", "r") as f_r:
                stored_menus = [eval(line.strip()) for line in f_r]

            menu_found = False
            updated_menus = []

            for menu in stored_menus:
                if menu["Category"] == category and menu["Item"] == item_name:
                    menu_found = True
                    continue  # Skip this menu (i.e., delete)
                updated_menus.append(menu)

            if not menu_found:
                print("Menu is not Found.")
                delete_menu(username, password)

            with open("./txt_files/Menu.txt", "w") as f_w:
                for menu in updated_menus:
                    f_w.write(str(menu) + "\n")

            print("Menu deleted successfully!")
        else:
            print("Invalid Iteam Name! Please Input only alphabets")
            delete_menu(username, password)
    else:
        print("Invalid Category name! Please Input only alphabets")
        delete_menu(username, password)
    wait_for_enter_and_redirect(lambda: manager_to_do(username, password))

def view_ingredients(username, password):
    with open("./txt_files/Ingredients.txt", "r") as f:
        ingredients = [eval(line.strip()) for line in f]

    if not ingredients:
        print(" Ingredient list is empty.")
        wait_for_enter_and_redirect(lambda: manager_to_do(username, password))

    print("\n    Requested Ingredients List:")
    print("-" * 35)
    print(f"{'S.N.'}\t{'Ingredient'}\t{'Quantity'}")
    print("-" * 35)
    for i, item in enumerate(ingredients, 1):
        print(f"{i}\t{item['name']}\t\t{item['quantity']}")
    print("-" * 35)
    wait_for_enter_and_redirect(lambda: manager_to_do(username, password))
