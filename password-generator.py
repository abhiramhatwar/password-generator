import random
import string

def generate_password(length=12, use_special_chars=True, avoid_ambiguous=True):
    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")
    
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    ambiguous_chars = 'l1I|o0O'

    if avoid_ambiguous:
        letters = ''.join(c for c in letters if c not in ambiguous_chars)
        digits = ''.join(c for c in digits if c not in ambiguous_chars)
        special_chars = ''.join(c for c in special_chars if c not in ambiguous_chars)

    characters = letters + digits
    if use_special_chars:
        characters += special_chars

    if length < 3:
        raise ValueError("Password length should be at least 3 characters to include all character sets.")
    
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(special_chars) if use_special_chars else random.choice(digits)
    ]
    
    password += [random.choice(characters) for _ in range(length - len(password))]

    random.shuffle(password)
    
    return ''.join(password)

if __name__ == "__main__":
    length = int(input("Enter the desired length of the password: "))
    use_special_chars = input("Include special characters? (yes/no): ").strip().lower() == 'yes'
    avoid_ambiguous = input("Avoid ambiguous characters? (yes/no): ").strip().lower() == 'yes'
    password = generate_password(length, use_special_chars, avoid_ambiguous)
    print(f"Generated password: {password}")
