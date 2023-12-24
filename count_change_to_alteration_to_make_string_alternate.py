class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        count0=0
        count1=0
        for i,char in enumerate(s):
            if i%2==0:
                if char=="1":
                    count0+=1
                else:
                    count1+=1
            else:
                if char=="1":
                    count1+=1
                else:
                    count0+=1
        return min(count0,count1)
            


