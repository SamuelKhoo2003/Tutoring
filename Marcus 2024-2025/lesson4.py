def task1():
  # Requirements:
  # - Create a loop that asks the user to guess a secret number between 1 and 10.
  # - If the guess is correct, print a success message and break the loop.
  # - If the guess is incorrect, print a message asking them to try again.
  # - Continue until the correct number is guessed.

  # Define the secret number (for example, set it to 7)
  secret_number = 7
  while True:
    num = int(input("Guess the number [1-10]: "))
    if num == secret_number:
      print("Congratulations your guess is correct! ")
      break
    else:
      print("Incorrect, please try again! ")
  pass


def task2():
  # Requirements:
  # - Create a loop that repeatedly asks the user to input numbers.
  # - Keep a running sum of the numbers entered.
  # - If the sum exceeds 100, print the final sum and break the loop.
  # - After each input, print the current sum unless the sum exceeds 100.

  # Initialize a variable to hold the sum of numbers
  total_sum = 0
  while True:
    num = int(input("Next number: "))
    total_sum += num # you are adding it to the total sum to keep track of all numbers written/inputted so far
    if total_sum > 100:
      print(f"The final sum is {total_sum}")
      break
    else:
      print(f"The sum is currently {total_sum}")
  # Your code here: Write the loop to keep adding numbers to the sum and break if it exceeds 100.
  pass


def task3():
    # Requirements:
    # - Create a loop that asks the user to input numbers.
    # - If the number is even, add it to a list.
    # - If the user inputs the number `0`, break the loop and print all the even numbers collected.
    # - After each even number is added, print a message indicating it was added.

    # Initialize an empty list to store even numbers
    even_numbers = []
    while True:
        num = int(input("Please enter a number or 0 to stop the programme: "))
        if num == 0:
           break
        if num % 2 == 0: # all even numbers are divisible by 2
            even_numbers.append(num)
            print(f"{num} was added to our list of even numbers.")
    print(f"The list of all even numbers is {even_numbers}")


    # Your code here: Write the loop to collect even numbers and stop when 0 is entered.
    pass


def task4():
    odd_numbers = []
    while True:
        num = int(input("Please enter a number or 0 to stop the programme: "))
        if num == 0:
            break
        if num % 2 == 1:# % gives me the remainder after dividng by x number
            odd_numbers.append(num)
            print(f"{num} was added to our list of odd numbers.")
    print(f"The list of all odd numbers is {odd_numbers}")

if __name__ == "__main__":
  task4()