class Course:
    def __init__(self, course_id, title, description):
        self.course_id = course_id
        self.title = title
        self.description = description
        self.students = []  # list of student_ids

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