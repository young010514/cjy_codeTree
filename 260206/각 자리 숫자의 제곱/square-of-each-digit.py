N = int(input())

# Please write your code here.
def abc(x):
    if x == 0:
        return 0
    
    return (x % 10) **2 + abc(x//10)
print(abc(N))