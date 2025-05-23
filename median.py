num1=list(map(int, input("Enter numbers separated by space: ").split()))
num2=list(map(int, input("Enter numbers separated by space: ").split()))
s=num1+num2
print(s)
if len(s)%2==0:
    r=len(s)//2
    print(s[r]+s[r-1])

else:
    r=len(s)//2
    print(s[r])
