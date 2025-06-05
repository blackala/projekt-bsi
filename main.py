import hashers
from utils import *
import os

def main():
    passwords = read_file('passwords.txt').splitlines()
    output_dir = 'hashed_passwords'
    os.makedirs(output_dir, exist_ok=True)
    make_file(hashers.hash_md5(passwords), os.path.join(output_dir, 'md5_passwords.txt'))
    make_file(hashers.hash_sha1(passwords), os.path.join(output_dir, 'sha1_passwords.txt'))
    make_file(hashers.hash_sha256(passwords), os.path.join(output_dir, 'sha256_passwords.txt'))
    make_file(hashers.hash_bcrypt(passwords), os.path.join(output_dir, 'bcrypt_passwords.txt'))

def make_file(passwords, name):
    output = '\n'.join(passwords)
    write_file(name, output)

main()