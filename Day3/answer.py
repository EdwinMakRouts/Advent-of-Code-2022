import numpy as np
f = open("Advent of Code\Day3\input.txt", "r")

sum = 0
abcd = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in f:
    comonLetters = []
    long = len(i) - 1
    cadena1 = i[0: int(long/2)]
    cadena2 = i[int(np.ceil(long/2)): long]

    for j in cadena1:
        for z in cadena2:
            if (j == z) and (j not in comonLetters):
                comonLetters.append(z)

    for j in comonLetters:
        aux = 0
        for z in abcd:
            if z.lower() == j:
                sum += aux + 1
            elif j == z:
                sum += aux + 27
            aux+=1

print ("Answer: " + str(sum))
"""Answer: 7826"""

"""PART 2"""
f = open("Advent of Code\Day3\input.txt", "r")
comonLetters = []
sum = 0

def only_chars (cadena):
    aux = ""
    for i in cadena:
        cond = str (i)
        if cond.isalpha():
            aux += cond
    return aux

line1 = only_chars (f.readline())
line2 = only_chars (f.readline())
line3 = only_chars (f.readline())

"""There are 300 lines in input, if the groups are of 3, so 300/3 = 100"""
for i in range(100):
    for j in line1:
        if j in line2 and j in line3:
            comonLetters.append(j)
            break
    line1 = only_chars (f.readline())
    line2 = only_chars (f.readline())
    line3 = only_chars (f.readline())

for j in comonLetters:
        aux = 0
        for z in abcd:
            if z.lower() == j:
                sum += aux + 1
            elif j == z:
                sum += aux + 27
            aux+=1

print ("Answer2: " + str(sum))
"""Answer2: 2577"""
