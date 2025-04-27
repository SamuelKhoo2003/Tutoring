# Tasks:
# 1. Define the Student Class
# Create a class named Student with the following attributes:

# student_id (str) → A unique student ID (e.g., "S12345")

# name (str) → Full name of the student

# age (int) → Age of the student

# grades (list, default = []) → A list to store grades

# 2. Implement the Following Methods:
# add_grade(grade) → Adds a new grade (integer) to the student's grade list.

# get_average_grade() → Returns the average grade of the student.

# get_student_info() → Returns a formatted string with student details.

# __str__() → Overrides the print function to display student details in a readable format.

class Student:
    def __init__(self, student_id, name, age, grades=[]):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grades = grades
    
    def add_grade(self, input_grade):
        self.grades.append(input_grade)

    def get_average_grade(self):
        if not self.grades:
            return "The student currently doesn't have any grades."
        total_grade = 0
        for student_grade in self.grades:
            total_grade = total_grade + student_grade[1]
        return f"{total_grade/len(self.grades)}"

example_student = Student("01234", "Marcus", 18)
# print(example_student.grades)
example_student.add_grade(("Chemistry", 90))
example_student.add_grade(("Maths", 75))
example_student.add_grade(("English", 80))
print(example_student.grades)
print(example_student.get_average_grade())
# The average grade for Marcus is X"
# [("Chemistry", 90)]

# difference between tuple and list is that you can't append to a tuple
# mytuple = ("History", 10, "English", 100, "Cat", "Monkey")
# print(mytuple[4])


# examplegrades = [("Chemistry", 90), ("Math", 80), ("English", 78)]
# for grade in examplegrades:
#     print(grade[1])

# testlist = ['a', 'b', ('c', 20, 30), 'd']
# for element in testlist:
    # print(element)


