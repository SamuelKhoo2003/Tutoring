# Daily Wage Calculator
def calculateDaily():
    wage = float(input("Hourly wages: "))
    hours = int(input("Hours worked: "))
    day = input("Day of the week: ")

    payment = wage * hours

    # if its the weekend you get paid 2x the normal amount
    if day.upper() == "SUNDAY" or day.upper() == "SATURDAY":
        payment *= 2

    print(f"Your daily wage is {payment} dollars.")


def floatExample(number):
    print(f"The float representation is {float(number)}")
    print(f"The integer representation is {int(number)}")

# Points Calculator
# We have a points calculator, get input of how many points on this card
# If points < 100 its worth normal, if >= 100 its worth 1.15x its normal amount
# Print how many points/value of points the person has
def pointsCalculator():
    cardPoints = int(input(f"How many points are on your card? "))
    if cardPoints >= 100:
        cardPoints *= 1.15
        print("Your points have a bonus value of 15%.")
    print(f"You now have {cardPoints} points.")


# This will give us the decimal part of a number and the integer part of a number
def numberCasting():
    number = float(input("Please type in a number: "))
    integer = int(number)
    decimal = number - integer
    print(f"The integer part is {integer} and the decimal part is {decimal}")

# This program should get the name and age for Person1 and Person2 
# then if Person1 is older than Person2 we print this out, viceversa, then a special statement if they are the same age
def findTheElder():
    def getPersonDetails():
        print("Person Details: ")
        name = input("Name: ")
        age = input("Age: ")
        return name, age

    name1, age1 = getPersonDetails()
    name2, age2 = getPersonDetails()
    if age1 > age2:
        print(f"The elder is {name1}.")
    elif age2 > age1:
        print(f"The elder is {name2}.")
    else:
        print(f"{name1} and {name2} are the same age.")

# Word comparison
# its an important concept to know
def compareWords():
    word1 = input("Please type in your first word: ")
    word2 = input("Please type in your second word: ")

    if word1 > word2:
        print(f"{word1} comes alphabetically last. ")
    elif word2 > word1:
        print(f"{word2} comes alphabetically last. ")
    else:
        print("Both of the words are the same. ")


# age check
def ageCheck():
    # get the age
    age = int(input("What is your age? "))

    # if age less than 0 we print it must be a mistake
    if age < 0:
        print("That must be a mistake.")
    # if age less than 5 we print I suspect you cant write yet
    elif age < 5:
        print("I suspect that you can't write yet! ")
    # else you print, Ok, you are years old
    else:
        print(f"Ok, you are {age} years old! ")

if __name__ == "__main__":
    ageCheck()
