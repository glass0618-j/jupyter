#!/usr/bin/env python
# coding: utf-8

# ## 유튜브 랭킹 데이터 수집하기

# In[1]:


from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd


# In[2]:


browser = webdriver.Chrome('D:/Kangjh/chromedriver.exe')
url = "https://youtube-rank.com/board/bbs/board.php?bo_table=youtube"
browser.get(url)


# In[3]:


html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')


# In[7]:


channel_list = soup.select('tr')
print(len(channel_list),'\n')
print(channel_list[101])


# In[8]:


channel_list = soup.select('form > table > tbody > tr')
print(len(channel_list),'\n')


# In[9]:


channel = channel_list[0]
print(channel)


# In[10]:


category = channel.select('p.category')[0].text.strip()
print(category)


# In[11]:


title = channel.select('h1 > a')[0].text.strip()
print(title)


# In[12]:


subscriber = channel.select('.subscriber_cnt')[0].text
view = channel.select('.view_cnt')[0].text
video = channel.select('.video_cnt')[0].text

print(subscriber)
print(view)
print(video)


# In[13]:


channel_list = soup.select('tbody > tr')
for channel in channel_list:
    title = channel.select('h1 > a')[0].text.strip()
    category = channel.select('p.category')[0].text.strip()
    subscriber = channel.select('.subscriber_cnt')[0].text
    view = channel.select('.view_cnt')[0].text
    video = channel.select('.video_cnt')[0].text
    print(title, category, subscriber, view, video)


# In[14]:


page = 1
url = 'https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&page={}'.format(page)
print(url)


# In[23]:


get_ipython().system('pip install openpyxl')
results = []
for page in range(1,11):
    url = f"https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&page={page}"
    browser.get(url)
    time.sleep(2)
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    channel_list = soup.select('form > table > tbody > tr')
    for channel in channel_list:
        title = channel.select('h1 > a')[0].text.strip()
        category = channel.select('p.category')[0].text.strip()
        subscriber = channel.select('.subscriber_cnt')[0].text
        view = channel.select('.view_cnt')[0].text
        video = channel.select('.video_cnt')[0].text
        data = [title, category, subscriber, view, video]
        results.append(data)


# In[35]:


df =pd.DataFrame(results)
df.cloumns = ['title', 'category', 'subscriber', 'view', 'video']
df.to_excel('D:/Kangjh/music/youtube_rank.xlsx', index=False)


# ## 유튜브 랭킹 데이터 시각화하기

# In[40]:


import pandas as pd
import matplotlib.pyplot as plt


# In[41]:


from matplotlib import font_manager, rc
import platform
if platform.system() == 'Windows':
    path = 'c:/Windows/Fonts/gulim.ttc'
    font_name = font_manager.FontProperties(fname = path).get_name()
    rc('font', family = font_name)
elif platform.system() == 'Darwin':
    rc('font', family = 'AppleGothic')
else:
    print('Check your OS system')


# In[42]:


df = pd.read_excel('D:/Kangjh/music/youtube_rank.xlsx' )
df.head()


# In[43]:


df['subscriber'][0:10]


# In[44]:


df['subscriber'].str.replace('만','0000')[0:10]


# In[45]:


df.info()


# In[ ]:





# In[ ]:


pivot_df = pivot_df.sort_values(by = 'subscriber_sum', ascending=False)
pivot_df.head(50)


# In[ ]:


plt.figure(figsize = (30,10))
plt.pie(pivot_df['subscriber_sum'], labels=pivot_df['category'], autopct='%1.1f%%')
plt.show()


# In[ ]:


pivot_df = pivot_df.sort_values(by='category_count', ascending=False)
pivot_df.head()
plt.figure(figsize = (30,10))
plt.pie(pivot_df['category_count'], labels=pivot_df['category'], autopct='%1.1f%%')
plt.show()


# ## 멜론, 벅스, 지니 크롤링 엑셀 파일 통합하기

# In[60]:


get_ipython().system('pip install openpyxl')
import pandas as pd

excel_names = ['D:/Kangjh/music/melon.xlsx','D:/Kangjh/music/bugs.xlsx','D:/Kangjh/music/genie.xlsx']

appended_data = pd.DataFrame()
for name in excel_names:
    pd_data = pd.read_excel(name)
    appended_data = appended_data.append(pd_data)


# In[61]:


appended_data.info()


# In[62]:


appended_data.to_excel('D:/Kangjh/music/total.xlsx', index=False)


# In[ ]:




