#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
def same_address(file_name):
    sample = pd.read_csv(file_name, sep=",", header = 0)
    sample = sample.loc[((sample['법정동자택주소']>1100000000)&(sample['법정동자택주소']<1200000000))|((sample['법정동자택주소']>4100000000)&(sample['법정동자택주소']<4200000000))]
    sample = sample.loc[sample['법정동자택주소'] == sample['법정동직장주소']]
    grouped = sample.groupby('법정동자택주소')[['집계인구수']]
    result = grouped.sum()
    return result


# In[3]:


sample = pd.read_csv('~/import_data/TB_KCB_OD_COMMU/TB_KCB_OD_COMMU_202003.csv', sep=",", header = 0)
sample


# In[47]:


import pandas as pd

sample = pd.read_csv('~/import_data/TB_KCB_OD_COMMU/TB_KCB_OD_COMMU_202003.csv', sep=",", header = 0)
sample = sample.loc[(sample['법정동자택주소']>1100000000)&(sample['법정동자택주소']<1200000000)]
grouped = sample.groupby('법정동자택주소')[['월평균카드소비금액','월환산평균소득금액']]
result = grouped.sum()
result.to_csv('./outputall/법정동별월평균금액.csv',sep=',')


# In[ ]:





# In[ ]:


sample = pd.read_csv('~/import_data/TB_KCB_OD_COMMU/TB_KCB_OD_COMMU_202003.csv', sep=",", header = 0)
sample


# In[4]:


import math
def trunc_10(x):
    return math.trunc(x/100)*100


# In[5]:


import pandas as pd

sample = pd.read_csv('~/import_data/TB_KCB_OD_COMMU/TB_KCB_OD_COMMU_202003.csv', sep=",", header = 0)
sample = sample.loc[((sample['법정동자택주소']>1100000000)&(sample['법정동자택주소']<1200000000))|((sample['법정동자택주소']>4100000000)&(sample['법정동자택주소']<4200000000))]
sample['법정동자택주소'] = sample['법정동자택주소'].apply(lambda x : trunc_10(x))
grouped = sample.groupby('법정동자택주소')[['월평균카드소비금액','월환산평균소득금액']]
result = grouped.sum()
result


# In[7]:


result.to_csv('./outputall/경기서울_법정동월평균금액.csv',sep=',')

