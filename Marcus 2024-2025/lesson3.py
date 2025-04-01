# take an input for 3 letters, given these 3 letters we want to find the middle letter
# e.g. b, a, c the middle is b, or for j, r, e the middle is j
# some base code has been written to get the letters
def task1():
    letter1 = input("Letter 1: ").lower()
    letter2 = input("Letter 2: ").lower()
    letter3 = input("Letter 3: ").lower()
    letters = [letter1, letter2, letter3]
    letters.sort()
    print(f"The middle letter is {letters[1]}")


# Create a Python program that calculates the amount of tax to be paid on a gift based on its value in dollars. The tax brackets are as follows:

# - No tax for gifts under 5,000 dollars.
# - For gifts between 5,000 and 25,000 dollars, the tax is 100 dollars plus 8% of the amount exceeding 5,000 dollars.
# - For gifts between 25,000 and 55,000 dollars, the tax is 1,700 dollars plus 10% of the amount exceeding 25,000 dollars.
# - For gifts between 55,000 and 200,000 dollars, the tax is 4,700 dollars plus 12% of the amount exceeding 55,000 dollars.
# - For gifts between 200,000 and 1,000,000 dollars, the tax is 22,100 dollars plus 15% of the amount exceeding 200,000 dollars.
# - For gifts exceeding 1,000,000 dollars, the tax is 142,100 dollars plus 17% of the amount exceeding 1,000,000 dollars.

# Write a program that takes the value of the gift in dollars as input and calculates and prints the tax based on the above rules.
def task2():
    gift_value = int(input("Value of gift: "))
    tax = 0
    if gift_value < 5000:
        tax = 0
    elif 5000 <= gift_value < 25000:
        tax = 100 + 0.08 * (gift_value - 5000)
    elif 25000 <= gift_value < 55000:
       tax = 1700 + 0.10 * (gift_value - 25000)
    elif 55000 <= gift_value < 200000:
       tax = 4700 + 0.12 * (gift_value - 55000)
    elif 200000 <= gift_value < 1000000:
       tax = 22100 + 0.15 * (gift_value - 200000)
    else:
       tax = 142100 + 0.17 * (gift_value - 1000000)

    print(f" The tax to be paid of a gift of ${gift_value} is: ${tax:.2f}")

# Write a Python program that converts a score (between 0 and 100) into a grade based on the following scale:

# If the score is less than 0 or greater than 100, the program should print "Grade: impossible!".
# For scores between 0 and 49, print "Grade: fail".
# For scores between 50 and 59, print "Grade: 1".
# For scores between 60 and 69, print "Grade: 2".
# For scores between 70 and 79, print "Grade: 3".
# For scores between 80 and 89, print "Grade: 4".
# For scores between 90 and 100, print "Grade: 5".
# The program should take the score as input and then print the corresponding grade based on the above criteria.
def task3():
    point = int(input("Number of points [0-100]: "))
    if point < 0 or point > 100:
        print("Grade: impossible!")
    elif point < 50:
        print("Grade: fail")
    elif point <60:
        print("Grade: 1")
    elif point < 70:
        print("Grade: 2")
    elif point < 80:
        print("Grade: 3")
    elif point < 90:
        print("Grade: 4")
    else:
        print("Grade: 5")

# Pin/Password Test
def pin_attempts():
    attempts = 0
    while True:
        pin = int(input("4 Digit PIN: "))
        attempts += 1
        if attempts > 5 or pin == 1234:
            break
        print("Wrong")
    if attempts > 5:
        print("Sorry maximum attempts for pin reached.")
    else:
        print(f"Correct it took you {attempts} attempts to get the right pin!")


def countdown():
    num = int(input("Please enter the number you would like to countdown from: "))
    if num < 0:
        print("Impossible to count down!")
        return
    else:
        print(num)
        while True:
            num -= 1
            print(num)
            if num == 0:
                break
        print("Now! ")

def password_checker():
    password1 = input("Password: ")
    while True:
        password2 = input("Confirm Password: ")
        if password1 != password2:
            print("They don't match!")
        else:
            break
    print("User password has been verified. ")

def numbers_tracker():
    count = 0
    positive = 0
    negative = 0
    num_sum = 0
    print("Please type in integer numbers or type in 0 to finish the program.")
    while True:
        num = int(input("Number: "))
        if num == 0:
            break
        count += 1
        num_sum += num
        if num > 0:
            positive += 1
        else:
            negative += 1
    
    print(f"Total numbers added: {count}")
    print(f"Positive numbers: {positive}")
    print(f"Negative numbers: {negative}")
    print(f"The sum of all numbers is {num_sum}")
    print(f"The mean of all numbers is {num_sum/count:.2f}")


if __name__ == "__main__":
    # pin_attempts()
    # countdown()
    # password_checker()
    numbers_tracker()