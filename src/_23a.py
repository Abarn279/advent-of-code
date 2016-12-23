from file_importer import FileImporter

# Get input
inp = [i.split() for i in FileImporter.get_input("/../input/23a.txt").split("\n")]
registers = { "a": 7, "b": 0, "c": 0, "d": 0 }

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

    elif instr[0] == "tgl":
        val = registers[instr[1]]
        ind_to_change = i + int(val)

        if ind_to_change >= len(inp):
            i += 1
            continue

        instr_to_change = inp[ind_to_change]
        
        # 1 arg vs 2
        if len(instr_to_change) == 2:
            if instr_to_change[0] == "inc":
                inp[ind_to_change][0] =  "dec"
            else:
                inp[ind_to_change][0] = "inc"

        if len(instr_to_change) == 3:
            if instr_to_change[0] == "jnz":
                inp[ind_to_change][0] =  "cpy"
            else:
                inp[ind_to_change][0] = "jnz"    

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

    i += 1
    
print(registers["a"])