#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[5]:


randomnum=random.randint(1,100)
print(randomnum)
a=int(input("make a guess:"))
if a==randomnum:
    print("perfect guess!")
elif a>randomnum:
        print("guess a lower number")
elif a<randomnum:
    print("guess a upper number")
    
    


# In[ ]:




