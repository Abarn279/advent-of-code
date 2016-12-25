from file_importer import FileImporter

# Get input
inp = [i.split() for i in FileImporter.get_input("/../input/25a.txt").split("\n")]

def check(inp):
    for i in range(len(inp) - 1):
        if inp[i] not in "01":
            return False
        if inp[i] == "0" and inp[i+1] != "1":
            return False
        if inp[i] == "1" and inp[i+1] != "0":
            return False
    return True

def get_first_repeated(inp):
    starting = 0
    
    while True:
        registers = { "a": starting, "b": 0, "c": 0, "d": 0 }
        orig = registers["a"]
        output = ""
        count = 0
        i = 0
        while i < len(inp):
            instr = inp[i]
            if instr[0] == "cpy":
                if not instr[2].isdigit():
                    if instr[1].lstrip('-').isdigit():
                        registers[instr[2]] = int(instr[1])
                    else:
                        registers[instr[2]] = registers[instr[1]]
            elif instr[0] == "inc":
                registers[instr[1]] += 1
            elif instr[0] == "dec":
                registers[instr[1]] -= 1

            elif instr[0] == "jnz":
                val = 0
                if instr[1].isdigit():
                    val = int(instr[1])
                else:
                    val = registers[instr[1]]
                if val != 0:
                    if instr[2].lstrip('-').isdigit():
                        i += int(instr[2])
                    else:
                        i += registers[instr[2]]
                    continue

            elif instr[0] == "out":
                output += str(registers[instr[1]])

            i += 1
            count += 1
            if count > 100000:
                break

        if check(output):
            print(orig)
            break
        
        starting += 1

get_first_repeated(inp)