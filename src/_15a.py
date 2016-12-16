from file_importer import FileImporter

# Get input
inp =  [i.strip().split(" ") for i in FileImporter.get_input("/../input/15a.txt").split("\n")]

disks = []
for i in inp:
    disks.append( [
        int(i[1][1:]), # ID
        int(i[3]), # Total Positions
        int(i[11][0:-1]) # Position at t=0
    ] )

time = 0

while True:
    # Check to see if disks are lined up right
    first_time = True
    added_time = 1
    for disk in disks:
        if (disk[2] + added_time) % disk[1] != 0:
            first_time = False
            break
        added_time += 1
        
    if first_time:
        print(time)
        break

    else:
        time += 1
        for disk in disks:
            disk[2] = (disk[2] + 1) % disk[1]
        