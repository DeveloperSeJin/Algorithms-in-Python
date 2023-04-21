width, height = 9, 9

matrix = []
max = 0
x, y = -1, -1

for row in range(height):
    dummy = input().split()
    matrix.append(dummy)

for i in range(len(matrix)) :
    for j in range(len(matrix[i])) :
        if max <= int(matrix[i][j]) :
            max = int(matrix[i][j])
            x, y = i + 1, j + 1
            
print(max)
print(f'{x} {y}')