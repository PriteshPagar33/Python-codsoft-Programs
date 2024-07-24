import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired length for the password: "))
        if length <= 0:
            print("Please enter a positive number.")
            return
        password = generate_password(length)
        print(f"Generated password: {password}")
        print("Thank you for using Password Generator by Pritesh")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
