matrix=[[1,2,3,20,4],[5,6,7,30,8],[9,10,11,40,12]]
row=len(matrix)
column=len(matrix[0])
left,top=0,0
right=column
bottom=row
ls=[]
while(left<right and top<bottom):
    for i in range(left,right):
        ls.append(matrix[top][i])
        print(matrix[top][i],"first")
    top+=1
    for i in range(top,bottom):
        ls.append(matrix[i][right-1])
        print(matrix[i][right-1],"sec")
    right-=1
    print(left,right,top,bottom)
    if not (left<right and top<bottom):
        break
    for i in range(right-1,left-1,-1):
        ls.append(matrix[bottom-1][i])
        print(matrix[bottom-1][i],"third")
    bottom-=1
    for i in range(bottom-1,top-1,-1):
        ls.append(matrix[i][left])
        print(matrix[i][left],"four")
    left+=1
print(ls)
