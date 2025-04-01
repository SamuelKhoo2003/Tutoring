# # Recap of basics
# def my_function(arg1, arg2):
#     if arg1 == arg2:
#         print("same character")
#         return
#         # return "same character"
#     else:
#         print("different character")
#         return
#         # return "different character"

# # Calling Functions
# a, b = 3, 3
# # print(my_function(a, b))
# my_function(a, b)

# Lists
my_list = [45, 32, 36]
# print(sum(my_list))
# print(sorted(my_list)) # returns sorted copy of your list
# my_list.sort() # this sorts it in place
# print(my_list)
my_list.append(47)
my_list.append(38)
my_list.append(47)
# my_list.pop()
# print(my_list)

# expected my_list
# [45, 32, 36, 47, 38, 47]
# 45 is at position 0
# 32 is at position 1
# 36 is at position 2 ...
# my_list.pop(2)
# my_list.pop(3)
# my_list.remove(47) # doesn't remove every instance only the first occurance
# print(my_list)
# my_list_2 = [20, 10, 10, 30]
# print(my_list_2.index(10)) # this is returning the index for the first instance of the value in your array/list
# print(my_list)
# print(my_list[4])

# printing elements in a list
# print()
# for i in range(len(my_list)): # this gives you the most control over iteration
#     print(f"Element at {i} is {my_list[i]}")

# for ele in my_list: # this works if you just want the elements
#     print(ele)

# for idx, ele in enumerate(my_list):
#     print(f"Element at {idx} is {ele}")
# for i in range(2, 10):
#     print(i)

# Sets
# print(set(my_list))
# my_set = set(my_list)
# print(my_set)
# my_set.add(30)
# print(my_set)
# my_set.remove(38)
# print(my_set)

# Arithemtic Operators
a, b = 4, 2
print(a + b)
print(a - b)
print(a * b)
print(a // b) # floor division (divides and rounds down)
print(a / b) # divides and gives decimaL answer
print(a % b) # the remainder after dividing

# if __name__ == "__main__":
