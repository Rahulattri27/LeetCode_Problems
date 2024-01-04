import collections
nums=[2,3,3,2,2,4,2,3,4]
dic=collections.defaultdict(int)
for i in nums:
    dic[i]+=1
ans=0
for i in dic.values():
    if i==1:
        print(-1) 
    ans+=i//3
    if i%3:
        ans+=1
print(ans)
            