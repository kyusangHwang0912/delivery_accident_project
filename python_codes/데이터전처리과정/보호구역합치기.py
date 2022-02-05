#!/usr/bin/env python
# coding: utf-8

# In[118]:


import pandas as pd

df = pd.read_csv('./upload/ChildGyeonggi00.csv')


# In[119]:


df.dropna(inplace=True)


# In[120]:


df.법정동 = df.법정동.apply(lambda x : int(x))


# In[121]:


import math
def trunc_10(x):
    return math.trunc(x/100)*100


# In[122]:


df['법정동'] = df['법정동'].apply(lambda x : trunc_10(x))


# In[123]:


child_gyeonggi = df.groupby('법정동')[['index']].sum()


# In[124]:


child_gyeonggi = child_gyeonggi.iloc[1:]


# In[125]:


child_gyeonggi


# In[126]:


child_seoul = pd.read_csv('./upload/ChildSeoul00.csv')
child_seoul.head()


# In[127]:


elder_seoul = pd.read_csv('./upload/ElderSeoul00.csv')
elder_gyenggi = pd.read_csv('./upload/ElderGyeonggi00.csv')


# In[128]:


child_seoul.dropna(inplace=True)
elder_seoul.dropna(inplace=True)
elder_gyenggi.dropna(inplace=True)


# In[129]:


child_seoul['법정동'] = child_seoul['법정동'].apply(lambda x : int(x))
elder_gyenggi['법정동'] = elder_gyenggi['법정동'].apply(lambda x : int(x))
elder_seoul['법정동'] = elder_seoul['법정동'].apply(lambda x : int(x))


# In[130]:


child_seoul['법정동'] = child_seoul['법정동'].apply(lambda x : trunc_10(x))
elder_gyenggi['법정동'] = elder_gyenggi['법정동'].apply(lambda x : trunc_10(x))
elder_seoul['법정동'] = elder_seoul['법정동'].apply(lambda x : trunc_10(x))


# In[ ]:





# In[132]:


child_seoul = child_seoul.groupby('법정동')[['index']].sum()
elder_gyenggi = elder_gyenggi.groupby('법정동')[['index']].sum()
elder_seoul = elder_seoul.groupby('법정동')[['index']].sum()


# In[134]:


child_seoul


# In[ ]:





# In[135]:


seoul = pd.merge(child_seoul, elder_seoul, on='법정동', how='outer')


# In[136]:


seoul.fillna(0,inplace=True)


# In[137]:


seoul = seoul.sum(axis=1).to_frame()


# In[138]:


gyeonggi = pd.merge(child_gyeonggi, elder_gyenggi, on='법정동', how='outer')


# In[139]:


gyeonggi.fillna(0,inplace=True)
gyeonggi = gyeonggi.sum(axis=1).to_frame()


# In[140]:


seoul.to_csv('./서울보호구역.csv',sep=',')


# In[141]:


gyeonggi.to_csv('./경기보호구역.csv',sep=',')


# In[ ]:




