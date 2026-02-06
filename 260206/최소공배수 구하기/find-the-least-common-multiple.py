n, m = map(int, input().split())

# Please write your code here.
def find_max(n,m):
    num = 1
    if n == m: 
        num = n
        return num
    for i in range(1,abs(n-m) +1):
        if n % i == 0 and m % i == 0 : num = i
    return num

num = find_max(n,m)
print(n*m//num)