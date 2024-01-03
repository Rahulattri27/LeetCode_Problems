bank=["011001","000000","010100","001000"]
prev=0
ans=0
for i in bank:
    n=i.count('1')
    if n==0:
        continue
    ans+=prev * n
    prev=n
print(ans)