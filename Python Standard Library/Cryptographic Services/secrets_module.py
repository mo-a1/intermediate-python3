import secrets
import string

# https://www.youtube.com/watch?v=xzlfXSBzhx8&ab_channel=IndianPythonista

lis = [154, 5, 6, 8, 1, 7, 45, 89, 56, 458, 44, 1, 23, 201, 10, 1, 0, 2, 5, 25, 8]

# choice
print(secrets.choice(lis))

# rand below
print(secrets.randbelow(100))

# rand bits
print(secrets.randbits(10))

# ############# generate random tokens ############ #

print("token_hex-> ", secrets.token_hex(16))

print("token_bytes-> ", secrets.token_bytes(6))

print("token_urlsafe-> ", secrets.token_urlsafe(10))

print(secrets.compare_digest("lsffd4d5d", "lsffd4d5d"))  # safe from time attacks

# ################## Examples ################ #

# generate password without conditions
alphabet = string.digits + string.ascii_letters
password = "".join(secrets.choice(alphabet) for _ in range(8))
print(password)

# generate password with conditions:-  one uppercase character and at least three digits:
while True:
    password = "".join(secrets.choice(alphabet) for _ in range(10))
    if any(ch.isupper() for ch in password) and sum(ch.isdigit() for ch in password) >= 3:
        print(password)
        break

# generate safe url
url = 'https://example.com/reset=' + secrets.token_urlsafe(8)
print(url)
