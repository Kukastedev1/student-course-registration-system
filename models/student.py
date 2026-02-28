import json

class Student:
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.courses = []  # list of course_ids

    def enroll(self, course_id):
        if course_id not in self.courses:
            self.courses.append(course_id)

    def drop_course(self, course_id):
        if course_id in self.courses:
            self.courses.remove(course_id)

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "email": self.email,
            "courses": self.courses
        }