#!/usr/bin/env python
# coding: utf-8

# In[129]:


import pandas as pd

df = pd.read_csv('./outputall/맵핑데이터.csv')
df.drop('Unnamed: 0',axis=1,inplace=True)
df.set_index('법정동코드',inplace=True)


# In[130]:


df = df.drop_duplicates(keep='first')


# In[131]:


# 보호구역 데이터들
경기보호구역 = pd.read_csv('./outputall/경기보호구역.csv',index_col='법정동')
서울보호구역 = pd.read_csv('./outputall/서울보호구역.csv',index_col='법정동')


# In[132]:


# 읍면동 별 다양한 데이터들
import pandas as pd
매출 = pd.read_csv('./outputall/매출.csv',index_col = '읍면동코드')
상권_숙박 = pd.read_csv('./outputall/상권_숙박.csv', index_col='Unnamed: 0')
상권_fnb = pd.read_csv('./outputall/상권_fnb.csv', index_col='Unnamed: 0')
평균금액 = pd.read_csv('./outputall/경기서울_법정동월평균금액.csv', index_col='법정동자택주소')


# In[133]:


# 필요없는 데이터 삭제
매출.drop('주소',axis=1,inplace=True)
상권_숙박.drop('주소',axis=1,inplace=True)
상권_fnb.drop('주소',axis=1,inplace=True)


# In[134]:


# 컬럼명 지정
상권_숙박.columns=['숙박업 개수']
상권_fnb.columns=['외식업 개수']
경기보호구역.columns=['경기_보호구역 수']
서울보호구역.columns=['서울_보호구역 수']


# In[135]:


# 인덱스명 통일하게 지정
매출.index.name = '법정동코드'
상권_숙박.index.name = '법정동코드'
상권_fnb.index.name = '법정동코드'
경기보호구역.index.name = '법정동코드'
서울보호구역.index.name = '법정동코드'
평균금액.index.name = '법정동코드'


# In[136]:


# 읍면동별 교통사고(서울)

seoul_accident = pd.read_csv('./outputall/서울시 사고수 데이터.csv')
gyungi_accident = pd.read_csv('./outputall/경기도 사고수 데이터.csv')


# In[137]:


seoul_accident.columns = ['법정동코드','주소','총 사고수']
gyungi_accident.columns = ['법정동코드','주소','총 사고수']


# In[138]:


all_accident = pd.concat([seoul_accident,gyungi_accident])
all_accident['법정동코드'] = all_accident['법정동코드'].apply(lambda x : int(x))
all_accident.set_index('법정동코드',inplace=True)


# In[139]:


all_accident.drop('주소',axis=1,inplace=True)


# In[140]:


type(매출.index), type(상권_숙박.index), type(상권_fnb.index), type(평균금액.index), type(all_accident.index), type(경기보호구역.index), type(서울보호구역.index)


# In[141]:


df_new = pd.merge(df,all_accident,
                  left_index=True,
                 right_index=True,
                 how='left')
df_new.shape



# In[142]:


df_new = pd.merge(df_new,매출,
                  left_index=True,
                 right_index=True,
                 how='left')
df_new.shape


# In[143]:


df_new = pd.merge(df_new,상권_fnb,
                  left_index=True,
                 right_index=True,
                 how='left')
df_new.shape


# In[144]:


df_new = pd.merge(df_new,상권_숙박,
                  left_index=True,
                 right_index=True,
                 how='left')
df_new.shape


# In[145]:


df_new = pd.merge(df_new,평균금액,
                  left_index=True,
                 right_index=True,
                 how='left')
df_new.shape


# In[146]:


df_new = pd.merge(df_new,경기보호구역,
                  left_index=True,
                 right_index=True,
                 how='left')
df_new.shape


# In[147]:


df_new = pd.merge(df_new,서울보호구역,
                  left_index=True,
                 right_index=True,
                 how='left')
df_new.shape


# In[148]:


df_new.fillna(0,inplace=True)
df_new['합'] = df_new.sum(axis=1)
df_final = df_new.loc[df_new['합']!=0]


# In[149]:


df_final.drop('합',axis=1,inplace=True)
df_final


# In[244]:


df_seoul = df_final.loc[df_final.index<1200000000]
df_gyeonggi = df_final.loc[df_final.index>1200000000]


# In[245]:


