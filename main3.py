import hashlib
import time


# hashes given
saltedHashes = {"3d12b4e927a859255d952e9810c73c5e831dd926698c37756336765ba506423e": "{d31", "efea8db5e83417453447131337b2cbdc031a4125c5e35cb872bca04c3f94c431": "{ahw)", "0bdf1284a4228fbe1b5747aea2a6fb7dbd651a7d8e60828aea6b54691fb37b09": "B}AV"}

# method to hash password with salt and 5 iterations
def hashPass(password, salt):
    combined = password + salt
    # loop through 5 iterations
    for _ in range(5):
        combined = hashlib.sha256(combined.encode()).hexdigest()
    return combined

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

            # check if matches given hash
            if hashPass(i, salt) == hashVal:
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