#!/usr/bin/env python
# coding: utf-8

# ## 6.2.2 스타벅스 분석 데이터 만들기

# In[36]:


# 예제 6-42 라이브러리 임포트
import pandas as pd


# In[37]:


# 예제 6-43 시군구 목록 데이터 불러오기
seoul_sgg = pd.read_excel('D:/Kangjh/starbucks/seoul_sgg_list.xlsx')
seoul_sgg.head()


# In[38]:


seoul_starbucks = pd.read_excel('D:/Kangjh/starbucks/seoul_starbucks.xlsx', header=0)
seoul_starbucks.head()


# In[39]:


sgg_names = []
for address in seoul_starbucks['주소']:
    sgg = address.split()[1]
    sgg_names.append(sgg)
seoul_starbucks['시군구명'] = sgg_names
seoul_starbucks.head()


# In[14]:


seoul_starbucks.to_excel('D:/Kangjh/starbucks/seoul_starbucks_list.xlsx', index=False)


# In[40]:


# 예제 6-44 서울시 스타벅스 매장 목록 데이터 불러오기
seoul_starbucks = pd.read_excel('D:/Kangjh/starbucks/seoul_starbucks_list.xlsx')
seoul_starbucks.head()


# In[41]:


# 예제 6-45 시군구별 스타벅스 매장 수 세기
starbucks_sgg_count = seoul_starbucks.pivot_table(
                                                index = '시군구명',
                                                values='매장명', 
                                                aggfunc='count'
                                                ).rename(columns={'매장명':'스타벅스_매장수'})
starbucks_sgg_count.head()


# In[42]:


# 예제 6-46 서울시 시군구 목록 데이터에 스타벅스 매장 수 데이터를 병합
seoul_sgg = pd.merge(seoul_sgg, starbucks_sgg_count, how='left', on='시군구명')
seoul_sgg.head()


# In[43]:


# 예제 6-47 서울시 시군구별 인구통계 데이터 불러오기
seoul_sgg_pop = pd.read_excel('D:/Kangjh/starbucks/sgg_pop.xlsx')
seoul_sgg_pop.head()


# In[44]:


# 예제 6-48 서울시 시군구 목록 데이터에 서울시 시군구별 인구통계 데이터를 병합
seoul_sgg = pd.merge(seoul_sgg, seoul_sgg_pop, how='left', on='시군구명')
seoul_sgg.head()


# In[45]:


# 예제 6-49 서울시 시군구 목록 데이터에 서울시 시군구별 사업체 수 통계 데이터를 병합
seoul_sgg_biz = pd.read_excel('D:/Kangjh/starbucks/sgg_biz.xlsx')
seoul_sgg = pd.merge(
    seoul_sgg, 
    seoul_sgg_biz,
    how='left',
    on='시군구명'
)
seoul_sgg.head()


# In[26]:


# 예제 6-50 병합 결과를 엑셀 파일로 저장
seoul_sgg.to_excel('D:/Kangjh/starbucks/seoul_sgg_stat.xlsx', index=False)


# In[46]:


import pandas as pd
import folium
import json


# In[47]:


seoul_starbucks = pd.read_excel('D:/Kangjh/starbucks/seoul_starbucks_list.xlsx')
seoul_starbucks.head()


# In[61]:


starbucks_map = folium.Map(
    location = [37.573050, 126.979189],
    tiles = 'Stamen Terrain',
    zoom_start = 11
)
starbucks_map


# In[60]:


for idx in seoul_starbucks.index:
    lat = seoul_starbucks.loc[idx, '위도']
    lng = seoul_starbucks.loc[idx, '경도']
    
    folium.CircleMarker(
        location = [lat,lng],
        fill = True,
        fill_color = 'green',
        fill_opacity = 1,
        color = 'yellow',
        weight = 1,
        radius = 3
    ).add_to(starbucks_map)

starbucks_map


# In[32]:


