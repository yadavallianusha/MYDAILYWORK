import random      # Import random module to select random characters
import string      # Import string module to get letters, digits, and symbols
# Ask the user to enter the password length
length = int(input("Enter password length: "))
# Combine all possible characters: uppercase, lowercase, digits, and punctuation
characters = string.ascii_letters + string.digits + string.punctuation
# Create an empty string to store the generated password
password = ""
# Loop for the given password length
for i in range(length):
    # Randomly choose one character from the characters string
    password += random.choice(characters)
# Print the final generated password
print("Generated Password:", password)
