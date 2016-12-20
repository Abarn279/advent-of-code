from file_importer import FileImporter

# Get input
inp =  [list(map(int, y.split("-"))) for y in [x.strip() for x in FileImporter.get_input("/../input/20a.txt").split("\n")]]
inp = sorted(inp, key=lambda x: x[0])

max0, max1 = inp[0][0], inp[0][1]

for i in inp:
    if i[0] > max0:
        max0 = i[0]

    if max0 > max1 + 1:
        print(max1 + 1)
        break
    
    if i[1] > max1:
        max1 = i[1]
