import hashlib

def xor_bytes(a, b):
    """XOR two byte strings together."""
    return bytes(x ^ y for x, y in zip(a, b))

def decrypt(ciphertext, key):
    """
    Decrypt the ciphertext using the provided key.
    
    Args:
        ciphertext: The encrypted data as bytes
        key: The encryption key as bytes
    
    Returns:
        Decrypted plaintext as string
    """
    key_hash = hashlib.sha256(key).digest()
    block_size = 16
    plaintext = b''
    
    # Decrypt each block
    for i in range(0, len(ciphertext), block_size):
        cipher_block = ciphertext[i:i + block_size]
        plain_block = xor_bytes(cipher_block, key_hash)
        plaintext += plain_block
    
    # Remove padding
    padding_length = plaintext[-1]
    plaintext = plaintext[:-padding_length]
    
    return plaintext.decode('utf-8')

def extract_token(decrypted_text, blockchain_length):
    """
    Extract the embedded token from the decrypted blockchain string.
    
    The token was inserted in the middle of the blockchain string.
    We need to figure out where the original blockchain ends and the token begins.
    
    Args:
        decrypted_text: The decrypted blockchain string with embedded token
        blockchain_length: Expected length of blockchain string (number of hashes * 64 + separators)
    
    Returns:
        tuple: (blockchain_string, embedded_token)
    """
    # The blockchain format is: hash1-hash2-hash3-hash4-hash5
    # Each SHA256 hash is 64 characters, with 4 dashes (for 5 blocks)
    # Total expected length: 5 * 64 + 4 = 324 characters
    
    midpoint = blockchain_length // 2
    
    # Extract the parts
    first_part = decrypted_text[:midpoint]
    # The rest contains: token + second_part
    remaining = decrypted_text[midpoint:]
    second_part = remaining[-(blockchain_length - midpoint):]
    token = remaining[:-(blockchain_length - midpoint)]
    
    blockchain_string = first_part + second_part
    
    return blockchain_string, token

def main():
    # The key from your output
    key = b'\xb1\xcd\xf2\xaekk\x1e\x1fT\x86a*?\xb7\x84p\x97\x89\xdbg.\x92\x87\xa5\xd4\xe3\xba\xc0\xc4\xeb\xd9)'
    
    # The encrypted blockchain from your output
    ciphertext = b'\xe5\xe6\xebY+W\xb9\xca\xfd\xb6\x06\x81\x8d8\xf0C\xe3\xb1\xbdZ\x7f\x04\xba\x98\xfe\xe6\x00\x82\x8d;\xf1D\xb2\xb4\xeaX,^\xbd\x98\xf8\xe7\x00\xd6\x80<\xf1\x17\xe3\xb5\xe8\x0b%Q\xec\x98\xfa\xe7\t\x84\x8d9\xfa\x1e\xfb\xe7\xebYxU\xee\x9f\xae\xe5\x03\xd3\x89h\xfbD\xb4\xb2\xeaX/_\xba\x98\xfa\xe2P\xd3\x88h\xacD\xb4\xe1\xeeX(Q\xe5\xcd\xff\xe2\x06\x80\x8f=\xff\x16\xb4\xb5\xbfV-R\xea\xce\xa9\xb3T\xd6\xdai\xfe\x10\xe6\xfa\xeb_/\x06\xee\xc9\xad\xe1U\x81\x8d5\xfbE\xef\xef\xb8\\*V\xe4\xc3\xf9\xb6\x08\x81\xddh\xfaD\xe7\xb2\xab\x06~\x08\x9f\xaf\xda\xaeS\xdb\xd7o\xa3y\xe5\x84\x89\x07K\x0e\x8e\x99\xc8\xe4@\xd4\xe0S\x90s\xbc\x9a\xeb\x1d)^\xbf\xb3\xc3\xa4r\xcd\xd5F\x92\\\x94\x9c\x84\x0cxV\xe9\x9d\xaa\xe7\x05\xca\x81:\xaaC\xe1\xe2\xe2\n/P\xed\x9f\xff\xb1\x07\xd6\x8bi\xfa\x10\xe1\xb5\xef\r$^\xe5\xc2\xf8\xb4\x00\x81\x95<\xf8\x17\xb7\xe4\xecV-T\xb8\xc3\xae\xe1T\x86\xdcn\xfb\x16\xb7\xe5\xb8\x0b\x7f^\xba\xce\xac\xb1T\x85\xdcn\xf0\x1f\xb3\xb3\xbaV.W\xbd\xcb\xaa\xecP\x86\x81;\xfb\x14\xef\xb6\xea\x0e/R\xeb\xcd\xab\xec\x03\xd6\x8c!\xf8\x16\xe2\xb2\xe2_\x7fW\xb8\x9d\xf9\xb1\x02\xd6\x8cn\xa9B\xb5\xee\xeb_|V\xbf\xcc\xf8\xec\x03\x87\x815\xaa\x1f\xb2\xb6\xed^)\x02\xed\xc3\xf8\xe7T\x86\x8fm\xf9\x13\xe5\xb2\xef_|R\xe9\xc3\xf8\xe4\x06\x82\xdc4\xca$'
    
    print("=" * 60)
    print("BLOCKCHAIN DECRYPTION TOOL")
    print("=" * 60)
    
    # Decrypt the ciphertext
    print("\n[1] Decrypting ciphertext...")
    decrypted_text = decrypt(ciphertext, key)
    print(f"Decrypted text length: {len(decrypted_text)} characters")
    print(f"Decrypted text:\n{decrypted_text}\n")
    
    # Extract the blockchain and token
    # 5 blocks = 5 hashes (64 chars each) + 4 separators = 324 characters
    blockchain_length = 5 * 64 + 4
    
    print("[2] Extracting embedded token...")
    blockchain_string, token = extract_token(decrypted_text, blockchain_length)
    
    print("\n" + "=" * 60)
    print("RESULTS")
    print("=" * 60)
    print(f"\nBlockchain string:\n{blockchain_string}\n")
    print(f"Embedded token:\n{token}\n")
    
    # Parse individual block hashes
    print("[3] Individual block hashes:")
    hashes = blockchain_string.split('-')
    for i, block_hash in enumerate(hashes):
        print(f"Block {i}: {block_hash}")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
