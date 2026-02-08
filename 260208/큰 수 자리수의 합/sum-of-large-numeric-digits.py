a, b, c = map(int, input().split())

# Please write your code here.
def abc(level, result, data):    
    if not data:
        print(result)
        return 
    abc(level +1, result + data%10, data // 10)
abc(0,0,a*b*c)