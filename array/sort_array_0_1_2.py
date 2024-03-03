arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]

count_of_0 = 0
count_of_1 = 0
count_of_2 = 0

for i in arr:
    if i == 0:
        count_of_0 += 1
    elif i == 1:
        count_of_1 += 1
    elif i ==2:
        count_of_2 += 1
        
new_li = []

while count_of_0 > 0:
    new_li.append(0) 
    count_of_0 -= 1

while count_of_1 > 0:
    new_li.append(1) 
    count_of_1 -= 1
    
while count_of_2 > 0:
    new_li.append(2) 
    count_of_2 -= 1
    
print(new_li)
    
