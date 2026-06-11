def make_password(words, length):
    pwd = "".join(words)

    while len(pwd) < length:
        pwd += str(len(pwd))
    if len(pwd) > length:
        pwd = pwd[:length]

    return pwd

# --- Main Program ---
print("=== Easy Memorable Password Generator ===")
count = int(input("How many words do you want to use?: "))
words = []
for i in range(count):
    w = input(f"Word {i+1}: ")
    words.append(w)

num_chars = int(input("Desired Length: "))
result = make_password(words, num_chars)
print(f"\nYour Password: {result}")
