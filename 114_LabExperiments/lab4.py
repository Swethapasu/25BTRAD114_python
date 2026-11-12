print("exp11")
# Create a log file
with open("log.txt", "w") as file:
    file.write("INFO: Program started\n")
    file.write("ERROR: File not found\n")
    file.write("WARNING: Low memory\n")
    file.write("INFO: Program running\n")
    file.write("ERROR: Connection failed\n")

# Initialize counters
error = 0
warning = 0
info = 0

# Read the log file
with open("log.txt", "r") as file:
    for line in file:
        if "ERROR" in line:
            error += 1
        elif "WARNING" in line:
            warning += 1
        elif "INFO" in line:
            info += 1

# Display results
print("ERROR count:", error)
print("WARNING count:", warning)
print("INFO count:", info)

print("exp12")
while True:
    print("\n1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Display Students")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll = input("Enter roll number: ")
        name = input("Enter name: ")
        marks = input("Enter marks: ")

        with open("students.txt", "a") as file:
            file.write(roll + "," + name + "," + marks + "\n")

        print("Student added successfully!")

    elif choice == "2":
        roll = input("Enter roll number to search: ")
        found = False

        with open("students.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")

                if data[0] == roll:
                    print("Name:", data[1])
                    print("Marks:", data[2])
                    found = True

        if not found:
            print("Student not found!")

    elif choice == "3":
        roll = input("Enter roll number to update: ")
        found = False
        records = []

        with open("students.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")

                if data[0] == roll:
                    data[1] = input("Enter new name: ")
                    data[2] = input("Enter new marks: ")
                    found = True

                records.append(",".join(data))

        with open("students.txt", "w") as file:
            for record in records:
                file.write(record + "\n")

        if found:
            print("Student updated successfully!")
        else:
            print("Student not found!")

    elif choice == "4":
        with open("students.txt", "r") as file:
            print("\nStudent Records:")
            print(file.read())

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")


print("exp13")
import csv

# Create CSV file
with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Basic", "Allowance", "Deduction"])

    writer.writerow(["Swetha", 20000, 5000, 2000])
    writer.writerow(["Priya", 25000, 6000, 3000])
    writer.writerow(["Rahul", 30000, 7000, 4000])

# Read CSV file
total_payroll = 0

with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)

    print("\n--- PAYROLL DETAILS ---")

    for row in reader:
        basic = int(row["Basic"])
        allowance = int(row["Allowance"])
        deduction = int(row["Deduction"])

        gross = basic + allowance
        net = gross - deduction

        total_payroll += net

        print("\nEmployee:", row["Name"])
        print("Gross Salary:", gross)
        print("Deduction:", deduction)
        print("Net Salary:", net)

print("\nTotal Payroll:", total_payroll)
