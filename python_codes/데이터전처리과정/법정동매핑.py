#!/usr/bin/env python
# coding: utf-8

# In[15]:


# 매핑데이터 불러오기
import pandas as pd
df = pd.read_csv('./upload/행정구역분류_행정동법정동매핑.csv')


# In[16]:


# 이상한 데이터 삭제
df = df.loc[df['행정구역코드']>1000000.0]
df.drop(2973,inplace=True)


# In[17]:


# 법정동 주소 컬럼 생성
df['주소'] = df['시도']+' '+df['시군구']+' '+df['법정동']


# In[18]:


# 경기/서울만 추출
df = df.loc[((df['법정동코드']>1100000000)&(df['법정동코드']<1200000000))|((df['법정동코드']>4100000000)&(df['법정동코드']<4200000000))]


# In[19]:


df


# In[7]:


# 앞 뒤 공백 제거
df.reset_index(inplace=True)
for i in range(len(df)):
    df['주소'][i] = df['주소'][i].strip()


# In[8]:


# 법정동코드와 주소 맵핑 데이터 생성
code = df.법정동코드.values.tolist()
add = df.주소.values.tolist()
raw_dongmap = {code[i]:add[i] for i in range(len(code))}


# In[35]:


# raw_dongmap 저장
import pickle

with open('raw_dongmap_all_final.pickle','wb') as fw:
    pickle.dump(raw_dongmap, fw)


# In[43]:


df[df['주소'] == '경기도 파주시 와동동']


# In[38]:


# 맵핑데이터를 csv로 저장 (분석과정에서 이 데이터에 하나씩 join 시키기 위함)
df.to_csv('./outputall/맵핑데이터.csv',sep=',')


# In[ ]:




