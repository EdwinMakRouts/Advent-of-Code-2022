import numpy as np
f = open("Advent of Code\Day1\input.txt", "r")
fw = open("Advent of Code\Day1\swer.txt", "w")


sum = 0

for i in f:
    line = i
    aux = ""
    for j in line:
        if j.isdigit():
            aux+=j

    if  aux.isdigit():
        sum += int(aux)
    else:
        fw.write(str (sum) + "\n")
        sum = 0
        

f.close()
fw.close()
fr = open("Advent of Code\Day1\swer.txt", "r")

max = 0
for i in fr:
    if int(i) > max:
        max = int(i)
fr.close()

print ("The total of Calories that he is carrying is " + str(max))
""" RESULT = 70509 """

fr = open("Advent of Code\Day1\swer.txt", "r")
array = [0, 0, 0]
minimo = 0

for i in fr:
    minimo = min(array)
    if int (i) > minimo:
        indice = array.index(minimo)
        array [indice] = int(i)
fr.close

print ("The top 3: " + str(array))
totalTOP3 = array[0] + array[1] + array[2]

print ("The total of Calories that the top 3 is carrying is " + str (totalTOP3))
""" RESULT = 208567 """