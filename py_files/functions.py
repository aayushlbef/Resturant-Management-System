from py_files.validation import *

def update_own_profile(username, password, file_location):

    with open(file_location, "r") as f_r:
        stored_users = [eval(line.strip()) for line in f_r]

    user_found = False
    for user in stored_users:
        if user["username"] == username and user["password"] == password:
            print("*"*10 + "New Profile" + "*"*10)
            new_full_name = profile_full_name()
            new_email = profile_email()
            new_age = profile_age()
            new_phone_number = profile_phone_num()
            new_username, new_password = login()

            user["Full Name"] = new_full_name
            user["Email"] = new_email
            user["age"] = new_age
            user["Phone Number"] = new_phone_number
            user["username"] = new_username
            user["password"] = new_password
            user_found = True
            break

    if not user_found:
        return ("Incorrect username or password")
        
    with open(file_location, "w") as f_w:
        for user in stored_users:
            f_w.write(str(user) + "\n")

    return ("User updated successfully!")


def profile_full_name():
    while True:
        name = input("Enter your Full Name: ").strip()
        name_parts = name.split()

        # Validate each part with user_name function
        if all(user_name(part) for part in name_parts):
            if len(name_parts) >= 2:
                full_name = " ".join(name_parts)
                break
            else:
                print("Please enter your full name (at least first and last name).")
        else:
            print("Invalid Name! Only alphabets are allowed.")
    return full_name 

def profile_email():
    while True:
        email = input("Enter your email:")
        if validate_email(email):
            break
        else:
            print("Invalid Email!")
    return email

def profile_age():
    while True:
        age = input("Enter your age: ")
        if validate_num(age) and int(age)<=100:
            break
        else:
            print("Invalid Age!")
    return age


def profile_phone_num():
    while True:
        phone_number = input("Enter your phone number: ")
        if validate_num(phone_number):
            if phone_number.startswith(("98", "97")):
                if len(phone_number) == 10:
                    break
                else:
                    print("Invalid Length of Phone Number! Please Input Phone Number Length of 10")
            else:
                print("Invalid Number! Number should staart from '98' or '97'")
        else:
            print("Invalid phone Number! Please Input Only Numbers.")
    
    return phone_number


def add_role(file_location):
    while True:
        full_name = profile_full_name()
        email = profile_email()
        age = profile_age()
        phone_number = profile_phone_num()
        username, password = login()

        with open(file_location, "r") as f_r:
            stored_user = [eval(line.strip()) for line in f_r]

        if any(user["username"] == username for user in stored_user):
            print("Username already exists!\n")
        else:
            with open(file_location, "a") as f_w:
                user_dict = {"Full Name": full_name, "Email": email, "age": age, "Phone Number": phone_number, "username": username, "password": password}
                f_w.write(str(user_dict) + "\n")
            break
    return ("User successfully added!")
    
def edit_role(file_location):
    print("*"*10 + "Enter Profile Details To Edit" + "*"*10)
    full_name = profile_full_name()
    email = profile_email()

    username, password = login()
   
    with open(file_location, "r") as f_r:
        stored_users = [eval(line.strip()) for line in f_r]
    
    user_found = False
    for user in stored_users:
        if user["username"] == username and user["password"] == password and user["Full Name"] == full_name and user["Email"] == email:
            print("*"*10 + "New Profile" + "*"*10)
            new_full_name = profile_full_name()
            new_email = profile_email()
            new_age = profile_age()
            new_phone_number = profile_phone_num()
            new_username, new_password = login()
            
            user["Full Name"] = new_full_name
            user["Email"] = new_email
            user["age"] = new_age
            user["Phone Number"] = new_phone_number
            user["username"] = new_username
            user["password"] = new_password
            user_found = True
            
    if not user_found:
        print("User not found.")
        edit_role(file_location)

    # Write the updated list back to the file
    with open(file_location, "w") as f_w:
        for user in stored_users:
            f_w.write(str(user) + "\n")

    return ("User updated successfully!")
    
def delete_role(file_location):
    print("*"*10 + "Enter Profile Details To Delete" + "*"*10)
    full_name = profile_full_name()
    email = profile_email()
    username, password = login()
    
    with open(file_location, "r") as f_r:
        stored_users = [eval(line.strip()) for line in f_r]

    user_found = False
    updated_users = []

    for user in stored_users:
        if user["username"] == username and user["password"] == password and user["Full Name"] == full_name and user["Email"] == email:
            user_found = True
            continue  # Skip this user (i.e., delete)
        updated_users.append(user)

    if not user_found:
        print("Username or password or Full Name or Email do not match.")
        delete_role(file_location)

    with open(file_location, "w") as f_w:
        for user in updated_users:
            f_w.write(str(user) + "\n")

    return ("User deleted successfully!")

#---------------------------------------------------------------------------------------------------------------------------

def wait_for_enter_and_redirect(next_function):
    while True:
        key = input("\nPress 'Enter' key to continue: ")
        if key == "":
            next_function()  # Call the passed function
            break
        else:
            print("Invalid Input! Please Press 'Enter' to continue.")


#---------------------------------------------------------------------------------------------------------------------------

def load_ingredients():
    with open("./txt_files/Ingredients.txt", "r") as f:
        return [eval(line.strip()) for line in f]

def save_ingredients(ingredients):
    with open("./txt_files/Ingredients.txt", "w") as f:
        for item in ingredients:
            f.write(str(item) + "\n")


    
