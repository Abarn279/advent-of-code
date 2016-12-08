from file_importer import FileImporter

def print_screen(screen):
    for i in screen:
        print(" ".join(i))
    print()

def create_rectangle(screen, width, height):
    for i in range(width):
        for j in range(height):
            screen[j][i] = "#"

def rotate_row(screen, row, amount):
    to_rotate = screen[row]
    rotated = []
    for i in range(len(to_rotate)):
        rotated.append(to_rotate[i - amount])
    screen[row] = rotated

def rotate_column(screen, column, amount):
    to_rotate = [row[column] for row in screen]
    rotated = []
    for i in range(len(to_rotate)):
        rotated.append(to_rotate[i - amount])
    
    for i in range(len(screen)):
        screen[i][column] = rotated[i]

# Get input
inp = [i.strip() for i in FileImporter.get_input("/../input/8a.txt").split("\n")]

# Index by going down, then across
screen = [["." for i in range(50)] for j in range(6)]

for command in inp:
    command = command.split(" ")

    if command[0] == "rect":
        expr = command[1].split("x")
        create_rectangle(screen, int(expr[0]), int(expr[1]))
        
    if command[0] == "rotate":
        row = int(command[2].split("=")[1])
        amount = int(command[4])
        if command[1] == "row":
            rotate_row(screen, row, amount)
        if command[1] == "column":
            rotate_column(screen, row, amount)

print_screen(screen)
            
        


