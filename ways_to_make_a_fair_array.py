nums=[1,1,1]
def sumoddeven(arr):
    even=0
    odd=0
    print(len(arr),"arr")
    for i in range(0,len(arr),2):
        even+=arr[i]
        print("i",i)
    for j in range(1,len(arr),2):
        odd+=arr[j]
        print("j",j)
    print(even,odd)
    if even==odd:
        return True
for i in range(len(nums)):
    arr=nums.copy()
    arr.pop(i)
    print(arr)
    if sumoddeven(arr):
        print(i)