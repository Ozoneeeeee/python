class StudentResult:
    def __init__(self, name, age, average_grade):
        self.name = name
        self.age = age
        self.average_grade = average_grade

    def has_passed(self):
        if self.average_grade >= 50:
            return True
        else:
            return False


result1 = StudentResult("Ram", 20, 75)
result2 = StudentResult("Sita", 21, 45)
result3 = StudentResult("Hari", 19, 60)


students = [result1, result2, result3]

for student in students:
    if student.has_passed():
        print(student.name, "passed")