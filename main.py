from py_files.login_register import login_roles
from py_files.functions import wait_for_enter_and_redirect

def cover_page():
    subject_code = "CT108-3-1"
    intake_code = "NP1F2503IT"
    submitted_by = [ # Making tuple inside list. So the data can't be changed.
        ("Aayush Kumar Gupta", "NP070889"),
        ("Hemant Bahadur Bam", "NP070904"),
        ("Monika Paudel", "NP070911"),
        ("Avash Paudel", "NP070892"),
    ]
    submitted_to = "Bishal Prasad Kurmi"

    # Output
    print("\n\tGroup Assignment")
    print(f"\nSubject Code: {subject_code}")
    print(f"\nIntake Code: {intake_code}")
    print("\nSubmitted By:")
    print("\tGroup: Team 6")
    for name, id in submitted_by: #Using loop to print all the values one by one
        print(f"  • {name} ({id})") #Print the name and their corresponding ID inside submitted_by variable.

    print("\nSubmitted to:")
    print(f"  {submitted_to}")
    wait_for_enter_and_redirect(login_roles)
    

if __name__ == "__main__":
    cover_page()