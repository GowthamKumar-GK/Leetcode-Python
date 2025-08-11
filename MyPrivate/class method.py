# class method

class college:
    collegename="nandha college of technology"

    @classmethod

    def change(cls,new):
        cls.collegename=new
print("before;",college.collegename)
college.change("nandha engineering college")
print("after:",college.collegename)
    
