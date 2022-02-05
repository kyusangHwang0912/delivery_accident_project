#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd

df = pd.read_csv('../outputall/맵핑데이터.csv')
df.drop('Unnamed: 0',axis=1,inplace=True)
df.set_index('법정동코드',inplace=True)


# In[7]:


df = df.drop_duplicates(keep='first')


# In[11]:


#보호구역 데이터들
경기보호구역 = pd.read_csv('../outputall/경기보호구역.csv',index_col='법정동')
서울보호구역 = pd.read_csv('../outputall/서울보호구역.csv',index_col='법정동')


# In[13]:


# 읍면동 별 다양한 데이터들

import pandas as pd
매출 = pd.read_csv('../outputall/매출.csv',index_col = '읍면동코드')
상권_숙박 = pd.read_csv('../outputall/상권_숙박.csv', index_col='Unnamed: 0')
상권_fnb = pd.read_csv('../outputall/상권_fnb.csv', index_col='Unnamed: 0')
평균금액 = pd.read_csv('../outputall/경기서울_법정동월평균금액.csv', index_col='법정동자택주소')


# In[14]:


매출.drop('주소',axis=1,inplace=True)
상권_숙박.drop('주소',axis=1,inplace=True)
상권_fnb.drop('주소',axis=1,inplace=True)


# In[15]:


# 컬럼명 지정
상권_숙박.columns=['숙박업 개수']
상권_fnb.columns=['외식업 개수']
경기보호구역.columns=['경기_보호구역 수']
서울보호구역.columns=['서울_보호구역 수']


# In[16]:


매출.index.name = '법정동코드'
상권_숙박.index.name = '법정동코드'
상권_fnb.index.name = '법정동코드'
경기보호구역.index.name = '법정동코드'
서울보호구역.index.name = '법정동코드'
평균금액.index.name = '법정동코드'


# In[18]:


# 읍면동별 교통사고(서울)

seoul_accident = pd.read_csv('../outputall/서울시 사고수 데이터.csv')
gyungi_accident = pd.read_csv('../outputall/경기도 사고수 데이터.csv')


# In[19]:


seoul_accident.columns = ['법정동코드','주소','총 사고수']
gyungi_accident.columns = ['법정동코드','주소','총 사고수']


# In[20]:


all_accident = pd.concat([seoul_accident,gyungi_accident])
all_accident['법정동코드'] = all_accident['법정동코드'].apply(lambda x : int(x))
all_accident.set_index('법정동코드',inplace=True)


# In[21]:


all_accident.drop('주소',axis=1,inplace=True)


# In[22]:


type(매출.index), type(상권_숙박.index), type(상권_fnb.index), type(평균금액.index), type(all_accident.index), type(경기보호구역.index), type(서울보호구역.index)


# In[23]:


df_new = pd.merge(df,all_accident,
                  left_index=True,
                 right_index=True,
                 how='left')
df_new.shape


# In[24]:


df_new = pd.merge(df_new,매출,
                  left_index=True,
                 right_index=True,
                 how='left')
df_new.shape


# In[25]:


df_new = pd.merge(df_new,상권_fnb,
                  left_index=True,
                 right_index=True,
                 how='left')
df_new.shape


# In[26]:


df_new = pd.merge(df_new,상권_숙박,
                  left_index=True,
                 right_index=True,
                 how='left')
df_new.shape


# In[27]:


df_new = pd.merge(df_new,평균금액,
                  left_index=True,
                 right_index=True,
                 how='left')
df_new.shape


# In[28]:


df_new = pd.merge(df_new,경기보호구역,
                  left_index=True,
                 right_index=True,
                 how='left')
df_new.shape


# In[29]:


df_new = pd.merge(df_new,서울보호구역,
                  left_index=True,
                 right_index=True,
                 how='left')
df_new.shape


# In[30]:


df_new.fillna(0,inplace=True)
df_new['합'] = df_new.sum(axis=1)
df_final = df_new.loc[df_new['합']!=0]


# In[31]:


df_final.drop('합',axis=1,inplace=True)
df_final


# In[32]:


df_seoul = df_final.loc[df_final.index<1200000000]
df_gyeonggi = df_final.loc[df_final.index>1200000000]


