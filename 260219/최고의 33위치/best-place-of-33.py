n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
result = 0
for i in range(n-2):
    for j in range(n-2):
        data =0
        for x in range(3):
            for y in range(3):
                data+= grid[i+x][j+y]
        result = max(result,data)
print(result)