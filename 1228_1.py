#!/usr/bin/env python
# coding: utf-8

# ## 1.웹서버에 요청하고 응답받기

# #### 1.웹서버에 웹 페이지 정보를 보내달라고 요청(request)
# #### 2. 웹서버가 웹 브라우저의 요정을 받다 웹페이지 정보를 보내는 과정 응답(response)

# In[2]:


import requests

url = "https://www.python.org/"
resp = requests.get(url)
print(resp)

urtl = "https://www.python.org/1"
resp = requests.get(url)
print(resp)


# ## 2.웹페이지 소스코드

# #### 웹서버의 응답 객체는 headers, cookies, text 등의 속성을 가짐
# #### 소스 코드를 확인하려면 text 속성 지정

# In[3]:


import requests

url = "https://www.python.org/"
resp = requests.get(url)

html = resp.text
print(html)


# ## 3. 로봇배제 표준

# #### 1. 로봇 배제 표준 "웹사이트에 로봇이 접근하는 것을 방지하기 위한 규약으로"
# ####    "일반적으로 접근 제한에 대한 설명을 robots.txt에 기술한다."고 설명
# #### 2. 대부분의 사이트들이 웹크롤링 로봇의 접근 권한에 대하여 설정, 웹페이지의 접근하기 전에 로봇 배제
# #### 표준을 확인, 가이드 라인 준수가 필요

# In[4]:


urls = ["https://www.naver.com/", "https://www.python.org/"]
filename = "robots.txt"

for url in urls:
    file_path = url+filename
    print(file_path)
    resp = requests.get(file_path)
    print(resp.text)
    print("\n")


# ## 4.BeautifulSoup 객체

# #### 1. 웹 서버로부터 HTML 소스코드를 가져온 다음에는 HTM 태그로 해석하기 위한 과정이 필요
# #### 2. HTML 소스코드를 해석하는 것을 parsing
# #### 3. HTML 문서에 정보를 추출하기 위해 BeautifulSoup 라이브러리 사용

# In[5]:


#import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
html_src = resp.text

soup = BeautifulSoup(html_src, 'html.parser')
print(type(soup))
print("\n")

print(soup.head)
print("\n")
print(soup.body)
print("\n")

print('title 태그 요소: ',soup.title)
print('title 태그 이름: ',soup.title.name)
print('title 태그 문자열: ',soup.title.string)


# ## 5.크롬 개발자 도구

# In[6]:


import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
html_src = resp.text

soup = BeautifulSoup(html_src, 'html.parser')

first_img = soup.find(name='img')
print(first_img)
print("\n")

target_img = soup.find(name='img', attrs={'alt':'Seoul-Metro-2004-20070722.jpg'})
print(target_img)


# ## 6.이미지 파일 저장

# #### 1. find() 함수는 HTML 문서에서 가장 처음으로 만나는 태그를 한 개 찾는다.

# In[12]:


import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
html_src = resp.text

soup = BeautifulSoup(html_src, 'html.parser')

target_img = soup.find(name='img', attrs={'alt':'Seoul-Metro-2004-20070722.jpg'})
print('HTML 요소: ', target_img)
print("\n")

target_img_src = target_img.get('src')
print('이미지 파일 경로: ', target_img_src)
print("\n")

target_img_resp = requests.get('http:' + target_img-src)
out_file_path = "./images/download_image.jpg"

with open(out_file_path, 'wb') as out_file:
    out_file.write(target_img_resp.content)
    print("이미지 파일로 저장하였습니다.")


# ## 7.웹 문서에 포함된 모든 하이퍼링크 추출

# #### 같은 조건을 만족하는 모든 태그를 찾을 때 find_all()

# In[13]:


import requests, re
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
html_src = resp.text
soup = BeautifulSoup(html_src, 'html.parser')

links = soup.find_all("a")
print("하이퍼링크의 개수: ",len(links))
print("\n")
print("첫 3개의 원소: ",links[:3])
print("\n")

wiki_links = soup.find_all(name="a", href=re.compile("/wiki/"), limit=3)
print("/wiki/ 문자열이 포함된 하이퍼링크: ",wiki_links)
print("\n")

external_links = soup.find_all(name="a", attrs={"class":"external text"}, limit=3)
print("class 속성으로 추출한 하이퍼링크: ", external_links)


# ## 8.CSS Select 활용1

# #### BeautifulSoup에서는 select() 메소드에 CSS 선택자를 매개변수로 전달하는 방법을 사용
# #### select()는 해당하는 태그를 모두 찾아서 리스트로 리턴

# In[15]:


import requests
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
html_src = resp.text
soup = BeautifulSoup(html_src, 'html.parser')

subway_image = soup.select('#mw-content-text > div > table:nth-child(3) > \
                            tbody > tr:nth-child(2) > td > a > img')
print(subway_image)
print("\n")
print(subway_image[0])
print("\n")
subway_image2 = soup.select('tr > td > a > img')
print(subway_image2[1])


# ## 9.CSS Select 활용2

# #### 클래스 선택자 '.' id 선택자 '#'

# In[16]:


import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
html_src = resp.text
soup = BeautifulSoup(html_src, 'html.parser')

links = soup.select('a')
print(len(links))
print("\n")

print(links[:3])
print("\n")

external_links = soup.select('a[class="external text"]')
print(external_links[:3])
print("\n")

id_selector = soup.select('#siteNotice')
print(id_selector)
print("\n")

id_selector2 = soup.select('div#siteNotice')
print(id_selector2)
print("\n")

id_selector3 = soup.select('p#siteNotice')
print(id_selector3)
print("\n")

class_selector = soup.select('.mw-headline')
print(class_selector)
print("\n")

class_selector2 = soup.select('span.mw-headline')
print(class_selector2)

