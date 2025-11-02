import random

# --- Helper Functions ---

def is_prime(n):
    """Simple check for small prime numbers."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_prime(start=100, end=300):
    """Generate a random prime number in a given range."""
    while True:
        num = random.randint(start, end)
        if is_prime(num):
            return num


def gcd(a, b):
    """Greatest Common Divisor."""
    while b:
        a, b = b, a % b
    return a


def mod_inverse(e, phi):
    """Find modular inverse of e under modulo phi."""
    for d in range(2, phi):
        if (d * e) % phi == 1:
            return d
    return None


# --- RSA Functions ---

def generate_keys():
    print("\n=== RSA Key Generation ===")

    # Step 1: Choose two prime numbers
    p = generate_prime()
    q = generate_prime()
    while q == p:
        q = generate_prime()

    # Step 2: Compute n and φ(n)
    n = p * q
    phi = (p - 1) * (q - 1)

    # Step 3: Choose public exponent e (commonly 3, 17, or 65537)
    e = 3
    while gcd(e, phi) != 1:
        e += 2

    # Step 4: Compute private key d
    d = mod_inverse(e, phi)

    print(f"Prime 1 (p): {p}")
    print(f"Prime 2 (q): {q}")
    print(f"n (p*q): {n}")
    print(f"φ(n): {phi}")
    print(f"Public key (e, n): ({e}, {n})")
    print(f"Private key (d, n): ({d}, {n})")

    return (e, n), (d, n)


def encrypt(public_key, message):
    e, n = public_key
    print("\nEncrypting message...")
    encrypted = [(ord(char) ** e) % n for char in message]
    return encrypted


def decrypt(private_key, encrypted_msg):
    d, n = private_key
    print("\nDecrypting message...")
    decrypted = ''.join([chr((char ** d) % n) for char in encrypted_msg])
    return decrypted


# --- MAIN PROGRAM ---
def main():
    print("=== RSA Encryption & Decryption ===")

    # User input
    message = input("Enter the message to encrypt: ")

    # Generate keys
    public_key, private_key = generate_keys()

    # Encryption
    encrypted_msg = encrypt(public_key, message)
    print(f"\nEncrypted Message: {encrypted_msg}")

    # Decryption
    decrypted_msg = decrypt(private_key, encrypted_msg)
    print(f"\nDecrypted Message: {decrypted_msg}")


if __name__ == "__main__":
    main()
