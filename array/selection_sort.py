arr = [10,2,8,3,1,4]
counter = 0
for i in range(0,len(arr)):
    index = i
    for j in range(i+1,len(arr)):
        if arr[j] < arr[index]:
            index = j
    counter = arr[index]
    arr[index] = arr[i]
    arr[i] = counter
print(arr)
    