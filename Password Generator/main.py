import random

print("=== Smart Memorable Password Generator ===")

w1 = input("Enter Word 1: ").strip().capitalize()
w2 = input("Enter Word 2: ").strip().capitalize()
w3 = input("Enter Word 3: ").strip().capitalize()

# Complexity
use_numbers = input("Add numbers? (yes/no): ").lower() == "yes"
use_symbols = input("Add symbols? (yes/no): ").lower() == "yes"

# Desired length
length = int(input("Desired Password Length: "))

# Combine words
password = w1 + w2 + w3
extra_chars = ""

if use_numbers:
    extra_chars += "0123456789"

if use_symbols:
    extra_chars += "!@#$%^&*"
    
while len(password) < length:
    if extra_chars:
        password += random.choice(extra_chars)
    else:
        password += random.choice("0123456789")
# Trim if too long
password = password[:length]

print("\nGenerated Password:", password)
