N = int(input())

# Please write your code here.
def abc(n):
    if n == 2 or n == 1 :
        return 1
    return abc(n-1) + abc(n-2)
print(abc(N))