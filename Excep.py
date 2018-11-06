# Exception Handling
a=int(input("Enter Divisor:"))
b=int(input("Enter DIvident:"))

try:
    print("Resource Opened")
    print(b/a)
except Exception as e:
    print("Exception : ",e)
finally:
    print("Resource Closed")
print("End_Reaced")
