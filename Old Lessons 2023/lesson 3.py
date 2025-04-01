# i = 0
# j = 0
# while i < 10 and j < 8:
#     print(f"j: {j}")
#     j += 1
#     print(f"i: {i}")
#     i += 1


# num = int(input("Please enter a number:"))
# while num != 10:
#     print(num)
#     num += 2 

# limit
# calculate the sum of consecutive numbers until the limit, starting from 1 as the first num 

limit = int(input("Limit:"))
print(f"The limit of consecutive numbers is: {limit}")

if limit <= 1:
  print("Limit is too low")
  
else:
  current_sum = 0
  current_number = 1
  
  while current_number < limit: 
    current_sum += current_number
    current_number += 1
    print(f"Your current sum is: {current_sum}")
    print(f"The next number being added is: {current_number}")
    
  print(current_sum)