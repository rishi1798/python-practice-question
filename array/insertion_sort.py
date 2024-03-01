arr = [6,4,5,8,3,2,9]
counter = 0
for i in range(1,len(arr)):
    for j in range(i,0,-1):
        if arr[j] < arr[j-1]:
            counter = arr[j-1]
            arr[j-1] = arr[j]
            arr[j] = counter
        else:
            break
print(arr)