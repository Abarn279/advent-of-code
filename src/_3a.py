from file_importer import FileImporter

# Get Input
inp = [i.strip().split("  ") for i in FileImporter.get_input("/../input/3a.txt").split("\n")]

possible = 0

for line in inp:
    line = sorted([int(i.strip()) for i in list(filter(None, line))])

    if line[0] + line[1] > line[2]:
        possible += 1
        
print(possible)