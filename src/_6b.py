from file_importer import FileImporter
import collections

# Get input
inp = [i.strip() for i in FileImporter.get_input("/../input/6a.txt").split("\n")]

# Transpose input to columns
columns = []
for column in range(0, len(inp[0])):
    columnToAdd = []
    for row in range(0, len(inp)):
        columnToAdd.append(inp[row][column])
    columns.append("".join(columnToAdd))

corrected = "".join([collections.Counter(column).most_common()[-1][0] for column in columns])
print(corrected)
