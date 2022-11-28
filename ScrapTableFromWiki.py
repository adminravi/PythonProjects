#!/usr/bin/env python
# coding: utf-8

# # SCRAPING TABLES FROM WIKI
# This is really helpful in quickly automating your work

# **First we need to import pandas**

# In[1]:


import pandas as pd


# **Load tables in a variable with pd.read_html**
# 
# *pd.read_html* : Read HTML tables into a list of DataFrame objects.

# In[2]:


money_earned = pd.read_html('https://en.wikipedia.org/wiki/List_of_Hindi_films_of_2022')


# **Accessing table**
# 
# Since *money_earned* is a list of tables, therefore, it can be accessed by it's index.

# In[5]:


money_earned[3]


# **To Check the number of tables in a webpage**
# 
# the len function returns the number of items in the list. This list contains tables as items. so the len function will return number of tables in the webpage. As you can see, there are 17 tables in the webpage.

# In[7]:


len(money_earned)


# If you try to access the 18th table by coding money_earned[17], you will get an "IndexError" since there are only 17 tables in the webpage and [17] points to the 18th table as indexing starts from 0.

# In[8]:


money_earned[17]


# ## Accessing the last table of the webpage

# In[9]:


money_earned[16]


# # Hope it was helpful, in case you want to be in touch, here's my twitter handle @ravivermaravi

# In[ ]:




