num="222"
maximum=""
default="0"
for i in range(1,len(num)-1):
    if num[i-1]==num[i] and num[i]==num[i+1]:
        print("loop")
        maximum = (maximum) if maximum else default
        if int(maximum)<int (num[i]):
            maximum=num[i]
                
               
print(maximum*3,"mai")