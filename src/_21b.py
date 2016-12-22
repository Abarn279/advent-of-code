from file_importer import FileImporter
import operator
import itertools

def swap_pos(inp, pos1, pos2):
    if pos1 > pos2:
        pos1, pos2 = pos2, pos1
    return inp[0:pos1] + inp[pos2] + inp[pos1 + 1:pos2] + inp[pos1] + inp[pos2 + 1:]

def swap_letter(inp, let1, let2):
    ind1, ind2 = inp.index(let1), inp.index(let2)
    return swap_pos(inp, ind1, ind2)

def rotate(inp, dir, steps):
    final = [[] for i in range(len(inp))]
    op = operator.add if dir == "right" else operator.sub
    for i in range(len(inp)):
        new_ind = (op(i, steps)) % len(inp)
        final[new_ind] = inp[i]
    return "".join(final)

def rotate_pos_based(inp, let):
    ind = inp.index(let)
    additional = 1 if ind >= 4 else 0
    return rotate(inp, "right", 1 + ind + additional)

def move_pos(inp, x, y):
    char, without = inp[x], inp[:x] + inp[x+1:]
    return without[:y] + char + without[y:]
    
def reverse_sub(inp, x, y):
    if x > y:
        x, y = y, x
    to_rev = inp[x:y+1]
    return inp[:x] + "".join(reversed(to_rev)) + inp[y+1:]

# Get input
inp =  [x.strip().split(" ") for x in FileImporter.get_input("/../input/21a.txt").split("\n")]

for i in itertools.permutations("abcdefgh"):
    password = "".join(i)
    original = password

    for command in inp:
        if command[0] == "swap":
            if command[1] == "position":
                password = swap_pos(password, int(command[2]), int(command[5]))
            if command[1] == "letter":
                password = swap_letter(password, command[2], command[5])
        
        if command[0] == "rotate":
            if command[1] == "left" or command[1] == "right":
                password = rotate(password, command[1], int(command[2]))
            if command[1] == "based":
                password = rotate_pos_based(password, command[6])

        if command[0] == "reverse":
            password = reverse_sub(password, int(command[2]), int(command[4]))
        
        if command[0] == "move":
            password = move_pos(password, int(command[2]), int(command[5]))

    if password == "fbgdceah":
        print(original)
        break

