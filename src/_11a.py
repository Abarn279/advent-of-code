from file_importer import FileImporter
from queue import Queue
from random import sample
from itertools import combinations

def get_string_rep(floors):
    s = "" 
    for f in floors:
        f = sorted(list(f))
        s += ",".join(f) + '\n'
    return s

def is_valid(floors): 
    for floor in floors:

        # If there's generators without microchips, then this floor is radioactive
        all_gens = set([i for i in floor if i[1] == 'G'])
        is_radioactive = False 
        for g in all_gens:
            if g[0] + 'M' not in floor:
                is_radioactive = True

        # If there's any microchips without generators AND there's radioactivity, then this configuration isn't valid
        for m in set([i for i in floor if i[1] == 'M']):
            if m[0] + 'G' not in floor and is_radioactive:
                return False
    return True

def is_done(floors):
    return len(floors[0]) == 0 and len(floors[1]) == 0 and len(floors[2]) == 0

floors = [None for i in range(4)]

elevator_floor = 0
floors[0] = set(["HM", "LM"])
floors[1] = set(["HG"])
floors[2] = set(["LG"])
floors[3] = set()

visited = set()
q = Queue() 
q.put((floors, elevator_floor, 0)) # Floor state, elevator floor, total steps

while not q.empty():
    floors, elevator, current_steps = q.get()
    visited.add((get_string_rep(floors), elevator))

    if is_done(floors):
        print(current_steps)
        break

    # pick zero, one, or two things at current floor
    for i in range(0, 3):

        # if there are at least i many things on this floor, proceed
        if len(floors[elevator]) >= i:

            # get all possible moveable combos of size i
            combos = list(combinations(floors[elevator_floor], i))

            # new state for both up and down
            for d in [-1, 1]:

                # Taking none, just move elevator
                if i == 0:
                    if elevator + d < 0 or elevator + d > 3:
                        continue

                    if (get_string_rep(floors), elevator + d) not in visited:
                        q.put((floors[:], elevator + d, current_steps + 1))

                    continue
            
                # Taking 1 or more 
                for combo in combos:
                
                    # elevator cant be outside of building
                    if elevator + d < 0 or elevator + d > 3:
                        continue

                    new_floors = floors[:]

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

print(visited)