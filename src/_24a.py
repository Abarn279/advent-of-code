from file_importer import FileImporter
from collections import deque, defaultdict
from aoc_utils import Vector2
import string
from searches import astar

class Node(Vector2):
    def __init__(self, x, y):
        super().__init__(x, y)
    def __add__(self, other):
        return Node(self.x + other.x, self.y + other.y)
    def __lt__(self, other):
        return False
    def __repr__(self):
        return "Node: " + super().__repr__()
    def __str__(self):
        return self.__repr__()

DIRECTIONS = [Node(0, 1), Node(0, -1), Node(1, 0), Node(-1, 0)]

def get_limits(grid):
    return {
        "y": (min(i.y for i in grid.keys()), max(i.y for i in grid.keys())),
        "x": (min(i.x for i in grid.keys()), max(i.x for i in grid.keys()))
    }

def print_grid(grid, cl):
    limits = get_limits(grid)
    for y in range(limits["y"][0], limits["y"][1] + 1):
        for x in range(limits["x"][0], limits["x"][1] + 1):
            print('@' if cl == Node(x, y) else grid[Node(x, y)], end="")
        print()

def get_distance_from_to_key(grid, from_key, to_key):
    ''' BFS to find distance from one key to another '''
    global DIRECTIONS

    # Locations
    current_location = from_key[0]
    end_location = to_key[0]

    def is_goal_fn(node):
        return node == end_location

    def heuristic(node: Node): 
        return node.manhattan_distance(end_location)

    def cost(a, b):
        return 1

    visited = set()
    def get_neighbors(node):
        neighbors = []
        for d in DIRECTIONS:
            new = node + d
            if new not in visited and grid[new] != '#':
                neighbors.append(new)
                visited.add(new)

        return neighbors
            
    def get_key_fn(node: Node):
        return node.to_tuple()

    return (end_location, astar(current_location, is_goal_fn, heuristic, cost, get_neighbors, get_key_fn)) 

def get_shortest_path(grid, starting_position, distance_map):
    ''' Get shortest path to getting all keys '''
    ####
    # A* NODE IS TUPLE -> (string of current keys, current cost, current location)
    # Indexed by:         (0                     , 1           , 2               )
    ####
    num_keys = sum(1 for i in grid.values() if i in string.digits)
    min_dist = 100000
    for this_char in distance_map:
        distances = distance_map[this_char]
        for other_char_key in distances:
            other_char_pos, distance_to_other = distance_map[this_char][other_char_key]
            if distance_to_other < min_dist:
                min_dist = distance_to_other

    finalNode = None

    def is_goal_fn(node):
        nonlocal finalNode
        is_goal = len(node[0]) == num_keys
        if is_goal:
            finalNode = node
        return is_goal 

    def heuristic(node): 
        return min_dist * (num_keys - len(node[0]))

    def cost(a, b):
        return b[1] - a[1] 

    def get_neighbors(node):
        keys_acquired = set(node[0])

        this_char = grid[node[2]]
        distances_from_here = distance_map[this_char]
        keys_available = []

        # Keys are available if keys_encountered on the path is a subset of keys_acquired
        for other_char_key in distances_from_here:
            other_char_pos, distance_to_other = distance_map[this_char][other_char_key]

            # If all of the keys on this path have been acquired, it's a viable path
            if other_char_key[1] not in keys_acquired:
                keys_available.append((other_char_pos, distance_to_other, other_char_key[1]))

        neighbors = []
        for key_point, distance_to, key_char in keys_available:
            new_node = ("".join(sorted(node[0])) + key_char, node[1] + distance_to, key_point)
            neighbors.append(new_node)

        return neighbors
            
    def get_key_fn(node):
        return node[0]

    return (astar(("", 0, starting_position), is_goal_fn, heuristic, cost, get_neighbors, get_key_fn), finalNode)

# Input and stuff
grid = {}
inp = FileImporter.get_input("/../input/24.txt").split("\n")
for y in range(len(inp)):
    for x in range(len(inp[y])):
        grid[Node(x, y)] = inp[y][x]

# Find starting position
[starting_position] = [i for i in grid.items() if i[1] == '0']
starting_position = (starting_position[0], '.')
grid[starting_position[0]] = '.'

distance_map = defaultdict(lambda: {})       # map of key char to a map of other key chars and the distance to them 
all_poi = [i for i in grid.items() if i[1] in string.digits] + [starting_position]

for poi in all_poi:
    other_pois = [i for i in all_poi if i[1] != poi[1]]
    for other_poi in other_pois:

        if other_poi[1] == '.':
            continue

        distance = get_distance_from_to_key(grid, poi, other_poi)
        distance_map[poi[1]][other_poi] = distance

r = get_shortest_path(grid, starting_position[0], distance_map)

final_poi = r[1][2]

print(r[0] + get_distance_from_to_key(grid, (final_poi, r[1][0][:-1]), starting_position)[1])