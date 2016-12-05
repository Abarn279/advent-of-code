from file_importer import FileImporter
import collections

# Get input
inp = [i.strip() for i in FileImporter.get_input("/../input/4a.txt").split("\n")]

final_sum = 0
for line in inp:
    name = "".join(line.split("[")[0].split("-")[:-1])
    most = sorted(sorted(collections.Counter(name).most_common(), key = lambda x: (x[0])), key = lambda x: (x[1]), reverse=True)[:5]
    expected_checksum = "".join([x[0] for x in most])
    
    existing_checksum = line.split("[")[1][:-1]
    # Checksums are equal
    if expected_checksum == existing_checksum:
        sector_id = int(line.split("[")[0].split("-")[-1])
        final_sum += sector_id

print(final_sum)
