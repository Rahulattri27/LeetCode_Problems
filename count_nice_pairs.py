#Method 1
nums=[13,10,35,24,76]
def rev(x):
    x=str(x)[::-1]
    return int(x)

def countNicePair(nums):
    count=0
    
    for i in range(len(nums)):
        print(nums[i])
        for j in range(i+1,len(nums)):
            print("j",nums[j])
            if nums[i]+rev(nums[j]) == rev(nums[i])+nums[j]:
                count+=1
                print(nums[i],nums[j])
    return count
print(countNicePair(nums))

#Method 2
import collections


ans=0
counter=collections.Counter()
for num in nums:
    num-=int(str(num)[::-1])
    print(num)
    
    ans+=counter[num]
    counter[num]+=1
    print("countr",counter[num])
    print("ans",ans)
