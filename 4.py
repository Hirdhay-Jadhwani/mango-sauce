import math

# --- Caesar Cipher (Substitution) ---
def caesar_encrypt(text, shift):
    """Encrypts text using Caesar cipher."""
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


def caesar_decrypt(text, shift):
    """Decrypts text encrypted with Caesar cipher."""
    return caesar_encrypt(text, 26 - shift)


# --- Columnar Transposition Cipher ---
def columnar_encrypt(text, key_width):
    """Encrypts text using columnar transposition."""
    text = text.replace(" ", "").upper()  # Clean text
    num_rows = math.ceil(len(text) / key_width)

    # Fill matrix row-wise
    matrix = []
    index = 0
    for _ in range(num_rows):
        row = []
        for _ in range(key_width):
            if index < len(text):
                row.append(text[index])
                index += 1
            else:
                row.append('X')  # Padding
        matrix.append(row)

    print("\nEncryption Matrix (Row-wise):")
    for row in matrix:
        print(" ".join(row))

    # Read column-wise
    cipher = ""
    for c in range(key_width):
        for r in range(num_rows):
            cipher += matrix[r][c]
    return cipher


def columnar_decrypt(cipher, key_width):
    """Decrypts text using columnar transposition."""
    num_rows = math.ceil(len(cipher) / key_width)

    # Create empty matrix
    matrix = [['' for _ in range(key_width)] for _ in range(num_rows)]

    # Fill matrix column-wise
    index = 0
    for c in range(key_width):
        for r in range(num_rows):
            matrix[r][c] = cipher[index]
            index += 1

    print("\nDecryption Matrix (Column-wise):")
    for row in matrix:
        print(" ".join(row))

    # Read row-wise
    plain = ""
    for r in range(num_rows):
        for c in range(key_width):
            plain += matrix[r][c]
    return plain


# --- Main Program ---
def main():
    print("=== Product Cipher (Caesar + Columnar Transposition) ===")
    
    # User inputs
    plaintext = input("Enter the plaintext: ")
    shift = int(input("Enter Caesar cipher shift value (e.g., 3): "))
    key_width = int(input("Enter number of columns for transposition: "))

    # Step 1: Caesar Encryption
    caesar_text = caesar_encrypt(plaintext, shift)
    print(f"\nAfter Caesar Encryption: {caesar_text}")

    # Step 2: Columnar Encryption
    final_cipher = columnar_encrypt(caesar_text, key_width)
    print(f"\nFinal Encrypted Text (Product Cipher): {final_cipher}")

    # --- Decryption ---
    print("\n--- Decryption Process ---")

    # Step 1: Reverse Columnar
    rev_trans_text = columnar_decrypt(final_cipher, key_width)
    print(f"\nAfter Reverse Columnar: {rev_trans_text}")

    # Step 2: Reverse Caesar
    original_text = caesar_decrypt(rev_trans_text, shift)
    print(f"After Reverse Caesar (Decrypted Plaintext): {original_text}")


if __name__ == "__main__":
    main()