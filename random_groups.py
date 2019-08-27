#!/usr/bin/python3

import sys
import random

if len(sys.argv) != 3:
    print("Usage: random_groups.py FILENAME GROUPSIZE")

filename = sys.argv[1]
try:
    size = int(sys.argv[2])
except ValueError:
    print("Usage: random_groups.py FILENAME GROUPSIZE")

with open(filename) as f:
    names = f.readlines()

names = [n.strip().title() for n in names]
    
num_groups = len(names) // size

# keep track of index numbers that haven't been selected
num_list = [i for i in range(len(names))]

# red, green, yellow, blue
color_codes = ["\033[1;31;40m", "\033[1;32;40m", "\033[1;33;40m", "\033[1;34;40m"]

if len(names) % size == 0:
    # evenly divisble
    for i in range(num_groups):
        print(f"{color_codes[i%4]}Group #{i+1}:",end=" ")
        for j in range(size):
            name_index = random.choice(num_list)
            num_list.remove(name_index)
            print(f"{color_codes[i%4]}{names[name_index]:20}",end="\t")
        print()
        print()


else:
    # there will be groups with 1 more than requested size
    big_groups = len(names) % size
    for i in range(big_groups):
        print(f"{color_codes[i%4]}Group #{i+1}:",end=" ")
        for j in range(size+1):
            name_index = random.choice(num_list)
            num_list.remove(name_index)
            print(f"{color_codes[i%4]}{names[name_index]:20}",end="\t")
        print()
        print()

    for i in range(num_groups - big_groups):
        print(f"{color_codes[(i+big_groups)%4]}Group #{i+1+big_groups}:",end=" ")
        for j in range(size):
            name_index = random.choice(num_list)
            num_list.remove(name_index)
            print(f"{color_codes[(i+big_groups)%4]}{names[name_index]:20}",end="\t")
        print()
        print()


# reset color back to default
print("\033[0;37;40m")