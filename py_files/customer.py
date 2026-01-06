from py_files.functions import *
from datetime import datetime

def customer_to_do(username, password):
    print(f"\n\tWelcome {username} to our Delicious Restaurant")
    to_do = input("Enter '1' to Order food,\nEnter '2' to View order status,\nEnter '3' to Send Feedback to Administrator,\nEnter '4' to Update own Profile,\nEnter '5' to go to login Page,\nEnter '6' to exit from code.\n\n")
    if to_do == "1":
        order_food(username, password)
    elif to_do == "2":
        view_order_status(username, password)
    elif to_do == "3":
        send_feedback(username, password)
    elif to_do == "4":
        print(update_own_profile(username, password, file_location="./txt_files/Customer.txt"))
        wait_for_enter_and_redirect(lambda: customer_to_do(username, password))
    elif to_do == "5":
        from py_files.login_register import login_roles
        login_roles()
    elif to_do == "6":
        exit("\tThank You! for Using our Program")
    else:
        print("\nInvalid Number!  Please Input Number (1 - 6)")
        customer_to_do(username, password)
    
def order_food(username, password):
    n = input("Enter '1' to add order,\nEnter '2' to edit order,\nEnter '3' to delete order.\n\n")
    if n == "1":
        add_order(username, password)
    elif n == "2":
        edit_order(username, password)
    elif n == "3":
        delete_order(username, password)
    else:
        print("\nInvalid Number!  Please Input Number (1 - 3)")
        order_food(username, password)

def add_order(username, password):
    with open("./txt_files/Menu.txt", "r") as f:
        stored_menus = [eval(line.strip()) for line in f]

    print("\n\t--- Menus ---")
    for i, menu in enumerate(stored_menus, start=1):
        print(f"{i}. Category: {menu['Category']},\t Item: {menu['Item']},\t Price: {menu['Price']}")

    item_ordered = False
    choice = input("\nEnter the number of the item you want to order: ")

    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(stored_menus):
            selected_item = stored_menus[choice - 1]
            quantity = input("Enter quantity: ")

            if quantity.isdigit() and int(quantity) > 0:
                quantity = int(quantity)

                order = {
                    "username": username,
                    "Item": selected_item["Item"],
                    "Price": float(selected_item["Price"]),
                    "Quantity": quantity,
                    "Total": float(selected_item["Price"]) * quantity
                }

                with open("./txt_files/temp_order.txt", "a") as o:
                    o.write(str(order) + "\n")

                print("Item added to order.")
                item_ordered = True
            else:
                print("Invalid quantity. Please enter a valid number greater than 0.")
                add_order(username, password)
        else:
            print("Invalid choice number. Please select a valid menu item.")
            add_order(username, password)
    else:
        print("Invalid input. Please enter a valid number.")
        add_order(username, password)

    if item_ordered:
        ask_payment(username, password)


def edit_order(username, password):
    with open("./txt_files/temp_order.txt", "r") as f:
        orders = [eval(line.strip()) for line in f]

    # Filter orders for current user
    user_orders = [order for order in orders if order["username"] == username]

    if not user_orders:
        print("You have no items in your order.")
        customer_to_do(username, password)

    # Display user's orders
    print("\nYour Current Orders:")
    for i, order in enumerate(user_orders, start=1):
        print(f"{i}. Item: {order['Item']}, Quantity: {order['Quantity']}, Total: {order['Total']}")

    choice = input("Enter the number of the item you want to edit: ")

    if choice.isdigit() and 1 <= int(choice) <= len(user_orders):
        index = int(choice) - 1
        selected_order = user_orders[index]

        new_quantity = input("Enter new quantity: ")
        if new_quantity.isdigit() and int(new_quantity) > 0:
            new_quantity = int(new_quantity)
            selected_order["Quantity"] = new_quantity
            selected_order["Total"] = new_quantity * selected_order["Price"]

            # Update all orders
            updated_orders = []
            for order in orders:
                if order["username"] == username and order["Item"] == selected_order["Item"]:
                    updated_orders.append(selected_order)
                else:
                    updated_orders.append(order)

            with open("./txt_files/temp_order.txt", "w") as f:
                for order in updated_orders:
                    f.write(str(order) + "\n")

            print("Order updated successfully.")
            ask_payment(username, password)
        else:
            print("Invalid quantity. Please enter a valid number greater than 0.")
            edit_order(username, password)
    else:
        print("Invalid choice. Please Input Order Number.")
        edit_order(username, password)


