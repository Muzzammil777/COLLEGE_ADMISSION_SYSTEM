# User database for demonstration purposes
users = {}

# Dictionary to store applicant details by user email
applicant_records = {}

# List of available courses with corresponding cut-off marks
course_cutoffs = {
    "CSE": 170,
    "ECE": 160,
    "CSBS": 150,
    "EEE": 140,
    "IT": 130,
    "MECH": 120,
    "CIVIL": 110,
    "AIML": 100,
    "AIDS": 90
}

# Function to handle login
def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if email in users and users[email] == password:
        print("Login Successful! Welcome, Applicant!")
        show_main_menu(email)
    else:
        print("Login Failed: Invalid email or password")

# Function to handle registration
def register():
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if email in users:
        print("Registration Failed: Email already registered")
    else:
        users[email] = password
        applicant_records[email] = None  # Initialize applicant record for the user
        print("Registration Successful! You can now log in")

# Function to add a new applicant
def add_applicant(email):
    if applicant_records[email] is not None:
        print("You have already added an applicant.")
        return

    name = input("Enter applicant's name: ")
    print("Select the course the applicant wants to take:")
    available_courses = [course for course, cutoff in course_cutoffs.items() if cutoff <= 200]
    for idx, course in enumerate(available_courses, start=1):
        print(f"{idx}. {course}")

    course_choice = int(input("Enter the number corresponding to the course: "))
    if 1 <= course_choice <= len(available_courses):
        course = available_courses[course_choice - 1]
        try:
            hsc_marks = float(input("Enter applicant's HSC marks: "))
            cutoff_marks = int(input("Enter applicant's cut-off marks: "))
            if cutoff_marks < course_cutoffs[course]:
                print(f"Error: Cut-off marks are below the required cutoff for {course}")
                return
            applicant_records[email] = {'name': name, 'course': course, 'hsc_marks': hsc_marks, 'cutoff_marks': cutoff_marks}
            if hsc_marks >= course_cutoffs[course]:
                applicant_records[email]['status'] = 'Approved'
            else:
                applicant_records[email]['status'] = 'Pending'
            print("Applicant added successfully!")
        except ValueError:
            print("HSC marks must be a float and cut-off marks must be an integer")
    else:
        print("Invalid course choice")

# Function to display the applicant added by the user
def display_applicant(email):
    if applicant_records[email] is None:
        print("You have not added any applicant yet.")
    else:
        print("Your Applicant:")
        for key, value in applicant_records[email].items():
            print(f"  {key}: {value}")

# Main menu function
def show_main_menu(email):
    while True:
        print("\nMain Menu:")
        print("1. Add Applicant")
        print("2. View Applicant")
        print("3. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_applicant(email)
        elif choice == '2':
            display_applicant(email)
        elif choice == '3':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

# Main function
def main():
    while True:
        print("\nWelcome to the College Admission System")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            login()
        elif choice == '2':
            register()
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
