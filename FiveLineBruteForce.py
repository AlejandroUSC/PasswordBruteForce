# Code operates in 3 lines of code (4 including the import statement)
import hashlib, time
def gen_password(length, alphabet): return (c + suffix for c in alphabet for suffix in ([''] if length == 1 else gen_password(length - 1, alphabet)))
hashes = [line.strip() for line in open('hashes.txt', 'r')]; alphabet = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
for length, hashed in enumerate(hashes, 1): sTime = time.time(); password = next((p for p in gen_password(length, alphabet) if hashlib.md5(p.encode()).hexdigest() == hashed), ''); print(f"{hashed} unhashed is: {password}. Time Taken: {time.time() - sTime:.3f}")


# Optional ^, goes after hashes delcaration
# now = datetime.datetime.now()
# print(f"Current date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Alternative code, same as above
# Except this code does not include the time taken to crack
# 4 lines of code (5 including the import statement)

# import hashlib
# def gen_password(length, alphabet): return (c + suffix for c in alphabet for suffix in ([''] if length == 1 else gen_password(length - 1, alphabet)))
# hashes = [line.strip() for line in open('hashes.txt', 'r')]
# alphabet = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
# for length, hashed in enumerate(hashes, 1): password = next((p for p in gen_password(length, alphabet) if hashlib.md5(p.encode()).hexdigest() == hashed), ''); print(f"{hashed} unhashed is: {password}")