starbucks_map.save('D:/Kangjh/starbucks/starbucks_map.html')


# In[59]:


starbucks_map2 = folium.Map(
    location = [37.573050, 126.979189],
    tiles = 'Stamen Terrain',
    zoom_start = 11
)

for idx in seoul_starbucks.index:
    lat = seoul_starbucks.loc[idx, '위도']
    lng = seoul_starbucks.loc[idx, '경도']
    store_type = seoul_starbucks.loc[idx, '매장타입']
    
    # 매장 타입별 색상 선택을 위한 조건문
    fillColor =''
    if store_type == 'general':
        fillColor = 'gray'
        size = 1
    elif store_type == 'reserve':
        fillColor = 'blue'
        size = 5
    elif store_type == 'generalDT':
        fillColor = 'red'
        size = 5
        
    folium.CircleMarker(
        location = [lat, lng],
        color = fillColor,
        fill = True,
        fill_color = fillColor,
        fill_opacity = 1,
        weight = 1,
        radius = size
    ).add_to(starbucks_map2)

starbucks_map2


# In[35]:


starbucks_map2.save('D:/Kangjh/starbucks/starbucks_map2.html')


# In[50]:


import pandas as pd
import folium
import json


# In[51]:


seoul_sgg_stat = pd.read_excel('D:/Kangjh/starbucks/seoul_sgg_stat.xlsx')
seoul_sgg_stat.head()


# In[52]:


sgg_geojson_file_path ='D:/Kangjh/starbucks/seoul_sgg.geojson'
seoul_sgg_geo = json.load(open(sgg_geojson_file_path, encoding='utf-8'))
seoul_sgg_geo['features'][0]['properties']


# In[55]:


starbucks_bubble = folium.Map(
    location = [37.573050, 126.979189],
    tiles = 'CartoDB dark_matter',
    zoom_start = 11
)


# In[58]:


def style_function(feature):
    return{
        'opacity':0.7,
        'weight':1,
        'color':'white',
        'fillOpacity':0,
        'dashArray':'5,5',
    }

folium.GeoJson(
    seoul_sgg_geo,
    style_function = style_function
).add_to(starbucks_bubble)

starbucks_bubble


# In[57]:


starbucks_mean = seoul_sgg_stat['스타벅스_매장수'].mean()
print(starbucks_mean)


# In[ ]:


for idx in seoul_sgg_stat.index:
    lat = seoul_sgg_stat.loc[idx, '위도']
    lng = seoul_sgg_stat.loc[idx, '경도']
    count = seoul_sgg_stat.loc[idx, '스타벅스_매장수']
    
    if count > starbucks_mean:
        fillColor = '#FF0000'
    else:
        fillColor = '#CCFF33'
        
    folium.CircleMarker(
        location = [lat, lng],
        color = 'FFFF00',
        fill_color = fillColor,
        fill_opacity = 0.7,
        weight = 1.5,
        radius = count/2
    ).add_to(starbucks_bubble)

starbucks_bubble


# In[ ]:


sgg_geojson_file_path = 'D:/Kangjh/starbucks/seoul_sgg.geojson'
seoul_sgg_geo_2 = json.load(open(sgg_geojson_file_path, encoding = 'utf-8'))
starbucks_choropleth = folium.Map(
    location = [37.573050, 126.979189],
    tiles = 'CartoDB dark_matter',
    zoom_start = 11
)

folium.Choropleth(
    geo_data = seoul_sgg_geo_2,
    data = seoul_sgg_stat,
    columns = ['시군구명', '스타벅스_매장수'],
    fill_color = 'YlGn',
    fill_opacity = 0.7,
    line_opacity = 0.5,
    key_on = 'properties.SIG_KOR_NM'
).add_to(starbucks_choropleth)

starbucks_choropleth


# In[62]:


#p.246
import pandas as pd
import json
import folium


# In[63]:


