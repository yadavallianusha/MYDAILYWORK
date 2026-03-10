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
length = int(input("Enter password length: "))
# Generate password
result = generate_password(length)
print("Generated Password:", result)
