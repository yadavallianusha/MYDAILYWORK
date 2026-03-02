num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice (1/2/3/4): ")

if choice == "1":
    print("Result:", num1 + num2) # add the num
elif choice == "2":
    print("Result:", num1 - num2) # Subtract two numbers
elif choice == "3":
    print("Result:", num1 * num2)# Multiply two numbers

elif choice == "4":
    if num2 != 0:
        print("Result:", num1 / num2)  # Divide two numbers
    else:
        print("Error: Division by zero is not allowed")
else:
    print("Invalid choice")
