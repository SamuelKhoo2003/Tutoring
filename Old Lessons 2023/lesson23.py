# 1. Find sum of digits in a number:
# Write a function that takes a string of an integer as input and returns the sum of its digits.
# e.g. number = 12345, should return 15

test1 = "12345"
# return 15

def sum_of_digits(number_str):
    digit_sum = 0
    for digit in number_str:
        digit_sum += int(digit)
        # remember to convert from string to int
    return digit_sum

# print(sum_of_digits(test1))

# 2. Find the factorial of a number:
# Write a function to compute the factorial of a given number. The factorial of a number n is the product of all positive integers less than or equal to n.
# e.g. number = 5, should return 120 as 5x4x3x2x1 = 120

def factorial_1(number_input):
    res = 1
    while number_input > 0:
        res *= number_input
        number_input -= 1
        # print((res, number_input))
    return res
# multiply down from 5 to 1 or up from 1 to 5

def factorial_2(number_input):
    if number_input == 0:
        return 1
    else:
        return number_input * factorial_2(number_input - 1)

# factorial_2(5)
# 5 * factorial_2(4)
# 5 * factorial_2(4) = 5 * 4 * factorial_2(3)

print(factorial_2(5))

def recursive_demo(input_x):
    if input_x > 0:
        print(input_x)
        return recursive_demo(input_x-1)
    else:
        print("end of recursion")

# recursive_demo(4)

# 3. Design a Stack Class in Python:
# Implement a Stack data structure in Python. A Stack follows the Last In, First Out (LIFO) principle, meaning the last element added to the stack will be the first one to be removed.

# Your stack should support the following operations:
# push(item): Add an item to the top of the stack.
# pop(): Remove and return the item from the top of the stack. If the stack is empty, return None.
# peek(): Return the top item from the stack without removing it. If the stack is empty, return None.
# is_empty(): Return True if the stack is empty, otherwise return False.
# size(): Return the number of items in the stack.
# e.g. 
# # Test the Stack class
# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)

# print("Size of stack:", stack.size())  # Output should be 3
# print("Top item:", stack.peek())       # Output should be 3
# print("Popped item:", stack.pop())     # Output should be 3

# print("Is stack empty?", stack.is_empty())  # Output should be False
# print("Size of stack:", stack.size())       # Output should be 2

# mylist = [1,2,3,4]
# stack = [1, 2, 3, 4, 5]

# demo = [1,2 ,3 ,4 ,5]
# print(demo[-1])
# print(demo[len(demo)-1])

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        # make sure we dont pop from an empty stack
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty")

    def is_empty(self):
        if len(self.items) == 0:
            return True
        return False

    def size(self):
        return len(self.items)


# stack1 = Stack()
# stack1.push(2)
# stack1.push(3)
# stack1.push(4)

# print("Size of stack:", stack1.size())
# print("Top item:", stack1.peek())
# stack1.pop()
# print("Stack empty status:", stack1.is_empty())
# print("Top item:", stack1.peek())

# 4. Employee Management System
# Create an Employee class to represent an employee with attributes such as name, age, position, and salary. Also, create an EmployeeManagementSystem class to manage a list of employees. The EmployeeManagementSystem class should support operations like adding an employee, removing an employee, searching for an employee by name, and listing all employees.

# The Employee class should support the following methods:
# __init__(self, name, age, position, salary): Constructor method to initialize an employee with name, age, position, and salary.
# get_name(self): Method to get the name of the employee.
# get_age(self): Method to get the age of the employee.
# get_position(self): Method to get the position of the employee.
# get_salary(self): Method to get the salary of the employee.

# The EmployeeManagementSystem class should support the following methods:
# __init__(self): Constructor method to initialize an empty list of employees.
# add_employee(self, employee): Method to add a new employee to the system.
# remove_employee(self, name): Method to remove an employee from the system by name.
# search_employee_by_name(self, name): Method to search for an employee by name and return their details.
# list_all_employees(self): Method to list all employees in the system.

class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position  = position
        self.salary = salary

    def get_salary(self):
        return self.salary

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_position(self):
        return self.position

class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []
    
    def add_employee(self, new_employee):
        if new_employee not in self.employees:
            self.employees.append(new_employee)
        else:
            print("Employee already in system")

    def remove_employee(self, employee_name):
        for employee in self.employees:
            if employee.get_name() == employee_name:
                self.employees.remove(employee)
                print("Removed")
                return
        print("Employee not found in system")

    def list_all_employees(self):
        for employee in self.employees:
            print("Name:", employee.get_name())
            print("Age:", employee.get_age())
            print("Salary:", employee.get_salary())
            print("Position:", employee.get_position())
            print()

employee1 = Employee("Sam", 20, "Intern", 5000)
employee2 = Employee("Marcus", 25, "Analyst", 10000)
employee3 = Employee("Grace", 35, "Associate", 60000)

mock_management = EmployeeManagementSystem()
mock_management.add_employee(employee1)
mock_management.add_employee(employee2)
mock_management.add_employee(employee3)
mock_management.list_all_employees()


mock_management.remove_employee("Grace")
mock_management.remove_employee("Mark")