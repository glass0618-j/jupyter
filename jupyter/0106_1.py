#!/usr/bin/env python
# coding: utf-8

# ## 지도 시각화

# #### 데이터 준비

# In[3]:


import pandas as pd
raw_total = pd.read_excel('C:/Users/Administrator/data/1_crawling_raw.xlsx', engine='openpyxl')
raw_total.head()


# In[5]:


raw_total.info()


# In[4]:


#위치 정보 가져오기
location_counts = raw_total['place'].value_counts( ) #빈도수 집계
location_counts


# In[6]:


#등록된 위치정보별 빈도수 데이터
location_counts_df = pd.DataFrame(location_counts)
location_counts_df.head()


# In[7]:


#위치 정보 빈도수 데이터 저장하기
location_counts_df.to_excel('D:/Kangjh/jeju/location_counts.xlsx')


# In[8]:


#위치 정보 종류 확인하기
locations = list(location_counts.index)
locations


# ### 카카오 검색 API를 활용한 장소 검색

# In[9]:


import requests

searching = '합정 스타벅스'
url = 'https://dapi.kakao.com/v2/local/search/keyword.json?query={}'.format(searching)

headers = {
    "Authorization": "KakaoAK 2a3163e89d7c98fbbfa828ba308f9d69"
}

places = requests.get(url, headers = headers).json()['documents']
places


# In[10]:


import requests

searching = '광주광역시청'
url = 'https://dapi.kakao.com/v2/local/search/keyword.json?query={}'.format(searching)

headers = {
    "Authorization": "KakaoAK 2a3163e89d7c98fbbfa828ba308f9d69"
}

places = requests.get(url, headers = headers).json()['documents']
places


# In[11]:


#카카오 로컬 API를 활용한 장소 검색 함수 만들기
def find_places(searching):
    url = 'https://dapi.kakao.com/v2/local/search/keyword.json?query={}'.format(searching)
    headers = {
        "Authorization": "KakaoAK 2a3163e89d7c98fbbfa828ba308f9d69"
    }
    places = requests.get(url, headers = headers).json()['documents']
    place = places[0]
    name = place['place_name']
    x = place['x']
    y = place['y']
    data = [name, x, y, searching]
    
    return data


# In[14]:


data = find_places('유스퀘어')
data


# In[ ]:


from tqdm.notebook import tqdm


# In[19]:


import time
locations_inform = [ ]
for location in tqdm(locations):
    try:
        data = find_places(location)       
        locations_inform.append(data) 
        time.sleep(0.5) 
    except:
        pass
locations_inform


# In[20]:


locations_inform_df = pd.DataFrame(locations_inform)
locations_inform_df.columns = ['name_official','경도','위도','인스타위치명']
locations_inform_df.to_excel('D:/Kangjh/jeju/locations.xlsx', index=False)


# In[24]:


# 인스타 게시량 및 위치정보 데이터 불러오기
location_counts_df = pd.read_excel('D:/Kangjh/jeju/location_counts.xlsx', index_col = 0, engine='openpyxl')
locations_inform_df = pd.read_excel('D:/Kangjh/jeju/locations.xlsx', engine='openpyxl')
location_counts_df.head()


# In[25]:


locations_inform_df.head()


# In[26]:


#위치 데이터 병합하기
location_data = pd.merge(locations_inform_df, location_counts_df, 
                         how = 'inner', left_on = 'name_official', right_index=True)
location_data.head()


# In[27]:


#데이터 중복 점검하기
location_data['name_official'].value_counts()


# In[33]:


#장소 이름 기준 병합하기
location_data = location_data.pivot_table(index = ['name_official','경도','위도'], values = 'place', aggfunc='sum')
location_data.head()


# In[34]:


location_data.to_excel('D:/Kangjh/jeju/location_inform.xlsx')


# In[35]:


location_data = pd.read_excel('D:/Kangjh/jeju/location_inform.xlsx', engine='openpyxl')
location_data.info()


# In[36]:


#지도 표시하기
import folium

Mt_Hanla = [33.362500, 126.533694]
map_jeju = folium.Map(location = Mt_Hanla, zoom_start = 11)

for i in range(len(location_data)):
    name = location_data ['name_official'][i]
    count = location_data ['place'][i]
    size = int(count)*2
    long = float(location_data['위도'][i])
    lat = float(location_data['경도'][i])
    folium.CircleMarker((long,lat), radius = size, color='red', popup=name).add_to(map_jeju)

map_jeju


# In[37]:


map_jeju.save('D:/Kangjh/jeju/jejumapu.html')
#크롬으로 열기


# In[38]:


#지도 표시하기(마커 집합)
from folium.plugins import MarkerCluster
locations = []
names = []

for i in range(len(location_data)):
    data = location_data.iloc[i]
    locations.append((float(data['위도']),float(data['경도'])))
    names.append(data['name_official'])

Mt_Hanla =[33.362500, 126.533694]
map_jeju2 = folium.Map(location = Mt_Hanla, zoom_start = 11)
                       
marker_cluster = MarkerCluster(
    locations=locations, popups=names,
    name='Jeju',
    overlay=True,
    control=True,
)

marker_cluster.add_to(map_jeju2)
folium.LayerControl().add_to(map_jeju2)

map_jeju2


# In[39]:


map_jeju2.save('D:/Kangjh/jeju/jeju_cluster.html')


# In[ ]:




