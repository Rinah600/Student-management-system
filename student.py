#has the student class
class Student:
    def __init__(self, student_id, name, age, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
    def display_details(self):
        print(f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Course: {self.course}")
student1 = Student("S001", "John Doe", 20, "Computer Science")