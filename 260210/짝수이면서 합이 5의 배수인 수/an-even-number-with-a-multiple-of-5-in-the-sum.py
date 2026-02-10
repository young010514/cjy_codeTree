n = int(input())

# Please write your code here.
def yesorno(num):
    if num % 2 ==0 and (num%10 + num //10) % 5 ==0 :
        print("Yes")
    else: print("No")
yesorno(n)