def delete_order(username, password):
    with open("./txt_files/temp_order.txt", "r") as f:
        orders = [eval(line.strip()) for line in f]

    user_orders = [order for order in orders if order["username"] == username]

    if not user_orders:
        print("You have no items in your order.")
        return

    print("\nYour Current Orders:")
    for i, order in enumerate(user_orders, start=1):
        print(f"{i}. Item: {order['Item']}, Quantity: {order['Quantity']}, Total: {order['Total']}")

    choice = input("Enter the number of the item you want to delete: ")

    if choice.isdigit() and 1 <= int(choice) <= len(user_orders):
        index = int(choice) - 1
        item_to_delete = user_orders[index]

        new_orders = []
        for order in orders:
            if not (order["username"] == username and order["Item"] == item_to_delete["Item"]):
                new_orders.append(order)

        with open("./txt_files/temp_order.txt", "w") as f:
            for order in new_orders:
                f.write(str(order) + "\n")

        print("Item removed from order.")
        ask_payment(username, password)
    else:
        print("Invalid choice. Please choose order Number.")
        delete_order(username, password)


def ask_payment(username, password):
    choice = input("Do you want to proceed to payment? (yes/no): ").lower()
    if choice == "yes":
        payment(username, password)
    elif choice == "no":
        wait_for_enter_and_redirect(lambda: customer_to_do(username, password))
    else:
        print("Invalid Input! Please input yes or no.")
        ask_payment(username, password)


def payment(username, password):
    with open("./txt_files/temp_order.txt", "r") as f:
        all_orders = [eval(line.strip()) for line in f]

    orders = [order for order in all_orders if order["username"] == username]

    if not orders:
        print("You have no orders to pay.")
        wait_for_enter_and_redirect(lambda: add_order(username, password))

    total_amount = sum(order["Total"] for order in orders)
    print("\nYour Order Summary:")
    for order in orders:
        print(f"{order['Quantity']} x {order['Item']} @ {order['Price']} = Rs. {order['Total']}")

    print(f"\nTotal amount to be paid: Rs. {total_amount}")
    confirm = input("Confirm payment? (yes/no): ").lower()

    if confirm == "yes":
        print(" Payment successful! Thank you for your order.")

        # Mark orders as Paid
        for order in orders:
            order["status"] = "Paid"
            order["chef"] = "Aayush"
            order["date"] = datetime.today().strftime("%Y-%m-%d")

        # Save Paid orders to OrderHistory.txt
        with open("./txt_files/OrderHistory.txt", "a") as f_hist:
            for order in orders:
                f_hist.write(str(order) + "\n")

        # Remove paid orders from temp_order.txt (keep others)
        remaining_orders = [order for order in all_orders if order["username"] != username]

        with open("./txt_files/temp_order.txt", "w") as f_temp:
            for order in remaining_orders:
                f_temp.write(str(order) + "\n")

    elif confirm == "no":
        print("Payment cancelled. Order is saved as pending (Unpaid).")

        updated_orders = []
        for order in all_orders:
            if order["username"] == username:
                order["status"] = "Unpaid"
            updated_orders.append(order)

        with open("./txt_files/temp_order.txt", "w") as f:
            for order in updated_orders:
                f.write(str(order) + "\n")
    else:
        print("Invalid Input! Please input yes or no.")
        payment(username, password)

    wait_for_enter_and_redirect(lambda: customer_to_do(username, password))

def view_order_status(username, password):
    print(f"\n🛒 Order Status for: {username}")

    # Load and filter pending orders
    pending_orders = []
    with open("./txt_files/temp_order.txt", "r") as f:
        for line in f:
            order = eval(line.strip())
            if order["username"] == username:
                pending_orders.append(order)

    # Load and filter completed orders
    completed_orders = []
    with open("./txt_files/OrderHistory.txt", "r") as f:
        for line in f:
            order = eval(line.strip())
            if order["username"] == username:
                completed_orders.append(order)

    if not pending_orders and not completed_orders:
        print(" No order found for your username.")
        wait_for_enter_and_redirect(lambda: customer_to_do(username, password))

    # Display pending orders
    if pending_orders:
        print("\n Pending Orders:")
        for i, order in enumerate(pending_orders, 1):
            print(f"{i}. Item: {order['Item']} | Qty: {order['Quantity']} | Total: Rs.{order['Total']}")
    else:
        print("\n No Pending Orders.")

    # Display completed orders
    if completed_orders:
        print("\n Completed Orders:")
        for i, order in enumerate(completed_orders, 1):
            print(f"{i}. Item: {order['Item']} | Qty: {order['Quantity']} | Total: Rs.{order['Total']}")
    else:
        print("\n No Completed Orders yet.")

    wait_for_enter_and_redirect(lambda: customer_to_do(username, password))

def send_feedback(username, password):
    with open("./txt_files/feedback.txt", "a") as f:
        feedback = input("\nEnter your feedback: ")
        if feedback == "":
            print("Feedback cannot be empty!")
            send_feedback(username, password)
        dict_cust = {"username":username,"feedback": feedback}
        f.write(str(dict_cust))
        f.write("\n")
        print("\n\tThanks for your feedback!")

    wait_for_enter_and_redirect(lambda: customer_to_do(username, password))