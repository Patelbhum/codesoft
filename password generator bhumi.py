import random
import string

def generate_password(length=8):
    if length < 8:
        print("Warning: It's recommended to use a password of at least 8 characters for security.")
    
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    
    all_characters = lowercase + uppercase + digits + special_chars
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

def main():
    print("Welcome to the Password Generator!")

    
    length = input("Enter the desired password length (default is 12): ").strip()
    
    if not length:
        length = 8
    else:
        try:
            length = int(length)
        except ValueError:
            print("Invalid input! Using default length of 12.")
            length = 8
    password = generate_password(length)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
