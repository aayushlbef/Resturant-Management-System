from py_files.functions import *
from datetime import datetime

def chef_to_do(username, password):
    print("\n\tWelcome to Chef Panel")
    print("\nWhat You Want to Do:\n")
    to_do = input("Enter '1' to View orders,\nEnter '2' to Update orders,\nEnter '3' to Request Ingredients,\nEnter '4' to Update own Profile,\nEnter '5' to go to login Page,\nEnter '6' to exit from code.\n\n")

    if to_do == "1":
        view_orders(username, password)
    elif to_do == "2":
        update_orders(username, password)
    elif to_do == "3":
        request_ingredients(username, password)
    elif to_do == "4":
        print(update_own_profile(username, password, file_location="./txt_files/Chef.txt"))
        wait_for_enter_and_redirect(lambda: chef_to_do(username, password))
    elif to_do == "5":
        from py_files.login_register import login_roles
        login_roles()
    elif to_do == "6":
        exit("\tThank You! for Using our Program")
    else:
        print("\nInvalid Number!  Please Input Number (1 - 6)")
        chef_to_do(username, password)

def view_orders(username, password):
    n = input("\nEnter '1' to View Current Orders,\nEnter '2' to View Order History\n\n")
    if n == "1":
        view_current_orders(username, password)
    elif n == "2":
        view_order_history(username, password)
    else:
        print("Invalid Number!  Please Input Number (1 - 2)")
        view_orders(username, password)

def view_current_orders(username, password):
    print("\nPending Orders:\n")
    with open("./txt_files/temp_order.txt", "r") as f:
        orders = [eval(line.strip()) for line in f]

    if not orders:
        print("No current pending orders.")
        wait_for_enter_and_redirect(lambda: chef_to_do(username, password))

    for i, order in enumerate(orders, start=1):
        print(f"{i}. Customer: {order['username']}, Item: {order['Item']}, Quantity: {order['Quantity']}, Total: Rs.{order['Total']}")

    wait_for_enter_and_redirect(lambda: chef_to_do(username, password))

def view_order_history(username, password):
    print("\n\t--- All Orders Placed by Customers ---\n")
    with open("./txt_files/OrderHistory.txt", "r") as f:
        orders = [eval(line.strip()) for line in f]

    if not orders:
        print("No orders have been placed yet.")
        wait_for_enter_and_redirect(lambda: chef_to_do(username, password))

    user_grouped = {}
    for order in orders:
        user = order["username"]
        if user not in user_grouped:
            user_grouped[user] = []
        user_grouped[user].append(order)

    for user, user_orders in user_grouped.items():
        print(f"\n Username: {user}")
        total = 0
        for o in user_orders:
            print(f" - {o['Quantity']} x {o['Item']} @ Rs. {o['Price']} = Rs. {o['Total']}")
            total += o['Total']
        print(f"   ➤ Total Bill: Rs. {total}")
        print("-" * 40)
    wait_for_enter_and_redirect(lambda: chef_to_do(username, password))

def update_orders(username, password):
    print("\nEnter '1' to Mark Pending Order to Completed,\nEnter '2' to Move COMPLETED order back to PENDING")
    n = input("Enter your choice (1 or 2): ")

    if n == "1":
        with open("./txt_files/temp_order.txt", "r") as f:
            pending_orders = [eval(line.strip()) for line in f]

        if not pending_orders:
            print("No pending orders to update.")
            wait_for_enter_and_redirect(lambda: chef_to_do(username, password))

        print("\n Pending Orders:")
        for i, order in enumerate(pending_orders, 1):
            print(f"{i}. {order['username']} | {order['Item']} | Qty: {order['Quantity']} | Total: Rs.{order['Total']}")

        selected = input("Enter the order number to mark as COMPLETED: ")
        if not selected.isdigit() or not (1 <= int(selected) <= len(pending_orders)):
            print("\nInvalid Number! Please Input Order Number.")
            update_orders(username, password)

        completed_order = pending_orders.pop(int(selected) - 1)
        completed_order["status"] = "Paid"
        completed_order["chef"] = username
        completed_order["date"] = datetime.today().strftime("%Y-%m-%d")

        with open("./txt_files/OrderHistory.txt", "a") as f:
            f.write(str(completed_order) + "\n")

        with open("./txt_files/temp_order.txt", "w") as f:
            for order in pending_orders:
                f.write(str(order) + "\n")

        print(f"\n Order from {completed_order['username']} marked as COMPLETED.")

    elif n == "2":
        with open("./txt_files/OrderHistory.txt", "r") as f:
            completed_orders = [eval(line.strip()) for line in f]

        if not completed_orders:
            print("No any completed orders to Moved.")
            wait_for_enter_and_redirect(lambda: chef_to_do(username, password))

        print("\n Completed Orders:")
        for i, order in enumerate(completed_orders, 1):
            print(f"{i}. {order['username']} | {order['Item']} | Qty: {order['Quantity']} | Rs.{order['Total']}")

        selected = input("Enter the order number to revert to PENDING: ")
        if not selected.isdigit() or not (1 <= int(selected) <= len(completed_orders)):
            print("Invalid selection! Please Input Order Number")
            update_orders(username, password)

        reverted_order = completed_orders.pop(int(selected) - 1)

        with open("./txt_files/temp_order.txt", "a") as f:
            f.write(str(reverted_order) + "\n")

        with open("./txt_files/OrderHistory.txt", "w") as f:
            for order in completed_orders:
                f.write(str(order) + "\n")

        print(f"\n Order from {reverted_order['username']} Moved back to PENDING.")
    else:
        print("\nInvalid Number!  Please Input Number (1 - 2)")
        update_orders(username, password)

    wait_for_enter_and_redirect(lambda: chef_to_do(username, password))

