#static method

class college:
    collegename="nct"

    @classmethod

    def change(cls,new):
        cls.collegename=new

    @staticmethod

    def collegeinfo():
        return "good college"
    
print("about:",college.collegeinfo())
print("before:",college.collegename)

college.change("NEC")

print("about:",college.collegeinfo())
print("before:",college.collegename)
