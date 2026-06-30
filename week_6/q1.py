class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def average_grade(self):
        total = 0

        for grade in self.grades:
            total += grade

        return total / len(self.grades)


student1 = Student("Ram", 20, [80, 75, 90])
student2 = Student("Sita", 21, [60, 70, 65])
student3 = Student("Hari", 19, [90, 85, 95])

print(student1.name, student1.average_grade())
print(student2.name, student2.average_grade())
print(student3.name, student3.average_grade())
