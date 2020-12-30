#!/usr/bin/env python
# coding: utf-8

# # 파이썬 기본실습

# In[6]:


print("hello")
print("my name is kangjh")


# ## pandas 사용법

# In[5]:


get_ipython().system('pip install pandas')


# In[8]:


import pandas as pd


# In[12]:


names = ['Bob','Jessica','Mary','John','Mel']
births = [1986, 1752, 1956, 1958, 2016]
custom = [1, 5, 45, 123, 666]
BabyDataSet = list(zip(names,births))
df = pd.DataFrame(data = BabyDataSet, columns=['Names','Births'])


# In[14]:


df.head()
#()안에 3넣으면 위에서부터 세 개만 나옴!


# In[15]:


print(df.dtypes)
print("==========")

print(df.index)
print("==========")

print(df.columns)


# In[16]:


df['Names']
#까먹지말기! 데이터프레임의 하나의 열을 선택한다.


# In[18]:


#0~3 번째 인덱스를 선택한다
df[0:3]


# In[19]:


#Births 열이 100보다 큰 데이터를 선택
df[df['Births']>100]


# In[20]:


#데이터프레임에서의 평균값을 계산한다
df.mean()


# In[21]:


df.sum()


# ## numpy 사용법

# In[23]:


# numpy는 파이썬의 고성능 과학 계산용 패키지


# In[25]:


import numpy as np


# In[26]:


arr1 = np.arange(15).reshape(3,5)
print(arr1)
# 3행 5열로 바꾼다는 말


# In[27]:


arr1.shape


# In[28]:


arr1.dtype


# In[29]:


arr2 = np.array([6,7,8])
print(arr2)


# In[30]:


arr3 = np.zeros((3,4))
print(arr3)


# In[31]:


arr4 = np.array([
    [1,2,3],
    [4,5,6]
], dtype = np.float64)

arr5 = np.array([
    [7,8,9],
    [10,11,12]
], dtype = np.float64)

print("arr4 + arr5 = ")
print(arr4+arr5,"\n")
print("arr4 - arr5 = ")
print(arr4-arr5,"\n")
print("arr4 * arr5 = ")
print(arr4*arr5,"\n")
print("arr4 / arr5 = ")
print(arr4/arr5,"\n")


# ## matplotlib 사용법

# In[35]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


# In[33]:


y = df['Births']
x = df['Names']

plt.bar(x,y)
plt.xlabel('Names')
plt.ylabel('Births')
plt.title('Bar plot')
plt.show()


# In[38]:


#랜덤 추출 시드 고정
np.random.seed(19920613)

#scatter plot 데이터 생성
x = np.arange(0.0, 100.0, 5.0)
y = (x*1.5)+np.random.rand(20) * 50

#scatter plot 출력
plt.scatter(x, y, c="r", alpha=0.5, label="scatter point")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc='upper left')
plt.title('Scatter plot')
plt.show()


# In[ ]:




