
def sortColors(self, nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    count_array=[0]*3
    for i in nums:
        count_array[i]+=1
    # for j in range(1,len(count_array)):
    #     count_array[j]=count_array[j-1]+count_array[j]
    array_index=0
    for i in range(count_array[0]):
        nums[array_index]=0
        array_index+=1
    for i in range(count_array[1]):
        nums[array_index]=1
        array_index+=1
    for i in range(count_array[2]):
        nums[array_index]=2
        array_index+=1
        
        

        


        