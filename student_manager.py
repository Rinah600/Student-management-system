#handles registration, searching, updating and deleting of students
from student import Student
COURSES = (
    "Computer Science",
    "Information Technology",
    "Software Engineering",
    "Data Science",
    "Information Systems"
)
class StudentManager:
#using a tuple with a for lopp
    def view_courses(self):

        print("\n===== AVAILABLE COURSES =====")

        for course in COURSES:
            print(course)
    def __init__(self):
        self.students = []
        self.student_ids = set()
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
        
#loops to process and view multiple records
    def view_students(self):
        if not self.students:
            print("No students have been registered yet.")
            return

        print("\n===== REGISTERED STUDENTS =====")

        for student in self.students:
            print("-------------------------")
            student.display_details()
            
    # method to search for a student
    def search_student(self, student_id):
        student = self.student_lookup.get(student_id)

        if student:
            print("\nStudent found!")
            student.display_details()
        else:
            print("Student not found.")
            
#a method to delete a student
    def delete_student(self, student_id):
        student = self.student_lookup.get(student_id)

        if student:
            self.students.remove(student)
            self.student_ids.remove(student_id)
            del self.student_lookup[student_id]
            print("Student deleted successfully!")
        else:
            print("Student not found.")
            
            
#update student details       
    def update_student(self, student_id):

        student = self.student_lookup.get(student_id)

        if student:
            print("Leave a field blank to keep its current value.")

            new_name = input("Enter new name: ")
            new_age = input("Enter new age: ")
            new_course = input("Enter new course: ")

            if new_name:
                student.name = new_name

            if new_age:
                try:
                    student.age = int(new_age)
                except ValueError:
                    print("Invalid age. Keeping the previous age.")

            if new_course:
                student.course = new_course

            print("Student details updated!")
        else:
            print("Student not found.")