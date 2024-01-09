class Solution:
    def reverseBits(self, n: int) -> int:
        rev=""
        while n:
            val=n&1
            rev+=str(val)
            n=n>>1
        for _ in range(32-len(rev)):
            rev += '0'
        c = 0
        n = 0
        while rev:
            n+= int(rev[-1])*(2**c)
            rev = rev[:-1]
            c += 1
        return n
            
        
            
        