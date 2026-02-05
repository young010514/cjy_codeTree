str = input()

# Please write your code here.
result = "No"
arr = []
for i in list(str):
    
    if i == "(":
        arr.append(i)
    else:
        arr.pop()
if arr == []:
    result = "Yes"
print(result)