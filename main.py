import hashlib
import time


# hashes given
hashes = ["c231726a6fdad30f6c67ba99bc2243c807e1a51b4327f7eacef27ca59ea2e64b", "8126bda31755b97d6bb694cccf2551c0a5d0fdcdeddb74ca2b82d1292dca8652", "8126bda31755b97d6bb694cccf2551c0a5d0fdcdeddb74ca2b82d1292dca8652"]

# method to read RockYou text and match passwords
def matchPasswords():
    # open and read password file
    with open("rockyou.txt", "r", encoding = "ISO-8859-1") as file:
        passwords = file.read().splitlines()
    
    # list for hashses and matching passwords
    matchedPasswords = []

    startTime = time.time()

    # iterate through each password in dataset
    for i in passwords:
        hashedPassword = hashlib.sha256(i.encode()).hexdigest()

        # check if computed hash matches any of previous hashes
        if hashedPassword in hashes:
            matchedPasswords.append((i, hashedPassword)) # store matching password and hash
    endTime = time.time() # end time
    duration = endTime - startTime # total time everything took

    return matchedPasswords, duration

# test run of function
matchedPasswords, duration = matchPasswords()

# print matched passwords with corresponding hashes
print(f"Matched passwords and their hashes:")
for password, hashed in matchedPasswords:
    print(f"Password: {password}, Hash: {hashed}")

# print total time taken to complete matching process
print(f"\nTime taken: {duration:.4f} seconds")