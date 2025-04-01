# RECAP
def myfunc(myinput):
    myinput * 2
    return myinput
# if we return theres no output

# curnum = 5
# print(myfunc(curnum))

mylist = [1, 2, 5, 7, 9, 10, 16]
# mylist.sort()
# mylist.append(5)

# i = 0
# while (i < 10):
#     print(i)
#     i+=1

# for i in range(10):
#     print(i)

# for curr_val in mylist:
#     print(curr_val)
    # we have set curr_val as a tracing variable , we dont specify any length/limit the range

# for i in range(len(mylist)):
#     print(mylist[i])


# 0 indexing
# indexing isnt limited to lists, it works for strings
# index =     0       1      2       3       4 or -1
ex_list = ["val1", "val2", "val3", "val4", "val5"]
# print(len(ex_list))  # print 5

# print(ex_list[-1]) # accesses the last element
#           0123456789-1
mystring = "test_string"
# print(mystring[::-1])
# print(mystring[0])
# print(mystring[-1])
# print(mystring[::2])
# print(mystring[2:7]) # if i put [i:j] without a ":" after j, it assumes normal jumping/index increments
# [2:7] all values from index 2 up to but not including index 7

# [first index where you want to print from: the last index you want to stop at: the gap/jump between indexes]
a = 2
b = 0
c = 4
# print(a == b)
# print(a != b)
# print(a ** b)
# print(a // c)
# print(a / c)
# print(a % c) # gives us the value of the remainder after a divides by c

# "*=", "+=" 
# a = a + 1
# a += 1


# DICTIONARIES
mydict = {}
numlist = [0, 0, 1, 2, 3, 3, 4, 4, 5, 6, 7, 7, 7]
ex_string = "hello there this is a test"
for mychar in ex_string:
    if mychar not in mydict:
        mydict[mychar] = 1
    else:
        mydict[mychar] += 1

# for num in numlist:
#     if num not in mydict:
#         mydict[num] = 1
#     else:
#         mydict[num] += 1

# print(mydict[" "])

for cur_char, char_count in mydict.items():
    if cur_char == " ":
        print(char_count)
    # print(cur_char, char_count)


# {'h': 3, 'e': 4, 'l': 2, 'o': 1, ' ': 5, 't': 4, 'r': 1, 'i': 2, 's': 3, 'a': 1}

# mylist.append('dvfgsdg')