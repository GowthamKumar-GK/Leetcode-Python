Target=10
arr=[1,2,3,4,5,6]
l=0
h=0
r=len(arr)-1
while (l<r):
    sum1=arr[l]+arr[r]
    if sum1==Target:
        h=1
        
        break
    elif sum1<Target:
        l=l+1
    elif sum1>Target:
        r=r-1
if h==0:
    print("No Combinations")
else:
   print(l,r)
   print(arr[l],arr[r])
