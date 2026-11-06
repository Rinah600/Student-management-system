#handles registration, searching, updating and deleting of students
from student import Student
class StudentManager:
    def__init__(self):
        self.students = []
        self.student_id = set()
        self.student_lookup = {}
        
#to register the students
        def add_student(self, student_id, name, age, course):

        if student_id in self.student_ids:
            print("Student ID already exists!")
            return

        student = Student(student_id, name, age, course)

        self.students.append(student)
        self.student_ids.add(student_id)
        self.student_lookup[student_id] = student

        print("Student registered successfully!")