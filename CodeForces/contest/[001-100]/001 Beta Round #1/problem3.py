x_coords = []
y_coords = []

for case in range(3):
    arr = map(float, raw_input().split())
    x_coords.append(arr[0])
    y_coords.append(arr[1])
    
   
def euclidean(x1,x2,y1,y2):
    return pow((pow((x1-x2),2) + pow((y1-y2),2)),0.5)
 
length = []
length.append(euclidean(x_coords[0],x_coords[1],y_coords[0],y_coords[1]))
length.append(euclidean(x_coords[0],x_coords[2],y_coords[0],y_coords[2]))
length.append(euclidean(x_coords[2],x_coords[1],y_coords[2],y_coords[1]))

            
fin  = sorted(length)
result = fin[0]*fin[1]
print(result)
        