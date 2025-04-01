def is_prime(myint):
    if (myint < 2):
        return False
    for curnum in range (2, int(myint**0.5)+1):
        if (myint % curnum == 0):
            return False
    return True

def fahrenheit_to_celsius(tmpf):
    return (tmpf - 32) *5/9

# temperature_fahrenheit = 75 
# temperature_celsius = fahrenheit_to_celsius(temperature_fahrenheit)
# print(temperature_fahrenheit, "degrees fahrenheit is equal to", temperature_celsius, "degrees celsius")

def celsius_to_fahrenheit(tmpc):
    return (tmpc * 9/5) + 32.
# print(f{tmpf} "in celcius is" {tmpc})

# print("Temperature Converter")
# print("1. Celsius to Fahrenheit")
# print("2. Fahrenheit to Celsius")

# choice = int(input("Enter your choice (1 or 2):"))

# if choice == 1:
#     temperature_celsius = float(input("Enter temperature in Celsius:"))
#     temperature_fahrenheit = celsius_to_fahrenheit(temperature_celsius)
#     print(f"{temperature_celsius} degrees Celsius is equal to {temperature_fahrenheit} degrees Fahrenheit")
# elif choice == 2:
#     temperature_fahrenheit = float(input("Enter temperature in Fahrenheit:"))
#     temperature_celsius = fahrenheit_to_celsius(temperature_fahrenheit)
#     print(f"{temperature_fahrenheit} degrees Fahrenheit is equal to {temperature_celsius} degrees Celsius")
# else:
#     print("Invalid choice, please enter either 1 or 2")

# list1 = [2, 2, 3, 4, 6, 7, 9, 4, 10, 0]
# mydict = {}
# for num in list1:
#     if num in mydict:
#         mydict[num] += 1
#     else:
#         mydict[num] = 1
# print(mydict)

# NOTE, for dictionary [num] looks for the value num in the dictionary and returns corresponding value, while list[num] returns value at position index num. 
# the 2 are not the same

def word_frequency(mystring):
    worddict = {}
    words = mystring.lower().split()
    for word in words:
        word = word.strip(".")
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1
    return worddict

sentence = "This is a sample test sentence. This sentence is a test."
# print(sentence.lower().split())
# word_frequency_dict = word_frequency(sentence)
print(word_frequency(sentence))
