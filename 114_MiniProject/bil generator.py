print("----- BILL -----")

name = input("Customer name: ")

items = []
total = 0

while True:
    item = input("Enter item: ")
    qty = int(input("Enter quantity: "))
    price = float(input("Enter price: "))

    amount = qty * price
    total = total + amount

    items.append([item, qty, price, amount])

    choice = input("Add another item? (y/n): ")

    if choice == "n":
        break

print("\n----- BILL -----")
print("Customer:", name)



print("----------------")
print("Total:", total)
print("Thank you!")
