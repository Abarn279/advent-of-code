from file_importer import FileImporter
from hashlib import md5
from queue import Queue

open_door = "bcdef"

def get_opens(hash):
    global open_door
    return {
        "U": hash[0] in open_door,
        "D": hash[1] in open_door,
        "L": hash[2] in open_door,
        "R": hash[3] in open_door
    }

def check_pos(x, y):
    if x < 0 or x > 3 or y < 0 or y > 3:
        return False
    return True

# Get input
inp =  FileImporter.get_input("/../input/17a.txt").strip()

# Const index names, applies to 'start' below, as well as any queue position
X = 0
Y = 1
CURRENT_PATH = 2

start = (0, 0, "")
vault = (3, 3)
visited = set()
q = Queue()
q.put(start)

paths = []

while not q.empty():
    current = q.get()
    
    if current[X] == 3 and current[Y] == 3:
        paths.append(current[CURRENT_PATH])
        continue

    to_hash = inp + current[CURRENT_PATH]
    if to_hash in visited:
        continue
    visited.add(to_hash)
    
    hashed = md5(to_hash.encode('utf8')).hexdigest()
    open_doors = get_opens(hashed)

    for key in open_doors:
        if open_doors[key]:
            if key == "U" and check_pos(current[X], current[Y] - 1):
                q.put( (current[X], current[Y] - 1, current[CURRENT_PATH] + "U") )
            if key == "D" and check_pos(current[X], current[Y] + 1):
                q.put( (current[X], current[Y] + 1, current[CURRENT_PATH] + "D") )
            if key == "L" and check_pos(current[X] - 1, current[Y]):
                q.put( (current[X] - 1, current[Y], current[CURRENT_PATH] + "L") )
            if key == "R" and check_pos(current[X] + 1, current[Y]):
                q.put( (current[X] + 1, current[Y], current[CURRENT_PATH] + "R") )
         
print(len(max(paths, key=len)))