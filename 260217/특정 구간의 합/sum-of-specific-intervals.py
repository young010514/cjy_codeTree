n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
for i in range(m):
    a,b= queries[i]
    result = 0
    for j in range(a-1,b):
        result += arr[j]
    print(result)