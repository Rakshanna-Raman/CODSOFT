import random

print("=== Simple Memorable Password Generator ===")

# 1. User Input: Get the base words from the user
w1 = input("Enter Word 1: ").strip().capitalize()
w2 = input("Enter Word 2: ").strip().capitalize()
w3 = input("Enter Word 3: ").strip().capitalize()
combined_words = w1 + w2 + w3

# 2. User Input: Get complexity choices and desired length
use_numbers = input("Add numbers? (yes/no): ").lower() == "yes"
use_symbols = input("Add symbols? (yes/no): ").lower() == "yes"
desired_length = int(input("Total length: "))

# 3. Create the endings if the user wants them
ending = ""
if use_numbers:
    ending += random.choice("0123456789")
if use_symbols:
    ending += random.choice("!@#$%^&*")

# 4. Cut the words to make perfect room for the ending
letters_needed = desired_length - len(ending)
sliced_words = combined_words[:letters_needed]

# 5. Combine them together
final_password = sliced_words + ending

# 6. Warn the user if the combined words were too short to reach the target length
if len(final_password) < desired_length:
    print(
        "\nNote: The words provided were too short to reach the desired length!"
    )

# 7. Print the final result
print("\n-----------------------------")
print("Your Generated Password:", final_password)
print("-----------------------------")