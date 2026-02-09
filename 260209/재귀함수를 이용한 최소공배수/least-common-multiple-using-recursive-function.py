n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
result = 1
for i in arr:
    result *= i
ans = result
def abc(level):
    global result, ans
    if level == len(arr):
        return
    data = 0
    for i in arr:
        if result // arr[level] % i != 0: data =1
    if data == 0 and ans > result // arr[level]:
        ans = result//arr[level]
    abc(level+1)
abc(0)
print(ans)