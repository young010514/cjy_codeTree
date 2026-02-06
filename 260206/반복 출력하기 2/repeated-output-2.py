n = int(input())

# Please write your code here.
def print_st(n):
    if n == 0 :
        return
    print("HelloWorld")
    print_st(n-1)
print_st(n)