#!/usr/bin/env python
# coding: utf-8

# 1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

# In[2]:


num = []
for i in range(2000,3200) :
    if (i%7 == 0) &(i%5 != 0) :
        num.append(i)
print(num)


# 2. Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name.

# In[2]:


fname = input("Enter your First Name:")
lname = input("Enter your Last Name:")

fullName = fname + ' ' +lname
#uname =''
print(fullName)

fullName[::-1]
#uname = uname + fullName[i]
    
#print(uname)


# 3. Write a Python program to find the volume of a sphere with diameter 12 cm.
#  Formula: V=4/3 * π * r3

# In[5]:


dia = input("Enter the diameter of the Sphere")
di = int(dia)
pi =3.1415926535897931
vol =4/3*pi* di**3
print("Volume is:",vol)

