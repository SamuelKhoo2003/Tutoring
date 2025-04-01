# import datetime
# import math

# result = math.lcm(15, 20)
# print(result)

# x = datetime.datetime.now()
# print(x)

# x = math.ceil(9.8)
# y = math.floor(9.2)
# print(x, y)

# math.ceil() # rounds up to larger integer
# math.floor() # rounds down to smaller integer
# math.lcm() # returns the least common multiple of two integers
# math.sqrt() # returns the square root of a number
# math.pow() # returns the power of a number
# math.abs() # returns the absolute value of a number

# mychar = "M"
# print(ord(mychar))

# s = "hHeElloO"
# # refchar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# newstring = ""
# for char in s:
#     if ord(char) > 100:
#         newstring += char
# print(newstring)
# print("hello")

# FizzBuzz Problem
#The function takes an input n where it iterates from 1 to n, if the number if is a multiple of 3 then we print Fizz if the number if a multiple of 5 we print Buzz, if it is a multiple of both we print FizzBuzz
def fizzbuzz(n):
    # if number multiple of 3, we should print fizz
    if n % 5 == 0 and n % 3 == 0:
        print("fizzbuzz")
    # if number is multiple of 5, we should print buzz
    elif n % 5 == 0:
        print("buzz")
    # if number if multiple of 3 and 5 we should print fizzbuzz
    elif n % 3 == 0:
        print("fizz")
    # else just print the number
    else:
        print(n)

# fizzbuzz(15)

def fizzbuzz2(n):
    res_string = ""
    if n % 3 == 0:
        res_string += "fizz"
    if n % 5 == 0:
        res_string += "buzz"
    if n % 3 != 0 and n % 5 != 0:
        res_string = n
    print(res_string)
# fizzbuzz2(15)


# "listen" and "silent" are anagrams

def anagram_check(s1, s2):
    # if len(s1) != len(s2):
    #     return False
    # for char in s2:
    #     if char not in s1:
    #         return False
    # return True
    if sorted(s1) != sorted(s2):
        return False
    return True

# print(anagram_check("listen", "silent")) # return true
# print(anagram_check("heart", "earth")) # return true
# print(anagram_check("hello", "apple")) # return false

def is_valid(nums):
    numlist = []
    for char in nums:
        if char != ".":
            curr_num = int(char) # convert string to integer
            if curr_num in numlist:
                return False
            if curr_num > 9 or curr_num < 0:
                return False
            numlist.append(int(char))
    return True

testlist = ["6", "7", "8", "9", "."]
print(is_valid(testlist))

# def is_valid_sudoku(board):
#     for row in board:
    # ["5","3",".",".","7",".",".",".","."],
    # ["6",".",".","1","9","5",".",".","."],
    # [".","9","8",".",".",".",".","6","."],
    # ["8",".",".",".","6",".",".",".","3"],
    # ["4",".",".","8",".","3",".",".","1"],
    # ["7",".",".",".","2",".",".",".","6"],
    # [".","6",".",".",".",".","2","8","."],
    # [".",".",".","4","1","9",".",".","5"],
    # [".",".",".",".","8",".",".","7","9"] 