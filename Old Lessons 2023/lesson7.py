def leannepalindromic(input_num: int) -> bool:
    return str(input_num) == str(input_num)[::1]

def marcuspalindromic(input_num: int) -> bool:
    numstr = str(input_num)
    reversedstr = numstr[::1]
    return reversedstr == numstr


# x = 12621
# if not leannepalindromic(x):
#     print("Number is not palindromic")
# else:
#     print("Number is palindromic")

# 4. Write a function isPrime(n: int) -> bool that determines whether a given integer n is a prime number. The function should return True if n is prime and False otherwise. Remember that a prime number is a positive integer greater than 1 that has no positive divisors other than 1 and itself.

def isPrime(number: int) -> bool:
    if number < 2:
        return False
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True


# for test1 in range(1, 999):
#     if isPrime(test1):
#         print(f"{test1} is prime")

# test2 = 99
# if not isPrime(test2):
#     print("This number is not a prime number")
# else:
#     print("This number is prime")


# recursion
# string manipulation
# vscode

# def recursedemo(n):
#     if n < 1:
#         return False
#     return recursedemo(n-1)