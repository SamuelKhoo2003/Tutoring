#Q1
# number = int(input("😎 Please type in a number: 😎"))
# if number < 0:
#    print("The number is negative.")
# elif number == 0:
#   print("The number is zero.")
# else:
#    print("The number is positive.")


# number = int(input("Enter a number"))
# # %2 basically checking whether it is even
# if number > 0:
#   print("The number is positive")
# else:
#   print("The number is negative") 


# Q2
# number = int(input("😎 Please type in a number: 😎"))

# if number < 0:
#    abs_value = -number
# else:
#    abs_value = number

# print("The absolute value of this number is", abs_value)

# number = int(input("Enter a number"))

# if number < 0:
#   print(f"The absolute value of the number is {number*-1}")

# else:
#   print(f"The absolute value of the number is {number}")

# demo ans
# num = int(input("Please enter a number"))
# print(abs(num))

#Q3
# Please write a program that prints all positive even numbers up to the limit inputed by the user initially. (this is similar to our limit while loop exercise!). If the limit is < 0 print an error! HINT: use the remainder check, num%2 = remainder after number divded by 2 
# Note: if remainder is 0 the number is even, if remainder is not 0, number is odd
# #Sample output1: 
#   Please type in a limit: 5
#   0
#   2
#   4
#   All even numbers up to 5 have been printed!
# #Sample output2: 
#   Please type in a limit: -3
#   No positive even numbers below -3
# #Sample output3:
#   Please type in a limit: 8
#   0
#   2
#   4
#   6
#   8
#   All even numbers up to 8 have been printed!

# limit = int(input("Please type in a limit: "))
# if limit < 0:
#     print(f"No positive even numbers below {limit}")
# else:
#     for i in range(limit+1): 
#         if i%2 == 0:
#             print(i)
#     print(f"All even numbers up to {limit} have been printed!")
    


# limit = int(input("Please type in a limit: "))
# res = []
# even = []
# if limit < 0:
#     print(f"No positive number in range of {limit}")
# else:
#     curr_sum =0
#     for i in range(limit +1) :
#         if i%3 == 0:
#             res.append(i)
#             curr_sum += i
#         if i%2 == 0:
#             even.append(i)
        
#     print(f"All numbers that are divisible by 3 up to {limit} is {res}")
#     print(f"All even numbers in range of {limit} are {even}")
#     print(f"The sum of all even numbers in range of {limit} is {sum(even)}")
#     print(f"The count of numbers divisible by 3 is {len(res)}")





# limit = int(input("Please type in a limit:"))
# if limit <0:
#     print(f"No positive numbers below {limit}")
# else:
#     for i in range(limit+1):
#         if i%3 == 0:
#             print(i)
#         if i%2 == 0:
#             print(i)

#     # for i in range(0, limit+1, 3):
#     #     print(i)
#     print(f"All numbers that are multiples of 3 have been printed up to {limit}")

# count_positive = 0
# count_negative = 0

# while True:
#     num = int(input("😎 Please enter a number 😎:"))
#     if num == 0:
#         break
#     elif num < 0:
#         count_negative += 1
#     else:
#         count_positive += 1

# print(f"The number of positive numbers added: {count_positive}")
# print(f"The number of positive numbers added: {count_negative}")

def helloworld():
    print("helloworld")

def numcheck(nums: int):
    tmplist = []
    for i in range(nums):
        tmplist.append(i)
    return tmplist

helloworld()
helloworld()
mylist = numcheck(6)
mylist.append(10)
print(mylist)

