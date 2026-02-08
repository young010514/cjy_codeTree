N = int(input())

# Please write your code here.
result = [0]
def abc(level):
    global result
    if level == N+1:
        print(result[-1])
        return 
    if level ==1:
        result.append(1)
        abc(level+1)
    elif level ==2:
        result.append(2)
        abc(level+1)
    else:
        data = result[level//3] + result[-1]
        result.append(data)
        abc(level+1)
abc(1)