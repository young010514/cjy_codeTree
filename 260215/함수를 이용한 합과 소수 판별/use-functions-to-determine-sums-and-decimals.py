a, b = map(int, input().split())

# Please write your code here.
def fun(a,b):
    cnt = 0
    for i in range(a,b+1):
        if i % 2 == 0 or i % 3 == 0 or i % 5 ==0 or i % 7 == 0: continue
        if ((i % 10) +(i // 10) )% 2 != 0 : continue
        cnt +=1
    return cnt
print(fun(a,b))