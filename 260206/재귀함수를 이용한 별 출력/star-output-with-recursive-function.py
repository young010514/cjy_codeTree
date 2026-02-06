n = int(input())

# Please write your code here.
def main(x):
    if x >n:
        return
    print("*" * x)
    main(x+1)
main(1)