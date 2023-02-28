import random
import string

# Function to generate a random password
def generate_password(words):
    password = ''
    for i in range(3):
        password += random.choice(words).title()
    password += ''.join(random.choices(string.punctuation + string.digits, k=3))
    password += random.choice(words).title()
    return password

# Function to check the password strength
def check_password_strength(password):
    # A strong password contains at least one uppercase letter, one lowercase letter, one digit and one symbol and is at least 8 characters long
    if len(password) < 8:
        return 'weak'
    if not any(char.islower() for char in password):
        return 'weak'
    if not any(char.isupper() for char in password):
        return 'weak'
    if not any(char.isdigit() for char in password):
        return 'weak'
    if not any(char in string.punctuation for char in password):
        return 'weak'
    return 'strong'

# Get the user input
words = input('Enter the words for the password (separated by commas): ').split(',')

# Generate a random password
password = generate_password(words)

# Check the password strength
strength = check_password_strength(password)

# Print the password and its strength
print('Your password is:', password)
print('The password strength is:', strength)

# Save the password to a text file
with open('passwords.txt', 'a') as f:
    f.write(password + '\n')
