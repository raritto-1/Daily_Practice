arr = [2, 2, 2, 2, 5, 5, 5, 8]
k = 3
threshold = 4
new_arr = []
l = 0 
for r in range(len(arr) - k + 1):  
    data = sum(arr[r:r+k])  
    if data >= threshold:
        new_arr.append(data)
print(new_arr)