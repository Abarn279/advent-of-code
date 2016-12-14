from file_importer import FileImporter
from queue import Queue

# Get input
fav_number = int(FileImporter.get_input("/../input/13a.txt"))

def check_position(x, y):
    global fav_number
    if x < 0 or y < 0:
        return False
    binary_rep = bin((x*x + 3*x + 2*x*y + y + y*y) + fav_number)
    return True if binary_rep.count("1") % 2 == 0 else False

start = (1, 1, 0)
visited = []
q = Queue()
q.put(start)
count = 0

while not q.empty():
    position = q.get()

    if (position[0], position[1]) in visited:
        continue 

    visited.append( (position[0], position[1]) )

    if position[2] > 50:
        break
    count += 1

    for i in range(-1, 2):
        for j in range(-1, 2):
            x, y, dist = position[0] + i, position[1] + j, position[2] + 1
            
            if abs(i) != abs(j):
                if check_position(x, y):
                    q.put( (x, y, dist) )

print(count)