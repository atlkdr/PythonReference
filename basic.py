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


