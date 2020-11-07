from file_importer import FileImporter
from aoc_utils import Vector2
import re
from searches import astar
from copy import deepcopy
import time 

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

class DataNode:
    def __init__(self, name, size, used, avail, usep):
        self.name = name
        self.size = int(size[:-1])
        self.used = int(used[:-1])
        self.avail = int(avail[:-1])
        gr = re.match('\/dev\/grid\/node-x(\d+)-y(\d+)', self.name).groups()
        self.pos = Node(*map(int, gr))

    def empty(self):
        self.used = 0
        self.avail = self.size

    def fill(self, amount):
        if self.used != 0:
            raise Exception()
        if self.avail != self.size:
            raise Exception()
        if amount > self.size:
            raise Exception()
        self.used = amount
        self.avail -= amount

    def __str__(self):
        return f'{self.name}, {self.size}, {self.used}, {self.avail}\n'

    def __hash__(self):
        return hash(str(self))

    def __repr__(self):
        return str(self)

# initial grid
grid = {} 
datanodes = [DataNode(*x.strip().split())
             for x in FileImporter.get_input("/../input/22a.txt").split("\n")][:]
for datanode in datanodes:
    grid[datanode.pos] = datanode

# set of full nodes that cant be transfered
full_nodes = set()

# get empty and full nodes from existing grid
empty = None
for k in grid:
    if grid[k].used == 0:
        empty = grid[k].pos
    if grid[k].size > 500:
        full_nodes.add(grid[k].pos)

# set initial wanted
wanted = Node(36, 0)
start = (wanted, empty)  # position of wanted data, position of current empty

def is_goal_fn(node):
    return node[0] == Node(0, 0)

# Heuristic
zero_pos = Node(0, 0)
def heuristic_fn(node):
    # return node[0].manhattan_distance(zero_pos) # slowest
    return node[0].manhattan_distance(zero_pos) + node[1].manhattan_distance(zero_pos) # fastest 
    # return node[0].manhattan_distance(zero_pos) + node[1].manhattan_distance(node[0]) # in the middle

DIRECTIONS = [Node(0, 1), Node(0, -1), Node(1, 0), Node(-1, 0)]

def get_key_fn(node):
    return node

def get_neighbors_fn(node):
    wanted = node[0]
    empty = node[1]
    neighbors = []

    # move in every direction, create a new state where the empty node is at current + d
    for d in DIRECTIONS:

        new_empty = empty + d

        if new_empty.x > 36 or new_empty.x < 0 or new_empty.y > 24 or new_empty.y < 0:
            continue

        if new_empty in full_nodes:
            continue

        # if wanted data is the one we just moved, reflect that in the new node
        new_wanted = wanted
        if new_empty == wanted:
            new_wanted = empty

        new = (new_wanted, new_empty)
        neighbors.append(new)

    return neighbors

s = time.time()
answer = astar(start, is_goal_fn, heuristic_fn,
               lambda x, y: 1, get_neighbors_fn, get_key_fn)
print(answer)
print(time.time() - s)
