def word_countdown():
  word = input("Please type a string: ")
  i = len(word) - 1
  while i >= 0:
    print(word[i])
    i -= 1

  pass

def task2():
    width = int(input("Please enter the width of the rectangle: "))
    length = int(input("Please enter the length of the rectangle: "))
    row = '#' * length
    for _ in range(width):
      print(row)
    #####
    #####
    #####
    pass

def task3():
    word = input("Please type in a word: ")
    underline = '-' * len(word)
    print(word)
    print(underline)
#   please type in a word: Marcus
#   Marcus
#   ------
#   pass

def task4():
   word = input("Please type in a word: ")
   center = "# " + word + " #"
   frame_edge = '#' * len(center)
   spacing = "#" + " " * (len(word) + 2) + "#"
   print(frame_edge)
   print(spacing)
   print(center)
   print(spacing)
   print(frame_edge)
#    Marcus
   ##########
   #        #
   # Marcus #
   #        #
   ##########
if __name__ == "__main__":
#   word_countdown()
#   task2()
#   task3()
  task4()