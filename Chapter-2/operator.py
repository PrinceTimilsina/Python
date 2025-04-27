#Arithmetic Operator 
a= 34

b = 30

c = a+b

print (c)

#Assignment Operator
a = 4-2 #Assign 4-2 in a
b = 6
# b-= 6 
b +=3  # Increment the value od b by 3 and the assign it to b
print(b)

# Comparison Operator

d = 5!=5
f = 4==4
print(d)  # Shows False
print(f)  # Shows True

#Logical Operators

e = True or False  #if one among these is true this(or) will return true only
print(e)

#------------------Truth Table of "OR"-----------------

print("True or False is", True or False)    #true
print("True or True is",True or True)       #true 
print("False or True is",False or True)     #true
print("False or False is",False or False)   #false

#------------------Truth Table of "AND"-----------------

print("True and True is",True and True)       #true 
print("True and False is", True and False)    #true
print("False and True is",False and True)     #true
print("False and False is",False and False)   #false

print(not(True))  #changes true to false