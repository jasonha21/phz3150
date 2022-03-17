#!/usr/bin/env python
# coding: utf-8

# In[19]:


def kepler_3rd(period):
    a1=((period**2)*(1**3)/(1**2))**(1/3)#uses the given period in earth years to calculate the distance in AU using keplers 3rd law equation
    return print("This planet's orbital distance is ",a1," AU.")

