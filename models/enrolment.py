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