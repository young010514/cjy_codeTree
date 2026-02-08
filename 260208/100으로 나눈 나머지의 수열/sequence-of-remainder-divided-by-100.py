N = int(input())

# Please write your code here.
result = []
def abc(level):
    global result
    if level ==N:
        return
    if level == 0:
        result.append(2)
        abc(level +1)
    elif level == 1 :
        result.append(4)
        abc(level +1)
    else:
        data = (result[level-1] * result[level-2]) % 100
        result.append(data)
        abc(level +1)
abc(0)
print(result[-1])