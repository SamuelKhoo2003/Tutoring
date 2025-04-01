mylist= [1, 2, 4]
myset = {1, 2, 3, 4}
mydict = {"a": "orange", "b": "apple", "c": "strawberry"}
print(mylist[2])
print(mydict["a"])

set1 = {"a", "b", "c"}
set2 = {1, 2, 3, "c"}
set4 = {"Marcus", "Leanne"}
inputlist = [7, 8, 9]
set3 = set1.union(inputlist)
set3  = set1.union(set2, set4)
set3  = set1 | set2
set1.update(set4)
print(set1)
print(set3)

lista = ['a', 'b', 'c']
llistb = ['c', 'd', 'e']
listc = lista.intersect(listb)
set3 = set1.intersection(set2)
set3 = set1.symmetric_difference(set2)
print(set3)

# we have a set of numberts called set1, another set called set2, we want to create evenset for all the even numbers present in both sets
set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {2, 4, 5, 8, 9, 10, 0}
set3 = set1.intersection(set2)
evenset = set()
for x in set3:
    if x % 2 == 0:
        evenset.add(x)
print(evenset)

word1 = "hello"
word2 = "python"

# crearte a word1set and a word2set using the 2 strings given, then return a set containing the common letters in both strings/sets
word1set = set(word1)
# for char in word1:
#     if char not in word1set:
#         word1set.add(char)
word2set = set(word2)
commonletters_set = word1set.intersection(word2set)
allletters_set = word1set.union(word2set)
# print(word1set)
# print(word2set)
print(commonletters_set)

# key : value structure DOESNT ALLOW DUPLICATES
studentdictionary = {
    "Bob": {
    "age": 16,
    "subjects": ["Math", "English", "Art", "Sport", "Science"],
    "parents": ("Jack", "Molly"),
    "favorite_teacher": "Mr. Tom"
    },
    "Mary": {
    "age": 15,
    "subjects": ["English", "Art", "Sport", "Science", "Music"],
    "parents": ("Jimmy", "May"),
    "favorite_teacher": "Mr. Craig"
    }
}
# # change bobs age to 17
studentdictionary["Bob"]["age"] += 1
# # print("Original age", )
# # add in favourite teacher
# # adding in history as a subject
# studentdictionary["subjects"].append("History")

# Mary decides she wants to student geography
studentdictionary["Mary"]["subjects"].append("Geography")
print(studentdictionary)