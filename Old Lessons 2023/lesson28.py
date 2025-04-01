# 1. use sets to write a function taking in 2 lists which returns the distinct values found in list1 but not list2. Your function should be of the form def distinct_diff(list1, list2), where list1 and list2 are integer or string lists respectively and it should return a set as a result. E.g. list1 = [1, 1, 2, 3, 4, 7, 7,'a','d','c']  and list2  = [2, 7,'d'] it should return the result of {1, 3, 4,'a','c'}. 

# my_set = {1, 2, 3, 4}
# my_set.add(5)
# # this is adding an element into the set
# print(my_set)
# Ans: {1, 2, 3, 4, 5}

# fruits = ['apple', 'orange', 'banana', 'cherry']
# # fruits.insert(1, "orange")
# # print(fruits)
# fruits.pop(1)
# fruits.pop() # we dont specify the index, it will remove the last element
# print(fruits)

# example_str = "hellothere"
# print(example_str.ischar())

# my_list = [1, 2, 3, 4, 5]
# for i in my_list:
#     if i == 4:
#         print("We break out of the loop here")
#         break
#     print(i)
# l1 = [1, 1, 2, 3, 4, 7, 7,'a','d','c']
# l2 = [2, 7,'d']
# def distinct_diff(list1, list2):
#     set1 = set(list1)
#     set2 = set(list2)
#     return set1 - set2
#     # return set1.symmetric_difference(set2)
# print(distinct_diff(l1, l2))
# # I expected to get {1, 3, 4, a, c}

# Given a list of keys and values as two seperate indexes, can you map these keys to their corresponding values using their index as a reference. 
# E.g. keys = ['Apples', 'Berries', 'Oranges', 'Bananas'] and values = [10, 20, 20, 10], 
# this should all be mapped together to form a dictionary of {'Apples': 10, 'Berries': 20, 'Oranges': 20, 'Bananas': 10}. 
# Write a function for this of the form def dict_map(keys, values). Your function should take in 2 lists and return a dictionary. 
# keys =  ['Apples', 'Berries', 'Oranges', 'Bananas'] 
# values = [10, 20, 20, 10]

# def dict_map(keys, values):
#     res_dict = {}
#     n = len(keys)
#     m = len(values)
#     if n != m:
#         print("Error there is a different number of keys and values")
#         return
#     else:
#         for i in range(n):
#             res_dict[keys[i]] = values[i]
#         return res_dict
    
# print(dict_map(keys, values))