#!/usr/bin/env python
# coding: utf-8

# ## 인스타그램 크롤링

# ### 인스타그램 접속 후 로그인하기

# In[22]:


from selenium import webdriver

driver = webdriver.Chrome("D:/Kangjh/chromedriver.exe")


# In[23]:


import time

driver.get('https://www.instagram.com/')
time.sleep(2)


# In[24]:


email = 'jee8863@naver.com'
input_id = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[0]
input_id.clear()
input_id.send_keys(email)

password ='kangji1405!'
input_pw = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[1]
input_pw.clear()
input_pw.send_keys(password)
input_pw.submit()
time.sleep(3)


# #### url 함수 만들기

# In[13]:


def insta_searching(word):
    url = 'https://www.instagram.com/explore/tags/' + word
    return url


# In[14]:


word = "제주도맛집"
url = insta_searching(word)
driver.get(url)


# #### 첫 번째 게시글 열기

# In[15]:


def select_first(driver):
    first = driver.find_element_by_css_selector("div._9AhH0")
    first.click()
    time.sleep(3)

select_first(driver)


# In[28]:


import re
from bs4 import BeautifulSoup
import unicodedata

def get_content(driver):
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    
    try:
        content = soup.select('div.C4VMK > span')[0].text
        content = unicodedata.normalize('NFC', content)
    except:
        content = ' '
    
    tags = re.findall(r'#[^\s#,\\]+', content)
    
    date = soup.select('time._1o9PC.Nzb55')[0]['datetime'][:10]
    
    try:
        like = soup.select('div.wpO6b > button')[0].text[4:-1]
    except:
        like = 0
    
    try:
        place = soup.select('div.M30cS')[0].text
        place = unicodedata.normalize('NFC', place)
    except:
        place=''
        
    data = [content, date, like, place, tags]
    return data

get_content(driver)


# #### 다음 게시글 열기

# In[29]:


def move_next(driver):
    
    right = driver.find_element_by_css_selector('a.coreSpriteRightPaginationArrow')
    right.click()
    time.sleep(3)

move_next(driver)


# #### 여러 게시글 정보 수집하기

# In[30]:


word = "제주도맛집"
url = insta_searching(word)

driver.get(url)
time.sleep(3)

select_first(driver)

results = [ ]

target = 50
for i in range(target):
    try:
        data = get_content(driver)
        results.append(data)
        move_next(driver)
    except:
        time.sleep(2)
        move_next(driver)
    

print(results[:2])


# In[31]:


import pandas as pd

results_df = pd.DataFrame(results)
results_df.columns = ['content','data','like','place','tags']
results_df.to_excel('D:/Kangjh/jeju/crawling_jejuMatjip.xlsx')


# In[ ]:




