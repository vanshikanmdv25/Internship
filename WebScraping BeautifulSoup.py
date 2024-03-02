#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


from bs4 import BeautifulSoup
import requests


# In[3]:


page1 = requests.get('https://www.imdb.com/list/ls056092300/')
page1


# In[4]:


films = BeautifulSoup(page1.content,'html.parser')
films


# In[5]:


name = []
for i in films.find_all('div', class_='lister-item-content' ):
    n= i.find('a').text
    name.append(n)
    
name


# In[6]:


rating = []
for i in films.find_all('div', class_='ipl-rating-star small'):
        r = films.find('span', class_='ipl-rating-star__rating').text.strip()
        rating.append(r)
    
rating


# In[7]:


yearofrelease= []
for i in films.find_all('span',class_="lister-item-year text-muted unbold"):
    yearofrelease.append(i.text.strip())
    
yearofrelease


# In[8]:


print(len(name),len(rating),len(yearofrelease))


# In[9]:


import pandas as pd


# In[10]:


df1 = pd.DataFrame({'Name':name,'Ratings':rating,'YearOfRelease':yearofrelease})
df1


# In[11]:


page2 = requests.get('https://peachmode.com/search?q=bags')
page2


# In[12]:


products = BeautifulSoup(page2.content)
products


# In[73]:


product_name= []
for i in products.find_all('div',class_="product-title"):
    product_name.append(i.text)

print(product_name)


# In[14]:


discounted_price= []
for i in products.find_all('div', class_="product-prices"):
    dp= products.find('span',class_="discounted_price st-money money done").text.strip()
    discounted_price.append(dp)
    
discounted_price


# In[63]:


actual_price= []
for i in products.find_all('div', class_="product-prices"):
    ap= products.find('span',class_="price st-money money done").text
    actual_price.append(i.text)
    
actual_price


# In[ ]:


print(len(product_name),len(discounted_price),len(actual_price))


# In[15]:


page3= requests.get('https://www.keaipublishing.com/en/journals/artificial-intelligence-in-agriculture/most-downloaded-articles/')
page3


# In[18]:


journals= BeautifulSoup(page3.content,'html.parser')
journals


# In[21]:


paper_title= []
for i in journals.find_all('h2',class_='h5 article-title'):
    paper_title.append(i.text.strip())
    
paper_title


# In[22]:


date=[]
for i in journals.find_all('p',class_='article-date'):
    date.append(i.text)
    
date


# In[23]:


authors=[]
for i in journals.find_all('p',class_='article-authors'):
    authors.append(i.text)
    
authors


# In[25]:


df3= pd.DataFrame({'article_title':paper_title,'article_date':date,'article_authors':authors})
df3


# In[26]:


page4= requests.get(' https://www.cnbc.com/world/?region=world')
page4


# In[29]:


news= BeautifulSoup(page4.content,'html.parser')
news


# In[32]:


headings= []
for i in news.find_all('div',class_='Card-titleContainer'):
    headings.append(i.text)
    
headings


# In[69]:


headline_date= []
for i in news.find_all('div',class_='Card-cardFooter'):
    headline_date.append(i.text)
    
headline_date


# In[39]:


news_link=[]
for i in news.find_all('div',class_='Card-titleContainer'):
    l= i.find('a')['href']
    news_link.append(l)
    
news_link


# In[70]:


page5= requests.get('https://www.bewakoof.com/bestseller?sort=popular')
page5


# In[71]:


tees= BeautifulSoup(page5.content,'html.parser')
tees


# In[79]:


product_name0=[]
for i in tees.find_all('h2',class_='clr-shade4 h3-p-name   undefined false'):
    product_name0.append(i.text)

product_name0


# In[80]:


product_price=[]
for i in tees.find_all('div',class_='discountedPriceText clr-p-black   false  '):
    product_price.append(i.text)
    
product_price


# In[81]:


product_image=[]
for i in tees.find_all('div',class_='productImg'):
    product_image.append(i['data-src'])
    
product_image


# In[82]:


page6= requests.get('https://www.nobroker.in/')
page6


# In[83]:


house= BeautifulSoup(page6.content)
house


# In[84]:


house_title=[]
for i in house.find_all('h2',class_='heading-6 flex items-center font-semi-bold m-0'):
    house_title.append(i.text)
    
house_title


# In[85]:


house_location=[]
for i in house.find_all('div',class_='mt-0.5p overflow-hidden overflow-ellipsis whitespace-nowrap max-w-70 text-gray-light leading-4 po:mb-0.1p po:max-w-95'):
    house_location.append(i.text)
    
house_location


# In[88]:


page7= requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/test')
page7


# In[90]:


cricket= BeautifulSoup(page7.content)
cricket


# In[91]:


batsmen_name=[]
for i in cricket.find_all('h3',class_='si-player-name'):
    batsmen_name.append(i.text)
    
batsmen_name


# In[ ]:




