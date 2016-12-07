from file_importer import FileImporter
import re

def get_aba(sequence):
    assert len(sequence) == 3
    # Make sure that sequence isn't all of the same char, then check if ABA
    return sequence if sequence != len(sequence) * sequence[0] and sequence[0] == sequence[2] else None

def is_bab_of(bab, aba):
    assert len(bab) == 3 and len(aba) == 3
    bab = bab + bab[1]
    return bab[1:] == aba

def get_substrings_len_3(sequence):
    assert len(sequence) >= 3
    subs = []
    for i in range(0, len(sequence) - 2):
        subs.append(sequence[i:i+3])
    return subs

def get_abas(sequence):
    assert len(sequence) >= 3
    abas = []
    sequences = get_substrings_len_3(sequence)
    for sequence in sequences:
        abas.append(get_aba(sequence))
    return filter(None, abas)

def supports_ssl(abas, babs):
    for i in abas:
        for j in babs:
            if is_bab_of(i, j):
                return True
    return False

# Get input
inp = [i.strip() for i in FileImporter.get_input("/../input/7a.txt").split("\n")]

count_support_SSL = 0
for ip in inp:
    without_hypernets = filter(None, re.split("\[\w*\]", ip))

    abas = []
    for sequence in without_hypernets:
        abas += get_abas(sequence)
    
    if len(abas) == 0: 
        continue

    hypernets = re.findall("\[\w*\]", ip)
    babs = []
    for sequence in hypernets:
        babs += get_abas(sequence)

    if supports_ssl(abas, babs):
        count_support_SSL += 1

print(count_support_SSL)
    
    
