# Procedial Oriented as well as Object Oriented Programming Possible 

print(5//2)
print(5%2)
print("Command's are \"Good\"")

# Ouput of previous Operation = _
string="MYSTRING"
print(string[-1]) # G

# string[i]=' '  NOT POSSIBLE else string = string[0:i-1] + ' ' string[i+1:]

# list.append(val) = list.insert(len(list)-1,val)

# list.remove(val) == val removed
# list.pop(index_of_pop) // OR last element is poped
# del list[:1] delete's without returning 

# tuple = ()  == Can't change values 
# set = {} == Collections of Unique Elements 
# NOTE : SEQUENCE NOT FOLLOWED ? = HASIHING IS FOLLOWED

# Variable just point to 21 Which is treated as an Object in Python

variable = 21 
a=variable
b=21
print(id(21))
print(id(variable))
print(id(a))
print(id(b))

# In python We Show the Intention of Constant With Capital

# data type's
# 1) none = NULL
# 2) numberic = INT,FLOAT,COMPLEX,BOOL
com=21+32j # complex(a,b)=com

# 3) Sequence =  range(from,till(Not Achieved),jump)

# Mapping / Dictionary = (key,value)
# Hence key = Set 

# ===============OPERATORS ===========================

# +=  valid
 
# Number System
# Binary = bin(21) 0b starting
# 0b101 = 5  Octal = o Heximal = x

# BITWISE OPERATOR
# ~ = Compliment 
# and = & , or = | 
# xor = ^

# Left Shift by 2 =>  21 << 2

# Divide or multiply fast with powers of 2 

# Concept of alias import math as m
import math
# Or from math import sqrt,pow use as pow(3,2)

pow_3=math.pow(3,2)
print(pow_3)
x=input("Please Enter Input: ") # Always is str format
# Conversion int(x)
print(eval(input("An Expression: ")))

import sys 

string = print(sys.argv[0])
import array as arr

val=arr.array('i',[1,2,3,4])
print(val.buffer_info()) # Address, No of elements
print(val[0])
# () Calls hence str object is not callable
new_arr=arr.array(val.typecode,(x for x in val))
print(new_arr)

from numpy import *

ar=array([1,2,34],int) # optional type
print(ar)
li=linspace(1,20,200) # 200 Parts Distributed
ar=arange(1,20,1) # Jump by 1
print(concatenate([ar,ar])); # Join Array

# Array Copy
car=ar.view()
las=ar.copy() # Gives Deep Copy
car[0]=-111
# Eveb After changing to different memory location using .view() Variable get chaned : Shallow copy
# For HARD COPY : ar.copy()
print(car[0],ar[0],las[0])
print(id(car),id(ar),id(las))

muldim=array([
    [1,2,3,21,21,21],
    [4,5,6,32,32,32]
])
threedim=muldim.reshape(2,2,3)
print(threedim[0][1][0]) # Arrays of 2*3 in number = 2

mat=matrix(muldim) # or 1  2 ; 2 21

# Pass by value / Reference
def func(x,default_val=21):
    x[0]=21212212
    print(default_val)

# Initially they have the same id (Address) but on change their Address changes

func(x=ar,default_val=121) # Gets updated when list is passed
print(ar[0])

def add(*var_arg):
    sum=0
    for i in var_arg:
        sum+=i
    print("Sum is:",sum)

add(1,2,3,2121,212,1212,11111,1111)

def data(**dictionary):
    for k,val in dictionary.items():
        print("Key=",k," Value=",val)

data(name="Don",birthplace="Orissa")

aas=212

def scope():
    globals()['aas']=-541 # Preereable than global aas as we Won't be able to have local aas
    #print(x) # Local Scope Preference

scope()
print(aas)

print("Printing list:{} HOW?".format(ar))

# One line recursion limit = sys.getrecursionlimit() => sys.setrecrsionlimit()

def my_fac(x):
    if x==1:
        return x
    else:
        return x*my_fac(x-1)

print(my_fac(3))

# Lambda Function
f=lambda x,y:x*y
print(f(2,4))
f2=lambda x:x%2==0

lx=[1,2,3,4,6,7]
evens=list(filter(f2,lx))
new_lx=list(map(lambda x:x+10,evens))
print(new_lx)


def only_when_this_moudule():
    print("Main Module Of Execution => CHanges if it is imported somewhere else")

if(__name__=="__main__"):
    only_when_this_moudule()

# Python Supports :
# Object Oriented Programming:
# Proceidal Oriented Programming: Broken into FUnctions and Modules
# Functional Programming: Functions as Parametes eg:- lambda expression

class Computer:
    maker="Charles"
    def __init__(self,cpu,ram):
        self.cpu=cpu # Instance Variable
        self.ram=ram
    def config(self):
        print("Config RAM:",self.ram," CPU:",self.cpu)
    def ram_com(self,*list_o):
        for i in list_o:
            if self.ram!=i.ram:
                return False
        return True

    @classmethod
    def maker_name(cls):
        print("Maker is : ",cls.maker)

    @staticmethod
    def static_met():
        print("This is A static Methord")
# Like Class Loader and Heap in java The memory consumed in heap by a Object is dependent on
# the number of varialbes and size of each variable in the class
# which is calculated by the constructor
comp1=Computer("i7","2GB")
comp2=Computer("i5","2GB")
comp3=Computer("i3","2GB")
Computer.maker="Baggage"
print("RAMS ARE SAME :",comp1.ram_com(comp2,comp3))
Computer.maker_name()
Computer.static_met()


class Student:
    def __init__(self,name):
        self.name=name
        self.test=[]
    def update_test(self,subject,marks):
        (self.test).append(Student.Exam(subject,marks))

    def print_result(self):
        print("Student Name:",self.name)
        for i in self.test:
            print("Subject:",i.subject," Marks:",i.marks)
    class Exam:
        def __init__(self,subject,marks):
            self.marks=marks
            self.subject=subject

s1=Student("Carles")
s1.update_test("Maths",90)
s1.update_test("English",96)
s1.update_test("Biology",86)
s1.print_result()


# Python has Multiple and Multilevel inheritance
class A:
    def __init__(self,val):
        print("Now Superclass is called")
    def tech1(self):
        print("Tech1")
class B(A):

    def __init__(self,val):
        print("First This is called")
        super().__init__(val)

    def tech2(self):
        print("Tech2")

class C:
    def tech3(self):
        print("Tech3")

# FOLLOWS MRO IE: Priority to Function calls and __init__ is given to left one

class D(C,A):
    pass

b=B(21)
b.tech1()

