#Constructor Method


class college:
    collegename="nandha engineering college"
    location="erode"
    def __init__(self,dept,fees):
        self.Department=dept
        self.Fees=fees
student1=college("IT",100000)
student2=college("AIDS",125000)
student3=college("CSE",90000)
print(student1.Department)
print(student2.Department)
print(student3.Fees)