seoul_columns = df_final.columns.difference(['경기_보호구역 수'])
gyeonggi_columns = df_final.columns.difference(['서울_보호구역 수'])


# In[246]:


df_seoul = df_seoul[seoul_columns]
df_gyeonggi = df_gyeonggi[gyeonggi_columns]


# In[247]:


df_seoul.columns = ['결제건수', '결제금액', '보호구역 수', '숙박업 개수', '외식업 개수', '월평균카드소비금액','월환산평균소득금액', '주소', '총 사고수']
df_gyeonggi.columns = ['결제건수', '결제금액', '보호구역 수', '숙박업 개수', '외식업 개수', '월평균카드소비금액','월환산평균소득금액', '주소', '총 사고수']


# In[186]:


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams["font.family"] = 'Gulim'
corr = df_gyeonggi.corr()

mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

plt.figure(figsize=(14,8))

plt.title('상관분석 결과')
sns.heatmap(corr,mask=mask, annot=True, cmap='Reds')
plt.show()


# In[309]:


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams["font.family"] = 'Gulim'
corr = df_seoul.corr()

mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

plt.figure(figsize=(14,8))

plt.title('상관분석 결과')
sns.heatmap(corr,mask=mask, annot=True, cmap='Reds')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[177]:


get_ipython().system('pip install geopandas')


# In[178]:


import geopandas as gpd


# In[179]:


gyungi_map = gpd.read_file('./upload/data/GyungidoDong.json')
gyungi_map['EMD_CD'] = gyungi_map['EMD_CD'].apply(lambda x : int(x))
gyungi_map['EMD_CD'] = gyungi_map['EMD_CD'].apply(lambda x : x*100)
gyungi_map


# In[180]:


gyungi_map = gyungi_map.loc[:,['EMD_CD','geometry']]
gyungi_map.columns = ['법정동코드','geometry']


# In[198]:


df_gyeonggi2 = df_gyeonggi
df_seoul2 = df_seoul


# In[199]:


df_gyeonggi2['법정동코드'] = df_gyeonggi.index
df_seoul2['법정동코드'] = df_seoul.index
df_gyeonggi2.index.name = 'index'
df_seoul2.index.name = 'index'


# In[200]:


merged2 = pd.merge(gyungi_map,df_gyeonggi2,
                  how='right',on='법정동코드')
merged2['법정동코드'] = merged2['법정동코드'].apply(lambda x : int(x))


# In[201]:


seoul_dong_map = gpd.read_file('./upload/data/LsmdAdmSectUmd11Wgs84.json')
seoul_dong_map['EMD_CD'] = seoul_dong_map['EMD_CD'].apply(lambda x : int(x))
seoul_dong_map['EMD_CD'] = seoul_dong_map['EMD_CD'].apply(lambda x : x*100)
seoul_dong_map


# In[202]:


seoul_dong_map = seoul_dong_map.loc[:,['EMD_CD','geometry']]
seoul_dong_map.columns = ['법정동코드','geometry']


# In[203]:


merged = pd.merge(seoul_dong_map,df_seoul2,
                  how='right',on='법정동코드')


# In[ ]:





# In[ ]:





# In[204]:


merged2.plot(column = '총 사고수', figsize=(11,11),cmap='Reds', edgecolor='k',legend=True)


# In[208]:


merged2.plot(column = '외식업 개수', figsize=(11,11),cmap='Reds', edgecolor='k',legend=True)


# In[ ]:


merged2.plot(column = '', figsize=(11,11),cmap='Reds', edgecolor='k',legend=True)


# In[392]:


merged2.sort_values(by='총 사고수',ascending=False)


# In[ ]:





# In[306]:


merged2.plot(column = '결제건수', figsize=(11,11),cmap='Reds', edgecolor='k',legend=True)


# In[307]:


merged.plot(column = '결제건수', figsize=(11,11),cmap='Reds', edgecolor='k',legend=True)


# In[ ]:





# In[ ]:





# In[387]:





# In[222]:


import statsmodels.api as sm


# In[248]:


df_gyeonggi


# In[249]:


feature_columns = df_gyeonggi.columns.difference(['총 사고수','주소'])
X_data = df_gyeonggi[feature_columns]
target = df_gyeonggi[['총 사고수']]
X_data = sm.add_constant(X_data, has_constant='add')
from sklearn.preprocessing import RobustScaler

