from student_manager import StudentManager, COURSES

manager = StudentManager()

def main():
    while True:
        print("\n================================")
        print("     STUDENT MANAGEMENT SYSTEM")
        print("================================")
        print("1. Register Student")
        print("2. View All Students")
        print("3. Search for a Student")
        print("4. Update Student Details")
        print("5. Delete Student")
        print("6. View Available Courses")
        print("7. Exit")
        print("================================")

        choice = input("Enter your choice: ").strip()

        print("You selected:", choice)

        if choice == "1":
            student_id = input("Enter Student ID: ").strip()
            name = input("Enter Student Name: ").strip()

            try:
                age = int(input("Enter Student Age: "))
            except ValueError:
                print("Please enter a valid age.")
                continue

            manager.view_courses()
            course = input("Enter Course Name: ").strip()

            if course not in COURSES:
                print("Invalid course selected!")
                continue

            manager.add_student(student_id, name, age, course)

        elif choice == "2":
            print("Displaying registered students...")
            manager.view_students()

        elif choice == "3":
            student_id = input("Enter Student ID to search: ").strip()
            manager.search_student(student_id)

        elif choice == "4":
            student_id = input("Enter Student ID to update: ").strip()
            manager.update_student(student_id)

        elif choice == "5":
            student_id = input("Enter Student ID to delete: ").strip()
            manager.delete_student(student_id)

        elif choice == "6":
            manager.view_courses()

        elif choice == "7":
            print("Thank you for using the Student Management System!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()