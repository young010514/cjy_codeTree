str = input()

# Please write your code here.
result = "No"
pop_result = True
arr = []
for i in list(str):
    
    if i == "(":
        arr.append(i)
    elif i == ")":
        if arr != []:
            arr.pop()
        else: 
            pop_result =  False
            break
if arr == [] and pop_result:
    result = "Yes"
print(result)