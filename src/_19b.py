from file_importer import FileImporter
from collections import deque
import math

# Node of a doubly linked list  
class Node: 
    def __init__(self, next=None, prev=None, data=None): 
        self.next = next # reference to next node in DLL 
        self.prev = prev # reference to previous node in DLL 
        self.data = data
    def remove_next(self):
        self.next.next.prev = self
        self.next = self.next.next
    def skip(self, n):
        t = self
        for i in range(n):
            t = t.next
        return t

# Get input
elf_count = int(FileImporter.get_input("/../input/19a.txt").strip())

# build DLL
first = Node(None, None, 1)
curr = first
for e in range(2, elf_count + 1):
    nxt = Node(curr, None, e)
    curr.next = nxt
    nxt.prev = curr
    curr = nxt
first.prev = curr
curr.next = first

# go back to first node
curr = first
target = first.skip(math.floor(elf_count / 2.0))

while curr.next.data != curr.data:
    target.prev.remove_next()
    target = target.next.next if elf_count % 2 == 1 else target.next
    elf_count -= 1
    curr = curr.next

print(curr.data)
