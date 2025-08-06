from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode

# temporary key --> later on: ECDH
KEY = b'This_is_my_32byte_long_AES_key!!'# ✔️ genau 32 Zeichen
BLOCK_SIZE = 16  # AES block size in bytes

def encrypt(plaintext):
    iv = get_random_bytes(BLOCK_SIZE) # Generate a random IV
    cipher = AES.new(KEY, AES.MODE_CBC, iv) # Create a new AES cipher object
    ciphertext = cipher.encrypt(pad(plaintext, BLOCK_SIZE)) # Encrypt the plaintext
    return b64encode(iv + ciphertext) # base64 wrapper

def decrypt(ciphertext_b64):
    try:
        data = b64decode(ciphertext_b64) # wrapper decode
        iv = data[:BLOCK_SIZE] # Extract the IV from the beginning
        ciphertext = data[BLOCK_SIZE:] # Extract the ciphertext
        cipher = AES.new(KEY, AES.MODE_CBC, iv) # Create a new AES cipher object with the IV
        plaintext = unpad(cipher.decrypt(ciphertext), BLOCK_SIZE) # Decrypt the ciphertext
        return plaintext
    except Exception as e:
        # Later on Logging/Errormsg.
        raise ValueError(f"Decryption failed: {e}")