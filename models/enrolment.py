"""

This file manages the relationship between Students and Courses.
Data will be stored in:
data/enrollments.json

1. Create an Enrollment class

2. Implement a function to enroll a student in a course
   Steps:
- Load enrollments.json
- Create a new enrollment record
- Append it to the list
- Save back to enrollments.json

3. Implement a function to get courses for a student
  Steps:
- Load enrollments.json
- Find all records with matching student_id
- Return the course_ids

4. Implement a function to get students in a course
  Steps:
- Load enrollments.json
- Find all records with matching course_id
- Return the student_ids

Do not create students or courses here.
Students and Courses are handled by Albert.

"""
import json
import os

# Points to our JSON "Database"
DATA_FILE = "data/enrolments.json"

class Enrollment:
    def __init__(self, student_id, course_id):
        self.student_id = student_id
        self.course_id = course_id

    @staticmethod
    def load_enrollments():
        """Reads the JSON file and returns a list of enrolments."""
        if not os.path.exists(DATA_FILE):
            return []
        try:
            with open(DATA_FILE, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    @staticmethod
    def save_enrollments(enrollments):
        """Writes the list of enrolments back to the JSON file."""
        # This ensures the 'data' folder exists before saving
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        with open(DATA_FILE, "w") as file:
            json.dump(enrollments, file, indent=4)

    @staticmethod
    def enrol_student(student_id, course_id):
        """Creates a new enrollment and saves it to the JSON file."""
        enrollments = Enrollment.load_enrollments()
        
        # Check if student is already in the course to prevent duplicates
        for entry in enrollments:
            if entry['student_id'] == student_id and entry['course_id'] == course_id:
                print(f"Alert: Student {student_id} is already enrolled in {course_id}!")
                return
        
        # Create a dictionary for the new enrollment
        new_entry = {
            "student_id": student_id,
            "course_id": course_id
        }
        
        # Add to the list and save
        enrollments.append(new_entry)
        Enrollment.save_enrollments(enrollments)
        print(f"Success: Enrolled student {student_id} into course {course_id}.")

    @staticmethod
    def get_courses_for_student(student_id):
        """Finds all course_ids for a specific student."""
        enrollments = Enrollment.load_enrollments()
        # Filters the list for matching student_id
        return [entry['course_id'] for entry in enrollments if entry['student_id'] == student_id]

    @staticmethod
    def get_students_in_course(course_id):
        """Finds all student_ids for a specific course."""
        enrollments = Enrollment.load_enrollments()
        # Filters the list for matching course_id
        return [entry['student_id'] for entry in enrollments if entry['course_id'] == course_id]

# --- TESTING AREA ---
if __name__ == "__main__":
    # This will create the data folder and file if they don't exist
    Enrollment.enrol_student("S101", "PYTHON_BASICS")
    print("Current Enrolments:", Enrollment.load_enrollments())
    