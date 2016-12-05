from file_importer import FileImporter
import collections

# Get input
inp = [i.strip() for i in FileImporter.get_input("/../input/4a.txt").split("\n")]

for room in inp:
    sector_id = int(room.split("[")[0].split("-")[-1])
    name = "".join(room.split("[")[0].split("-")[:-1])
    shift = sector_id % 26
    new_char = [((( ord(i) + shift ) % 97 ) % 26 ) + 97 for i in name if i != "-"]
    shifted = "".join([ chr(j) for j in new_char])
    if "north" in shifted:
        print(sector_id)
        break