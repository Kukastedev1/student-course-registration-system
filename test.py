from models.student import Student
from models.course import Course

s1 = Student(1, "Albert", "albert@mail.com")
c1 = Course(101, "Python", "Intro to Python")

s1.enroll(101)
c1.add_student(1)

print(s1.to_dict())
print(c1.to_dict())