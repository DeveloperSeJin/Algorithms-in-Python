loop = 5
max = 15

matrix = []

for i in range(loop) :
    dummy = list(input())
    matrix.append(dummy)

for i in range(max) :
    for j in range(max) :
        try :
            print(matrix[j][i], end = '')
        except :
            print(end = '')