str = input()

# Please write your code here.
result = "No"
arr = []
for i in list(str):
    
    if i == "(":
        arr.append(i)
    elif i == ")":
        if arr:
            arr.pop()
        else: break
if arr == []:
    result = "Yes"
print(result)