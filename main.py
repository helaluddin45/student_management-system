class Student:
    def __init__(self, name, roll, age):
        self.name = name
        self.roll = roll
        self.age = age

    def show_info(self):
        print(f"Name: {self.name}, Roll: {self.roll}, Age: {self.age}")


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self):
        name = input("Enter student name: ")
        roll = int(input("Enter roll number: "))
        age = int(input("Enter age: "))
        student = Student(name, roll, age)
        self.students.append(student)
        print("✅ Student added successfully!\n")

    def list_students(self):
        if not self.students:
            print("⚠️ No students found.\n")
        else:
            print("\n--- Student List ---")
            for student in self.students:
                student.show_info()
            print()

    def search_student(self):
        roll = int(input("Enter roll number to search: "))
        for student in self.students:
            if student.roll == roll:
                print("🔎 Student found:")
                student.show_info()
                print()
                return
        print("❌ Student not found.\n")

    def remove_student(self):
        roll = int(input("Enter roll number to remove: "))
        for student in self.students:
            if student.roll == roll:
                self.students.remove(student)
                print("🗑️ Student removed successfully!\n")
                return
        print("❌ Student not found.\n")


def main():
    system = StudentManagementSystem()

    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. List Students")
        print("3. Search Student")
        print("4. Remove Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            system.add_student()
        elif choice == "2":
            system.list_students()
        elif choice == "3":
            system.search_student()
        elif choice == "4":
            system.remove_student()
        elif choice == "5":
            print("👋 Exiting program...")
            break
        else:
            print("⚠️ Invalid choice, try again.\n")


if __name__ == "__main__":
    main()
