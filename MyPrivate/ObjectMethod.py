
#Object Method

class student:
    def __init__(self,name,dept):
        self.Name=name
        self.Department=dept
    def display(self):
        print(self.Name)
        print(self.Department)

student1=student("GK","CS")
student2=student("Santa","Arts")

student1.display()
student2.display()

