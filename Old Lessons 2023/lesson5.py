# 1. Write me a function def homecountry(country: str) -> str:, this function should return the sentence "Your home country is ...". An example behaviour for this is seen below:
# homecountry(Malaysia)
# output: Your home country is Malaysia

def homecountry(country: str) -> str:
    return f"home country is {country}"

# newstring = "marcus' " + homecountry("Canada")
# print(newstring)
# print(result)  # Output: "Your home country is Canada."

# 2. Construction a function which prints the sum of a list of numbers and returns a sorted version of the original list. Your function should be def sumsort(nums: List[int]) -> List[int]:
# hint: remember the difference between printing and returning, also remember to use .sort() to sort a list!
# example behaviour is seen below:
# output:
# 44
# [0, 3, 5, 7, 9, 20]


# testvar = "hello there"
# print(testvar)


# def marcus_sumsort(nums: list[int]) -> list[int]:
#     print(sum(nums))
#     # nums = nums.sort()
#     return sorted(nums)

# testlist1 = [5, 2, 8, 3, 1]
# print(marcus_sumsort(testlist1))

def leanne_sumsort(nums: list[int]) -> list[int]:
    print(sum(nums))
    nums.sort()
    return nums

testlist2 = [4, 7, 11, 3, 6]
# result2=leanne_sumsort(testlist2)
print(leanne_sumsort(testlist2))


# 3. Write me a function def basicmath() that has 2 input statements for integers and then prints out the sum, multiplication and difference of both inputs. This is a harder question so spend some time thinking about it and ask me for more hints if needed!
# example behaviour is seen below:
# basicmath()
# output:
# Enter your 1st value: (the user should input a number/float here, for now lets just set this at 7)
# Enter your 2nd value: (the user should input a number/float here, for now lets just set this a 5)
# Sum is = 12
# Difference is = 2
# Product is = 35
# hints: remember to use abs() when finding the difference to return the absolute value. Remember that there should be no input statements outside of your function. Below you can find an idea of how to start:
# def basicmath():
#   val1 = int(input(...))
#   val2 = int(input(...))
#   this is followed by code which produced the values which I requested.

#Marcus

# def marcusbasicmath():
#     num1 = int(input("Enter your first number"))
#     num2 = int(input("Enter your second number"))
#     total_sum = num1 + num2
#     different = abs(num1 - num2)
#     product = num1 * num2
#     print("sum is = ", total_sum)
#     print("difference is  = ", different)
#     print("Product is = ", product)

# marcusbasicmath()



# #leanne
# def leannebasicmath():
#     val1_int = float(input("Choose a number"))
#     val2_int = float(input("Choose a another number"))
#     # val1_int = float(val1)
#     # val2_int = float(val2)
#     my_sum = val1_int + val2_int
#     difference = abs(val1_int - val2_int)
#     product = val1_int * val2_int
#     print(f"The sum is: {my_sum}")
#     print(f"The difference is: {difference}")
#     print(f"The product is: {product}")

# leannebasicmath()

# testlist = [0, 9, 8, 5, 20]
# testlist.sort(reverse = True)
# print(testlist)

# sorted(testlist)