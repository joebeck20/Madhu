# AES 256 encryption/decryption using pycryptodome library

from base64 import b64encode, b64decode
import hashlib
from Cryptodome.Cipher import AES
import os
from Cryptodome.Random import get_random_bytes
import json


def encrypt(plain_text, password):
    # generate a random salt
    salt = get_random_bytes(AES.block_size)

    # use the Scrypt KDF to get a private key from the password
    private_key = hashlib.scrypt(
        password.encode(), salt=salt, n=2 ** 14, r=8, p=1, dklen=32)

    # create cipher config
    cipher_config = AES.new(private_key, AES.MODE_GCM)

    # return a dictionary with the encrypted text
    cipher_text, tag = cipher_config.encrypt_and_digest(bytes(plain_text, 'utf-8'))
    return {
        'cipher_text': b64encode(cipher_text).decode('utf-8'),
        'salt': b64encode(salt).decode('utf-8'),
        'nonce': b64encode(cipher_config.nonce).decode('utf-8'),
        'tag': b64encode(tag).decode('utf-8')
    }

def main():

    f=open("file_a","w+")
    data='assignment'
    f.write(data)
    f.close()

    #known to both client and server
    password = 'madhu20'

    #opening file to read and encrypt
    f = open('file_a', 'r')
    data=f.read()
    f.close()

    # encrypting file1
    encrypted = encrypt(data, password)

    #converting dict to str
    encrypted=json.dumps(encrypted)


    f=open('file_b','w+')
    f.write(encrypted)
    f.close()

main()