from file_importer import FileImporter
import re
import itertools
from queue import Queue
import copy

def check_done(building):
    for i in range(len(building) - 1):
        if len(building[i]) > 0:
            return False
    return True

inp = [i.strip() for i in FileImporter.get_input("/../input/11a.txt").split("\n")]
building = [set() for i in range(len(inp))]
elevator = 0 # Floor of elevator

for floor in range(len(inp)):
    items = re.findall("(?:a )(\S\S)\S* (\S)\S*", inp[floor])
    for i in items:
        building[floor].add(i[0] + i[1])

visited = []
q = Queue()
# Building configuration, elevator position, steps from original
start = ( building[:], 0, 0 )
q.put(start)

while not q.empty():
    current_state = q.get()

    # Are we done?
    if check_done(current_state[0]):
        print(current_state[2])
        break

    # Have we been here before?
    if ( (current_state[0], current_state[1]) ) in visited:
        continue

    # Append building w/ elevator position
    visited.append( (current_state[0], current_state[1]) ) 
    
    # Will the chips melt?
    non_connected_chips = [i for i in current_state[0][current_state[1]] if i.endswith('m') and i[0] + i[1] + "g" not in current_state[0][current_state[1]]]
    if len(non_connected_chips) and len([j for j in current_state[0][current_state[1]] if j.endswith('g')]):
        continue

    # Get possible moves
    possible_ups = list(itertools.combinations(current_state[0][current_state[1]], 2)) + list(itertools.combinations(current_state[0][current_state[1]], 1))
    possible_downs = possible_ups[:] if current_state[1] != 0 else []
    possible_ups = possible_ups if current_state[1] != len(current_state[0]) - 1 else []

    for possible_up in possible_ups:
        new_config = copy.deepcopy(current_state[0])
        elevator = current_state[1]

        for element in possible_up:
            new_config[elevator].remove(element)
            new_config[elevator + 1].add(element)
        
        q.put( (new_config, elevator + 1, current_state[2] + 1) )
    
    for possible_down in possible_downs:
        new_config = copy.deepcopy(current_state[0])
        elevator = current_state[1]

        for element in possible_down:
            new_config[elevator].remove(element)
            new_config[elevator - 1].add(element)
        
        q.put( (new_config, elevator - 1, current_state[2] + 1) )