#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import pickle
import re

df = pd.read_csv('./upload/행정구역분류_행정동법정동매핑.csv', sep=',')
df = df[df['시도'] == '서울특별시']


# In[14]:


df = df.loc[:, ['시군구', '법정동코드']]


# In[15]:


index = df['시군구'].drop_duplicates(keep='first').index.tolist()


# In[16]:


df = df.iloc[index, :].drop(0)


# In[17]:


df


# In[18]:


code = df.법정동코드.values.tolist()
add = df.시군구.values.tolist()
raw_goomap = {code[i]:add[i] for i in range(len(code))}


# In[20]:


len(raw_goomap)


# In[21]:


# raw_dongmap 저장
import pickle

with open('raw_goomap_final.pickle','wb') as fw:
    pickle.dump(raw_goomap, fw)

