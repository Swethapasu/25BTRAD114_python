students = {}

while True:
    print("\n--- ATTENDANCE TRACKER ---")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. Display Attendance")
    print("4. Calculate Attendance Percentage")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")

        if name not in students:
            students[name] = []
            print("Student added successfully!")
        else:
            print("Student already exists!")

    elif choice == 2:
        name = input("Enter student name: ")

        if name in students:
            status = input("Enter attendance (P/A): ").upper()

            if status == "P" or status == "A":
                students[name].append(status)
                print("Attendance recorded!")
            else:
                print("Enter P for Present or A for Absent.")
        else:
            print("Student not found!")

    elif choice == 3:
        print("\n--- ATTENDANCE DETAILS ---")

        for name, records in students.items():
            print(name, ":", records)

    elif choice == 4:
        print("\n--- ATTENDANCE PERCENTAGE ---")

        for name, records in students.items():
            total = len(records)
            present = records.count("P")

            if total > 0:
                percentage = (present / total) * 100
                print(name, ":", percentage, "%")
            else:
                print(name, ": No attendance records")

    elif choice == 5:
        print("Exiting Attendance Tracker...")
        break

    else:
        print("Invalid choice! Try again.")
