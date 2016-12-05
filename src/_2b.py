from file_importer import FileImporter

def get_key(current, direction, keypad):
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
    
    if -1 in new or 5 in new or keypad[new[1]][new[0]] == "x":
        return current
    return new

# Get input
inp = [i.strip() for i in FileImporter.get_input("/../input/2a.txt").split("\n")]

keypad = ["xx1xx", "x234x", "56789", "xABCx", "xxDxx"]
# Start on 5
current_key = [2, 0]
code = ""

for line in inp:
    for d in line:
        current_key = get_key(current_key, d, keypad)
    code += keypad[current_key[1]][current_key[0]]

print(code)
