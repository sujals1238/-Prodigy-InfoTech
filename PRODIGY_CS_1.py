def caesar_cipher(text, shift, mode='encrypt'):
    if mode == 'decrypt':
        shift = -shift
    
    shifted_text = ""
    
    for char in text:
        if char.isalpha():
            if char.islower():
                shifted = (ord(char) - ord('a') + shift) % 26 + ord('a')
            elif char.isupper():
                shifted = (ord(char) - ord('A') + shift) % 26 + ord('A')
            shifted_text += chr(shifted)
        else:
            shifted_text += char
    
    return shifted_text

def main():
    while True:
        choice = input("Do you want to encrypt or decrypt? (encrypt/decrypt): ").lower()
        if choice not in ['encrypt', 'decrypt']:
            print("Invalid choice. Please enter 'encrypt' or 'decrypt'.")
            continue
        
        message = input("Enter the message: ")
        shift = int(input("Enter the shift value (a positive integer): "))
        
        if choice == 'encrypt':
            encrypted_message = caesar_cipher(message, shift, 'encrypt')
            print("Encrypted message:", encrypted_message)
        else:
            decrypted_message = caesar_cipher(message, shift, 'decrypt')
            print("Decrypted message:", decrypted_message)
        
        another = input("Do you want to perform another operation? (yes/no): ").lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()