#!/usr/bin/env python
# coding: utf-8

# In[52]:


import pandas as pd
kto_201901 = pd.read_excel('C:/Users/Administrator/data/files/kto_201901.xlsx',
                          engine = 'openpyxl',
                          header = 1,
                          usecols = 'A:G',
                          skipfooter=4)
kto_201901.head()


# In[53]:


kto_201901.tail()


# In[54]:


kto_201901.info()


# In[55]:


kto_201901.describe()


# In[56]:


condition = (kto_201901['관광'] == 0)             | (kto_201901['상용'] == 0)             | (kto_201901['공용'] == 0)             | (kto_201901['유학/연수'] == 0)
kto_201901[condition]


# In[57]:


kto_201901['기준년월'] = '2019-01'
kto_201901.head()


# In[58]:


kto_201901['국적'].unique()


# #### unique 함수는 칼럼 내 중복을 제거한 값, 원소를 보여주는 함수(국적 컬럼 보기)

# In[59]:


continents_list = ['아시아주','미주','구주','대양주','아프리카주','기타대륙','교포소계']
continents_list


# In[60]:


condition = (kto_201901.국적.isin(continents_list) == False)
kto_201901_country = kto_201901[condition]
kto_201901_country['국적'].unique()


# In[61]:


kto_201901_country.head()


# In[62]:


kto_201901_country_newindex = kto_201901_country.reset_index(drop = True)
kto_201901_country_newindex.head()


# In[63]:


# reset_index()는 인덱스 값을 0부터 순차적으로 다시 초기화
# drop = True는 쓰지 않을 경우 기존 인덱스 값이 새로운 칼럼으로 생성됨


# In[64]:


continents = ['아시아']*25 + ['아메리카']*5 + ['유럽']*23 + ['오세아니아']*3 + ['아프리카']*2 + ['기타대륙'] + ['교포']
print(continents)


# In[65]:


kto_201901_country_newindex['대륙'] = continents
kto_201901_country_newindex.head()


# In[66]:


kto_201901_country_newindex['관광객비율(%)'] = round(kto_201901_country_newindex['관광'] / kto_201901_country_newindex['계']*100, 1)

kto_201901_country_newindex['유학/연수(%)'] = round(kto_201901_country_newindex['유학/연수'] / kto_201901_country_newindex['계']*100, 1)

kto_201901_country_newindex.head()


# In[67]:


kto_201901_country_newindex.sort_values(by='관광객비율(%)',ascending=False).head()


# In[68]:


kto_201901_country_newindex.sort_values(by='관광객비율(%)',ascending=True).head()


# In[69]:


kto_201901_country_newindex.pivot_table(values = '관광객비율(%)', 
                                        index='대륙',
                                        aggfunc='mean')


# In[70]:


condition = (kto_201901_country_newindex['국적']=='중국')
kto_201901_country_newindex[condition]


# In[71]:


tourist_sum = sum(kto_201901_country_newindex['관광'])
tourist_sum


# In[72]:


kto_201901_country_newindex['전체비율(%)'] =     round(kto_201901_country_newindex['관광'] / tourist_sum*100,1)
kto_201901_country_newindex.head()


# In[73]:


kto_201901_country_newindex.sort_values('전체비율(%)',ascending=False).head()


# ### 데이터 전처리 과정 함수 만들기

# In[74]:


def create_kto_data(yy, mm):
    file_path = 'C:/Users/Administrator/data/files/kto_{}{}.xlsx'.format(yy,mm)
    
    df = pd.read_excel(file_path, header = 1, skipfooter = 4, usecols = 'A:G',
                      engine='openpyxl')
    
    df['기준년월'] = '{}-{}'.format(yy,mm)
    
    ignore_list = ['아시아주','미주','구주','대양주','아프리카주','기타대륙','교포소계']
    condition = (df['국적'].isin(ignore_list) == False)
    df_country = df[condition].reset_index(drop = True)
    
    continents = ['아시아']*25 + ['아메리카']*5 + ['유럽']*23 + ['대양주']*3 + ['아프리카']*2 + ['기타대륙'] + ['교포']
    df_country['대륙'] = continents
    
    df_country['관광객비율(%)'] = round(df_country.관광 / df_country.계 *100, 1)
    
    tourist_sum = sum(df_country['관광'])
    df_country['전체비율(%)'] = round(df_country['관광'] / tourist_sum*100, 1)
    
    return(df_country)


