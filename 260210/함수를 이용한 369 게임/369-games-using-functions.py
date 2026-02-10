a, b = map(int, input().split())

# Please write your code here.
cnt =0
def find(num):
    
    if num % 3 ==0 :
        return 1
    else : return 0
def num369(num):
    if num % 10 in [3,6,9]:
        return 1
    elif num //10 in [3,6,9]:
        return 1
    else:return 0
    
for i in range(a,b+1):
    if find(i) or num369(i):
        cnt += 1
print(cnt)