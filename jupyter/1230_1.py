#!/usr/bin/env python
# coding: utf-8

# ## 구글 트랜드는 구글에서 제공하는 검색서비스

# In[1]:


get_ipython().system('pip install pytrends')
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import os

keyword = "Galaxy Phone"
period = "today 3-m"

trend_obj = TrendReq()
trend_obj.build_payload(kw_list=[keyword], timeframe=period)

trend_df = trend_obj.interest_over_time()
print(trend_df.head())

plt.style.use("ggplot")
plt.figure(figsize=(14,5))
trend_df[keyword].plot()
plt.title("Google Trends over time", size=15)
plt.legend(labels=[keyword], loc="upper right")

cwd = os.getcwd()
plt.show()


# In[51]:


from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import os

keyword = "Maple Story"
period = "today 3-m"

trend_obj = TrendReq()
trend_obj.build_payload(kw_list=[keyword], timeframe=period)

trend_df = trend_obj.interest_over_time()
print(trend_df.head())

plt.style.use("ggplot")
plt.figure(figsize=(14,5))
trend_df[keyword].plot()
plt.title("Google Trends over time", size=15)
plt.legend(labels=[keyword], loc="upper right")

cwd = os.getcwd()
plt.show()


# ## 멜론 크롤링 결과를 엑셀로 저장하기

# In[35]:


from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('D:/Kangjh/chromedriver.exe')
url = 'http://www.melon.com/chart/index.htm'
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')


# In[33]:


song_data = []
rank = 1

songs = soup.select('table > tbody > tr')
for song in songs:
    title = song.select('div.rank01 > span > a')[0].text
    singer = song.select('div.rank02 > a')[0].text
    song_data.append(['Melon',rank,title,singer])
    rank = rank+1


# In[36]:


import pandas as pd
columns = ['서비스', '순위', '타이틀', '가수']
pd_data = pd.DataFrame(song_data, columns = columns)
pd_data.head(100)


# In[57]:


pd_data.to_excel('D:/Kangjh/music/melon.xlsx', index=False)


# In[37]:


from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('D:/Kangjh/chromedriver.exe')
url = 'https://maplestory.nexon.com/'
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')


# ## 버즈 웹크롤링

# In[38]:


from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('D:/Kangjh/chromedriver.exe')
url = 'https://music.bugs.co.kr/chart'
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')


# In[39]:


songs = soup.select('tr')
print(len(songs))


# In[40]:


songs = soup.select('tbody > tr')
print(len(songs))


# In[41]:


songs = soup.select('table > tbody > tr')
print(len(songs))


# In[42]:


songs = soup.select('table.byChart > tbody > tr')
print(len(songs))


# In[43]:


print(songs[0])


# In[44]:


song = songs[0]


# In[45]:


title = song.select('a')
len(title)


# In[46]:


title = song.select('p > a')
len(title)


# In[47]:


title = song.select('p.title > a')[0].text
title


# In[48]:


singer = song.select('p.artist > a')[0].text.strip()
singer


# In[52]:


songs = soup.select('table.byChart > tbody > tr')
for song in songs:
    title = song.select('p.title > a')[0].text
    singer = song.select('p.artist > a')[0].text
    print(title, singer, sep = '|')


# In[53]:


song_data = []
rank = 1
songs = soup.select('table.byChart > tbody > tr')
for song in songs:
    title = song.select('p.title > a')[0].text
    singer = song.select('p.artist > a')[0].text
    song_data.append(['Bugs', rank, title, singer])
    rank= rank+1


# In[54]:


import pandas as pd
columns = ['서비스', '순위', '타이틀', '가수']
pd_data = pd.DataFrame(song_data, columns=columns)
pd_data.info()


# In[56]:


pd_data.to_excel('D:/Kangjh/music/bugs.xlsx', index=False)


# ## 지니 웹크롤링

# In[60]:


from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('D:/Kangjh/chromedriver.exe')
url='https://www.genie.co.kr/chart/top200'
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')


# In[62]:


songs = soup.select('tr')
print(len(songs))


# In[64]:


songs = soup.select('tbody > tr')
print(len(songs))


# In[65]:


songs = soup.select('table > tbody > tr')
print(len(songs))


# In[134]:


songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
print(len(songs))


# In[135]:


song_data = []
rank = 1
songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
for song in songs:
    title = song.select('td.info > a.title.ellipsis')[0].text
    singer = song.select('td.info > a.artist.ellipsis')[0].text
    song_data.append(['Genie', rank, title, singer])
    rank= rank+1


# In[136]:


import pandas as pd
columns = ['서비스', '순위', '타이틀', '가수']
pd_data = pd.DataFrame(song_data, columns=columns)
pd_data.info()


# In[137]:


songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
for song in songs:
    title = song.select('td.info > a.title.ellipsis')[0].text.strip()
    singer = song.select('td.info > a.artist.ellipsis')[0].text.strip()
    print(title, singer, sep = '|')


# In[ ]:




