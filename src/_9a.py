from file_importer import FileImporter

# Get input
inp = FileImporter.get_input("/../input/9a.txt").strip()

def take_marker(s):
    return x != ")"

final = ""
while len(inp) > 0:

    # Marker start
    if inp[0] == "(":
        inp = inp[1:]
        marker = ""
        while inp[0] != ")":
            marker += inp[0]
            inp = inp[1:]

        #Start after paren
        inp = inp[1:]
        chars_repeat, times = map(int, marker.split("x"))
        to_add = (inp[0: chars_repeat]) * times
        final += to_add
        inp = inp[chars_repeat-1:]

    # Regular char
    else:
        final += inp[0]

    inp = inp[1:]

print(len(final))