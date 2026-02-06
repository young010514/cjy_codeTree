N = int(input())

# Please write your code here.
def main(x):
    if x == 1:
        return 1
    return x * main(x-1)
print(main(N))