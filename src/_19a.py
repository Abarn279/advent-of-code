from file_importer import FileImporter
from collections import OrderedDict

# Get input
inp =  int(FileImporter.get_input("/../input/19a.txt").strip())

# List of elf ID's
elves = [i for i in range(1, inp + 1)]

while len(elves) != 1:
    size = len(elves)
    # delete all evens
    del elves[1::2]
    # if list size was odd and we haven't accounted for final item, append it to front and restart :)
    if size % 2 != 0:
        elves.insert(0, elves.pop())

print(elves[0])