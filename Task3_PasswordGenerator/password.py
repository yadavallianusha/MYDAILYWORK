# Password Generator Program
import random
import string
# Function to generate password
def generate_password(length):
    # All possible characters
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    # Loop to create password
    for i in range(length):
        password += random.choice(characters)
    return password
# Ask user for password length
try:
    length = int(input("Enter password length: "))
except ValueError:
    print("Enter a valid number!")
    exit()
# Generate password
result = generate_password(length)
print("Generated Password:", result)
