class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        a=2
        b=3
        if n==2:
            return a
        if n==3:
            return b
        for i in range(4,n+1):
            c=a+b
            a=b
            b=c
        return b
        