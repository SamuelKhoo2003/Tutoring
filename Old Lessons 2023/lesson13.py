def reverse_list1(my_list):
    result_list= []
    for i in range(len(my_list)-1, -1, -1):
        result_list.append(my_list[i])
    return result_list

def reverse_list2(my_list):
    return my_list[::-1]

#           0, 1, 2, 3, 4
testlist = [1, 2, 3, 4, 5]
# print(testlist[2])
# reverse_list1(testlist)
# print(testlist)
# print(testlist[::-1]) # this is reversing the list

# for a range(starting index, ending index, gap)
#          0,  1,   2,  3
example = [89, 100, 76, 45]
# print(example[1])

res = reverse_list1(example)
print(res)

[]
[45]
[45, 76]
[45, 76, 100]
[45, 76, 100, 89]