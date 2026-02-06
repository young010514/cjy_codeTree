n = int(input())

# Please write your code here.
def print_num(n):
    num = 1
    for _ in range(n):
        for _ in range(n):
            print(num, end=' ')
            if num == 9: num =1
            else : num +=1
        print()
print_num(n)