"""#constructor Method
class College:
    CollegeName="Nandha Engineering college"
    Location="Erode"
    def __init__(self,department,fees):
        self.Department=department
        self.Fees=fees
Student1=College('Information Technology',70000)
Student2=College('CSE',90000)
Student3=College('AI-DS',97000)
print(Student1.Department)"""

"""#Object Method
class Student:
    def __init__(self, name,department):
        self.name = name
        self.department = department

    # Object method to display student details
    def display (self):
        print(self.name)
        print(self.department)
# Creating objects of the Student class
student1 = Student("GK","Information Technology")
student2 = Student("Santa", "CSE")

# Calling object methods to display student details
student1.display()

student2.display()
"""


"""#class method
class College:
    CollegeName = "Nandha Engineering College"  

    @classmethod
    def change_college_name(cls, new_name):
        cls.CollegeName = new_name 

# Printing before changing the name
print("Before:", College.CollegeName)

# Calling the class method to change the name
College.change_college_name("Nandha College of Technology")

# Printing after changing the name
print("After:", College.CollegeName)
"""




#static method
class College:
    CollegeName = "Nandha Engineering College"   

    @classmethod
    def change_college_name(cls, new_name):
        cls.CollegeName = new_name

    @staticmethod
    def college_info():
        return "Colleges provide education for students in various fields."  # Static Method

# Calling and displaying static method output
print("Info:", College.college_info())

# Printing before changing the college name
print("Before:", College.CollegeName)

# Changing the college name using class method
College.change_college_name("ABC Engineering College")

# Printing after changing the college name
print("After:", College.CollegeName)































