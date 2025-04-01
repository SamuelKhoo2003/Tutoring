def task_demo():
    # num_array = [1, 2, 3, 4, 5, 6, 7, 8]
    # stack = []
    # for number in num_array:
    #     stack.append(number)
    #     print(stack)
    #     if number % 2 != 0:
    #         stack.pop()
    #     print(stack)
    # return stack

    # stack = ["ele1", "ele2", "ele3", "ele4"]
    # removed = None
    # while stack and removed != "ele2":
    #     removed = stack.pop()
    #     print(removed, stack)
    # return stack

    array = [2, 4, 6, 8]
    test_string =  "thisisatest"
    final = ["ele1", 2, "ele3", 4]

    # for num in array:
    #     print(num)
    # for i in range(0, len(array)):
    #     print(array[i])
    # for character in test_string:
    #     print(character)
    # for i in range(0,len(test_string)):
    #     print(test_string[i])

    # for i in range(0,len(final)):
    #     # print(i)
    #     print(final[i])
    pass


def task1():
    # a stack follows a LIFO (last in first out order) [1, 2, 3] stack.pop() == 3
    # (()) trying to check if its balanced (this is balanced)
    # )() not balanced
    # )( not balanced
    bracket_string = input("Please type in a string of parentheses: ")
    for character in bracket_string:
        print(character)
    # stack = []

    pass

def task2():
    # print out the value at every even index/position of an array
    array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    for i in range(0, len(array)):
        if i % 2 == 0:
            print(array[i])
    pass

def task3():
    pass

def task4():
    pass

if __name__ == "__main__":
    # task_demo()
    task2()
    # print(task_demo())
    # print(task1())
