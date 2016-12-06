from file_importer import FileImporter
import collections

# Get input
inp = [i.strip() for i in FileImporter.get_input("/../input/6a.txt").split("\n")]

# Transpose input to columns, get most common for each column
corrected = "".join([collections.Counter(column).most_common()[0][0] for column in zip(*inp)])
print(corrected)
