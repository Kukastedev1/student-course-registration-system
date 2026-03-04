"""
Main Program
CLI Menu System with Admin Clearance
"""

from services.auth_service import AuthService
from models.course import Course
from models.enrolment import Enrollment


def main_menu():
    print("\n==== Student Course Registration System ====")
    print("1. Register")
    print("2. Login")
    print("3. Admin Login")
    print("4. Exit")


def system_menu():
    print("\n==== System Menu ====")
    print("1. Enroll Course")
    print("2. Drop Course")
    print("3. View Student Courses")
    print("4. View Available Courses")
    print("5. Logout")


def admin_menu():
    print("\n==== Admin Menu ====")
    print("1. Clear Student for Enrollment")
    print("2. Logout")


def display_courses(courses):
    if courses:
        print("\nAvailable Courses:")
        for c in courses:
            print(f"{c['course_id']} - {c['title']} | {c['description']}")
    else:
        print("No courses available.")


def main():
    while True:
        main_menu()
        choice = input("Select option: ")

        # ================= REGISTER =================
        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            message = AuthService.register(username, password)
            print(message)

        # ================= STUDENT LOGIN =================
        elif choice == "2":
            username = input("Username: ")
            password = input("Password: ")

            user = AuthService.login(username, password)

            if isinstance(user, str):
                print(user)
            else:
                print(f"\nWelcome {user.username}!")

                # ✅ Show available courses immediately after login
                display_courses(Course.get_all_courses())

                # Student menu loop
                while True:
                    system_menu()
                    option = input("Choose option: ")

                    # Enroll
                    if option == "1":
                        course_id = input("Course ID: ")
                        student_id = input("Student ID: ")

                        try:
                            Enrollment.enrol_student(student_id, course_id)
                            print("Course added successfully.")
                        except Exception as e:
                            print(f"Enrollment failed: {e}")

                    # Drop
                    elif option == "2":
                        course_id = input("Course ID: ")
                        student_id = input("Student ID: ")

                        try:
                            Enrollment.drop_course(student_id, course_id)
                            print("Course dropped successfully.")
                        except Exception as e:
                            print(f"Drop failed: {e}")

                    # View student courses
                    elif option == "3":
                        student_id = input("Student ID: ")

                        try:
                            courses = Enrollment.get_courses_for_student(student_id)
                            if courses:
                                print("\nCourses for this student:")
                                for course in courses:
                                    print(f"  {course}")
                            else:
                                print("No courses found.")
                        except Exception as e:
                            print(f"Error: {e}")

                    # View available courses
                    elif option == "4":
                        display_courses(Course.get_all_courses())

                    # Logout
                    elif option == "5":
                        print("Logging out...")
                        break

                    else:
                        print("Invalid option.")

        # ================= ADMIN LOGIN =================
        elif choice == "3":
            admin_pass = input("Enter admin password: ")

            if admin_pass != "admin123":
                print("Incorrect admin password!")
                continue

            print("Welcome Admin!")

            while True:
                admin_menu()
                admin_option = input("Choose option: ")

                if admin_option == "1":
                    student_username = input("Enter student username to clear: ")
                    message = AuthService.clear_student(student_username)
                    print(message)

                elif admin_option == "2":
                    print("Admin logging out...")
                    break

                else:
                    print("Invalid option.")

        # ================= EXIT =================
        elif choice == "4":
            print("Exiting system...")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()