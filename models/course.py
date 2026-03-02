import json
import os

DATA_FILE = "data/courses.json"

class Course:

    def __init__(self, course_id, title, description):
        self.course_id = course_id
        self.title = title
        self.description = description
        self.students = []

    def add_student(self, student_id):
        if student_id not in self.students:
            self.students.append(student_id)

    def remove_student(self, student_id):
        if student_id in self.students:
            self.students.remove(student_id)

    def to_dict(self):
        return {
            "course_id": self.course_id,
            "title": self.title,
            "description": self.description,
            "students": self.students
        }

    @staticmethod
    def load_courses():

        if not os.path.exists(DATA_FILE):
            return []

        with open(DATA_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []

    @staticmethod
    def save_courses(courses):

        with open(DATA_FILE, "w") as file:
            json.dump(courses, file, indent=4)

    @staticmethod
    def get_all_courses():

        return Course.load_courses()

    @staticmethod
    def course_exists(course_id):

        courses = Course.load_courses()

        for course in courses:
            if course["course_id"] == course_id:
                return True

        return False