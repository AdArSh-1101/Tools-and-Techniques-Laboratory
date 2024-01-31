#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hello world")


# In[28]:


n = input("Enter  name: ")
a = int(input("Enter age: "))
print("Hello,", n)
print("You are", a, "years old.")


# In[29]:


# Constants
PI = 3.14
print(PI)
# single-line comment


# In[30]:


a=10
b=3
c=float(a/b)
print(c)


# In[31]:


a = 5
b = 2

add = a + b
sub = a - b
mul = a * b
div = a / b

print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Division:", div)


# In[9]:


a="Adarsh Mishra"
a=a.lower()
print(a)
a=a.upper()
print(a)
print(a.lower().isupper())
b=len(a)
print(b)
c=a[0]
print(c)
d=a.index("M")
print(d)
d=a.index("MISHRA")
print(d)
d=a.index("SHR")
print(d)
a=a.replace("MISHRA","Mishra")
print (a)


# In[12]:


x = True
y = False
a= x and y
o = x or y
n = not x
print("AND Result:", a)
print("OR Result:", o)
print("NOT Result:", n)


# In[15]:


name=["abc",2.05,False,"xyz","pqr","lmn"]
print(name[0])
print(name)
print(name[-1])
print(name[-2])
print(name[1:])
print(name[1:3])
name[0]=1234
print(name)
print("\n\n\n\nlist functions: ")
a=[2,4,1,3,7,6]
a.sort()#sorting
print(a)
a.reverse()#reverse
print(a)



# In[16]:


a = True
if a:
    print("lol")
if 2 > 9:
    print("???")
else:
    print("....")
b = False
if a or b:
    print("abcde")
elif a:
    print("/////")
else:
    print("bnm,")
if a and b:
    print("xyz")
def max_num(x, y, z):
    if x >= y and x >=z:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z
c = max_num(7, 9, 100)
print(c)


# In[33]:


a = int(input("Enter a number: "))
for i in range(1,a):
   
    print("remainder", a%i)
    

c = int(input("Enter a number: "))
while c < a:
    if(c%2==0):
        print(c)
    c+=1