# In[33]:


seoul_columns = df_final.columns.difference(['경기_보호구역 수'])
gyeonggi_columns = df_final.columns.difference(['서울_보호구역 수'])


# In[34]:


df_seoul = df_seoul[seoul_columns]
df_gyeonggi = df_gyeonggi[gyeonggi_columns]


# In[35]:


df_seoul.columns = ['결제건수', '결제금액', '보호구역 수', '숙박업 개수', '외식업 개수', '월평균카드소비금액','월환산평균소득금액', '주소', '총 사고수']
df_gyeonggi.columns = ['결제건수', '결제금액', '보호구역 수', '숙박업 개수', '외식업 개수', '월평균카드소비금액','월환산평균소득금액', '주소', '총 사고수']


# In[36]:


df_seoul.corr()


# In[ ]:





# In[37]:


df_score_seoul = df_seoul[['외식업 개수','월평균카드소비금액','보호구역 수','숙박업 개수','주소']]



# In[38]:


df_score_seoul


# In[39]:


외식업점수_index = df_score_seoul.sort_values(by='외식업 개수',ascending=False).index.tolist()
월평균카드소비금액점수_index = df_score_seoul.sort_values(by='월평균카드소비금액',ascending=False).index.tolist()
보호구역수점수_index = df_score_seoul.sort_values(by='보호구역 수',ascending=False).index.tolist()
숙박업개수점수_index = df_score_seoul.sort_values(by='숙박업 개수',ascending=False).index.tolist()

외식업_map = {외식업점수_index[i-1]:range(1,467)[-i] for i in range(1,len(df_score_seoul)+1)}
월평균카드소비금액_map = {월평균카드소비금액점수_index[i-1]:range(1,467)[-i] for i in range(1,len(df_score_seoul)+1)}
보호구역수_map = {보호구역수점수_index[i-1]:range(1,467)[-i] for i in range(1,len(df_score_seoul)+1)}
숙박업개수_map = {숙박업개수점수_index[i-1]:range(1,467)[-i] for i in range(1,len(df_score_seoul)+1)}

df_score_seoul['외식업점수'] = df_score_seoul.index
df_score_seoul['월평균카드소비금액점수'] = df_score_seoul.index
df_score_seoul['보호구역수점수'] = df_score_seoul.index
df_score_seoul['숙박업개수점수'] = df_score_seoul.index


# In[40]:


df_score_seoul['외식업점수'] = df_score_seoul['외식업점수'].replace(외식업_map)
df_score_seoul['월평균카드소비금액점수'] = df_score_seoul['월평균카드소비금액점수'].replace(월평균카드소비금액_map)
df_score_seoul['보호구역수점수'] = df_score_seoul['보호구역수점수'].replace(보호구역수_map)
df_score_seoul['숙박업개수점수'] = df_score_seoul['숙박업개수점수'].replace(숙박업개수_map)


# In[41]:


df_score_seoul.sort_values(by='외식업 개수',ascending=False)


# In[42]:


df_score_seoul['점수'] = df_score_seoul['외식업점수']*0.004 + df_score_seoul['월평균카드소비금액점수']*0.003 + df_score_seoul['보호구역수점수']*0.002 + df_score_seoul['숙박업개수점수']*0.001


# In[43]:


df_score_seoul.sort_values('점수',ascending=False)


# In[ ]:





# In[44]:


import math
def trunc_100000(x):
    return math.trunc(x/100000)*100000


# In[45]:


df_score_seoul['법정동코드(구)'] = df_score_seoul.index
df_score_seoul['법정동코드(구)'] = df_score_seoul['법정동코드(구)'].apply(lambda x : trunc_100000(x))
df_score_seoul


# In[51]:


# raw_dongmap 저장
import pickle

with open('../outputall/raw_goomap_final.pickle','rb') as fw:
    goomap = pickle.load(fw)


# In[52]:


df_score_seoul['구'] = df_score_seoul['법정동코드(구)'].replace(goomap)


# In[53]:


df_score_seoul[df_score_seoul['구'] == '노원구'].sort_values('점수',ascending=False)


# In[ ]:




