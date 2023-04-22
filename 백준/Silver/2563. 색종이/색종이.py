width, height = 100, 100
colored_paper_width, colored_paper_height = 10, 10

matrix = [[0] * width for _ in range(height)]

loop = int(input())

for i in range(loop) :
    x, y = map(int, input().split())
    for j in range(colored_paper_width) :
        for k in range(colored_paper_height) :
            matrix[x + j][(height - colored_paper_height - 1)  - y + k] = 1


count = 0
for m in matrix :
    for n in m :
        if n == 1 :
            count += 1
print(count)