seoul_sgg_stat = pd.read_excel('D:/Kangjh/starbucks/seoul_sgg_stat.xlsx')
seoul_sgg_stat.head()


# In[64]:


sgg_geojson_file_path ='D:/Kangjh/starbucks/seoul_sgg.geojson'
seoul_sgg_geo = json.load(open(sgg_geojson_file_path, encoding='utf-8'))


# In[ ]:


starbucks_choropleth = folium.Map(
    location = [37.573050, 126.979189],
    tiles = 'CartoDB dark_matter',
    width = 700, height = 600,
    min_zoom = 10,
    max_zoom = 12,
    zoom_start = 11
)

folium.Choropleth(
    geo_data = seoul_sgg_geo_2,
    data = seoul_sgg_stat,
    columns = ['시군구명', '주민등록인구'],
    fill_color = 'YlGn',
    fill_opacity = 0.7,
    line_opacity = 0.5,
    key_on = 'properties.SIG_KOR_NM'
).add_to(starbucks_choropleth)

starbucks_choropleth


# In[68]:


sgg_geojson_file_path ='D:/Kangjh/starbucks/seoul_sgg.geojson'
seoul_sgg_geo = json.load(open(sgg_geojson_file_path, encoding='utf-8'))

viz_map_1 = folium.Map(
    location = [37.573050, 126.979189],
    tiles = 'CartoDB dark_matter',
    zoom_start = 11
)

def style_function(feature):
    return{
        'opacity':0.7,
        'weight':1,
        'color':'white',
        'fillOpacity':0
    }

folium.GeoJson(
    seoul_sgg_geo_1,
    style_function = style_function,
).add_to(viz_map_1)

#만 명당 매장 수 기준 상위 10% 추출 값
top = seoul_sgg_stat ['만명당_매장수'].quantile(0.9)
for idx in seoul_sgg_stat.index:
    lat = seoul_sgg_stat.loc[idx, '위도']
    lng = seoul_sgg_stat.loc[idx, '경도']
    r = seoul_sgg_stat.loc[idx, '만명당_매장수']
    if r > top:
        fillColor = '#FF3300'
    else:
        fillColor = '#CCFF33'
        
    folium.CircleMarker(
        location = [lat, lng],
        color = '#FFFF00',
        fill_color = fillColor,
        fill_opacity = 0.7,
        weight = 1.5,
        radius = r*10
    ).add_to(viz_map_1)
    
viz_map_1


# In[66]:


#인구 1만 명당 스타벅스 매장 수
seoul_sgg_stat['종사자수_만명당_매장수'] = seoul_sgg_stat['스타벅스_매장수'] / (seoul_sgg_stat['종사자수'] / 10000)
seoul_sgg_stat.head()


# In[67]:


seoul_sgg_geo_1 = json.load(open(SGG_GEOJSON_FILE_PATH, encoding = 'utf-8'))

viz_map_1 = folium.Map(
    location = [37.573050, 126.979189],
    tiles = 'CartoDB dark_matter',
    zoom_start = 11
)

folium.GeoJson(
    seoul_sgg_geo_1,
    style_function = style_function,
).add_to(viz_map_1)

top = seoul_sgg_stat ['종사자수_만명당_매장수'].quantile(0.9)
for idx in seoul_sgg_stat.index:
    name = seoul_sgg_stat.loc[idx, '시군구명']
    lat = seoul_sgg_stat.loc[idx, '위도']
    lng = seoul_sgg_stat.loc[idx, '경도']
    r = seoul_sgg_stat.loc[idx, '종사자수_만명당_매장수']
    
    if r > top:
        fillColor = '#FF3300'
    else:
        fillColor = '#CCFF33'
        
    folium.CircleMarker(
        location = [lat, lng],
        color = '#FFFF00',
        fill_color = fillColor,
        fill_opacity = 0.7,
        weight = 1.5,
        radius = r*10
    ).add_to(viz_map_1)
    
viz_map_1


# In[ ]:




