import random
import string

def gen_pass(length):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    all_characters = lowercase_letters + uppercase_letters + digits + special_characters
    length = max(length, 8)
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

try:
    password_length = int(input("Enter the desired password length: "))
except ValueError:
    print("Invalid input. Please enter a valid integer for the password length.")
    exit()

generated_password = gen_pass(password_length)
print("Generated Password:", generated_password)
