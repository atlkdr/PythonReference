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
