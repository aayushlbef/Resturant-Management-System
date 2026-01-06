from py_files.chef import chef_to_do
from py_files.customer import customer_to_do
from py_files.manager import manager_to_do
from py_files.validation import *
from py_files.administrator import admin_to_do
from py_files.functions import *

def credentials_checker(role_no, file_location): #Function which read administator txt file and retrive username and password and send them to checker function
    attempts = 3
    while attempts > 0:
        username, password = login()
        with open(file_location, "r") as file:
            stored_user = [eval(line.strip()) for line in file]
        for user in stored_user:
            if user["username"] == username and user["password"] == password:
                if role_no == "1":
                    admin_to_do(username, password) #Go to Administrator Panal
                elif role_no == "2":
                    manager_to_do(username, password) #Go to Manager Panal
                elif role_no == "3":
                    chef_to_do(username, password) #Go to Chef Panal
                elif role_no == "4":
                    customer_to_do(username, password) #Go to Customer Panal
                return  # Exit after successful login
        # If we reach here, login failed
        attempts -= 1 #subtract 1 from attempts
        if attempts > 0:
            print(f"\nInvalid credentials. You have {attempts} attempts remaining.\n")
        else:
            print("\nLogin limit exceeded. Login unsuccessful!\n")
            exit("\tThank You! for Using our Program") #exit program when limit exceed.

def customer_register(role_no, file_location):
    full_name = profile_full_name()
    email = profile_email()
    age = profile_age()
    phone_number = profile_phone_num()
    username, password = login()

    with open(file_location, "r") as costm_r: #Opening customer.txt file to read all content and verify if usename and passwor is in content or not.
        stored_user = [eval(line.strip()) for line in costm_r] #Read then content inside the customer.txt
        for user in stored_user:
            if user["username"] == username:
                print("Username already exit!")
                customer_register(role_no, file_location)

        with open(file_location, "a") as costm_w: #If user is not registered then add them to customer.txt
            dict = {"Full Name": full_name, "Email": email, "age": age, "Phone Number": phone_number, "username": username, "password": password}
            costm_w.write(str(dict))
            costm_w.write("\n")
            print("User successfully registered!")
        login_navigation = input("\nPress 'Enter' to go to login page: ")
        print("")
        if login_navigation.lower() == "": #ask user to goto login page or not
            credentials_checker(role_no, file_location)
        else:
            exit("You have Pressed something else, So.... Thank You for using Our Program.\n")

def login_roles(): #Function which ask user, their role of getting access.
    print("\n\tWelcome to login page.")
    role_no = input('''Enter number according to your role:
                     1.Administrator
                     2.Manager
                     3.Chef
                     4.Customer
                     5.Exit Program\n''') #Taking 1 for administator, 2 for manager, 3 for chef, 4 for customer.
    if role_no == "1" :
        credentials_checker(role_no, file_location="./txt_files/Administrator.txt") #Take no. and file location to credentials_checker
    elif role_no == "2" :
        credentials_checker(role_no, file_location="./txt_files/Manager.txt")
    elif role_no == "3" :
        credentials_checker(role_no, file_location="./txt_files/Chef.txt")
    elif role_no == "4" :
        cos_login = input("Enter '1' for login,\nEnter '2' for register:\n") # Ask user to login or register
        while True: #to let ask user value again and again if they do not enter value 1-2
            if cos_login == "1" :
                credentials_checker(role_no, file_location="./txt_files/Customer.txt")
                break
            elif cos_login == "2" :
                customer_register(role_no, file_location="./txt_files/Customer.txt") #Take no. and file location to Customer register
                break
            else:
                print("\nInvalid Number!")
                cos_login = input("Enter '1' for login,\nEnter '2' for register:\n")
    elif role_no == "5" :
        exit("Thanks for using our program.")
    else:
        print("\nInvalid Number!")
        login_roles() #repeat itself if we do not enter number between 1 - 4.
