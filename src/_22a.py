from file_importer import FileImporter

def get_name(file):
    return file.split("-", 1)[1]

FILESYSTEM, SIZE, USED, AVAIL, USEP = 0, 1, 2, 3, 4
inp =  [x.strip().split() for x in FileImporter.get_input("/../input/22a.txt").split("\n")][2:]

pairs = 0
for a in range(len(inp)):
    node_a = inp[a]
    for b in range(a+1, len(inp)):
        node_b = inp[b]

        if int(node_a[USED][:-1]) != 0 and int(node_a[USED][:-1]) < int(node_b[AVAIL][:-1]):
            pairs += 1
            break

        if int(node_b[USED][:-1]) != 0 and int(node_b[USED][:-1]) < int(node_a[AVAIL][:-1]):
            pairs += 1

print(pairs)
            