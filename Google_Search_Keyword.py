#!/usr/bin/env python
# coding: utf-8

# ## Keyword Search Google [Using googlesearch module]

# In[25]:


import pandas as pd
from googlesearch import search 
def search_google(query):
    parent_=[]  
    for j in search(query, tld="co.in", num=10, stop=50, pause=2):
        child_=[]
        link_=j
        site_name=link_.split("/")[2]
        child_.append(site_name)
        child_.append(link_)
        parent_.append(child_) 
    return pd.DataFrame(parent_,columns=['Site Name','URL Link'])


# In[30]:


search_google("'java'")


# In[31]:


search_google("'python'")


# In[32]:


search_google("'what is machine learning'")


# In[ ]:




