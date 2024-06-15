height = [4,2,0,3,2,5]
n = len(height)
left_max = [0] * n  
right_max = [0] * n 
 

max_height = 0
for i in range(n):
    left_max[i] = max_height
    max_height = max(max_height, height[i])
    #find the max for the each point of the list from the left
    

max_height = 0
for i in range(n - 1, -1, -1):
    right_max[i] = max_height
    max_height = max(max_height, height[i])
    #find the max for the each point of the list from the right