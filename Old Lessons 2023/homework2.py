
# 1. Please write a function named mean, which takes three integer arguments. The function should print out the arithmetic mean of the three arguments.
# mean(5, 3, 1)
# mean(10, 1, 1)
# this should print out:
# 3.0
# 4.0
# hint: use def mean(a, b, c)
# list = [9, 10]
# print(sum(list))

# def test():
#     print("test")

# def test2(a):
#     print(a)
# def testfunction(nums: list):


# def mean(a: int, b: int, c: int):
#     return ((a + b + c)/3)

# print(mean(10, 1, 1))


# testfunction

# 2. Write a Python function to multiply all the numbers in a list.
# nums = [8, 2 , 3, -1, 7]
# multiplyall(nums)
# this should print out:
# -336
# hint: use *= and a for loop to iterat through a list
# e.g. for i in nums:
#         print(i)
#       this will print out all numbers within the list
# how would this be used to multiply all the numbers?

# def Leanne_multiplyall(nums: list[int]) -> int:
#     result = 1
#     for num in nums:
#         result *= num
#     return result

# print(Leanne_multiplyall(nums))

# yourname = input("What is your name")

def showEmployee(name: str, salary: int) -> str:
    print(f"Name: {name} salary: {salary}")
# Name: Ben salary: 12000

def Marcus_showStudent(student: str, age: int, gender: str) -> str:
   print(f"name: {student} Age: {age} gender: {gender}")
Marcus_showStudent("Marcus", 12, "Male")

def Leanne_showStudent(student: str, age: int, gender: str) -> str:
    print(f"Name: {student} Age: {age}, Gender: {gender}")
Leanne_showStudent("Leanne",15,"Female")