N = int(input())

# Please write your code here.
def abc(x):
    if x == 1 :
        return 0
    if x % 2 ==0 :
        x //= 2
    else : x //= 3
    return 1 + abc(x)
print(abc(N))