
# check if length of majority element is greater than lenght of array
# time complexity is 0(n log n) becz majority has time complexity of 0(n log n) compared to loop o(n)


def isMajority(arr):
    arr.sort() # this has time complexity of o(n log n)
    li =[]
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            li.append(arr[i])
            if len(li) > len(arr)/2:
                return True
        if i == len(arr)-2 and arr[i] == arr[i-1]:
            li.append(arr[i])
            if len(li) > len(arr)/2:
                return True
    return False
    

arr = [1, 2, 3, 3, 3, 10]
value = isMajority(arr)
print(value)