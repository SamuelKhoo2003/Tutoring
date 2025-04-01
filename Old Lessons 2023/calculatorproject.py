# TEST CASES)

# MAIN
print("<Welcome to Calculator V1>")
activate = input("Please type start to continue!\n")

if activate == "start":
    n1 = float(input("Please enter your first number!\n"))
    while n1 > 999:
        print("Error, please enter a number less than 999.")
        n1 = float(input("Please enter your first number!\n"))

    op = input("Please enter your calculator operation.\n")
    operation_check = ["x", "X", "*", "-", "+", "/", "//", "%", "^", "**"]
    while op not in operation_check:
        print("Error, operator entered is invalid!")
        op = input("Please enter your calculator operation.\n")

    n2 = float(input("Please enter your second number!\n"))
    while n2 > 999:
        print("Error, please enter a number less than 999.")
        n2 = float(input("Please enter your second number!\n"))

    res  = float('-inf') # its saying that this variable has no value at the moment

    if op == "X" or op == "x" or op == "*":
        res = n1 * n2

    if op == "+":
        res = n1 + n2

    if op == "-":
        res = n1 - n2

    if op == "^" or op == "**":
        if n1 > 10 or n2 > 20:
            print("Error, the value calculated is too large!")
        else:
            res = n1 ** n2

    if op == "/":
        if n2 == 0:
            print("Error, can't divide anything by zero, please change your inputs.")
        else:
            res = n1 / n2

    if op == "//":
        if n2 == 0:
            print("Error, can't divide anything by zero, please change your inputs.")
        else:
            res = n1 // n2

    if op == "%":
        if n2 == 0:
            print("Error, can't divide anything by zero, please change your inputs.")
        else:
            res = n1 % n2

    if res != float('-inf'):
        print(f"The result of {n1} {op} {n2} is {res}")
    else:
        print("An error has occurred, please try again.")
else:
    print("Terminating calculator, thank you and have a nice day :)")

