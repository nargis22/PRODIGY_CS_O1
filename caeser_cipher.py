# task-1 caeser cipher (encrypt and decryprt text/message)

def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha(): # Check if the character is a letter
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            result += chr(shifted)
        else:
            result += char
    return result

# usage:
text = input("enter your text")
shift =3
encrypted_text = caesar_cipher(text, shift)
print("Encrypted text:", encrypted_text)

decrypted_text = caesar_cipher(encrypted_text, -shift)
print("Decrypted text:", decrypted_text)