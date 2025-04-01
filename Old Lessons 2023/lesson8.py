# recursion is when you call a function inside itself

def countdown(n):
    print(n)
    if n == 0:
        return
    else:
        countdown(n-1)

# the flow of the function countdown(5) -> countdown(4) -> countdown(3) .... countdown(0)

# non recursive
def leannefindFactorial(num: int) -> int:
    if num <= 0:
        return -1
    result = 1
    while num > 0:
        result *= num
        num = num - 1
    return result

def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num-1)

# print(factorial(4))

def findLargestSmallest(numbers: list[int]) -> tuple:
    if not numbers:
        return None

    numbers.sort()
    smallest = numbers[0]
    largest = numbers[-1]
    # smallest = largest = numbers[0]
    # for num in numbers:
    #     if num < smallest:
    #         smallest = num
    #     if num > largest:
    #         largest = num

    return largest, smallest

testlist = [8, 6, 5, 3, 9, 0, 21]

# print(findLargestSmallest(testlist))
testsentence = "Hello There"
def reverseWords(sentence: str) -> str:
    newlist = sentence.split()
    newlist.sort(reverse = True)
    newstr = " ".join(newlist)
    return newstr

# print(reverseWords(testsentence))
# for i in range(0, len(testsentence),2):
    # print(testsentence[i])
'[startingidx : endingidx : jump]'
print(testsentence[::])


