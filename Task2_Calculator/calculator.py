import time
import psutil
import os

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

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
except ValueError:
    print("Invalid input! Enter numbers only.")
    exit()
print("\nChoose operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = input("Enter choice (1/2/3/4): ")
# Measure only the calculation
start_time = time.perf_counter()
result = calculate(num1, num2, choice)
end_time = time.perf_counter()
print("Result:", result)
execution_time = end_time - start_time
process = psutil.Process(os.getpid())
memory_usage = process.memory_info().rss / 1024 / 1024
print("\nPerformance Metrics")
print("Execution Time:", round(execution_time, 8), "seconds")
print("Memory Usage:", round(memory_usage, 2), "MB")
