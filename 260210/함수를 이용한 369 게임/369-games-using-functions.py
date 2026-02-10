a, b = map(int, input().split())

# Please write your code here.
cnt = 0


def find(num):
    if num % 3 == 0:
        return 1
    else:
        return 0


def num369(num):
    lst = list(map(int, list(str(num))))
    for x in lst:
        if x in [3, 6, 9]:
            return 1
    return 0


for i in range(a, b + 1):
    if find(i) or num369(i):
        cnt += 1
print(cnt)