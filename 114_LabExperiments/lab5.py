print("exp14")

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited successfully!")
        else:
            print("Invalid amount!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount!")
        elif amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal successful!")
        else:
            print("Insufficient balance!")

    def display(self):
        print("Account Holder:", self.name)
        print("Balance:", self.__balance)

account = BankAccount("Swetha", 5000)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Balance Enquiry")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter amount: "))
        account.withdraw(amount)

    elif choice == "3":
        account.display()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")



print("exp15")


class Library:

    def __init__(self):
        self.books = ["Python", "Java", "C Programming"]
        self.issued = []

    def display(self):
        print("\nAvailable Books:")
        for book in self.books:
            if book not in self.issued:
                print(book)

    def issue(self, book):
        if book in self.books and book not in self.issued:
            self.issued.append(book)
            print("Book issued successfully!")
        else:
            print("Book not available!")

    def return_book(self, book):
        if book in self.issued:
            self.issued.remove(book)
            print("Book returned successfully!")
        else:
            print("Invalid return!")

library = Library()

while True:
    print("\n1. Display Books")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.display()

    elif choice == "2":
        book = input("Enter book name: ")
        library.issue(book)

    elif choice == "3":
        book = input("Enter book name: ")
        library.return_book(book)

    elif choice == "4":
        print("Exiting Library System...")
        break

    else:
        print("Invalid choice!")

print("exp16")

import random

n = int(input("Enter number of dice rolls: "))

frequency = [0, 0, 0, 0, 0, 0]

for i in range(n):
    result = random.randint(1, 6)

    print("Roll", i + 1, ":", result)

    frequency[result - 1] += 1

print("\nDice Frequency:")

for i in range(6):
    print(i + 1, ":", frequency[i])
