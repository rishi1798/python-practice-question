def max_and_min(arr):
    sorted_array = sorted(arr)
    return sorted_array[0],sorted_array[-1]

arr = [1, 423, 6, 46, 34, 23, 13, 53, 4 ]
min,max = max_and_min(arr)
print("minimum element is:",min,"maximum is:",max)