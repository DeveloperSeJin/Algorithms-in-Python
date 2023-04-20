n, m = input().split()

matrix1 = [[0 for col in range(int(m))] for row in range(int(n))]

matrix2 = [[0 for col in range(int(m))] for row in range(int(n))]

for i in range(int(n)) :
    dummy = input().split()
    
    matrix1[i] = list(map(int, dummy))

for i in range(int(n)) :
    dummy = input().split()
    
    matrix2[i] = list(map(int, dummy))
    
for i in range(len(matrix1)) :
    for j in range(len(matrix1[i])) :
        print(matrix1[i][j] + matrix2[i][j], end = ' ')
    print()