N = int(input())

# Please write your code here.
def abc(x):
    if x <= 0:
        return 0
    return x + abc(x-2)
print(abc(N))