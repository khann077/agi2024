#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tarfile
from six.moves import urllib
from scipy import stats 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime


# In[3]:


DOCUMENT_PATH = "/Users/ekalitsi/PregrantWomenNeedTimeOff"
DOCUMENT_PATH2 = "/Users/ekalitsi/PregrantWomenNeedTimeOff"


# In[4]:


import os 
import pandas as pd 
def load_data(employee  = DOCUMENT_PATH):
    csv_path = os.path.join(employee, "Data.csv")
    return pd.read_csv(csv_path)

df = load_data()
display(df)


# In[5]:


df_cleaned = df[
    ~df['api_job_gender'].isin([-1]) &
    (df['year_of_passing_to'] != "NULL") &
    (df['year_of_passing_from'] != "NULL") &
    (df['hq_marks_cgpa_from'] != "NULL") &
    (df['hq_marks_cgpa_to'] != "NULL")
   
]
df_cleaned.dtypes

# Removed -1 in Prefference in Gender
# year_of_passing_to & year_of_passing_from: earlist year companies accept applicants 
# hq_marks_cgpa_from: removed NULL in job characteristic; preferred max percentage score of the applicant

# remove na
# remove invalid fields
# remove...

# save out cleaned data


# In[7]:


len(df_cleaned)


# In[ ]:




