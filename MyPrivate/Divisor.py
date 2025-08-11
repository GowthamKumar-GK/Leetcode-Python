n=int(input())

for i in range(n):
    num = int(input())
    start=2
    s=[]
    while start<num:
        if num%start==0:
            s=s+[start]
        start=start+1
    print(s)
            
