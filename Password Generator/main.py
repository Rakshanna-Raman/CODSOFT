import secrets

def make_password(w1, w2, w3, length):
    # Standardize inputs: strip spaces and capitalize
    word1 = w1.strip().capitalize()
    word2 = w2.strip().capitalize()
    word3 = w3.strip().capitalize()
    
    pwd = f"{word1}_{word2}_{word3}"
    if len(pwd) < length:
        while len(pwd) < length:
            pwd += str(secrets.randbelow(10))
            
    elif len(pwd) > length:
        pwd = pwd[:length]
        
    if pwd.endswith('_'):
        if len(pwd) == len(word1) + 1:
            pwd = pwd[:-1] + word2[0]
        else:
            pwd = pwd[:-1] + word3[0]
        
    return pwd

# --- Main Program ---
print("=== Smart Memorable Password Generator ===")
w1 = input("Word 1: ")
w2 = input("Word 2: ")
w3 = input("Word 3: ")
num_chars = int(input("Desired Length: "))

result = make_password(w1, w2, w3, num_chars)
print(f"\nYour Password: {result}")
