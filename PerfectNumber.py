n=int(input())
start=1
r=0
while start<n:
    if n%start==0:
        r=r+start
    start=start+1
if r==n:
    print("Perfect Number")
else:
    print("Not a Perfect Number")
        
