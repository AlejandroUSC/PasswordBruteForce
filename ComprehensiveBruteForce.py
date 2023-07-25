#  Proj: Brute Force Password Cracking
#  Desc: A brute force password cracker works by iterating through every 
#        combination of characters sequentially until it finds a password match.
#        Students will draft a script to crack MD5 hashed passwords, the same
#        hashing algorithm used by most Linux distributions. Students will
#        then analyze the cracking of various passwords of predetermined length,
#        documenting how long the script took to crack it.
# 

# Import statement allows us to call other modules and use their resources
import hashlib, time, datetime

# Recursive function that allows us to slowly append characters 1 by 1
# Returns a generated word of size length
def gen_password(length, alphabet):
    if length == 0:
        yield ''
    else:
        for c in alphabet:
            for suffix in gen_password(length - 1, alphabet):
                yield c + suffix

# Reads from the hashes.txt file and creates a list called hashes
# which contains all 8 of our preloaded MD5 hashes
with open('hashes.txt', 'r') as file:
    content = file.readlines()
    hashes = [cont.strip() for cont in content]

# A string named alphabet that contains all of our available characters to use
alphabet = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
# alphabet = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789'

# Quick little print statement that displays the time the script began to run
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

# A loop that will iterate for as many hashes there exists in the list (our case 8)
for length, hashed in enumerate(hashes,1):
    # Take measurement of the time the loop began
    sTime = time.time()
    
    # Another loop that will call gen_password passing it the parameters required to construct our
    # word of size length.
    for password in gen_password(length, alphabet):
        # The password that was generated will have to be converted into a binary sequence (.encode())
        # which then the hashlib module/import will create into a MD5 hash. Lastly it must use the 
        # .hexdigest() function to convert the MD5 into legible value, hexadecimal
        # Finally the passwords MD5 hashcode in hex is compared to the hash value we have from hashes.txt
        # Once found program breaks from the loop and prints the password along with the time taken to find
        if hashlib.md5(password.encode()).hexdigest() == hashed:
            break
    # Once found it will display it to the terminal along with the time taken
    print(hashed + " unhashed is: " + password + ". Time Taken: {:.3f}".format(time.time() - sTime))