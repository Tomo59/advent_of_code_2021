#/usr/bin/env python3

def p1(depths):
    return sum([1 for x in range(len(depths)-1) if depths[x+1] > depths[x]])

def p2(depths):
    return sum([1 for x in range(len(depths)-3) if depths[x+3] > depths[x]])

if __name__ == "__main__":
    f = open('input.txt', 'r')
    depths = [int(x) for x in f.readlines()]
    print("part1: {}".format(p1(depths)))
    print("part2: {}".format(p2(depths)))
