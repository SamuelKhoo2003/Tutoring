# 1. Write a Python function that takes a list of strings as input and returns a set containing all the unique words present in the list.
# e.g. string_list = ["Hello world", "Python is awesome", "Hello Python"] should give an output of {"Hello", "world", "Python", "is", "awesome"}

# def string_set(string_list):
#     res_set = set()
#     for string in string_list:
#         temp_string_list = string.split()
#         for char in temp_string_list:
#             # print(char)
#             res_set.add(char)
#             # print(res_set)
#         # for char in string:
#         #     print(char)
#         # print(string)
#     return res_set
# string_list = ["Hello world", "Python is awesome", "Hello Python"]
# print(string_set(string_list))

# demo_str = "this.is.a.demo.for.showing.string.splitting"
# demo_res = demo_str.split(".")
# print(demo_res)

# 2. Write a Python function that takes a list of elements as input and returns a new list with duplicate elements removed, preserving the original order of elements. You should solve this problem using sets.
# e.g input_list = [1, 2, 3, 2, 4, 5, 6, 5] should give output of [1, 2, 3, 4, 5, 6]

# def marcus_attempt(input_list):
#     res = []
#     input_set = set(input_list)
#     for element in input_set:
#         res.append(element)
#         print(res)
#     return res
#     # for element in input_list:
#     # def remove_duplicate(input_list)
#     #     for element in input_list:

# input_list = [1, 2, 3, 2, 4, 5, 6, 5]
# # print(set(input_list))
# print(marcus_attempt(input_list))
# print(leanne_attempt(input_list))

# 3. Write a Python function that takes a string as input and returns a dictionary where the keys are the words in the string, and the values are the frequency of each word.
# e.g. input = "Python is an amazing programming language. Python is used for web development, data science, and more."
# output = {
#     'python': 2,
#     'is': 2,
#     'an': 1,
#     'amazing': 1,
#     'programming': 1,
#     'language.': 1,
#     'used': 1,
#     'for': 1,
#     'web': 1,
#     'development,': 1,
#     'data': 1,
#     'science,': 1,
#     'and': 1,
#     'more.': 1
# }

# example_input = "Python is an amazing programming language. Python is used for web development, data science, and more."
# example_input2 = "Today is Sam's birthday, today he turns twenty, today he is planning a Birthday party."
# # print(example_input.split())

# # our base logic was iterating over string and counting how many times each words appear as we go across
# def freq_dict(example_input):
#     res_dict = {}
#     for word in example_input.split():
#         tmp = word.lower().strip(".,")
#         if tmp in res_dict:
#             res_dict[tmp] += 1
#         else:
#             res_dict[tmp] = 1
#         # print(res_dict)
#     return res_dict

# print(freq_dict(example_input2))

# 4. Write a Python function that takes a string as input and returns a dictionary where   keys are the characters in the string, and the values are the frequency of each character.
# e.g. input = "Hello World"
# output  = {
# 'H': 1,
# 'e': 1,
# 'l': 3,
# 'o': 2,
# ' ': 1,
# 'W': 1,
# 'r': 1,
# 'd': 1
# }

# def marcus(input_str):
#     count_characters = {}
#     for char in input_str:
#         if char not in count_characters:
#             count_characters[char] = 1
#         else:
#             count_characters[char] += 1
#         # print(char)
#     return count_characters
#     # def count_characters(string):

# def leanne(input_str):
#     def count_characters:
#         count_character ={}
#         for character in string:
#     input_string = "Hello world"

# myinput = "Hello World"
# myinput2 = "This is a different test sentence"
# print(marcus(myinput))
# print(leanne(myinput2))

def func(input):
    return input + 10

# by default we always expect to return something
# inside the brackets of a function tends to be its input
# new_res = func(2)+4
# print(new_res)
# # func(2)

# mylist= ['a', 2, 'b', 4, 'c']
# print(mylist[0])

myset = {1, 2, 3, 4} # NO DUPLICATE ELEMENTS
myset.remove(4)
myset.add(4)
myset.add('marcus')
print(myset)
# print(myset[0]) # THIS DOESNT EXIST

mydict = {'b': "HELLO", 'a': 4} # KEYS HAVE TO BE UNIQUE
print(mydict['a'])
mydict['a'] += 6
print(mydict)
# print(mydict[0])

