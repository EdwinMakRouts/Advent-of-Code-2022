f = open("Advent of Code\Day4\input.txt", "r")

def takeN1 (cosas):
    aux = ""
    for i in cosas:
        if i == "-":
            break
        else:
            aux+=i
    return aux

def takeN2 (cosas):
    aux = ""
    count = 0
    for i in cosas:
        if i == "-":
            count+=1
        elif count == 1:
            aux+=i
    return aux

total = 0
totalOverlap = 0
for i in f:
    part1 = ""
    part2 = ""
    
    for j in i:
        if j == ",":
            part2 = part1
            part1 = ""
        else:
            part1 += j
    
    p1n1 = int(takeN1(part1))
    p1n2 = int(takeN2(part1))
    p2n1 = int(takeN1(part2))
    p2n2 = int(takeN2(part2))

    if (p1n1 <= p2n1 and p1n2 >= p2n2) or (p2n1 <= p1n1 and p2n2 >= p1n2):
        total += 1
    """p1n1 contenido entre p2n1 y p2n2 || p2n1 contenido entre p1n1 y p1n2"""
    if (p1n1 >= p2n1 and p1n1 <= p2n2) or (p1n1 <= p2n1 and p1n2 >= p2n1):
        totalOverlap += 1 

print ("Answer: " + str(total))
"""Answer: 431"""
print ("Answer2: " + str(totalOverlap))
"""Answer: 823"""
