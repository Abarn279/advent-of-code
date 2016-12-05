from file_importer import FileImporter
import hashlib

# Get input
inp = FileImporter.get_input("/../input/5a.txt")

count = 0
password = [None for i in range(8)]
while True:
    to_hash = inp + str(count)
    hashed = hashlib.md5(to_hash.encode('utf-8')).hexdigest()
    if hashed[:5] == "00000":
        # ignore invalid
        try:
            if not password[int(hashed[5])]:
                password[int(hashed[5])] = hashed[6]

                if None not in password:
                    print("".join(password))
                    break
        except:
            pass
    count += 1
