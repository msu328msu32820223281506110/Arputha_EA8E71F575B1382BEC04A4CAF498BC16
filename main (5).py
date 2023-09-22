def sort_students(students):
    students.sort(key=lambda x: x.CGPA, reverse=True)
class Student:
    def __init__(self, name, roll_number, CGPA):
        self.name = name
        self.roll_number = roll_number
        self.CGPA = CGPA
students = [
    Student("John", "18001", 9.8),
    Student("Alice", "18003", 9.2),
    Student("Bob", "18002", 9.5),
    Student("Eva", "18005", 8.5),
    Student("David", "18004", 9.0),
]
sort_students(students)
for student in students:
    print(student.name, student.roll_number, student.CGPA)
