# Simple Calculator Program
# Function to perform calculation
def calculate(num1, num2, choice):
    if choice == "1":
        return num1 + num2
    elif choice == "2":
        return num1 - num2
    elif choice == "3":
        return num1 * num2
    elif choice == "4":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed"
    else:
        return "Invalid choice"
# Take input numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
# Show menu
print("\nChoose operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = input("Enter choice (1/2/3/4): ")
# Call function
result = calculate(num1, num2, choice)
print("Result:", result)
