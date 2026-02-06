N = int(input())

# Please write your code here.
def abc(x):
    if x ==0 :
        return 0
    return abc(x-1) + x
print(abc(N))