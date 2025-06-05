import hashlib
import bcrypt

def hash_md5(passwords):
    hashed_passwords = []
    for password in passwords:
        password_bytes = password.encode('utf-8')
        md5_hash = hashlib.md5()
        md5_hash.update(password_bytes)
        hashed_passwords.append(md5_hash.hexdigest())
    return hashed_passwords

def hash_sha1(passwords):
    hashed_passwords = []
    for password in passwords:
        password_bytes = password.encode('utf-8')
        sha1_hash = hashlib.sha1()
        sha1_hash.update(password_bytes)
        hashed_passwords.append(sha1_hash.hexdigest())
    return hashed_passwords

def hash_sha256(passwords):
    hashed_passwords = []
    for password in passwords:
        password_bytes = password.encode('utf-8')
        sha256_hash = hashlib.sha256()
        sha256_hash.update(password_bytes)
        hashed_passwords.append(sha256_hash.hexdigest())
    return hashed_passwords

def hash_bcrypt(passwords):
    hashed_passwords = []
    for password in passwords:
        password_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password_bytes, salt)
        hashed_passwords.append(hashed.decode('utf-8'))
    return hashed_passwords