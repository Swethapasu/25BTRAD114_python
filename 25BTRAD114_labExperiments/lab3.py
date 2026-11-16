print("Exp8")
contacts = []

while True:
    print("\n--- CONTACT BOOK ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")

        contact = {"name": name, "phone": phone}
        contacts.append(contact)
        print("Contact added successfully!")

    elif choice == "2":
        name = input("Enter name to search: ")
        found = False

        for contact in contacts:
            if contact["name"] == name:
                print("Phone:", contact["phone"])
                found = True

        if not found:
            print("Contact not found!")

    elif choice == "3":
        name = input("Enter name to update: ")
        found = False

        for contact in contacts:
            if contact["name"] == name:
                contact["phone"] = input("Enter new phone: ")
                print("Contact updated!")
                found = True

        if not found:
            print("Contact not found!")

    elif choice == "4":
        name = input("Enter name to delete: ")
        found = False

        for contact in contacts:
            if contact["name"] == name:
                contacts.remove(contact)
                print("Contact deleted!")
                found = True
                break

        if not found:
            print("Contact not found!")

    elif choice == "5":
        for contact in contacts:
            print(contact["name"], "-", contact["phone"])

        if len(contacts) == 0:
            print("Contact book is empty!")

    elif choice == "6":
        print("Exiting Contact Book...")
        break

    else:
        print("Invalid choice!")

print("exp9")

students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))

    students[name] = marks

print("\n--- STUDENT RESULTS ---")

for name, marks in students.items():

    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 70:
        grade = "C"
    elif marks >= 60:
        grade = "D"
    elif marks >= 50:
        grade = "E"
    else:
        grade = "F"

    print("Name:", name)
    print("Marks:", marks)
    print("Grade:", grade)
    print("----------------")

print("exp10")

sentence = input("Enter a sentence: ")

words = sentence.split()

frequency = {}

for word in words:

    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("\n--- WORD FREQUENCY ---")

for word, count in frequency.items():
    print(word, ":", count)
