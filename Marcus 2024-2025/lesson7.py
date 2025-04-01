def task1():
    word = input("Please type in a string: ")
    count = 0
    # "aeiou"
    for character in word:
        if character in "aeiouAEIOU":
            count += 1
    return count

def task2():
    # "" t
    # "t" te
    # "te" tes
    # "tes" test count + 1
    # 'test' tests count + 1

    word = input("Please type in a string: ")
    seen_string = ""
    count = 0
    repeat_characters = []
    for character in word:
        if character in seen_string:
            # print(character)
            repeat_characters.append(character)
            count += 1
        seen_string += character
    return (count, repeat_characters)

def task3():
    # return an array of the first character of every word within the sentence
    # Marcus is cooking fried rice ["M", "i", "c", "f", "r"]
    # test
    # 0123

    # word[0] = t
    # word[1] = e
    # word[2] = s
    # word[3] = t
    sentence = input("Please type in a sentence: ")
    # print(sentence, " BEFORE")
    sentence = sentence.split()
    # print(sentence, " AFTER")
    first_characters = []
    for word in sentence:
        # print(word[0])
        first_characters.append(word[0])
    return first_characters

def task4():
    # return an array of the last character of every word within a sentence
    # Marcus is cooking fried rice ["s", "s", "g", "d", "e"]
    sentence = input("Please type in a sentence: ")
    # print(sentence)
    sentence = sentence.split()
    # print(sentence)
    last_characters = []
    for word in sentence:
        # print(word[-1])
        last_characters.append(word[-1])
    return last_characters

if __name__ == "__main__":
    # print(task1())
    # print(task2())
    # print(task3())
    print(task4())


