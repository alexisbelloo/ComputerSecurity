import hashlib
import time


# hashes given
saltedHashes = {"8c47d907a41c1ed2118c7e55eaec35c77f5c7e42f540fac48ffaae759e81d3b4": "o|%Eg", "810225544dab8028701275a3c460d3782b49f1db761d4e5c825926af3ab93e7c": "p}[eD", "34604383be265e3e74132ee54d406364e03cae9181b613683c220c96f4d76868": "j&/|!"}


# method to read RockYou text and match passwords
def findSaltedPasswords():
    # open and read password file
    with open("rockyou.txt", "r", encoding = "ISO-8859-1") as file:
        passwords = file.read().splitlines()
    
    # list for hashses and matching passwords
    matchedPasswords = []

    startTime = time.time()

    # iterate through each password in dataset
    for i in passwords:
        for hashVal, salt in saltedHashes.items():
            saltedPass = i + salt # add salt to password
            hashedPass = hashlib.sha256(saltedPass.encode()).hexdigest()

            # check if matches given hash
            if hashedPass == hashVal:
                matchedPasswords.append((i, salt, hashVal))
    endTime = time.time() # end time
    duration = endTime - startTime # total time everything took

    return matchedPasswords, duration

# test run of function
matchedPasswords, duration = findSaltedPasswords()

# print results
print("Matched passwords, salts, and hashes:")
for password, salt, hashed in matchedPasswords:
    print(f"Password: {password}, Salt: {salt}, Hash: {hashed}")

print(f"\nTime taken: {duration:.4f} seconds")