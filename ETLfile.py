#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import required libriaries


# In[15]:


import os
import sys


# In[16]:


import pandas as pd


# In[17]:


import json
import csv


# In[ ]:


# define file paths of market 


# In[18]:


os.chdir(r"C:\Users\PC\Desktop\Assignment_5_datat_pipeline_individual\Akua-Agyare-E-Commerce-DataPipeline-Project\DATASET")


# In[ ]:


# import all data from market 1


# In[19]:


file1 = r"C:\Users\PC\Desktop\Assignment_5_datat_pipeline_individual\Akua-Agyare-E-Commerce-DataPipeline-Project\DATASET/M1_Customers1.json"


# In[20]:


customers1 = pd.read_json(file1, encoding = 'unicode_escape')


# In[21]:


customers1


# In[22]:


file2 = r"C:\Users\PC\Desktop\Assignment_5_datat_pipeline_individual\Akua-Agyare-E-Commerce-DataPipeline-Project\DATASET/M1_Orders1.csv"


# In[23]:


orders1 = pd.read_csv(file2, encoding = 'unicode_escape')


# In[24]:


orders1


# In[45]:


file3 = r"C:\Users\PC\Desktop\Assignment_5_datat_pipeline_individual\Akua-Agyare-E-Commerce-DataPipeline-Project\DATASET/M1_Deliveries1.csv"


# In[50]:


deliveries1 = pd.read_csv(file3, encoding = 'unicode_escape')


# In[51]:


file4 = r"C:\Users\PC\Desktop\Assignment_5_datat_pipeline_individual\Akua-Agyare-E-Commerce-DataPipeline-Project\DATASET/M2_Customers2.json"


# In[55]:


customers2 = pd.read_json(file4, encoding = 'unicode_escape')


# In[56]:


customers2


# In[59]:


file5 = r"C:\Users\PC\Desktop\Assignment_5_datat_pipeline_individual\Akua-Agyare-E-Commerce-DataPipeline-Project\DATASET/M2_Orders2.csv"


# In[60]:


orders2 = pd.read_csv(file5, encoding = 'unicode_escape')


# In[61]:


orders2


# In[62]:


file6 = r"C:\Users\PC\Desktop\Assignment_5_datat_pipeline_individual\Akua-Agyare-E-Commerce-DataPipeline-Project\DATASET/M2_Deliveries2.csv"


# In[63]:


deliveries2 = pd.read_csv(file6, encoding = 'unicode_escape')


# In[64]:


deliveries2


# In[ ]:


# Data pre-processing and transformation


# In[ ]:


# check for missing values where column data is empty or dash


# In[74]:


customers1.isnull().sum()


# In[73]:


orders1.isnull().sum()


# In[75]:


deliveries1.isnull().sum()


# In[47]:


deliveries1


# In[49]:


deliveries1.info()


# In[76]:


deliveries2.isnull().sum()


# In[77]:


customers2.isnull().sum()


# In[78]:


orders2.isnull().sum()


# In[ ]:





# In[81]:


def drop_empty_or_dash_columns(deliveries1):
    return deliveries1.dropna(axis=1, how='all')


# In[85]:





# In[87]:


def drop_empty_or_dash_columns(customers1):
    return customers1.dropna(axis=1, how='all')


# In[88]:


customers1


# In[ ]:


def drop_empty_or_dash_columns(customers1):
    return customers1.dropna(axis=1, how='all')

