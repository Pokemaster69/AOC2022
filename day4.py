import sys
import re
data=[]
for line in sys.stdin:
    temp = re.split(r'[,-]', line)
    data.append([int(x) for x in temp])

def between(test, low, high):
    return test in range(low,high+1)

def part1():
    count=0
    for ass in data:
        if (ass[0]>=ass[2] and ass[1]<=ass[3]) or (ass[0]<= ass[2] and ass[1]>=ass[3]):
            count+=1
    return count

def part2():
    count=0
    for ass in data:
        if between(ass[0], ass[2],ass[3]) or between(ass[1],ass[2],ass[3]) or between(ass[2],ass[0],ass[1]) or between(ass[3],ass[0],ass[1]):
            count+=1
    return count

print("Part1: ", part1(), "Part2: ", part2())