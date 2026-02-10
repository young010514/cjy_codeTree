a,b= map(int,input().split())

def check(num):
    for x in range(2,num):
        if num % x == 0:
            return False
    return True


data = 0
for i in range(a,b+1):
    if check(i):
        data += i
print(data)