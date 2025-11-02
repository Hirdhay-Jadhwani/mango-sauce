def display_alphabet_mapping():
    print("Alphabet and Numerical Mapping:")
    print("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z")
    print("0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25")

def preprocess_text(text):
    return ''.join(char.upper() for char in text if char.isalpha())

def generate_key(plaintext, key):
    key = key.upper()
    key_length = len(key)
    return (key * (len(plaintext) // key_length) + key[:len(plaintext) % key_length])

def vigenere_encrypt(plaintext, key):
    plaintext = preprocess_text(plaintext)
    key = generate_key(plaintext, key)
    ciphertext = ""
    for i in range(len(plaintext)):
        p = ord(plaintext[i]) - ord('A')
        k = ord(key[i]) - ord('A')
        c = (p + k) % 26
        ciphertext += chr(c + ord('A'))
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    ciphertext = preprocess_text(ciphertext)
    key = generate_key(ciphertext, key)
    plaintext = ""
    for i in range(len(ciphertext)):
        c = ord(ciphertext[i]) - ord('A')
        k = ord(key[i]) - ord('A')
        p = (c - k) % 26
        plaintext += chr(p + ord('A'))
    return plaintext

def main():
    display_alphabet_mapping()
    plaintext = input("\nEnter plaintext (letters only): ")
    key = input("Enter key (letters only): ")
    ciphertext = vigenere_encrypt(plaintext, key)
    print(f"\nEncrypted Text: {ciphertext}")
    decrypted_text = vigenere_decrypt(ciphertext, key)
    print(f"Decrypted Text: {decrypted_text}")

if __name__ == "__main__":
    main()