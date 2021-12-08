#/usr/bin/env python3

import re

def p1(diagnostics):
    middle = len(diagnostics) / 2
    gamma = 0
    epsilon = 0
    for bit in [sum(x) for x in zip(*diagnostics)]:
        gamma <<= 1
        epsilon <<= 1
        if bit > middle:
            gamma += 1 
        else:
            epsilon += 1
    return gamma * epsilon

def p2(diagnostics):
    d_oxygen = diagnostics.copy()
    d_co2 = diagnostics.copy()
    # search oxygen
    i = 0
    while len(d_oxygen) > 1:
        bit = sum([x[i] for x in d_oxygen])
        if bit >= len(d_oxygen)/2:
            d_oxygen = list(filter(lambda l: l[i] == 1, d_oxygen))
        else:
            d_oxygen = list(filter(lambda l: l[i] == 0, d_oxygen))
        i += 1
    oxygen = 0
    for b in d_oxygen[0]:
        oxygen <<= 1
        oxygen += b
    # search co2
    i = 0
    while len(d_co2) > 1:
        bit = sum([x[i] for x in d_co2])
        if bit >= len(d_co2)/2:
            d_co2 = list(filter(lambda l: l[i] == 0, d_co2))
        else:
            d_co2 = list(filter(lambda l: l[i] == 1, d_co2))
        i += 1
    co2 = 0
    for b in d_co2[0]:
        co2 <<= 1
        co2 += b
    return oxygen * co2

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        diagnostics = [list(map(int,list(x.rstrip()))) for x in f.readlines()]
    print("part1: {}".format(p1(diagnostics)))
    print("part2: {}".format(p2(diagnostics)))
