def caesar_cipher_encrypt(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                encrypted_char = chr(((ord(char) - ord('a') + shift_amount) % 26) + ord('a'))
            else:
                encrypted_char = chr(((ord(char) - ord('A') + shift_amount) % 26) + ord('A'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(ciphertext, shift):
    return caesar_cipher_encrypt(ciphertext, -shift)

def atbash_cipher_encrypt(plaintext):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            if char.islower():
                encrypted_char = chr(ord('a') + 25 - (ord(char) - ord('a')))
            else:
                encrypted_char = chr(ord('A') + 25 - (ord(char) - ord('A')))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

plaintext = "Hello, World!"
caesar_shift = 3

caesar_encrypted = caesar_cipher_encrypt(plaintext, caesar_shift)
caesar_decrypted = caesar_cipher_decrypt(caesar_encrypted, caesar_shift)

atbash_encrypted = atbash_cipher_encrypt(plaintext)

print("Plaintext:", plaintext)
print("Caesar Encrypted:", caesar_encrypted)
print("Caesar Decrypted:", caesar_decrypted)
print("Atbash Encrypted:", atbash_encrypted)