def request_ingredients(username, password):
    n = input("\nEnter '1' for add ingredients,\nEnter '2' for edit ingredients,\nEnter '3' for delete ingredients:\n\n")
    if n == "1":
        add_ingredients(username, password)
    elif n == "2":
        edit_ingredients(username, password)
    elif n == "3":
        delete_ingredients(username, password)
    else:
        print("\nInvalid Number! Please Input Number (1 - 3)")
        request_ingredients(username, password)

def add_ingredients(username, password):
    name = input("Enter ingredient name: ").strip().capitalize()
    quantity = input("Enter quantity (e.g. 2 kg): ").strip()

    if name == "" or quantity == "":
        print("Ingredient name and quantity cannot be empty!")
        add_ingredients(username, password)

    ingredients = load_ingredients()
    for item in ingredients:
        if item["name"].lower() == name.lower():
            print(" Ingredient already exists.")
            add_ingredients(username, password)

    ingredients.append({"name": name, "quantity": quantity})
    save_ingredients(ingredients)
    print(" Ingredient added successfully.")

    wait_for_enter_and_redirect(lambda: chef_to_do(username, password))

def edit_ingredients(username, password):
    ingredients = load_ingredients()
    if not ingredients:
        print("No ingredients found.")
        chef_to_do(username, password)

    print("\n Ingredients:")
    for i, item in enumerate(ingredients, 1):
        print(f"{i}. {item['name']} - {item['quantity']}")

    choice = input("Enter the number of ingredient to edit: ")
    if not choice.isdigit() or not (1 <= int(choice) <= len(ingredients)):
        print("Invalid selection. Please Input Ingreadient Number.")
        edit_ingredients(username, password)

    new_quantity = input(f"Enter new quantity for {ingredients[int(choice) - 1]['name']}: ")
    if new_quantity.strip() == "":
        print("Quantity cannot be empty.")
        edit_ingredients(username, password)
    ingredients[int(choice) - 1]["quantity"] = new_quantity
    save_ingredients(ingredients)
    print(" Ingredient updated successfully.")

    wait_for_enter_and_redirect(lambda: chef_to_do(username, password))

def delete_ingredients(username, password):
    ingredients = load_ingredients()
    if not ingredients:
        print("No ingredients found.")
        chef_to_do(username, password)

    print("\n Ingredients:")
    for i, item in enumerate(ingredients, 1):
        print(f"{i}. {item['name']} - {item['quantity']}")

    choice = input("Enter the number of ingredient to delete: ")

    if not choice.isdigit() or not (1 <= int(choice) <= len(ingredients)):
        print("Invalid selection! Please Input Ingredient Number.")
        delete_ingredients(username, password)

    if not (1 <= int(choice) <= len(ingredients)):
        print("Invalid selection! Please Input Ingredient Number.")
        delete_ingredients(username, password)

    removed = ingredients.pop(int(choice) - 1)
    save_ingredients(ingredients)
    print(f"🗑️ Ingredient '{removed['name']}' deleted successfully.")

    wait_for_enter_and_redirect(lambda: chef_to_do(username, password))
