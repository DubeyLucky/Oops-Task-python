#!/usr/bin/env python
# coding: utf-8

# Q1, Create a vehicle class with an init method having instance variables as name_of_vehicle, max_speed
# and average_of_vehicle.

# In[9]:


class vehicle:
    
    def __init__ (self, name_ve,max_speed,avg_speed):  #by init method we can inserting the data
        self.name_ve = name_ve
        self.max_speed = max_speed
        self.avg_speed = avg_speed   
        
    def giv(self):  #returning function
        return self.name_ve, self.max_speed,self.avg_speed
    
    
Tata = vehicle("Tata Nexon",240,120)
Jeep = vehicle("Jeep Compass",240,120)
    


# In[10]:


Tata.giv()


# In[11]:


Tata.name_ve


# In[12]:


Tata.max_speed


# In[13]:


Tata.avg_speed


# In[15]:


Jeep.giv()


# In[16]:


Jeep.name_ve


# In[17]:


Jeep.max_speed


# In[18]:


Jeep.avg_speed


# Q2. Create a child class car from the vehicle class created in Que 1, which will inherit the vehicle class.
# Create a method named seating_capacity which takes capacity as an argument and returns the name of
# the vehicle and its seating capacity.

# In[46]:


class car(vehicle):
    
    def seating_capacity(self):
        return "Tata = 8 Jeep =8"


# In[47]:


Tata = car("Tata Nexon",240,120)
Jeep = car("Jeep Compass",240,120)


# In[48]:


Tata.giv()


# In[49]:


Tata.seating_capacity()


# Q3. What is multiple inheritance? Write a python code to demonstrate multiple inheritance.

# In[50]:


class A:
    def a(self):
        print("Hi,a")
    
class B:
    def b(self):
        print("Hi,b")
        
class C(A,B):
    pass

obj = C()


# In[54]:


obj.a()


# In[55]:


obj.b()


# In[56]:


obj


# Q4. What are getter and setter in python? Create a class and create a getter and a setter method in this
# class.

# Getters and setters in Python are different from those in other OOPs languages. The primary use of getters and setters is to ensure data encapsulation in object-oriented programs. In contrast to other object-oriented languages, private variables in Python are not hidden fields.

# In[58]:


class ATM:
    def __init__(self, pin,balance):
        self.__pin = pin
        self.__balance = balance
    
    def Check_Balance(self) :
        return self.__balance
    
    def Witdraw(self,amount):
        if self.__balance >= amount:
            self.__balance = self.__balance - amount
            return True
        else:
            return Flase
            
    def Deposit(self,amount):
        self.__balance = self.__balance + amount
        
        


# Q5.What is method overriding in python? Write a python code to demonstrate method overriding.

# In[ ]:




