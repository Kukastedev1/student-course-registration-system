from models.student import Student
from models.course import Course

# Create Students
engine = Student("SDFT001", "Engine Kukaste", "engine@mail.com")
albert = Student("SDFT002", "Albert Mochama", "albert@mail.com")
athanas = Student("SDFT003", "Athanas Mochama", "athanas@mail.com")
kimberly = Student("SDFT004", "Kimberly Ayiaki", "kimberly@mail.com")

# Create Course
python_course = Course("CS101", "Python Programming", "Intro to Python")

# Enroll Students
engine.enroll("CS101")
albert.enroll("CS101")
athanas.enroll("CS101")
kimberly.enroll("CS101")

python_course.add_student("SDFT001")
python_course.add_student("SDFT002")
python_course.add_student("SDFT003")
python_course.add_student("SDFT004")

# Print Results
print(engine.to_dict())
print(albert.to_dict())
print(athanas.to_dict())
print(kimberly.to_dict())

print(python_course.to_dict())