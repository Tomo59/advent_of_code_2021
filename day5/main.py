#/usr/bin/env python3

import re

def p1(segments):
    m = [0] * 1000000 # 1000 x 1000 arrays 
    for s in segments:
        (x1, y1, x2, y2) = s
        if x1 == x2:
            for y in range(abs(y1-y2)+1):
                m[x1 + 1000*(min(y1,y2) + y)] += 1
        if y1 == y2:
            for x in range(abs(x1-x2)+1):
                m[(min(x1,x2) + x) + 1000*y1] += 1
    return len(list(filter(lambda l: l >= 2, m)))

def p2(segments):
    m = [0] * 1000000 # 1000 x 1000 arrays 
    for s in segments:
        (x1, y1, x2, y2) = s
        #print(s)
        if x1 == x2:
            for y in range(abs(y1-y2)+1):
                m[x1 + 1000*(min(y1,y2) + y)] += 1
        if y1 == y2:
            for x in range(abs(x1-x2)+1):
                m[(min(x1,x2) + x) + 1000*y1] += 1
        if abs(x1-x2) == abs(y1-y2):
            if (x1-x2) * (y1-y2) > 0:
                for u in range(abs(y1-y2)+1):
                    m[min(x1,x2) +u + 1000*(min(y1,y2) + u)] += 1
                    #print("point({},{})".format(min(x1,x2) +u , min(y1,y2) + u))
            else:
                for u in range(abs(y1-y2)+1):
                    if x1 < x2:
                        m[x1 + u + 1000*(y1 - u)] += 1
                        #print("point({},{})".format(x1+u , y1-u))
                    else:
                        m[x2 + u + 1000*(y2 - u)] += 1
                        #print("point({},{})".format(x2+u , y2-u))
    return len(list(filter(lambda l: l >= 2, m)))

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        segments = [list(map(int, re.findall(r"[\d']+", l))) for l in f.readlines()]
    print("part1: {}".format(p1(segments)))
    print("part2: {}".format(p2(segments)))
