N = int(input())

# Please write your code here.
def abc(x):
    if x == 0:
        return
    print(x,end=' ')
    abc(x-1)
    print(x,end=' ')
abc(N)