from file_importer import FileImporter
from aoc_utils import Vector2

# Get input
inp = FileImporter.get_input("/../input/18.txt").strip()

width = len(inp)
rows = 400000

row = {}
total = 0

for i, j in enumerate(inp):
    if j == '^':
        row[i] = 1
    else:
        row[i] = 0
        total += 1

for y in range(1, rows):

    row_underneath = {}

    for x in range(width): # 0 safe, 1 trap
        left = 0 if x == 0 else row[x - 1]
        center = row[x]
        right = 0 if x == width - 1 else row[x + 1]

        if (left + center == 2 and left + center + right == 2) or (center + right == 2 and left + center + right == 2) or (left == 1 and left + center + right == 1) or (right == 1 and left + center + right == 1):
            row_underneath[x] = 1
        else:
            row_underneath[x] = 0
            total += 1

    row = row_underneath

print(total)