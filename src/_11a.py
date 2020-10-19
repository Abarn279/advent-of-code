from file_importer import FileImporter
from collections import deque
from itertools import combinations
from searches import astar
import time

def get_string_rep(floors):
    ''' hash function for visited set '''
    s = "" 
    for f in floors:
        f = sorted(list(f))
        s += ",".join(f) + '|'
    return s

def is_valid(floors): 
    ''' checks to see if a configuration is valid ''' 
    for floor in floors:

        # If there's generators without microchips, then this floor is radioactive
        all_gens = set([i for i in floor if i[1] == 'G'])
        is_radioactive = len(all_gens) > 0

        # If there's any microchips without generators AND there's radioactivity, then this configuration isn't valid
        for m in set([i for i in floor if i[1] == 'M']):
            if m[0] + 'G' not in floor and is_radioactive:
                return False
    return True

def copy_state(floors):
    return [i.copy() for i in floors]

def is_done(floors):
    return len(floors[0]) == 0 and len(floors[1]) == 0 and len(floors[2]) == 0

start = time.time()
floors = [None for i in range(4)]

# part 1
# floors[0] = set(["TG", "TM", "PG", "SG"])
# floors[1] = set(["PM", "SM"])
# floors[2] = set(["XG", "XM", "RG", "RM"])
# floors[3] = set()

# part 1 sean
floors[0] = set(["SG", "SM", "PG", "PM"])
floors[1] = set(["TG", "RG", "RM", "CG", "CM"])
floors[2] = set(["TM"])
floors[3] = set()

# part 2
# floors[0] = set(["TG", "TM", "PG", "SG", "EG", "EM", "DG", "DM"])
# floors[1] = set(["PM", "SM"])
# floors[2] = set(["XG", "XM", "RG", "RM"])
# floors[3] = set()

# test
# floors[0] = set(["HM", "LM"])
# floors[1] = set(["HG"])
# floors[2] = set(["LG"])
# floors[3] = set()

def heuristic(n):
    total = 0
    for floor_ind in range(len(n[0])):
        total += len(n[0][floor_ind]) * (3 - floor_ind)
    return total

def get_neighbors(n):
    global visited 

    floors = n[0]
    elevator = n[1]
    current_steps = n[2]
    neighbors = []

    # pick one or two things at current floor
    for i in range(1, 3):

        # if there are at least i many things on this floor, proceed
        if len(floors[elevator]) >= i:

            # get all possible moveable combos of size i
            combos = list(combinations(floors[elevator], i))

            # new state for both up and down
            for d in [-1, 1]:

                # Taking 1 or more 
                for combo in combos:
                
                    # elevator cant be outside of building
                    if elevator + d < 0 or elevator + d > 3:
                        continue

                    # create a copy of the existing state so that we don't share references of sets within
                    new_floors = copy_state(floors)

                    # try to make the move
                    for c in combo:
                        new_floors[elevator].remove(c)
                        new_floors[elevator + d].add(c)

                    # don't add if invalid config
                    if not is_valid(new_floors):
                        continue

                    neighbors.append((new_floors, elevator + d, current_steps + 1))
    return neighbors

steps = astar(start = (floors, 0, 0), 
    is_goal_fn = lambda x: is_done(x[0]),
    heuristic_fn = heuristic,
    cost_fn = lambda a, b: 1,
    get_neighbors_fn = get_neighbors,
    get_key_fn = lambda x: (get_string_rep(x[0]), x[2])
)

print(steps)
print(time.time() - start)
