class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display_info(self):
        return f"Name: {self.name}, Roll: {self.roll}"

student1 = Student("Saida", 101)
print(student1.display_info())

