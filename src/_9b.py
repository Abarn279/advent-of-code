from file_importer import FileImporter
import re

# Get input
inp = FileImporter.get_input("/../input/9a.txt").strip()

def get_decompressed_len(inp):
    split = re.split("(\(\w*\))", inp, 1)
    final = ""

    # Base case 1
    if (len(split) == 1):
        return len(split[0])

    if (len(split) == 3): 
        final += split[0]
        split = split[1:]

    marker, rest = split
    num_chars, times = map(int, marker[1:len(marker) - 1].split("x"))

    to_decompress = rest[:num_chars]
    rest = rest[num_chars:]
    to_decompress_len = len(to_decompress)

    if "(" in to_decompress and ")" in to_decompress:
        to_decompress_len = get_decompressed_len(to_decompress)

    # Base case 2
    final_len = len(final) + (to_decompress_len * times)

    return final_len + get_decompressed_len(rest)

print(get_decompressed_len(inp))