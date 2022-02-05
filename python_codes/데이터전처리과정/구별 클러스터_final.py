#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
df = pd.read_excel('./upload/1820SeoulGuAccidentDeadHurtBadHurt.xlsx',header=1, engine='openpyxl')


# In[15]:


df_2020 = df.iloc[1:,[0,1,10,11,12,13]]
df_2020.columns = ['시도','시군구','사고건수','사망자수','부상자수','중상자수']


# In[16]:


df_2020.head()


# In[17]:


df_2020_acc = df_2020[['시군구','사고건수']]


# In[18]:


y = df_2020_acc[['시군구']]
X = df_2020_acc[['사고건수']]


# In[24]:


from sklearn.preprocessing import RobustScaler

scaler = RobustScaler()

X_scaled = scaler.fit_transform(X)


# In[25]:


from sklearn.cluster import KMeans

Kmeans = KMeans(n_clusters=4, init='k-means++', max_iter=300)
Kmeans.fit(X)


# In[26]:


y['cluster'] = Kmeans.labels_


# In[27]:


y['사고수'] = X


# In[28]:


y.sort_values(by='사고수',ascending=False)

