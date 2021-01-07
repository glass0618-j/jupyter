#!/usr/bin/env python
# coding: utf-8

# ### 스타벅스 사이트 크롤링

# In[2]:


from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


# In[3]:


driver = webdriver.Chrome('D:/Kangjh/chromedriver.exe')
url = 'https://www.starbucks.co.kr/store/store_map.do?disp=locale'
driver.get(url)


# In[5]:


seoul_btn = '#container > div > form > fieldset > div > section > article.find_store_cont > article > article:nth-child(4) > div.loca_step1 > div.loca_step1_cont > ul > li:nth-child(1) > a'
driver.find_element_by_css_selector(seoul_btn).click()


# In[6]:


all_btn = '#mCSB_2_container > ul > li:nth-child(1) > a'
driver.find_element_by_css_selector(all_btn).click()


# In[7]:


html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')


# In[8]:


starbucks_soup_list = soup.select('li.quickResultLstCon')
print(len(starbucks_soup_list))


# In[9]:


starbucks_soup_list[0]


# In[11]:


#스타벅스 매장 정보 샘플 확인
starbucks_store = starbucks_soup_list[0]
name = starbucks_store.select('strong')[0].text.strip()
lat = starbucks_store['data-lat'].strip()
lng = starbucks_store['data-long'].strip()
store_type = starbucks_store.select('i')[0]['class'][0][4:]
address = str(starbucks_store.select('p.result_details')[0]).split('<br/>')[0].split('>')[1]
tel = str(starbucks_store.select('p.result_details')[0]).split('<br/>')[1].split('<')[0]

print(name)
print(lat)
print(lng)
print(store_type)
print(address)
print(tel)


# In[12]:


#서울시 스타벅스 매장 목록 데이터 만들기
starbucks_list = []
for item in starbucks_soup_list:
    name = item.select('strong')[0].text.strip();
    lat = item['data-lat'].strip()
    lng = item['data-long'].strip()
    store_type = item.select('i')[0]['class'][0][4:]
    address = str(item.select('p.result_details')[0]).split('<br/>')[0].split('>')[1]
    tel = str(item.select('p.result_details')[0]).split('<br/>')[1].split('<')[0]
    
    starbucks_list.append( [ name, lat, lng, store_type, address, tel])


# In[13]:


#pandas의 데이터프레임 생성
columns = ['매장명','위도','경도','매장타입', '주소','전화번호']
seoul_starbucks_df = pd.DataFrame(starbucks_list, columns = columns)
seoul_starbucks_df.head()


# In[14]:


seoul_starbucks_df.info()


# In[15]:


seoul_starbucks_df.to_excel('D:/Kangjh/starbucks/seoul_starbucks_list.xlsx', index=False)


# In[ ]:




