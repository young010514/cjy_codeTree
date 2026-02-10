a, b = map(int, input().split())

# Please write your code here.
cnt =0
def find(num):
    global cnt
    if num % 3 ==0 :
        cnt +=1
    elif num // 10 != 0 and (num //10) % 3 ==0:
        cnt += 1
    elif  num % 3 !=0  and (num % 10 ) % 3 == 0:
        cnt += 1
for i in range(a,b+1):
    find(i)
print(cnt)