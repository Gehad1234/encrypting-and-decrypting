def encrypt(message, key):
    ciphertext = ""
    for char in message:
        if char.isalpha():
            # Convert character to its corresponding position in the alphabet
            if char.isupper():
                char_position = ord(char) - ord('A')
            else:
                char_position = ord(char) - ord('a')

            # Apply encryption function f(p) = (p + k) mod 26
            encrypted_position = (char_position + key) % 26

            # Convert back to character
            if char.isupper():
                encrypted_char = chr(encrypted_position + ord('A'))
            else:
                encrypted_char = chr(encrypted_position + ord('a'))

            ciphertext += encrypted_char
        else:
            ciphertext += char  # Preserve non-alphabetic characters
    return ciphertext


def decrypt(ciphertext, key):
    decrypted_message = ""
    for char in ciphertext:
        if char.isalpha():
            # Convert character to its corresponding position in the alphabet
            if char.isupper():
                char_position = ord(char) - ord('A')
            else:
                char_position = ord(char) - ord('a')

            # Apply decryption function f_inv(p) = (p - k) mod 26
            decrypted_position = (char_position - key) % 26

            # Convert back to character
            if char.isupper():
                decrypted_char = chr(decrypted_position + ord('A'))
            else:
                decrypted_char = chr(decrypted_position + ord('a'))

            decrypted_message += decrypted_char
        else:
            decrypted_message += char  # Preserve non-alphabetic characters
    return decrypted_message


# Display options to the user
print("Choose an option: (1 for encryption) or (2 for decryption)")

# Take option and key from the user
option = input("Enter your choice (1 or 2): ")
key = int(input("Enter the k value (key): "))

if option == '1':
    message = input("Enter the message: ")
    encrypted_message = encrypt(message, key)
    print("The Encrypted message:", encrypted_message)
elif option == '2':
    message = input("Enter the message: ")
    decrypted_message = decrypt(message, key)
    print("The Decrypted message:", decrypted_message)
else:
    print("Invalid option. Please choose 1 for encryption or 2 for decryption.")
