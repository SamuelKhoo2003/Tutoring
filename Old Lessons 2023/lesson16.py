
# 1. Write a function find_max(mygrid) that finds and returns the maximum value in the given grid.
mygrid =  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[1, 2, 3, 4]
def find_max (mygrid):
    curr_max = 0
    for row in mygrid:
        for value in row:
            if value > curr_max:
                curr_max = value
    return curr_max

print(f"The maximum value in the grid is: {find_max(mygrid)}")

# 2. Write me a function that returns the sum of the diagonal from a square grid in the case of grid:

def diag_sum (mygrid):
    diagsum = 0
    for i in range(len(mygrid)):
        diagsum += mygrid[i][i]
    return diagsum

print(f"The sum of diagonals in the grid is: {diag_sum(mygrid)}")
            # 0       1       2       3      4     5
# mylist = ["hello", "hi", "here", "marcus", 10, 90.23]
#  0 1 2
# 0_
# 1  _
# 2    _
# [[123],
# [456],
# [789]]
# # print(mygrid[0][1])
# # print(mygrid[2][0])
# # print(mygrid[2][2])
# # # print(mylist[2])
# # print(mygrid[1][2])

# print(mygrid[0][0], mygrid[1][1], mygrid[2][2])

# numlist = [10, 67, 40]
# print(sum(numlist))

