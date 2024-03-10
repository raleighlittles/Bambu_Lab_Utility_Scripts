#!/usr/bin/env python3

# This requires Python3.9 and pycryptodome
# Usage: python3 bambu_decrypt.py <file>

from Cryptodome.Cipher import AES
from hashlib import sha256
from sys import argv
from os.path import basename, splitext

KEY_MATERIAL = bytes.fromhex("fb a3 59 36 de f0 cd 5d 09 8e ed c0 d0 08 68 f4 3a c0 3c 77 a5 d3 7c 82 1b fc 89 27 8f 48 dd db f1 01 c0 7b 36 bf 77 a3 4c 80 7e 25 43 c6 8d 82 56 fe 32 48 0b 1c 63 06 dc c2 38 6f 88 60 41 83 fb a3 59 36 de f0 cd 5d 09 8e ed c0 d0 08 68 35 42 1a f9 5a d5 ba 10 f3 c8 33 3f 2f 2b 50 e2 43 8a 4e 25 f0 42 43 bd 98 a7 c1 5c ae f9 a3 40")
KEY_LEN = 16
#NONCE = bytes.fromhex("30 31 32 33 34 35 36 37 38 39 30 31 32 33 34 35") # Currently unused, but may be used in the future
NONCE_ZERO = bytes.fromhex("00 00 00 00 00 00 00 00")
INNER_HEADER_LEN = 0x70
SHA256_LEN = 0x20
INNER_HEADER_SHA256_OFFSET = INNER_HEADER_LEN - SHA256_LEN
OUTER_HEADER_LEN = 0x1a0

def decrypt_data(key_idx, in_data):
    key_start = key_idx*KEY_LEN
    cipher = AES.new(KEY_MATERIAL[key_start:key_start+KEY_LEN], AES.MODE_CTR, nonce=NONCE_ZERO)
    return cipher.decrypt(in_data)

def is_correct_decrypt(out_data):
    sha256_correct = out_data[INNER_HEADER_SHA256_OFFSET:INNER_HEADER_SHA256_OFFSET+SHA256_LEN]
    sha256_actual = sha256(out_data[INNER_HEADER_LEN:]).digest()
    return sha256_correct == sha256_actual

def main(in_file):
    if not in_file.endswith(".sig"):
        print("Input file must end with .sig")
        return
    
    in_file_name = basename(in_file)

    out_file = splitext(in_file)[0]

    in_data = None
    with open(in_file, "rb") as f:
        in_data = f.read()
    
    in_data = in_data[OUTER_HEADER_LEN:]

    key_idx = None
    if in_file_name[:7] == "update-":
        key_idx = 0
    elif in_file_name[:3] == "mc_":
        key_idx = 1
    elif in_file_name[:3] == "th_":
        key_idx = 2
    elif in_file_name[:4] == "ams_":
        key_idx = 3

    out_data = None
    if key_idx is not None:
        out_data = decrypt_data(key_idx, in_data)
        if not is_correct_decrypt(out_data):
            print(f"Thought key {key_idx} would apply, but key is wrong for file {in_file_name}! Report this to @Doridian!")
            key_idx = None

    if key_idx is None:
        print(f"Unknown key index for file {in_file_name}, testing all available keys...")
        for i in range(0, len(KEY_MATERIAL) // KEY_LEN):
            out_data = decrypt_data(i, in_data)
            if is_correct_decrypt(out_data):
                key_idx = i
                break
            
        if key_idx is None:
            print("No key found :(")
            return
        else:
            print(f"Found key index {key_idx} for file {in_file_name}. Report this to @Doridian!")

    with open(out_file, "wb") as f:
        f.write(out_data[INNER_HEADER_LEN:])

    print(f"Decrypted data written to {out_file}")

if __name__ == "__main__":
    main(argv[1])
