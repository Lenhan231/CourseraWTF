handle = open("dayso.txt","r")
data = handle.readlines()
matrix = [[]]
for line in data:
    matrix[line[1]][line[2]].append(1)
    matrix[line[2]][line[1]].append(1)