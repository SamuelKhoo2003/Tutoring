def LeanneFilterList(mylist, k):
    res = []
    for word in mylist:
        if len(word) == k:
            res.append(word)
    return res

# doing things inplace

testlist = ['hello', 'marcus', 'bingo', 'dog', 'right']
# print(LeanneFilterList(testlist, 5))


# 2. Write a function def findFactorial(num: int) -> int: this function should find and return the factorial of the number inputed. I would recommend either using a for or while loop to complete this operation!. If the factorial cannot be found, then the function should return -1. This function should not print anything!
# Remember that you can only find the factorial for numbers above 0, so keep this in mind with you while loop (e.g. if num > 0 or while num != 0). Theres many ways to approach this so choose the way which you understand/suits you best. 
# Factorial explaination: 5 factorial is 5x4x3x2x1 = 120

def leannefindFactorial(num: int) -> int:
    if num <= 0:
        return -1
    result = 1
    while num > 0:
        result *= num
        num = num - 1
    return result

def marcusfindfactorial(num: int) -> int:
    if num <= 0:
        return -1
    factorial = 1
    while num > 0:
        factorial *= num
        num -= 1
    return factorial


# print(leannefindFactorial(5))
# print(marcusfindfactorial(5))

print("abcdef"[::-2])