def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    while True:
        print("\n1. Encrypt\n2. Decrypt\n3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            message = input("Enter message to encrypt: ")
            shift = int(input("Enter shift value: "))
            print("Encrypted message:", encrypt(message, shift))
        elif choice == '2':
            message = input("Enter message to decrypt: ")
            shift = int(input("Enter shift value: "))
            print("Decrypted message:", decrypt(message, shift))
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
0