scaler = RobustScaler()

Scaled_X_data = scaler.fit_transform(X_data)
model1 = sm.OLS(target,Scaled_X_data)
fitted_model1 = model1.fit()


# In[250]:


X_data.columns


# In[251]:


fitted_model1.summary()


# In[252]:


from statsmodels.stats.outliers_influence import variance_inflation_factor

vif = pd.DataFrame()
vif['VIF Factor'] = [variance_inflation_factor(X_data.values,i) for i in range(X_data.shape[1])]
vif['features'] = X_data.columns
vif


# In[253]:


feature_columns1 = df_gyeonggi.columns.difference(['총 사고수','월환산평균소득금액','주소'])


# In[254]:


X_data2 = df_gyeonggi[feature_columns1]
target2 = df_gyeonggi[['총 사고수']]
X_data2 = sm.add_constant(X_data2, has_constant='add')

scaler = RobustScaler()
Scaled_X_data2 = scaler.fit_transform(X_data2)
model2 = sm.OLS(target2,Scaled_X_data2)
fitted_model2 = model2.fit()


# In[255]:


feature_columns1


# In[256]:


fitted_model2.summary()


# In[257]:


from statsmodels.stats.outliers_influence import variance_inflation_factor

vif = pd.DataFrame()
vif['VIF Factor'] = [variance_inflation_factor(X_data2.values,i) for i in range(X_data2.shape[1])]
vif['features'] = X_data2.columns
vif


# In[264]:


feature_columns2 = df_gyeonggi.columns.difference(['총 사고수','월환산평균소득금액','주소','결제금액'])
X_data3 = df_gyeonggi[feature_columns2]
target3 = df_gyeonggi[['총 사고수']]
X_data3 = sm.add_constant(X_data3, has_constant='add')

scaler = RobustScaler()
Scaled_X_data3 = scaler.fit_transform(X_data3)
model3 = sm.OLS(target3,Scaled_X_data3)
fitted_model3 = model3.fit()


# In[259]:


feature_columns2


# In[260]:


fitted_model3.summary()


# In[261]:


from statsmodels.stats.outliers_influence import variance_inflation_factor

vif = pd.DataFrame()
vif['VIF Factor'] = [variance_inflation_factor(X_data3.values,i) for i in range(X_data3.shape[1])]
vif['features'] = X_data3.columns
vif


# In[ ]:





# In[265]:


feature_columns_seoul = df_seoul.columns.difference(['총 사고수','월환산평균소득금액','주소','결제금액'])
X_data_seoul = df_seoul[feature_columns_seoul]
X_data_seoul = sm.add_constant(X_data_seoul, has_constant='add')
target_seoul = df_seoul[['총 사고수']]
Scaled_X_data_seoul = scaler.transform(X_data_seoul)


# In[267]:


pred_seoul = fitted_model3.predict(Scaled_X_data_seoul)


# In[268]:


from sklearn.metrics import mean_squared_error
import numpy as np

np.sqrt(mean_squared_error(target_seoul,pred_seoul))


# In[ ]:





# In[ ]:





# In[269]:


feature_columns_im = df_gyeonggi.columns.difference(['총 사고수','월환산평균소득금액','주소','결제금액'])
X_data_im = df_gyeonggi[feature_columns_im]
target = df_gyeonggi[['총 사고수']]

scaler = RobustScaler()
Scaled_X_data_im = scaler.fit_transform(X_data_im)


# In[270]:


X_test = df_seoul[feature_columns_im]
Scaled_X_test = scaler.transform(X_test)
target_test = df_seoul[['총 사고수']]


# In[ ]:





# In[271]:


from sklearn.ensemble import RandomForestRegressor

clf = RandomForestRegressor(n_estimators=20, max_depth=20, max_features=3)
clf.fit(X_data_im, target)


# In[272]:


f_i = clf.feature_importances_
f_i_s = pd.Series(f_i, index=X_data_im.columns)
f_i_s = f_i_s.sort_values(ascending=False)


# In[273]:


import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams["font.family"] = 'Gulim'
plt.figure(figsize=(15,6))
plt.title('중요변수')
sns.barplot(x=f_i_s, y=f_i_s.index)
plt.show()


# In[274]:


pred_y_rf = clf.predict(X_test)


# In[275]:


from sklearn.metrics import mean_squared_error
import numpy as np

