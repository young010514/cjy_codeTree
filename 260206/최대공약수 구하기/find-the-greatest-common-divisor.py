n, m = map(int, input().split())

# Please write your code here.
result = 1
def main(n,m):
    for i in range(1, abs(n-m)+1):
        if n%i == 0 and m % i == 0 : result = i
    return result
print(main(n,m))