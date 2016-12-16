from file_importer import FileImporter
import re

def get_dragon_curve(a):
    b = reversed(a)
    b = ''.join('1' if x == '0' else '0' for x in b)
    return a + "0" + b

def get_checksum(inp):
    final = ""
    pairs = re.findall("..", inp)
    for pair in pairs:
        if pair[0] == pair[1]:
            final += "1"
        else:
            final += "0"
    if len(final) % 2 == 0:
        return get_checksum(final)
    return final

# Get input
for_checksum =  FileImporter.get_input("/../input/16a.txt").strip()

disk_length = 272

# Get proper input to compute checksum
while len(for_checksum) < disk_length:
    for_checksum = get_dragon_curve(for_checksum)
for_checksum = for_checksum[:disk_length]

print(get_checksum(for_checksum))
