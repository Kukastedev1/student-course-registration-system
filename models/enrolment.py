import json
import os
from models.course import Course

DATA_FILE = "data/enrolments.json"
STUDENTS_FILE = "data/students.json"


class Enrollment:
    def __init__(self, student_id, course_id):
        self.student_id = student_id
        self.course_id = course_id

    @staticmethod
    def load_enrollments():
        """Load enrollments from JSON file."""
        if not os.path.exists(DATA_FILE):
            return []

        try:
            with open(DATA_FILE, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    @staticmethod
    def save_enrollments(enrollments):
        """Save enrollments to JSON file."""
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

        with open(DATA_FILE, "w") as file:
            json.dump(enrollments, file, indent=4)

    @staticmethod
    def student_exists(student_id):
        """Check if student exists in students.json."""
        if not os.path.exists(STUDENTS_FILE):
            return False

        try:
            with open(STUDENTS_FILE, "r") as file:
                students = json.load(file)

                for student in students:
                    if student["student_id"] == student_id:
                        return True
        except (json.JSONDecodeError, FileNotFoundError):
            return False

        return False

    @staticmethod
    def enrol_student(student_id, course_id):
        """Enroll student into a course with validation."""

        enrollments = Enrollment.load_enrollments()

        # Validate student exists
        if not Enrollment.student_exists(student_id):
            print("Student does not exist!")
            return

        # Validate course exists
        if not Course.course_exists(course_id):
            print("Course does not exist!")
            return

        # Prevent duplicate enrollment
        for entry in enrollments:
            if entry["student_id"] == student_id and entry["course_id"] == course_id:
                print(f"Alert: Student {student_id} is already enrolled in {course_id}!")
                return

        # Add enrollment
        new_entry = {
            "student_id": student_id,
            "course_id": course_id
        }

        enrollments.append(new_entry)
        Enrollment.save_enrollments(enrollments)

        print(f"Success: Enrolled student {student_id} into course {course_id}.")

    @staticmethod
    def drop_course(student_id, course_id):
        """Remove enrollment."""
        enrollments = Enrollment.load_enrollments()

        updated_enrollments = [
            e for e in enrollments
            if not (e["student_id"] == student_id and e["course_id"] == course_id)
        ]

        Enrollment.save_enrollments(updated_enrollments)

        print(f"Student {student_id} dropped from course {course_id}")

    @staticmethod
    def get_courses_for_student(student_id):
        """Return list of course IDs for a student."""
        enrollments = Enrollment.load_enrollments()

        return [
            entry["course_id"]
            for entry in enrollments
            if entry["student_id"] == student_id
        ]

    @staticmethod
    def get_students_in_course(course_id):
        """Return list of student IDs in a course."""
        enrollments = Enrollment.load_enrollments()

        return [
            entry["student_id"]
            for entry in enrollments
            if entry["course_id"] == course_id
        ]