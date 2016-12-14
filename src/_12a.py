from file_importer import FileImporter

# Get input
inp = [i.split(" ") for i in FileImporter.get_input("/../input/12a.txt").split("\n")]
registers = { "a": 0, "b": 0, "c": 0, "d": 0 }

i = 0
while i < len(inp):
    instr = inp[i]
    if instr[0] == "cpy":
        if instr[1].isdigit():
            registers[instr[2]] = int(instr[1])
        else:
            registers[instr[2]] = registers[instr[1]]
    elif instr[0] == "inc":
        registers[instr[1]] += 1
    elif instr[0] == "dec":
        registers[instr[1]] -= 1

    if instr[0] == "jnz":
        val = 0
        if instr[1].isdigit():
            val = int(instr[1])
        else:
            val = registers[instr[1]]
        if val != 0:
            i += int(instr[2])
            continue

    i += 1
    
print(registers["a"])