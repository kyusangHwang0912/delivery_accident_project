#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().system('pip install xlrd')
get_ipython().system('pip install openpyxl')


# In[1]:


import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = 'Gulim'

df = pd.read_excel('~/upload/1920BiAccident.xlsx', engine='openpyxl')
df.columns


# In[2]:


df = df.loc[:, ['사고번호', '사고일시', '시군구']]


# In[3]:


pd.set_option('display.max_rows', 10)


# In[4]:


import re

df['사고일시'] = df['사고일시'].apply(lambda x : re.sub('[0-9]*년 |[0-9]*월 |[0-9]*일 ', '', x))
df['사고일시'] = df['사고일시'].apply(lambda x : x.strip())


# In[6]:


import pickle

with open('../raw_dongmap_all_final.pickle', 'rb') as f:
    dong = pickle.load(f)
dong1 = {v:k for k, v in dong.items()}


# In[7]:


df['시군구'].replace(dong1, inplace=True)


# In[8]:


df = df.groupby(['시군구', '사고일시'])[['사고번호']].count()


# In[9]:


df.columns = ['count']


# In[10]:


df_sort_values_시군구_count = df.sort_values(['시군구', 'count'], ascending=False)


# ## 강남구

# In[15]:


대치동 = df_sort_values_시군구_count.loc[1168010600]
대치동 = 대치동.sort_index()
대치동.plot(kind='bar', color = 'lightgreen').savefig('./강남구.png')


# In[32]:


논현동 = df_sort_values_시군구_count.loc[1168010800]
논현동 = 논현동.sort_index()
논현동.plot(kind='bar', color = 'lightgreen')


# In[33]:


역삼동 = df_sort_values_시군구_count.loc[1168010100]
역삼동 = 역삼동.sort_index()
역삼동.plot(kind='bar', color = 'lightgreen')


# ## 관악구

# In[34]:


신림동 = df_sort_values_시군구_count.loc[1162010200]
신림동 = 신림동.sort_index()
신림동.plot(kind='bar', color = 'lightgreen')


# In[35]:


봉천동 = df_sort_values_시군구_count.loc[1162010100]
봉천동 = 봉천동.sort_index()
봉천동.plot(kind='bar', color = 'lightgreen')


# ## 강서구

# In[36]:


화곡동 = df_sort_values_시군구_count.loc[1150010300]
화곡동 = 화곡동.sort_index()
화곡동.plot(kind='bar', color = 'lightgreen')


# In[37]:


마곡동 = df_sort_values_시군구_count.loc[1150010500]
마곡동 = 마곡동.sort_index()
마곡동.plot(kind='bar', color = 'lightgreen')


# ## 동대문구

# In[38]:


장안동 = df_sort_values_시군구_count.loc[1123010600]
장안동 = 장안동.sort_index()
장안동.plot(kind='bar', color = 'lightgreen')


# In[39]:


답십리동 = df_sort_values_시군구_count.loc[1123010500]
답십리동 = 답십리동.sort_index()
답십리동.plot(kind='bar', color = 'lightgreen')


# ## 송파구

# In[40]:


잠실동 = df_sort_values_시군구_count.loc[1171010100]
잠실동 = 잠실동.sort_index()
잠실동.plot(kind='bar', color = 'lightgreen')


# In[41]:


가락동 = df_sort_values_시군구_count.loc[1171010700]
가락동 = 가락동.sort_index()
가락동.plot(kind='bar', color = 'lightgreen')


# ## 영등포구

# In[42]:


신길동 = df_sort_values_시군구_count.loc[1156013200]
신길동 = 신길동.sort_index()
신길동.plot(kind='bar', color = 'lightgreen')


# In[43]:


대림동 = df_sort_values_시군구_count.loc[1156013300]
대림동 = 대림동.sort_index()
대림동.plot(kind='bar', color = 'lightgreen')


# ## 서초구

# In[44]:


서초동 = df_sort_values_시군구_count.loc[1165010800]
서초동 = 서초동.sort_index()
서초동.plot(kind='bar', color = 'lightgreen')


# ## 마포구

# In[45]:


성산동 = df_sort_values_시군구_count.loc[1144012500]
성산동 = 성산동.sort_index()
성산동.plot(kind='bar', color = 'lightgreen')


# ## 성북구

# In[46]:


정릉동 = df_sort_values_시군구_count.loc[1129013300]
정릉동 = 정릉동.sort_index()
정릉동.plot(kind='bar', color = 'lightgreen')


# ## 중랑구

# In[47]:


면목동 = df_sort_values_시군구_count.loc[1126010100]
면목동 = 면목동.sort_index()
면목동.plot(kind='bar', color = 'lightgreen')


# ## 성동구

# In[48]:


성수동2가 = df_sort_values_시군구_count.loc[1120011500]
성수동2가 = 성수동2가.sort_index()
성수동2가.plot(kind='bar', color = 'lightgreen')


# ## 동작구

# In[49]:


사당동 = df_sort_values_시군구_count.loc[1159010700]
사당동 = 사당동.sort_index()
사당동.plot(kind='bar', color = 'lightgreen')


# ## 강북구

# In[50]:


미아동 = df_sort_values_시군구_count.loc[1130510100]
미아동 = 미아동.sort_index()
미아동.plot(kind='bar', color = 'lightgreen')


# ## 노원구

# In[51]:


상계동 = df_sort_values_시군구_count.loc[1135010500]
상계동 = 상계동.sort_index()
상계동.plot(kind='bar', color = 'lightgreen')


# ## 중구

# In[52]:


신당동 = df_sort_values_시군구_count.loc[1114016200]
신당동 = 신당동.sort_index()
신당동.plot(kind='bar', color = 'lightgreen')


# ## 은평구

# In[53]:


음암동 = df_sort_values_시군구_count.loc[1138010700]
음암동 = 음암동.sort_index()
음암동.plot(kind='bar', color = 'lightgreen')


# ## 구로구

# In[54]:


음암동 = df_sort_values_시군구_count.loc[1153010200]
음암동 = 음암동.sort_index()
음암동.plot(kind='bar', color = 'lightgreen')


# ## 광진구

# In[55]:


자양동 = df_sort_values_시군구_count.loc[1121510500]
자양동 = 자양동.sort_index()
자양동.plot(kind='bar', color = 'lightgreen')


# In[ ]:




