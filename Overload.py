
# OPERATOR OVERLOADING
x=21
print(x.__or__(2))
print(x|2)

class Student:
    def __init__(self,*marks):
        self.marks=0
        for i in marks:
            self.marks+=i
    def __add__(self,*objects):
        self.total=self.marks
        for i in objects:
            self.total+=i.marks
        return Student(self.total)
    def __gt__(self,other):
        return self.marks>other.marks
    # Changes The default Mthord Of prinintg 
    def __str__(self):
        return ("Student Scored:"+str(self.marks))

s1=Student(90,90,90)
s2=Student(90,80,90)
s3=s1+s2
if s3>s1:
    print("S3 has more marks than s1 which is:",s3.marks)
print(s2)
