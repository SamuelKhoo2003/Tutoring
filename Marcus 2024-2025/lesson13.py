# Objective:
# Create a Passport class in Python that models the attributes and functionalities of a passport. Your class should include:

# An initializer (__init__ method) to set up a passport’s attributes.
# Methods to update passport details and check validity.
# A method to display passport information.
# Tasks:
# 1. Define the Passport Class
# Create a class named Passport with the following attributes:

# passport_number (str) → A unique passport number (e.g., "A12345678")
# name (str) → Full name of the passport holder
# country (str) → The country of citizenship
# date_of_birth (str) → Date of birth in format "YYYY-MM-DD"
# date_of_issue (str) → Date when the passport was issued
# date_of_expiry (str) → Expiry date of the passport
# visa_entries (list, default = []) → A list to store visa stamps

# 2. Implement the Following Methods:
# renew_passport(new_expiry_date) → Updates the passport expiry date.
# add_visa_entry(country, date) → Adds a visa entry (as a tuple) to the visa list.
# get_passport_info() → Returns a formatted string with passport details.

class Passport:
    def __init__(self, passport_number, name, country, date_of_birth, date_of_issue, date_of_expiry, visa_entries=[]):
        self.passport_number = passport_number
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth
        self.date_of_issue = date_of_issue
        self.date_of_expiry = date_of_expiry
        self.visa_entries = visa_entries

    # def get_name(self):
    #     return f"The owner of this passport is {self.name}"

    # def get_country(self):
    #     return f"The passport owner is born in {self.country}" 

    def get_passport_info(self):
        visa_info = "\n".join(f"{country} - {date}" for country, date in self.visa_entries) or "No visa entries"
        return (f"Passport Number: {self.passport_number}\n"
            f"Name: {self.name}\n"
            f"Nationality: {self.country}\n"
            f"Date of Birth: {self.date_of_birth}\n"
            f"Date of Issue: {self.date_of_issue}\n"
            f"Date of Expiry: {self.date_of_expiry}\n"
            f"Visa Entries:\n{visa_info}")

    def get_passport_date(self):
        return f"The passport was issued on {self.date_of_issue} and expires on {self.date_of_expiry}."

    def renew_passport(self, new_issue, new_expiry):
        self.date_of_issue = new_issue
        self.date_of_expiry = new_expiry
        print(f"Passport renewed, new issue date is {self.date_of_issue} and new expiry date is {self.date_of_expiry}.")

    def add_visa_entry(self, country, date):
        self.visa_entries.append((country, date))
        print(f"Visa for {country} has been added on {date}")

    def __str__(self):
        return self.get_passport_info()
    

p1 = Passport(123456, "Samuel", "Malaysia", "26-10-2003", "07-01-2024", "07-01-2029")
p2 = Passport(242456, "Marcus", "Hong Konger", "6-7-2011", "09-05-2024", "01-12-2030")
print(p2)
print(p1)