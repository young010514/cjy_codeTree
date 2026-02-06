n = int(input())

# Please write your code here.
def num(x):
    if x > n:
        print()
        return
    print(x,end=' ')
    num(x+1) 
    print(x,end=' ')
num(1)