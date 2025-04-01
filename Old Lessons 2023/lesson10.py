# homework 1

def leanne_is_leap_year(year):
  if year % 4 == 0:
    if year % 100 != 0:
        return True
    else:
        if year % 400 == 0:
           return True
    return False

# leap year is when its divisble by 4, if the year is also divisble by 100, then it also needs to be divisible by 400

def marcus_is_leap_year(year):
  if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
      return True
  else:
      return False


# yearlist = [2023, 2020, 2000, 1900, 2024]
# for year in yearlist:
#     if leanne_is_leap_year(year):
#        print(f"{year} is a leap year")
#     else:
#        print(f"{year} is not a leap year")

def leanne_square_maker (dimensions: int, newchar: str):
    print(f"Square of Dimensions {dimensions} x {dimensions}:")
    for i in range (dimensions):
        print(newchar * dimensions)

#  Your output for print_triangle(5, *) should be:
#  Printing a triangle with height 5:
#  * 1
#  ** 2
#  *** 3
#  **** 4
#  ***** 5
# each time increment by 1,

def leanne_triangle_maker (height: int, newchar: str):
   print(f"Printing a triangle with height {height} with character {newchar}:")
   for i in range(1, height + 1):
      print(newchar * i)
   return

# def marcus_triangle_maker (height: int, newchar: str):
#    print(f"Printing a triangle with height {height}")
#    return

# inp_height = int(input("Please enter the height and width of the triangle: "))
# inp_char = input("Please enter the character used within the triangle: ")
# leanne_triangle_maker(inp_height, inp_char)

# mychar = "M"
# mynum = 5
# print(mychar * mynum)

# for i in range(mynum):
#    print(mychar)
# #    print(mychar, end="")


# Printing a Christmas tree with height 5:
# 1     * 1 = 2x1 -1       space = 4, 3, 2, 1, 0
# 2    *** 3 = 2x2 -1
# 3   ***** 5 = 2x3 - 1
# 4  ******* 7 = 2x4 - 1
# 5 ********* 9 = 2x5 - 1



def christmas_tree_maker (height: int, newchar: str):
    print(f"Printing a christmas tree with height {height} and with character {newchar}:")
    for i in range(1, height + 1):
        num_spaces = height - i
        num_characters = 2*i - 1
        print(" "*num_spaces + newchar*num_characters)
    base_space = height - 1
    print(" "*base_space + newchar)

inp_height = int(input("Please enter the height and width of the christmas tree: "))
inp_char = input("Please enter the character used within the christmas tree: ")
christmas_tree_maker(inp_height, inp_char)
