#!/usr/bin/env python
# coding: utf-8

# # 멕시코풍 프랜차이즈 Chipotle의 주문 데이터 분석하기

# ## 1.데이터의 기초 정보 살펴보기

# In[1]:


import pandas as pd

file_path = '../data/chipotle.tsv'
chipo = pd.read_csv(file_path, sep = '\t')


# In[2]:


print(chipo.shape)
print("=====================")
print(chipo.info())


# In[3]:


chipo.head(10)


# In[4]:


print(chipo.columns)
print("======================================")
print(chipo.index)


# In[5]:


chipo['order_id'] = chipo['order_id'].astype(str)


# In[6]:


print(chipo.describe())


# In[7]:


print(len(chipo['order_id'].unique()))
print(len(chipo['item_name'].unique()))


# ## 2. 탐색과 시각화

# In[8]:


# 가장 많이 주문한 아이템 10개 출력
item_count = chipo['item_name'].value_counts()[:10]
for idx, (val, cnt) in enumerate(item_count.iteritems(),1):
    print("Top", idx, ":", val, cnt)


# In[9]:


chipo['item_name'].value_counts().index.tolist()[0]


# In[12]:


## item당 주문 개수 출력
order_count = chipo.groupby('item_name')['order_id'].count()
order_count[:10]


# In[12]:


item_quantity = chipo.groupby('item_name')['quantity'].sum()
item_quantity[:10]
# item당 주문 총량을 출력


# In[13]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt

item_name_list = item_quantity.index.tolist()
x_pos = np.arange(len(item_name_list))
order_cnt = item_quantity.values.tolist()

plt.bar(x_pos,order_cnt, align='center')
plt.ylabel('ordered_item-count')
plt.title('Distribution of all order item')

plt.show()


# In[15]:


# 아이템 가격 히스토그램을 출력
plt.hist('item_price')
plt.ylabel('counts')
plt.title('Histogram of item price')

plt.show()


# In[23]:


chipo['item_price']=chipo['item_price'].apply(lambda x: float(x[1:]))
chipo.describe()


# In[24]:


# 가장 비싼 주문에서 item이 총 몇 개 팔렸는지 계산
chipo.groupby('order_id').sum().sort_values(by='item_price',ascending=False)[:5]


# In[18]:


chipo_salad = chipo[chipo['item_name']=="Veggie Salad Bowl"]
chipo_salad = chipo_salad.drop_duplicates(['item_name','order_id'])
print(len(chipo_salad))
chipo_salad.head(50)


# In[25]:


chipo.groupby('order_id')['item_price'].sum()


# In[26]:


chipo.groupby('order_id')['item_price'].sum().describe()[:10]


# In[27]:


chipo_orderid_group = chipo.groupby('order_id').sum()
results = chipo_orderid_group[chipo_orderid_group.item_price >= 10]

print(results[:10])
print(results.index.values)


# In[28]:


chipo_one_item = chipo[chipo.quantity==1]
price_per_item = chipo_one_item.groupby('item_name').min()
price_per_item.sort_values(by = 'item_price',ascending=False)[:10]


# In[29]:


chipo_chicken = chipo[chipo['item_name']=='Chicken Bowl']
chipo_chicken_ordersum = chipo_chicken.groupby('order_id').sum()['quantity']
chipo_chicken_result = chipo_chicken_ordersum[chipo_chicken_ordersum >= 2]

print(len(chipo_chicken_result))
chipo_chicken_result.head(5)


# In[30]:


ac = chipo[chipo['item_name']=="Chicken Bowl"]
acr = ac[ac['quantity']>=2]
print(len(acr))
acr.head(5)


# In[ ]:




