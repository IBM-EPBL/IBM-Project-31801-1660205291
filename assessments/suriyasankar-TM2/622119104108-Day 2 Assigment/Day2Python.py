#Python

#datatypes

#numeric --> int float, complex , boolean
print('#Numeric Datatype\n')
print(type(1))
print(type(1.45))
print(type(True))

#sequence --> list ,tuple,string
print('\n#Sequence Datatype\n')
print(type([1,2,3,4]))
print(type((1,2,3,4,5)))
print(type("IBM"))

#Operators -->
"""
Arithmetic operators -- +,-,*,/,%
Assignment Operators -- ==
Comparison operators -- <,>,<=,>=,=
Logical operators -- and , or ,not
Identity operators -- is ,is not
Membership operators -- in,not in
Bitwise operators -- & , | , ~ , ^ , >> , <<
"""
print('\n#Operators\n')

print("Arithmetic Operator :",2+3)
print("Comparison Operator :",2<3)
print("logical Operator :",True and True)
print("Bitwise Operator :",2&3)


#Slicing
print('\n#Slicing\n')
a=[1,2,3,4,5,6]
b="job recommentation"

print(a[0:3])
print(b[0:3])


# Conditional Statements
"""
If
elif
Nested If
"""
print('\n#Conditional Statement\n')
a=20
b=10
if a>b:
    print(a)
else:
    print(b)

# Conditional Statements
"""
For
While
"""
print('\n#Looping Statement\n')
print('\n#For Loop\n')
st="Tamil"
for i in st:
    print(i)
print('\n#while Loop\n')

i = 1
while i < 6:
  print(i)
  i += 1
