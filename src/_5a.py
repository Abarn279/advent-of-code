from file_importer import FileImporter
import hashlib

# Get input
inp = FileImporter.get_input("/../input/5a.txt")

count = 0
password = ""
while True:
    to_hash = inp + str(count)
    hashed = hashlib.md5(to_hash.encode('utf-8')).hexdigest()
    if hashed[:5] == "00000":
        password += hashed[5]
        if len(password) == 8:
            break
    count += 1
