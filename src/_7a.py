from file_importer import FileImporter
import re

def is_abba(sequence):
    assert len(sequence) == 4
    # Make sure that sequence isn't all of the same char, then check if ABBA
    return sequence != len(sequence) * sequence[0] and sequence[:2] == "".join(reversed(sequence[-2:]))

def get_substrings_len_4(sequence):
    assert len(sequence) >= 4
    subs = []
    for i in range(0, len(sequence) - 3):
        subs.append(sequence[i:i+4])
    return subs

def has_abba(sequence):
    assert len(sequence) >= 4
    sequences = get_substrings_len_4(sequence)
    for sequence in sequences:
        if is_abba(sequence):
            return True
    return False

# Get input
inp = [i.strip() for i in FileImporter.get_input("/../input/7a.txt").split("\n")]

count_support_TLS = 0
for ip in inp:
    hypernets = re.findall("\[\w*\]", ip)

    valid = True
    for hypernet in hypernets:
        if has_abba(hypernet[1:len(hypernet) - 1]):
            valid = False
            break

    if valid:
        without_hypernets = filter(None, re.split("\[\w*\]", ip))

        for addr in without_hypernets:
            if has_abba(addr):
                count_support_TLS += 1
                break

print(count_support_TLS)
    
    
