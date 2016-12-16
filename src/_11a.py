from file_importer import FileImporter
import re
import itertools
import queue

def get_min_steps(building):
    # Move the stuff!
    #for element in elements_to_move:
     #   building[elevator].remove(element)
      #  building[elevator + next_move_direction].append(element)
    
    # Move elevator up or down
    #elevator += next_move_direction

    # Check floor we moved to to make sure it's not busted
    #non_connected_chips = [i for i in building[elevator] if i.endswith('m') and i[0] + "g" not in building[elevator]]
    #if len(non_connected_chips) and len([j for j in building[elevator] if j.endswith('g')]):
     #   return 10000000

    # Set up possible combinations to bring up/down
    #possible_ups = list(itertools.combinations(building[elevator], 2)) + list(itertools.combinations(building[elevator], 1))
    #possible_downs = possible_ups[:] if elevator != 0 else []
    #possible_ups = possible_ups if elevator != len(building) - 1 else []


    # If all have made it to top, 
    #if len(building[-1]) == sum([len(floor) for floor in building]):
     #   return 1

    #return 1 # + min (get_min_steps for all possible moves)


inp = [i.strip() for i in FileImporter.get_input("/../input/11a.txt").split("\n")]

building = [[] for i in range(len(inp))]

# Floor of elevator
elevator = 0

itemCount = 0
for floor in range(len(inp)):
    items = re.findall("(?:a )(\S)\S* (\S)\S*", inp[floor])
    for i in items:
        itemCount += 1
        building[floor].append(i[0] + i[1])

print(get_min_steps(building))