class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display_info(self):
        return f"Name: {self.name}, Roll: {self.roll}, Marks: {self.marks}"

    def calculate_average(self):
        if len(self.marks) == 0:
            return 0
        return sum(self.marks) / len(self.marks)


student1 = Student("Saida", 101, [85, 90, 78, 92])
print(student1.display_info())
print(f"Average Marks: {student1.calculate_average()}")
