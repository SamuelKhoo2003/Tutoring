mygrid =  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#   012
# 0 123
# 1 456
# 2 789

n = len(mygrid)
m = len(mygrid[0])

# for rows in mygrid:
#     print(rows)

def sumofgrid(mygrid):
    total = 0
    for i in range(len(mygrid)): # going through the rows
        for j in range(len(mygrid[i])): # going through each element within the rows
            total += mygrid[i][j]
    return total

def sumofgrid2(mygrid):
    total = 0
    for rows in mygrid:
        total += sum(rows)
    return total

def evensumofgrid(mygrid):
    total = 0
    for i in range(len(mygrid)):
        for j in range(len(mygrid[i])):
            if (mygrid[i][j]%2 == 0):
                total += mygrid[i][j]
    return total

def rowsumofgrid(mygrid):
    rowsums = []
    for row in mygrid:
        rowsum = sum(row)
        rowsums.append(rowsum)
    return rowsums

# mygrid = [[1,2,3], [4,5,6], [7,8,9]]
# print(rowsumofgrid(mygrid))

# [6, 15, 24]

def columnsumofgrid(mygrid):
    colsums = []
    for j in range(len(mygrid[0])): # changing columms
        currtotal = 0
        for i in range(len(mygrid)): # changing rows
            currtotal += mygrid[i][j]
        colsums.append(currtotal)
    return colsums

# print(columnsumofgrid(mygrid))
# mylist = []
# mylist.append(10)
# print(mylist)


def buildgrid(rowlength, columnlength):
    newgrid = []
    for _ in range(rowlength):
        tmplist = [] # init rows
        for _ in range(columnlength):
            tmplist.append(0) # adding values to rows
        newgrid.append(tmplist)
    return newgrid

for row in buildgrid(4, 5):
    print(row)

