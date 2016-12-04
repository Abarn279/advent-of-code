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

def get_coordinate (current_heading, current_point):
    assert current_heading in [0, 90, 180, 270]
    new_point = current_point[:]
    if current_heading == 0:
        new_point[1] += 1
    elif current_heading == 90:
        new_point[0] += 1
    elif current_heading == 180:
        new_point[1] -= 1
    elif current_heading == 270:
        new_point[0] -= 1
    return new_point

def coord_str(coord):
    """returns set hashable coordinate string"""
    return ",".join(str(x) for x in coord)

def get_visited_twice(inp):
    # Set of visited points
    visited = set()

    # Starting Coordinate point
    current_point = [0, 0]
    visited.add(coord_str(current_point))

    # North
    current_direction = 0

    for d in inp:
        current_direction = get_heading(current_direction, d[0])

        for block in range(0, int(d[1:])):
            current_point = get_coordinate(current_direction, current_point)
            if coord_str(current_point) not in visited:
                visited.add(coord_str(current_point))
            else:
                return current_point


# Get input
inp = [i.strip() for i in FileImporter.get_input("/../input/1a.txt").split(",")]
visited_twice = get_visited_twice(inp)

print(abs(visited_twice[0]) + abs(visited_twice[1]))
