n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
m = arr[0]
def abc(x):
    global m
    if x == len(arr):
        return
    if m < arr[x]: m = arr[x]
    abc(x+1)
abc(0)
print(m)