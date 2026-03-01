"""
Main Program

CLI Menu System

"""

from services.auth_service import login, register
from models.student import add_student, get_all_students
from models.course import add_course, get_all_courses
from models.enrolment import enroll_student, get_student_courses

"""
Main Menu

"""

def main_menu():
    print("\n==== Student Course Registration System ====")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

"""
System menu after login

"""

def system_menu():
    print("\n==== System Menu ====")
    print("1. Add Student")
    print("2. Add Course")
    print("3. Enroll Student")
    print("4. View Student Courses")
    print("5. View All Students")
    print("6. View All Courses")
    print("7. Logout")


def main():

    while True:

        main_menu()

        choice = input("Select option: ")
        if choice == "1":

            username = input("Enter username: ")
            password = input("Enter password: ")
            role = input("Enter role(admin/student): ")

            register(username, password, role)

            print("User registered successfully.")

        elif choice == "2"

            username = input("Username: ")
            password = input("Password: ")

            user = login(username, password)
            
            if user:
                print(f"\nWelcome{user['username']}!")
                
                # System menu loop
                while True:

                    system _menu()
                    option = input("Choose option: ")
                
                # Add Student
                if option == "1":

                    name = input("Student name: ")

                    add_student(name)

                    print("Student added successfully.")

                # Add Course
                elif option == "2":

                    course_name = input("Course name: ")
                    
                    add_course(course_name)

                    print("Course added successfully.")

                # Enroll Student
                elif option == "3":

                    student_id = int(input("Student ID: "))
                    course_id = int(input("Course ID: "))

                    enroll_student(student_id, course_id)

                    print("Student enrolled successfully.")
                
                # View Student Courses
                elif option == "4":

                    student_id = int(input("Student ID: "))
                    courses = get_student_courses(student_id)

                    print("Courses for this student:")
                    for c in courses:
                        print(c)

                # View All Students
                elif option == "5"

                    students = get_all_students()

                    for s in students:
                        print(s)

                # View All Courses
                elif option == "6"

                    courses = get_all_courses()

                    for c in courses:
                        print(c)

                # Logout
                elif option == "7"

                    print("Logging out...")
                    break

                else:
                    print("Invalid option.")

        else:
            print("Invalid login credentials.")

"""

Exit

"""
        elif choice == "3":
            print("Exiting system...")
            break

        else:
            print("Invalid choice.")


# Run Program
if __name__ = "__main__"
    main()

