import hashlib

# we can know the length of hash string by divide the algorithm bytes num by 4... EX: sha256 -> 256/4 = 64 character
# because every character takes 4 bytes

name = hashlib.sha256("mohamed".encode())
print(name.hexdigest())
print(len(name.hexdigest()), "character", len(name.hexdigest())*4, " bytes")
print(name.name)
print(name.update(" ali".encode()))  # change the string which used in hash -> from mohamed to mohamed ali
print(hashlib.sha256("mohamed ali".encode()).hexdigest())
print(name.hexdigest())

users_dict = {
    "mohamed_ali": "129d9c4ed9e9247c3001cffee918b6b153c04fa9711f70877c59d5c88c0e9817"
}

# while True:
#     name = input("Username: ")
#     if name in users_dict:
#         password = input("Password: ")
#         if users_dict[name] == hashlib.sha256(password.encode()).hexdigest():
#             print(f"welcome {name}")
#         else:
#             print("Incorrect password")
#     else:
#         print("user not found")
