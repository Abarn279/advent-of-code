from file_importer import FileImporter

def get_key(current, direction):
    assert direction in "RDLU"
    new = current[:]
    if direction == "U":
        new[1] -= 1
    if direction == "D":
        new[1] += 1
    if direction == "R":
        new[0] += 1
    if direction == "L":
        new[0] -= 1
    if -1 in new or 3 in new:
        return current
    return new

# Get input
inp = [i.strip() for i in FileImporter.get_input("/../input/2a.txt").split("\n")]

keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Start on 5
current_key = [1, 1]
code = ""

for line in inp:
    for d in line:
        current_key = get_key(current_key, d)
    code += str(keypad[current_key[1]][current_key[0]])

print(code)
