#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import re
pd.set_option('display.max_rows', None)


# In[2]:


# mapping data 불러오기
with open('./raw_dongmap_all_final.pickle', 'rb') as f:
    dong = pickle.load(f)
with open('./team_share/맵핑데이터/업종대분류코드.pickle', 'rb') as f:
    대분류 = pickle.load(f)
with open('./team_share/맵핑데이터/업종중분류코드.pickle', 'rb') as f:
    중분류 = pickle.load(f)
with open('./team_share/맵핑데이터/가맹점상태코드.pickle', 'rb') as f:
    가맹점상태 = pickle.load(f)


# In[3]:


# 함수 정의
# 가동중인 외식업 가맹점 개수 집계 함수
def frnc(file):
    Frnc_info_201901 = pd.read_csv(file, sep=",")
    Frnc_info_201901 = Frnc_info_201901[((Frnc_info_201901['읍면동코드']>1100000000)&(Frnc_info_201901['읍면동코드']<1200000000))|((Frnc_info_201901['읍면동코드']>4100000000)&(Frnc_info_201901['읍면동코드']<4200000000))]
    Frnc_info_201901 = Frnc_info_201901[(Frnc_info_201901['업종대분류코드'] == 3) & (Frnc_info_201901['가동코드'] == 1)]
    Frnc_info_201901
    grouping = Frnc_info_201901.groupby(['읍면동코드'])
    result = grouping.sum()[['가맹점수']]
    return result

# 가동중인 외식업 가맹점 개수 집계 함수 for 12월 --> 데이터가 다름
def frnc1(file):
    Frnc_info_201901 = pd.read_csv(file, sep=",")
    Frnc_info_201901 = Frnc_info_201901[((Frnc_info_201901['읍면동']>1100000000)&(Frnc_info_201901['읍면동']<1200000000))|((Frnc_info_201901['읍면동']>4100000000)&(Frnc_info_201901['읍면동']<4200000000))]
    Frnc_info_201901 = Frnc_info_201901[(Frnc_info_201901['업종대분류'] == 3) & (Frnc_info_201901['가동여부'] != 2)]
    Frnc_info_201901
    grouping = Frnc_info_201901.groupby(['읍면동'])
    result = grouping.sum()[['가맹점수']]
    return result


# In[4]:


# 각 월별 frnc 함수 적용
frnc202001 = frnc('~/import_data/TB_SHC_FRNC_INFO/TB_SHC_FRNC_INFO_202001.csv')
frnc202002 = frnc('~/import_data/TB_SHC_FRNC_INFO/TB_SHC_FRNC_INFO_202002.csv')
frnc202003 = frnc('~/import_data/TB_SHC_FRNC_INFO/TB_SHC_FRNC_INFO_202003.csv')
frnc202004 = frnc('~/import_data/TB_SHC_FRNC_INFO/TB_SHC_FRNC_INFO_202004.csv')
frnc202005 = frnc('~/import_data/TB_SHC_FRNC_INFO/TB_SHC_FRNC_INFO_202005.csv')
frnc202006 = frnc('~/import_data/TB_SHC_FRNC_INFO/TB_SHC_FRNC_INFO_202006.csv')
frnc202007 = frnc('~/import_data/TB_SHC_FRNC_INFO/TB_SHC_FRNC_INFO_202007.csv')
frnc202008 = frnc('~/import_data/TB_SHC_FRNC_INFO/TB_SHC_FRNC_INFO_202008.csv')
frnc202009 = frnc('~/import_data/TB_SHC_FRNC_INFO/TB_SHC_FRNC_INFO_202009.csv')
frnc202010 = frnc('~/import_data/TB_SHC_FRNC_INFO/TB_SHC_FRNC_INFO_202010.csv')
frnc202011 = frnc('~/import_data/TB_SHC_FRNC_INFO/TB_SHC_FRNC_INFO_202011.csv')
frnc202012 = frnc1('~/import_data/TB_SHC_FRNC_INFO/TB_SHC_FRNC_INFO_202012.csv')


# In[5]:


# 2020년 집계를 위해 1월부터 12월 add
result = frnc202001.add(frnc202002, fill_value=0)
result = result.add(frnc202003, fill_value=0)
result = result.add(frnc202004, fill_value=0)
result = result.add(frnc202005, fill_value=0)
result = result.add(frnc202006, fill_value=0)
result = result.add(frnc202007, fill_value=0)
result = result.add(frnc202008, fill_value=0)
result = result.add(frnc202009, fill_value=0)
result = result.add(frnc202010, fill_value=0)
result = result.add(frnc202011, fill_value=0)
result = result.add(frnc202012, fill_value=0)
result.sort_values(by='가맹점수',ascending=False)
result.가맹점수 = result.가맹점수.astype(int)


# In[7]:


# 결과 저장
result.to_csv('outputall/상권_fnb.csv',sep=',')

