nums=[1,2,3,1,2,3]
k=2
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d={}
        for i in range(len(nums)):

            if nums[i] in d and abs(d[nums[i]]-i)<=k:
                return True
                break
            else:
                d[nums[i]]=i
        return False
