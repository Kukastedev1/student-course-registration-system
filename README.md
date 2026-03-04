#  Student Course Registration System

## Project Overview

This is a Command Line Interface (CLI) based Student Course Registration System developed using Python and Object-Oriented Programming (OOP) principles.

The system allows students to register, log in (after admin clearance), enroll in courses, drop courses, and view their enrolled courses. It also includes an admin role responsible for clearing students before enrollment access is granted.

---

##  Learning Objectives Achieved

This project demonstrates understanding of:

- Object-Oriented Programming (Classes & Objects)
- Encapsulation and method organization
- Role-based authentication system
- File-based data persistence using JSON
- Password hashing using SHA256
- CLI application design
- Git branching and Pull Request workflow

---

## System Architecture

The project follows a modular structure:

student-course-registration-system/
│
├── data/
│   ├── users.json
│   ├── courses.json
│   └── enrollments.json
│
├── models/
│   ├── user.py
│   ├── course.py
│   └── enrollment.py
│
├── services/
│   └── auth_service.py
│
├── main.py
└── README.md

---

##  Student Functionalities

- Register account
- Login (after admin clearance)
- View available courses
- Enroll in a course
- Drop a course
- View enrolled courses

---

##  Admin Functionalities

- Login as admin
- Clear students for enrollment access

Students cannot log in unless cleared by the admin.

---

##  Authentication & Security

- Passwords are hashed using SHA256 before storage.
- Raw passwords are never stored in the JSON file.
- Role-based login system (student/admin).
- Clearance system prevents unauthorized enrollment access.

---

##  How to Run the Project

1. Clone the repository:

git clone https://github.com/Kukastedev1/student-course-registration-system.git

2. Navigate into the project folder:

cd student-course-registration-system

3. Run the program:

python main.py

---

## Sample Admin Credentials

If creating an admin account:

Username: admin  
Password: admin123  

Admin accounts are automatically cleared.

---

##  Git Workflow Used

- Created feature branches (models, cli, enrollment)
- Used Pull Requests to merge into main branch
- Resolved merge conflicts where necessary
- Maintained clean commit messages

---

##  OOP Concepts Applied

1. Class abstraction (User, Course, Enrollment)
2. Instance methods and static methods
3. Data encapsulation inside model classes
4. Separation of concerns (models vs services)
5. Modular design for maintainability

---

## Limitations

- Uses JSON instead of a relational database
- No graphical interface (CLI only)
- No course capacity limits
- No advanced validation

---

##  Future Improvements

- Database integration (SQLite/PostgreSQL)
- GUI or Web version (Flask/Django)
- Course capacity management
- Password strength validation
- Activity logging

---


---

##  Academic Declaration

This project was developed as part of coursework to demonstrate understanding of Object-Oriented Programming and Git workflow practices.