np.sqrt(mean_squared_error(target_seoul,pred_y_rf))


# In[ ]:





# In[576]:


############################################# 점수 #####################################################################################################


# In[276]:


df_score_seoul = df_seoul[['외식업 개수','결제건수','월평균카드소비금액','보호구역 수','숙박업 개수','주소']]



# In[277]:


df_score_seoul


# In[278]:


외식업점수_index = df_score_seoul.sort_values(by='외식업 개수',ascending=False).index.tolist()
결제건수점수_index = df_score_seoul.sort_values(by='결제건수',ascending=False).index.tolist()
월평균카드소비금액점수_index = df_score_seoul.sort_values(by='월평균카드소비금액',ascending=False).index.tolist()
보호구역수점수_index = df_score_seoul.sort_values(by='보호구역 수',ascending=False).index.tolist()
숙박업개수점수_index = df_score_seoul.sort_values(by='숙박업 개수',ascending=False).index.tolist()

결제건수_map = {결제건수점수_index[i-1]:range(1,467)[-i] for i in range(1,len(df_score_seoul)+1)}
외식업_map = {외식업점수_index[i-1]:range(1,467)[-i] for i in range(1,len(df_score_seoul)+1)}
월평균카드소비금액_map = {월평균카드소비금액점수_index[i-1]:range(1,467)[-i] for i in range(1,len(df_score_seoul)+1)}
보호구역수_map = {보호구역수점수_index[i-1]:range(1,467)[-i] for i in range(1,len(df_score_seoul)+1)}
숙박업개수_map = {숙박업개수점수_index[i-1]:range(1,467)[-i] for i in range(1,len(df_score_seoul)+1)}

df_score_seoul['외식업점수'] = df_score_seoul.index
df_score_seoul['결제건수점수'] = df_score_seoul.index
df_score_seoul['월평균카드소비금액점수'] = df_score_seoul.index
df_score_seoul['보호구역수점수'] = df_score_seoul.index
df_score_seoul['숙박업개수점수'] = df_score_seoul.index


# In[279]:


df_score_seoul['외식업점수'] = df_score_seoul['외식업점수'].replace(외식업_map)
df_score_seoul['결제건수점수'] = df_score_seoul['외식업점수'].replace(결제건수_map)
df_score_seoul['월평균카드소비금액점수'] = df_score_seoul['월평균카드소비금액점수'].replace(월평균카드소비금액_map)
df_score_seoul['보호구역수점수'] = df_score_seoul['보호구역수점수'].replace(보호구역수_map)
df_score_seoul['숙박업개수점수'] = df_score_seoul['숙박업개수점수'].replace(숙박업개수_map)


# In[280]:


df_score_seoul.sort_values(by='외식업 개수',ascending=False)


# In[295]:


df_score_seoul['점수'] = df_score_seoul['외식업점수']*0.005 + df_score_seoul['결제건수점수']*0.004 +df_score_seoul['월평균카드소비금액점수']*0.003 + df_score_seoul['보호구역수점수']*0.002 + df_score_seoul['숙박업개수점수']*0.001


# In[296]:


df_score_seoul.sort_values('점수',ascending=False)


# In[ ]:





# In[ ]:





# In[283]:


import math
def trunc_100000(x):
    return math.trunc(x/100000)*100000


# In[284]:


df_score_seoul['법정동코드(구)'] = df_score_seoul.index
df_score_seoul['법정동코드(구)'] = df_score_seoul['법정동코드(구)'].apply(lambda x : trunc_100000(x))
df_score_seoul


# In[286]:


# raw_dongmap 저장
import pickle

with open('./team_share/outputall/raw_goomap_final.pickle','rb') as fw:
    goomap = pickle.load(fw)


# In[287]:


df_score_seoul['구'] = df_score_seoul['법정동코드(구)'].replace(goomap)


# In[297]:


df_score_seoul[df_score_seoul['구'] == '강남구'].sort_values('점수',ascending=False)


# In[299]:


df_score_save = df_score_seoul[['주소','외식업점수','결제건수점수','보호구역수점수','숙박업개수점수','점수','법정동코드(구)','구']]


# In[300]:


df_score_save


# In[304]:


import dataframe_image as dfi

pd.set_option('display.max_rows',None)
df_score_save.to_csv('./최종점수.csv',sep=',')

