f = open("Advent of Code\Day2\input.txt", "r")
fw = open("Advent of Code\Day2\cosas.txt", "w")

array = ['X', 'Y', 'Z']
        
for i in f:
    line = ""
    for j in i:
        if j == 'X':
            line += 'A'
        elif j == 'Y':
            line += 'B'
        elif j == 'Z':
            line += 'C'
        else:
            line += j
    fw.write(line)

f.close()
fw.close()
fr = open("Advent of Code\Day2\cosas.txt", "r")
array2 = ['A', 'B', 'C']
points = 0

for i in fr:
    playerA = i[0:1]
    playerB = i[2:3]
    if playerA == playerB:
        points += 3 + (array2.index(playerB) + 1)
    elif (playerA == 'A' and playerB == 'B') or (playerA == 'B' and playerB == 'C') or (playerA == 'C' and playerB == 'A'):
        points += 6 + (array2.index(playerB) + 1)
    else:
        points += 0 + (array2.index(playerB) + 1)
print ("Points: " + str(points))

fr.close()
f = open("Advent of Code\Day2\input.txt", "r")
fw = open("Advent of Code\Day2\cosas2.txt", "w")

for i in f:
    line = ""
    for j in i:
        if j == 'X':
            line += 'L'
        elif j == 'Y':
            line += 'D'
        elif j == 'Z':
            line += 'W'
        else:
            line += j
    fw.write(line)

f.close()
fw.close()
fr = open("Advent of Code\Day2\cosas2.txt", "r")

points = 0

for i in fr:
    playerA = i[0:1]
    playerB = i[2:3]

    if playerB == 'D':
        points += 3 + (array2.index(playerA) + 1)
    elif playerB == 'W':
        if playerA == 'A':
            points += 6 + 2
        elif playerA == 'B':
            points += 6 + 3
        else:
            points += 6 + 1
    elif playerB == 'L':
        if playerA == 'A':
            points += 0 + 3
        elif playerA == 'B':
            points += 0 + 1
        else:
            points += 0 + 2
print ("Points: " + str(points))

fr.close()

