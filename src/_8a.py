from file_importer import FileImporter

# Get input
inp = [i.strip() for i in FileImporter.get_input("/../input/8a.txt").split("\n")]

rects = [x for x in inp if x.split(" ")[0] == "rect"]

pixels = 0
for rect in rects:
    expr = rect.split(" ")[1].split("x")
    pixels += int(expr[0]) * int(expr[1])

print(pixels)