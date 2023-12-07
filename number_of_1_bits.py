class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        
        while n:
            count+=n&1
            n>>=1
        return count

n=0o11111111111111111111111111111101
s=Solution()
print(s.hammingWeight(n))
