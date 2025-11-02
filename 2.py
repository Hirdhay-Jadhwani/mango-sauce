import string

def generate_key_matrix(key):
    """Generates the 5x5 Playfair key matrix."""
    matrix = []
    key = key.upper().replace(" ", "").replace("J", "I")

    key_chars = []
    for char in key:
        if char not in key_chars:
            key_chars.append(char)

    alphabet = string.ascii_uppercase.replace("J", "")
    for char in alphabet:
        if char not in key_chars:
            key_chars.append(char)

    for i in range(0, 25, 5):
        matrix.append(key_chars[i:i+5])

    return matrix


def find_coords(matrix, char):
    """Finds the (row, col) coordinates of a character in the matrix."""
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == char:
                return r, c
    return -1, -1


def prepare_plaintext(plaintext):
    """Prepares plaintext: uppercase, J->I, split doubles, pad odd length."""
    plaintext = plaintext.upper().replace(" ", "").replace("J", "I")
    prepared = ""
    i = 0

    while i < len(plaintext):
        a = plaintext[i]
        prepared += a

        if i + 1 >= len(plaintext):
            prepared += "X"
            break

        b = plaintext[i+1]

        if a == b:
            prepared += "X"
            i += 1
        else:
            prepared += b
            i += 2

    return prepared


def crypt(text, matrix, mode='encrypt'):
    """Encrypts or decrypts text using the Playfair rules."""
    result = ""
    shift = 1 if mode == 'encrypt' else -1

    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        r1, c1 = find_coords(matrix, a)
        r2, c2 = find_coords(matrix, b)

        if r1 == r2:
            result += matrix[r1][(c1 + shift) % 5]
            result += matrix[r2][(c2 + shift) % 5]
        elif c1 == c2:
            result += matrix[(r1 + shift) % 5][c1]
            result += matrix[(r2 + shift) % 5][c2]
        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]

    return result


# --- MAIN EXECUTION (User Input) ---
print("=== Playfair Cipher ===")

# Take user inputs
key = input("Enter the key: ")
plaintext = input("Enter the plaintext: ")

# Generate matrix
key_matrix = generate_key_matrix(key)
print("\nKey Matrix (5x5):")
for row in key_matrix:
    print(row)

# Prepare plaintext
prepared = prepare_plaintext(plaintext)
print(f"\nPrepared Text (Digraphs): {prepared}")

# Encrypt
ciphertext = crypt(prepared, key_matrix, mode='encrypt')
print(f"\nEncrypted Text: {ciphertext}")

# Decrypt
decrypted_text = crypt(ciphertext, key_matrix, mode='decrypt')
print(f"Decrypted Text: {decrypted_text}")
