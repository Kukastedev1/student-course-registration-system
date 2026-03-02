"""
Main Program
CLI Menu System
"""

from services.auth_service import AuthService
from models.student import Student
from models.course import Course
from models.enrolment import Enrollment

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
    print("1. Enroll Course")
    print("2. Drop Course")
    print("3. View Student Courses")
    print("4. View Available Courses")
    print("5. Logout")


def main():

    while True:

        main_menu()

        choice = input("Select option: ")

        # REGISTER
        if choice == "1":

            username = input("Enter username: ")
            password = input("Enter password: ")

            message = AuthService.register(username, password)
            print(message)

        # LOGIN
        elif choice == "2":

            username = input("Username: ")
            password = input("Password: ")

            user = AuthService.login(username, password)
           
            if user:

                print(f"\nWelcome {user.username}!")

                # SYSTEM MENU LOOP
                while True:

                    system_menu()

                    option = input("Choose option: ")

                    # Enroll Course
                    if option == "1":

                        course_id = input("Course ID: ")
                        student_id = input("Student ID: ")
                        Enrollment.enrol_student(student_id, course_id)

                        print("Course added successfully.")

                    # Drop Course
                    elif option == "2":

                        course_id = input("Course ID: ")
                        student_id = input("Student ID: ")
                        Enrollment.drop_course(student_id, course_id)
                        
                        print("Course dropped successfully.")

                    # View Student Courses
                    elif option == "3":

                        student_id = input("Student ID: ")
                        courses = Enrollment.get_courses_for_student(student_id)

                        if courses:
                            print("\nCourses for this student:")
                            for course in courses:
                                print(course)

                        else:
                            print("No courses found for this student.")


                    # View Available Courses
                    elif option == "4":

                        courses = Course.get_all_courses()

                        if not courses:
                            print("No courses available.")

                        else:
                            print("\nAvailable Courses:")

                            for c in courses:
                                print(f"{c['course_id']} - {c['title']} | {c['description']}")
                     

                    # Logout
                    elif option == "5":

                        print("Logging out...")
                        break

                    else:
                        print("Invalid option.")

            else:
                print("Invalid login credentials.")

        # EXIT
        elif choice == "3":

            print("Exiting system...")
            break

        else:
            print("Invalid choice.")


# Run Program
if __name__ == "__main__":
    main()