from py_files.functions import *

def admin_to_do(username, password): #take username and password as an argument.
    print("\n\tWelcome to Admin Panel")
    print("\nWhat You Want to Do:\n")
    to_do = input("Enter '1' to Manage Staff,\nEnter '2' to View sales report based on month, chef,\nEnter '3' to View feedback sent by customers,\nEnter '4' to Update own Profile,\nEnter '5' to go to login Page,\nEnter '6' to exit from code.\n\n") 
    if to_do == "1":
        staff_to_do = input("\nEnter '1' to manage Manager,\nEnter '2' to manage Chef:\n\n") #ask user to choose between manager and chef
        while True:
            if staff_to_do == "1":
                manage_manager(username, password) #Go to manage_manager() with username and password argument.
                break
            elif staff_to_do == "2":
                manage_chef(username, password) #Go to manage_chef() with username and password argument.
                break
            else:
                print("\n\nInvalid Number! Please Enter Number (1 or 2)")
                staff_to_do = input("\nEnter '1' to manage Manager,\nEnter '2' to manage Chef\n") #Again ask for choice if invalid input is given
    elif to_do == "2":
        view_sales_report(username, password)
    elif to_do == "3":
        view_feedback(username, password)
    elif to_do == "4":
        print(update_own_profile(username, password, file_location="./txt_files/Administrator.txt"))
        wait_for_enter_and_redirect(lambda: admin_to_do(username, password))
    elif to_do == "5":
        from py_files.login_register import login_roles
        login_roles()
    elif to_do == "6":
        exit("\tThank You! for Using our Program") #exit the program
    else:
        print("\nInvalid Number! Please Input Number (1 - 6)")
        admin_to_do(username, password) #repeat itself if we do not enter number between 1 - 6.

def manage_manager(username, password):
    n = input("\nEnter '1' for add,\nEnter '2' for edit,\nEnter '3' for delete:\n\n")
    if n=="1":
        print(add_role(file_location="./txt_files/Manager.txt"))
    elif n=="2":
        print(edit_role(file_location="./txt_files/Manager.txt"))
    elif n=="3":
        print(delete_role(file_location="./txt_files/Manager.txt"))
    else:
        print("\nInvalid Number! Please Input Number (1 - 3)")
        manage_manager(username, password)
    wait_for_enter_and_redirect(lambda: admin_to_do(username, password))

def manage_chef(username, password):
    n = input("\nEnter '1' for add,\nEnter '2' for edit,\nEnter '3' for delete:\n\n")
    if n=="1":
        print(add_role(file_location="./txt_files/Chef.txt"))
    elif n=="2":
        print(edit_role(file_location="./txt_files/Chef.txt"))
    elif n=="3":
        print(delete_role(file_location="./txt_files/Chef.txt"))
    else:
        print("\nInvalid Number!  Please Input Number (1 - 3)")
        manage_chef(username, password)
    wait_for_enter_and_redirect(lambda: admin_to_do(username, password))
    
def view_sales_report(username, password):
    while True:
        n = input("\n\nEnter '1' to View Sales Report By Month,\nEnter '2' to View Sales By Chef\n\n")
        if n == "1":
            view_sales_by_month(username, password)
            break
        elif n == "2":
            view_sales_by_chef(username, password)
            break
        else:
            print("\n Invalid input! Please enter '1' or '2'.")

def load_completed_orders():
    with open("./txt_files/OrderHistory.txt", "r") as f:
        return [eval(line.strip()) for line in f if eval(line.strip()).get("status") == "Paid"]

def view_sales_by_month(username, password):
    orders = load_completed_orders()
    if not orders:
        print(" There are no orders yet.")
        admin_to_do(username, password)

    while True:
        month = input("Enter Year and Month (YYYY-MM): ").strip()
        if is_valid_year_month(month):
            break
        else:
            print("Invalid format! Please enter in YYYY-MM format.")

    monthly_orders = [o for o in orders if o.get("date", "").startswith(month)]

    if not monthly_orders:
        print(f"No sales found for {month}.")
    else:
        total = sum(order["Total"] for order in monthly_orders)
        print(f"\n Sales Report for {month}:")
        for o in monthly_orders:
            print(f"- {o['date']} | {o['Item']} x{o['Quantity']} = Rs. {o['Total']} (Chef: {o.get('chef', 'N/A')})")
        print(f"\n Total Sales: Rs. {total}")

    wait_for_enter_and_redirect(lambda: admin_to_do(username, password))

def view_sales_by_chef(username, password):
    orders = load_completed_orders()
    if not orders:
        print(" There are no orders yet.")
        admin_to_do(username, password)

    while True:
        chef_name = input("Enter chef name: ").strip().lower()
        if chef_name.isalpha():
            break
        else:
            print("Invalid chef name! Please enter alphabetic characters only.")

    chef_orders = [o for o in orders if o.get("chef", "").lower() == chef_name]

    if not chef_orders:
        print(f"No sales found for chef '{chef_name}'.")
    else:
        total = sum(order["Total"] for order in chef_orders)
        print(f"\n Sales Report for Chef {chef_name.capitalize()}:")
        for o in chef_orders:
            print(f"- {o['date']} | {o['Item']} x{o['Quantity']} = Rs. {o['Total']}")
        print(f"\n Total Sales: Rs. {total}")

    wait_for_enter_and_redirect(lambda: admin_to_do(username, password))

def view_feedback(username, password):
    n = input("\nEnter '1' to See all Feedback,\nEnter '2' to see Specific User Feedback:\n\n")
    with open("./txt_files/feedback.txt", "r") as f:
        stored_feedback = [eval(line.strip()) for line in f]
        if not stored_feedback:
            print("There is no feedback yet.")   
        if n == "1":
            for feedback1 in stored_feedback:
                print('\t' + feedback1["username"] +'=\t'+ feedback1["feedback"])
        elif n == "2":
            count = 0
            while True:
                specified_user = input("Enter the username of that specific user: ").strip().lower()
                if specified_user.isalpha():
                    print("\n")
                    for feedback2 in stored_feedback:
                        if feedback2["username"].strip().lower() == specified_user:
                            print('\t' + feedback2["username"] + ' =\t' + feedback2["feedback"])
                            count +=1
                    break
                else:
                    print("Invalid Name! Please Input only alphabets.")
            if count==0:
                print("No feedback found for that user.")
        else:
            print("\nInvalid Number! Please Input Number (1 - 2)")
            view_feedback(username, password)
    wait_for_enter_and_redirect(lambda: admin_to_do(username, password))

