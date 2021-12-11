#/usr/bin/env python3

def in_array(k):
    (i,j) = k
    return i>=0 and j>=0 and i<10 and j<10


def neighbours(k):
    (i,j) = k
    r = [
            (i+1,j+1),
            (i  ,j+1),
            (i-1,j+1),
            (i-1,j  ),
            (i-1,j-1),
            (i  ,j-1),
            (i+1,j-1),
            (i+1,j  )
        ]
    return filter(in_array, r)

def print_aoc(energy):
    for i in range(10):
        for j in range(10):
            print(energy[(i,j)], end="")
        print("")

def next_step(energy):
    flash = 0
    for k in energy:
        energy[k] += 1
    while 10 in energy.values():
        for k,e in energy.items():
            if e == 10:
                for neighbour in neighbours(k):
                    if energy[neighbour] < 10:
                        energy[neighbour] += 1
                energy[k] = 11
                flash += 1
    for k in energy:
        if energy[k] == 11:
            energy[k] = 0
    return energy,flash

def p1(energy):
    flashes = 0
    for i in range(100):
        energy,f = next_step(energy)
        flashes += f
        #print("Step {}".format(i))
        #print_aoc(energy)
    return flashes

def p2(energy):
    i = 0
    flashes = 0
    while sum(energy.values()) != 0:
        energy,f = next_step(energy)
        flashes += f
        i += 1
        #print("Step {}".format(i))
        #print_aoc(energy)
    return i

if __name__ == "__main__":
    energy = dict()
    with open('input.txt', 'r') as f:
        for i,l in enumerate(f.readlines()):
            for j,e in enumerate(list(l.rstrip())):
                energy[(i,j)] = int(e)
    print_aoc(energy)
    print("part1: {}".format(p1(energy.copy())))
    print("part2: {}".format(p2(energy)))
