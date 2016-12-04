from file_importer import FileImporter

# Get new heading from current plus direction
def get_heading (current_heading, direction):
    assert direction in "LR"
    new_heading = current_heading - 90 if direction == "L" else current_heading + 90
    if new_heading == -90: 
        new_heading = 270
    if new_heading == 360:
        new_heading = 0
    assert new_heading in [0, 90, 180, 270]
    return new_heading

# Blocks gone in each heading
block_count = {
    "0": 0,
    "90": 0,
    "180": 0,
    "270": 0
}

# North
current_direction = 0

# Get input
inp = [i.strip() for i in FileImporter.get_input("/../input/1a.txt").split(",")]

for d in inp:
    current_direction = get_heading(current_direction, d[0])
    block_count[str(current_direction)] += int(d[1:])

distance_in_blocks = abs(block_count["0"] - block_count["180"]) + abs(block_count["90"] - block_count["270"])
print(distance_in_blocks)
