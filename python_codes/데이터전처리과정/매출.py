#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
def sample(file_name):
    # 1~12월 데이터 불러오기
    sample = pd.read_csv(file_name, sep=",", header = 0)
    # 경기/서울 지역만 추출
    sample = sample.loc[((sample['읍면동코드']>1100000000)&(sample['읍면동코드']<1200000000))|((sample['읍면동코드']>4100000000)&(sample['읍면동코드']<4200000000))]
    # 읍면동별 결제건수/결제금액 그룹핑
    grouped = sample.groupby('읍면동코드')[['결제건수','결제금액']]
    # 읍면동별 결제건수/결제금액의 합
    읍면동별매출_2020 = grouped.sum()
    return 읍면동별매출_2020


# In[2]:


# 1~12월 데이터 함수적용
month_01 = sample("~/import_data/TB_SHC_SALE_CUST_INFO/TB_SHC_SALE_CUST_INFO_202001.csv")
month_02 = sample("~/import_data/TB_SHC_SALE_CUST_INFO/TB_SHC_SALE_CUST_INFO_202002.csv")
month_03 = sample("~/import_data/TB_SHC_SALE_CUST_INFO/TB_SHC_SALE_CUST_INFO_202003.csv")
month_04 = sample("~/import_data/TB_SHC_SALE_CUST_INFO/TB_SHC_SALE_CUST_INFO_202004.csv")
month_05 = sample("~/import_data/TB_SHC_SALE_CUST_INFO/TB_SHC_SALE_CUST_INFO_202005.csv")
month_06 = sample("~/import_data/TB_SHC_SALE_CUST_INFO/TB_SHC_SALE_CUST_INFO_202006.csv")
month_07 = sample("~/import_data/TB_SHC_SALE_CUST_INFO/TB_SHC_SALE_CUST_INFO_202007.csv")
month_08 = sample("~/import_data/TB_SHC_SALE_CUST_INFO/TB_SHC_SALE_CUST_INFO_202008.csv")
month_09 = sample("~/import_data/TB_SHC_SALE_CUST_INFO/TB_SHC_SALE_CUST_INFO_202009.csv")
month_10 = sample("~/import_data/TB_SHC_SALE_CUST_INFO/TB_SHC_SALE_CUST_INFO_202010.csv")
month_11 = sample("~/import_data/TB_SHC_SALE_CUST_INFO/TB_SHC_SALE_CUST_INFO_202011.csv")
month_12 = sample("~/import_data/TB_SHC_SALE_CUST_INFO/TB_SHC_SALE_CUST_INFO_202012.csv")


# In[3]:


# 1~12월 데이터 합으로 집계 = 2020년의 읍면동별 결제건수/결제금액
읍면동별매출_2020 = month_01.add(month_02, fill_value=0)
읍면동별매출_2020 = 읍면동별매출_2020.add(month_03, fill_value=0)
읍면동별매출_2020 = 읍면동별매출_2020.add(month_04, fill_value=0)
읍면동별매출_2020 = 읍면동별매출_2020.add(month_05, fill_value=0)
읍면동별매출_2020 = 읍면동별매출_2020.add(month_06, fill_value=0)
읍면동별매출_2020 = 읍면동별매출_2020.add(month_07, fill_value=0)
읍면동별매출_2020 = 읍면동별매출_2020.add(month_08, fill_value=0)
읍면동별매출_2020 = 읍면동별매출_2020.add(month_09, fill_value=0)
읍면동별매출_2020 = 읍면동별매출_2020.add(month_10, fill_value=0)
읍면동별매출_2020 = 읍면동별매출_2020.add(month_11, fill_value=0)
읍면동별매출_2020 = 읍면동별매출_2020.add(month_12, fill_value=0)


# In[5]:


읍면동별매출_2020


# In[10]:


읍면동별매출_2020.to_csv('outputall/매출.csv',sep=',')

