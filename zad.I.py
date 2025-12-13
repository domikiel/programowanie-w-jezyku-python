class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        if not self.marks:
            return False
        average = sum(self.marks) / len(self.marks)
        return average > 50

student_1 = Student("Marek", [50, 60, 70])
student_2 = Student("Bartek", [35, 40, 50])

print(student_1.is_passed())
print(student_2.is_passed())

