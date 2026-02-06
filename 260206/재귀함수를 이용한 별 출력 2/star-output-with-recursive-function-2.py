n = int(input())

# Please write your code here.
def abc(x):
    if x == 0:
        return
    print("* " * x)
    abc(x-1)
    print("* " * x)
abc(n)