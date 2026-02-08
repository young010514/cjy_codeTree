n = int(input())

# Please write your code here.
cnt = 0
def abc(num):
    if num == 1:
        return
    global cnt
    cnt += 1
    abc(num//2) if num % 2 ==0 else abc(num * 3 +1)
abc(n)
print(cnt)