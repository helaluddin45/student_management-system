class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display_info(self):
        return f"Name: {self.name}, Roll: {self.roll}"

student1 = Student("Saida", 101)
print(student1.display_info())
def calculate_average(marks):
    if len(marks) == 0:
        return 0
    return sum(marks) / len(marks)

marks_list = [85, 90, 78, 92]
average = calculate_average(marks_list)
print(f"Average Marks: {average}")
