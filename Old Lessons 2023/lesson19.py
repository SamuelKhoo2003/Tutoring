# class Rectangle():
#   def __init__(self, height, width):
#     self.height = height
#     self.width = width

#   def calculate_area(self):
#     return 
  
#   def calculate_perimeter(self):
#     return
  
#   def print_details(self):
#     return

class Rectangle():
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_area(self):
        return (self.height * self.width)

    def calculate_perimeter(self):
        return (self.height + self.width)*2

    def print_details(self):
        print(f"the area of the rectangle is {self.calculate_area()} and the perimeter is {self.calculate_perimeter()}")

    def is_square(self):
        return self.width == self.height
    
    def calculate_diagonal(self):
        return

# Class Rectangle():
#   def __init__ (self, height, width)
#     self.height = height 
#     self.width = width

#   def calculate_area(self):
#     return self.height * self.width

#   def calculate_perimeter(self):
#     return 2 * (self.height + self.width)

#   def print_details(self):
#     print("Rectangle Details:")
#     print("width:", self.width)
#     print("height", self.height )
#     print("area", self.calculate_area())
#     print("perimeter", self.calculate_perimeter())
        
# rectangle1 = Rectangle(5, 8)
# rectangle1.print_details()





class Student():
    def __init__(self,name, age, courses):
        self.name = name
        self.age = age
        self.courses = courses

    def add_course(self, new_course):
        self.courses.append(new_course)

    def remove_course(self, removal_course):
        for course in self.courses:
            if course == removal_course:
                self.courses.remove(removal_course)

    def print_info(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)
        print("Student Courses:", self.courses)


student1 = Student("Alice", 20, ["Math", "History", "English"])
# # student1.print_info()
# student1.add_course("Physics")
# student1.remove_course("History")
# student1.print_info()


# testlist = [1,2,3,4]
# print(testlist)
# testlist.append(7)
# print(testlist)
# testlist.remove(2)
# print(testlist)


class Book:
    def __init__ (self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def print_details(self):
        print("Title:", self.title, "Author:", self.author, "Price:", self.price)

class Bookstore:
    def __init__(self):
        self.books = []

    def add_book(self, new_book):
        self.books.append(new_book)

    def print_all_books(self):
        print("Books in bookstore:")
        for book in self.books:
            book.print_details()

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return False


bookstore = Bookstore()

# bookstore = []

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 15.99)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 12.50)

bookstore.add_book(book1)
# bookstore = [Book("The Great Gatsby", "F. Scott Fitzgerald", 15.99)]

bookstore.add_book(book2)
# bookstore = [Book("The Great Gatsby", "F. Scott Fitzgerald", 15.99), Book("To Kill a Mockingbird", "Harper Lee", 12.50)]
# book1.print_details()
bookstore.print_all_books()

search_result = bookstore.search_book("Samuel's Diary")
if search_result:
    print("Book found:")
    search_result.print_details()
else:
    print("Book not found.")