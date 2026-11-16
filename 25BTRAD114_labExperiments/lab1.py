print("exp2")

print("Hello, World!") 
print("Welcome to Python Programming.")

print("exp3")
name = input("Enter your name: ") 
age = int(input("Enter your age: ")) 
 
next_year_age = age + 1 
double_age = age * 2 

print(f"\nHello, {name}!") 
print(f"You are currently {age} years old.") 
print(f"Next year, you will be {next_year_age} years old.") 
print(f"Twice your age is {double_age}.")

print("exp4")
print("=== Simple Calculator ===") 
num1 = float(input("Enter first number: ")) 
num2 = float(input("Enter second number: ")) 

addition = num1 + num2 
subtraction = num1 - num2 
multiplication = num1 * num2 
division = num1 / num2 if num2 != 0 else "Cannot divide by zero" 
 
print(f"Addition: {num1} + {num2} = {addition}") 
print(f"Subtraction: {num1} - {num2} = {subtraction}") 
print(f"Multiplication: {num1} * {num2} = {multiplication}") 
print(f"Division: {num1} / {num2} = {division}")
      
