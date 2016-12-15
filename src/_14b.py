from file_importer import FileImporter
from hashlib import md5

def get_first_repeated(seq, count):
    for i in range(len(seq) - (count - 1)):
        if seq[i:i+count] == count * seq[i]:
            return seq[i]
    return None

def has_repeated_sequence(seq, char, count):
    for i in range(len(seq) - (count - 1)):
        if seq[i:i+count] == count * char:
            return True
    return False

def get_hash(salt, ind, cache):
    hashed = ""
    if ind not in cache:
        to_hash = salt + str(ind)
        hashed = md5(to_hash.encode('utf-8')).hexdigest()
        for i in range(2016):
            hashed = md5(hashed.encode('utf8')).hexdigest()
        cache[ind] = hashed
    else:
        hashed = cache[ind]
    return hashed

# Get input
inp =  FileImporter.get_input("/../input/14a.txt").strip()

index = 0
keys = 0

hash_cache = {} # Couldn't wait to use this one.

while True:
    hashed = get_hash(inp, index, hash_cache)

    first_repeated = get_first_repeated(hashed, 3)
    if first_repeated:

        for i in range(index+1, index+1001):
            hashed = get_hash(inp, i, hash_cache)
            if has_repeated_sequence(hashed, first_repeated, 5):
                keys += 1
                break
    
    if keys == 64:
        print(index)
        break   
    index += 1
    