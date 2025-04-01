# Lists are declared using []
# Sets are declared using set() or {}
# Dictionaries are declared using {}

# Core difference between all of them is that lists are indexed so the values are ordered in position 0,1,2,3 ... so on, but dictionaries and sets are not ordered, they are kind off like a bowl of values with no specific order. The difference between dictionaries and sets is that dictionaries have a feature called mapping in which a certain value within the dictionary is "mapped to another", this is a key and value relation. 

# E.g. dict - {'a': 10, 'b': 20}, when we call the dict['a'] we will get the value 10 and when we call dict['b'] we will get 20, these are the only ways for us to acces the 10 and 20 value within this dictionary (it has to be through calling the key value directly). 

# For functions remembers that we should always practice returning a value instead of printing, this allows for the value to be further used in future. Aside from this functions can also have inputs which have be named and introduced when defining them e.g def functionname(input1, input2):

# Remember the different set operations of difference, union, intersection, add and remove. Making good use of these are important when handling questions and large data sets. Also remember that value elements within a dictionary can be modified. 

# Also dont forget about topics like f_strings and string operations and slicing (heavily based of indexing in lists), topics like recursion so calling a function within a function are also important!

# Then lastly remind yourself about classes, how class items are declared as well as class functions, remember the self property as well and how to declare class specific variables. Classes can exist within classes and are initialised using Class classname:, followed by a def __init__(self) as the first function/property. # print(teststr[:4])

# print(teststr[3:7])
# print(teststr[2:9])
# print(teststr[2:9:2])
#  [ starting idx : ending idx : jump intervals]
# [2:5:2]

# Arithmetic Operations
# print(7%5) # module
# print(7//5) # floor division
# print(7/5)  # normal division
# print(7*5) # multiplication
# print(7**5) # power of/exponential
# nums = 10
# # nums = nums + 5
# nums += 5

# print(int(8.956))

# class TestClass:
#     # we want to define x, y
#     def __init__ (self, x, y):
#         self.x = x
#         self.y = y
#         self.z = 100

#     def sum_all(self):
#         return(self.x + self.y + self.z)

# x = 150, y = 200
# testsolution = TestClass(150, 200)
# print(testsolution.sum_all()) # IMPORTANT TO REMEMBER THE BRACKETS

mymatrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(len(mymatrix))
# print(len(mymatrix[0]))
# print(mymatrix[0])

n = len(mymatrix) # 3
m = len(mymatrix[0]) # 3 


# for i in range(7):
#     print(i)
# for i in range(n):
#     for j in range(m):
#         print(mymatrix[i][j])
#         # print((i, j))

# print(mymatrix[1][0])

# 1 2 3
# 4 5 6
# 7 8 9

# print(10 == 10)
# >=, <=, <, >, ==, !=
# nums = 10
# nums2 = 15
# nums = 15
# if nums == 10:
#     print("Happy")
# elif nums == 15:
#     print("Also Happy")
# else:
#     print("Not Happy")

# test_input = input("Hello There What IS Your Name?")
# print(test_input)

# nums_arr = [1, 3, 4, 2, 8, 6]
# nums_arr.sort()
# print(nums_arr)