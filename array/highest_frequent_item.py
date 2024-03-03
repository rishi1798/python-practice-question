arr = [1,1,2,3,5,1,2,3,2,3,1,1,1,4,5,5]
d ={}
for i in arr:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

print(d)
sorted_dict = sorted(d.items(),key=lambda x:x[1])
print("highest frequent item in array is:",sorted_dict[-1][0],"appears",sorted_dict[-1][1],"times in array")
        
