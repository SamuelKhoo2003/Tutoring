def marcus_multiplication_table (number, range_start, range_end):
    print(f"Multiplication Table for {number} (from {range_start} to {range_end})")
    for i in range(range_start, range_end+1):
        result = number * i
        print(f"{number} x {i} = {result}")

def leanne_multiplication_table (number, range_start, range_end):
    print(f"Multiplication Table for {number} (from {range_start} to {range_end})")
    for i in range(range_start, range_end+1):
        answer = number*i
        print(f"{number} x {i} = {answer}")

# try:
#     number = int(input("Choose a number for its multiplication table"))
# except:

# marcus_multiplication_table (5, 1, 10)

# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21

# Square of Dimensions 5 x 5:

#####
#####
#####
#####
#####

def marcus_square_maker (dimensions, newchar):
    print(f"Square of Dimensions {dimensions} x {dimensions}:")
    for i in range(dimensions):
        for j in range (dimensions):
            print(newchar, end="")
        print("")

def leanne_square_maker (dimensions: int, newchar: str):
    print(f"Square of Dimensions {dimensions} x {dimensions}:")
    for i in range (dimensions):
        print(newchar * dimensions)

# marcus_square_maker(5, "S")
# leanne_square_maker(5, "W")


def marcus_rectangle_maker (length: int, width: int, newchar: str):
    print(f"Rectangle of Dimensions {length} x {width}:")
    for i in range(length):
        for j in range (width):
            print(newchar, end="")
        print("")

def leanne_rectangle_maker (length: int, width: int, newchar: str):
    print(f"Rectangle of Dimensions {length} x {width}:")
    for i in range (length):
        print(newchar * width)
marcus_rectangle_maker(7, 4, "#")
leanne_rectangle_maker(7, 4, "W")

