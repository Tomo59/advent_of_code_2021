#/usr/bin/env python3

import re

def p1(instructions):
    horizontal_pos = 0
    depth = 0
    for i in instructions:
        if i[0] == "forward":
            horizontal_pos += int(i[1])
        elif i[0] == "down":
            depth += int(i[1])
        elif i[0] == "up":
            depth -= int(i[1])
        else:
            print("UNKNOWN INSTRUCTION")
    return horizontal_pos * depth

def p2(instructions):
    horizontal_pos = 0
    depth = 0
    aim = 0
    for i in instructions:
        if i[0] == "forward":
            horizontal_pos += int(i[1])
            depth += aim * int(i[1])
        elif i[0] == "down":
            aim += int(i[1])
        elif i[0] == "up":
            aim -= int(i[1])
        else:
            print("UNKNOWN INSTRUCTION")
    return horizontal_pos * depth

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        instructions = [re.split(" ", x.rstrip()) for x in f.readlines()]
    print("part1: {}".format(p1(instructions)))
    print("part2: {}".format(p2(instructions)))
