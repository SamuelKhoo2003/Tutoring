def task1(n: int):
  # Start by initializing a variable n to any value (for example, n = 7), which represents the number for which the multiplication table will be generated.
  # Use a while loop to print the multiplication table from n * 1 to n * 10.
  # During each iteration, print the current multiplication result in the format n * i = result.
  # After printing, increment the multiplier (i) by 1 and continue the loop until i reaches 10.
#   2 x 1 = 2
#   2 x 2 = 4
#   2 x 3 = 6
#   2 x 4 = 8
#   .
#   .
#   .
#   2 x 10 = 20
  for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
  pass

def task2():
  # Loop through numbers from 1 to 20 (inclusive).
  # For each number:
  # Print "Fizz" if the number is divisible by 3.
  # Print "Buzz" if the number is divisible by 5.
  # Print "FizzBuzz" if the number is divisible by both 3 and 5.
  # If none of these conditions are true, just print the number itself.
    # range(start number, what you want you want to go up to/end number + 1, optional the difference you are changing by defaults to 1)
    # i = 1
    # while i < 21:
    #    print(i)
    #    i = i + 1

    for i in range(1, 21):
        if i % 5 == 0 and i % 3 == 0:
           print("FizzBuzz")
        elif i % 3 == 0:
           print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
           print(i)

    pass

def task3():
  # Python fundamental: Reverse a string
  # print out the reverse of the string
  my_string = "Hello, World!"
  return my_string[::-1]

#   new_str = ""
#   for i in range(len(my_string)-1, -1, -1):
#     new_str += my_string[i]
#   return new_str

    # for i in range(13, -1, -1):
    #     print(i)

    # return "DONE"


def task4():
   # leap year checker
   # we want the user to be able to enter a year and we check if it is a leap year or not
   # a year is a leap year if (it is divisible by 400) or (it is divislbe by 4 and not 100)
    num = int(input("Please type in a year: "))
    if num % 400 == 0 or (num % 4 == 0 and num % 100 != 0):
        print("That year is a leap year.")
    else:
      print("That year is not a leap year.")
    pass

if __name__ == "__main__":
    # task1(5)
    # task2()
    #   print(task3())
    task4()