# In[75]:


kto_test = create_kto_data(2018,12)
kto_test.head()


# #### 반복문(for)을 통해 다수의 엑셀 데이터 불러와서 합치기

# In[76]:


for yy in range(2010, 2021):
    for mm in range(1, 13):
        yymm = '{}-{}'.format(yy,mm)
        print(yymm)


# In[77]:


mm = 1
print(mm)


# In[78]:


print(str(mm).zfill(2))


# In[79]:


for yy in range(2010, 2021):
    for mm in range(1, 13):
        mm_str = str(mm).zfill(2)
        yymm =  '{}-{}'.format(yy, mm_str)
        print(yymm)


# In[96]:


df = pd.DataFrame()

for yy in range(2010, 2021):
    for mm in range(1, 13):
        try:
            temp = create_kto_data(str(yy), str(mm).zfill(2))
            
            df = df.append(temp, ignore_index=True)
        
        except:
            pass


# In[97]:


df.head()


# In[99]:


df.tail()


# In[100]:


df.info()


# In[101]:


df.to_excel('D:/Kangjh/travel/kto_total1.xlsx', index = False)


# #### 국적별 필터링된 데이터를 엑셀 파일로 저장하기

# In[102]:


condition = (df['국적'] == '중국')
df_filter = df[condition]
df_filter.head()


# In[103]:


file_path = 'D:/Kangjh/travel/[국적별 관광객 데이터]중국.xlsx'
df_filter.to_excel(file_path, index=False)


# In[104]:


cntry_list = df['국적'].unique()
cntry_list


# In[105]:


len(cntry_list)


# In[106]:


for cntry in cntry_list:
    condition = (df['국적'] == cntry)
    df_filter = df[condition]
    
    file_path = 'D:/Kangjh/travel/[국적별 관광객 데이터] {}.xlsx'.format(cntry)
    
    df_filter.to_excel(file_path, index = False)


# ### 시계열 그래프 그리기

# In[123]:


import pandas as pd
import numpy as np

df = pd.read_excel('D:/Kangjh/travel/kto_total1.xlsx',engine='openpyxl')
df.head()
df.info()


# In[124]:


from matplotlib import font_manager, rc
import platform

if platform.system() == 'Windows':
    path = 'C:/Windows/Fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
elif platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
else:
    print('Check your OS system')


# In[129]:


df['년도'] = df['기준년월'].str.slice(0,4)
df['월'] = df['기준년월'].str.slice(5, 7)
df.head()


# In[130]:


condition = (df['국적'] == '중국')
df_filter = df[condition]
df_filter.head()


# In[132]:


df_pivot = df_filter.pivot_table(values = '관광',
                                index = '년도',
                                columns = '월')
df_pivot


# In[133]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[134]:


plt.figure(figsize = (16, 10))

sns.heatmap(df_pivot, annot = True, fmt = '.0f', cmap='RdYlGn_r')

plt.title('중국 관광객 히트맵')

plt.show()


# In[135]:


for cntry in cntry_list:
    condition = (df['국적'] == cntry)
    df_filter = df[condition]
    
    df_pivot = df_filter.pivot_table(values = '관광',
                                    index = '년도',
                                    columns = '월')
    
    plt.figure(figsize = (16,10))
    
    sns.heatmap(df_pivot, annot = True, fmt = '.0f', cmap = 'rocket_r')
    
    plt.title('{} 관광객 히트맵'.format(cntry))
    
    plt.show()


# In[ ]:




