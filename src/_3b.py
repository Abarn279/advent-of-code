from file_importer import FileImporter

# Get Input
inp = [[int(j) for j in list(filter(None, i.strip().split("  ")))] for i in FileImporter.get_input("/../input/3a.txt").split("\n")]
triangles = []

for column in range(3):
    for index in range(0, len(inp), 3):
        triangles.append(sorted([
            inp[index][column],
            inp[index + 1][column],
            inp[index + 2][column]
        ]))

possible = 0

for triangle in triangles:
    if triangle[0] + triangle[1] > triangle[2]:
        possible += 1
        
print(possible)