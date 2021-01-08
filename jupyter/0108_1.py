#!/usr/bin/env python
# coding: utf-8

# ## 서울열린데이터광장의 open API를 활용한 공용데이터 수집

# In[5]:


import requests
import pandas as pd


# In[6]:


SEOUL_API_AUTH_KEY='6f717558676a65653130346753724462'


# In[7]:


url = 'http://openapi.seoul.go.kr:8088/{}/json/SdeTlSccoSigW/1/25'.format(SEOUL_API_AUTH_KEY)
print(url)


# In[8]:


result_dict = requests.get(url).json()
result_dict


# In[9]:


result_data = result_dict['SdeTlSccoSigW']

print(result_data['list_total_count'])
print(result_data['RESULT'])
print(result_data['row'][0])


# In[10]:


data_list = result_data['row']
sample_df = pd.DataFrame(data_list)
sample_df.head()


# In[11]:


def seoul_open_api_data(url, service):
    data_list = None
    try:
        result_dict = requests.get(url).json()
        result_data = result_dict[service]
        code = result_data['RESULT']['CODE']
        if code == 'INFO-000':
            data_list = result_data['row']
    except:
        pass
    return data_list


# In[12]:


sgg_url = 'http://openapi.seoul.go.kr:8088/{}/json/SdeTlSccoSigW/1/25'.format(SEOUL_API_AUTH_KEY)
sgg_data_list = seoul_open_api_data(url, 'SdeTlSccoSigW')
sgg_data_list[0]


# In[13]:


columns = ['SIG_CD','SIG_KOR_NM','LAT','LNG']
sgg_df = pd.DataFrame(data=sgg_data_list, columns=columns)
sgg_df.head()


# In[14]:


sgg_df.columns = ['시군구코드','시군구명','위도','경도']
sgg_df.head()


# In[15]:


sgg_df.info()


# In[17]:


sgg_df.to_excel('D:/Kangjh/Seoul_data/seoul_sgg_list.xlsx', index=False)


# In[22]:


pop_data_list = pd.read_excel('D:\Kangjh\Seoul_data/Jumin_Ingu.xlsx',
                             header=2,
                             usecols= 'A:D',
                             engine='openpyxl')

sgg_pop_df = pd.DataFrame(data = pop_data_list)


# In[23]:


sgg_pop_df.head()


# In[24]:


sgg_pop_df.info()


# In[25]:


condition = sgg_pop_df['자치구'] != '합계'
sgg_pop_df_selected = sgg_pop_df[condition]
sgg_pop_df_selected.head(10)


# In[26]:


sgg_pop_df_selected.info()


# In[27]:


columns = ['자치구', '계']
sgg_pop_df_final = sgg_pop_df_selected[columns]


# In[28]:


sgg_pop_df_final.head()


# In[29]:


sgg_pop_df_final.columns = ['시군구명', '주민등록인구']
sgg_pop_df_final.info()
sgg_pop_df_final.head()


# In[30]:


sgg_pop_df_final.to_excel('D:/Kangjh/Seoul_data/sgg_pop.xlsx', index=False)


# In[35]:


biz_data_list = pd.read_excel('D:\Kangjh\Seoul_data/Saneop.xlsx', engine='openpyxl')

sgg_biz_df = pd.DataFrame(data = biz_data_list)


# In[ ]:




