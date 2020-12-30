#!/usr/bin/env python
# coding: utf-8

# In[4]:


import requests
from bs4 import BeautifulSoup


base_url = "https://news.google.com"
search_url = base_url + "/search?q=%ED%8C%8C%EC%9D%B4%EC%8D%AC&hl=ko&gl=KR&ceid=KR%3Ako"
resp = requests.get(search_url)
html_src = resp.text
soup = BeautifulSoup(html_src, 'html.parser')
news_items = soup.select('div[class="xrnccd"]')
print(len(news_items))
print(news_items[0])
print("\n")
print("========================")

for item in news_items[:3]:
    link = item.find('a', attrs={'class':'VDXfz'}).get('href')
    news_link = base_url + link[1:]
    print(news_link)
    
    news_title = item.find('a',attrs={'class':'DY5T1d'}).getText()
    print(news_title)
    
    news_content = item.find('span', attrs={'class':'xBbh9'}).text
    print(news_content)
    
    news_agency = item.find('a', attrs={'class':'wEwyrc AVN2gc uQIVzc Sksgp'}).text
    print(news_agency)
    
    news_reporting = item.find('time', attrs={'class':'WW6dff uQIVzc Sksgp'})
    news_reporting_datetime = news_reporting.get('datetime').split('T')
    news_reporting_date = news_reporting_datetime[0]
    news_reporting_time = news_reporting_datetime[1][:-1]
    print(news_reporting_date,news_reporting_time)
    print("\n")
    
def google_news_clipping(url, limit=5):
    
    resp = requests.get(url)
    html_src = resp.text
    soup = BeautifulSoup(html_src, 'html.parser')
    
    news_items = soup.select('div[class="xrnccd"]')
    
    links=[]; titles=[]; contents=[]; agencies=[]; reporting_dates=[]; reporting_times=[];
    
    for item in news_items[:limit]:
        link = item.find('a', attrs={'class':'VDXfz'}).get('href')
        news_link = base_url + link[1:]
        links.append(news_link)
        
        news_title = item.find('a', attrs={'class':'DY5T1d'}).getText()
        titles.append(news_title)
        
        news_content = item.find('span', attrs={'class':'xBbh9'}).text
        contents.append(news_content)
        
        news_agency = item.find('a', attrs={'class':'wEwyrc AVN2gc uQIVzc Sksgp'}).text
        agencies.append(news_agency)
        
        news_reporting = item.find('time', attrs={'class':'WW6dff uQIVzc Sksgp'})
        news_reporting_datetime = news_reporting.get('datetaime').split('T')
        news_reporting_date = news_reporting_datetime[0]
        news_reporting_time = news+reporting_datetime[1][:-1]
        reporting_dates.append(news_reporting_date)
        reporting_times.append(news_reporting_time)
    
    result = {'link':links, 'title':titles, 'contents':contents, 'agency':agencies,               'date':reporting_dates, 'time':reporting_times}
    
    return result


news = goolgle_news_clipping(search_url, 2)
print(news)
    
    


# In[ ]:


from selenium import webdriver

driver = webdriver.Chrome("D:/Kangjh/chromedriver")

driver.implicitly_wait(3)

driver.get("https://www.danawa.com/")

login = driver.find_element_by_css_selector('li.my_page_service')


# In[ ]:




