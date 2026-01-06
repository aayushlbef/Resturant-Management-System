def user_name(username):
    return username.isalpha()  # Example check: only letters allowed

def validate_email(email):
    return email.endswith(("@gmail.com", "@outlook.com", "@yahoo.com"))

def validate_num(num):
    return num.isdigit()

def login():  # Function to take username and password as input from user
    username = input("Enter your username: ")
    if user_name(username):
        password = input("Enter your password: ")
        return username, password
    else:
        print("Invalid Username! Please include only alphabets.")
        return login()

#-----------------------------------------------------------Validation Panal----------------------------------------------------------------
    
def is_valid_year_month(s):
    # Split the string by dash
    parts = s.split('-')
    
    # Check for exactly two parts
    if len(parts) != 2:
        return False
    
    year, month = parts
    
    # Validate year: 4 digits, numeric
    if not (year.isdigit() and len(year) == 4):
        return False
    
    # Validate month: 2 digits, numeric, and between 01 and 12
    if not (month.isdigit() and len(month) == 2):
        return False
    
    if not (1 <= int(month) <= 12):
        return False

    return True
