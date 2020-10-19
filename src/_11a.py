from file_importer import FileImporter
from queue import Queue
from random import sample
from itertools import combinations

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

floors = [None for i in range(4)]

floors[0] = set(["TG", "TM", "PG", "SG"])
floors[1] = set(["PM", "SM"])
floors[2] = set(["XG", "XM", "RG", "RM"])
floors[3] = set()

# BFS
visited = set()
q = Queue() 
q.put((floors, 0, 0)) # Floor state, elevator floor #, total steps

while not q.empty():
    floors, elevator, current_steps = q.get()
    visited.add((get_string_rep(floors), elevator))

    if is_done(floors):
        print(current_steps)
        break

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

                    # don't add if already visited
                    if (get_string_rep(new_floors), elevator + d) in visited:
                        continue

                    # don't add if invalid config
                    if not is_valid(new_floors):
                        continue

                    q.put((new_floors, elevator + d, current_steps + 1))
