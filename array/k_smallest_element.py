def k_smallest_element(arr,k):
    
    
    sorted_array = sorted(arr)
    print(sorted_array)
    for i in range(len(sorted_array)):
        if i==k-1:
            return sorted_array[i]
        


arr = [7,10,4,3,20,15]
k = 2
num = k_smallest_element(arr,k)
print(num)