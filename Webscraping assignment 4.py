#!/usr/bin/env python
# coding: utf-8

# In[1]:


import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time
import re


# # Question 1

# In[2]:


driver1= webdriver.Chrome()


# In[3]:


#opening the page
driver1.get('https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos')


# In[4]:


#scraping details
name1=[]
uploader1=[]
date1=[]
views1=[]

name_tags1= driver1.find_elements(By.XPATH,'//table[@class="sortable wikitable sticky-header static-row-numbers sort-under col3center col4right jquery-tablesorter"]/tbody/tr/td[1]')
for i in name_tags1:
    details= i.text
    name1.append(details)
    
uploader_tags1= driver1.find_elements(By.XPATH,'//table[@class="sortable wikitable sticky-header static-row-numbers sort-under col3center col4right jquery-tablesorter"]/tbody/tr/td[2]')
for i in uploader_tags1:
    details= i.text
    uploader1.append(details)
    
date_tags1= driver1.find_elements(By.XPATH,'//table[@class="sortable wikitable sticky-header static-row-numbers sort-under col3center col4right jquery-tablesorter"]/tbody/tr/td[4]')
for i in date_tags1:
    details= i.text
    date1.append(details)

views_tags1= driver1.find_elements(By.XPATH,'//table[@class="sortable wikitable sticky-header static-row-numbers sort-under col3center col4right jquery-tablesorter"]/tbody/tr/td[3]')
for i in views_tags1:
    details= i.text
    views1.append(details)


# In[5]:


print(len(name1),len(uploader1),len(date1),len(views1))


# In[6]:


df1= pd.DataFrame({'Name':name1,'Artist':uploader1,'Upload date':date1,'Views':views1})
df1


# # Question 2

# In[7]:


driver2= webdriver.Chrome()


# In[8]:


driver2.get('https://www.bcci.tv/')


# In[9]:


#clicking fixtures
fixtures= driver2.find_element(By.XPATH,'/html/body/header/div[3]/div[2]/ul/div[1]/a[2]')
fixtures.click()


# In[10]:


#scraping details
series2=[]
place2=[]
date2=[]
time2=[]

series_tags2= driver2.find_elements(By.XPATH,'//h5[@class="match-tournament-name ng-binding"]')
for i in series_tags2:
    details= i.text
    series2.append(details)
    
place_tags2= driver2.find_elements(By.XPATH,'//div[@class="match-place ng-scope"]')
for i in place_tags2:
    details= i.text
    place2.append(details)
    
date_tags2= driver2.find_elements(By.XPATH,'//div[@class="match-dates ng-binding"]')
for i in date_tags2:
    details= i.text
    date2.append(details)
    
time_tags2= driver2.find_elements(By.XPATH,'//div[@class="match-time no-margin ng-binding"]')
for i in time_tags2:
    details= i .text
    time2.append(details)


# In[11]:


print(len(series2),len(place2),len(date2),len(time2))


# In[12]:


df2= pd.DataFrame({'Series':series2,'Place':place2,'Date':date2,'Time':time2})
df2


# # Question 3

# In[15]:


driver3= webdriver.Chrome()


# In[16]:


driver3.get('http://statisticstimes.com/')


# In[17]:


#going to indian economy page
economy= driver3.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[2]/div[2]/button')
economy.click()

india= driver3.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[2]/div[2]/div/a[3]')
india.click()


# In[18]:


#clicking gdp of indian states
gdp_page= driver3.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/ul/li[1]/a')
gdp_page.click()


# In[21]:


#scraping details
rank3=[]
state3=[]
gsdp1=[]
gsdp2=[]
share3=[]
gdp3=[]

rank_tags3= driver3.find_elements(By.XPATH,'//table[@class="display dataTable"]/tbody/tr/td[1]')
for i in rank_tags3[0:33]:
    details= i.text
    rank3.append(details)
    
state_tags3= driver3.find_elements(By.XPATH,'//table[@class="display dataTable"]/tbody/tr/td[2]')
for i in state_tags3[0:33]:
    details= i.text
    state3.append(details)
    
gsdp1_tags3= driver3.find_elements(By.XPATH,'//table[@class="display dataTable"]/tbody/tr/td[5]')
for i in gsdp1_tags3[0:33]:
    details= i.text
    gsdp1.append(details)
    
gsdp2_tags3= driver3.find_elements(By.XPATH,'//table[@class="display dataTable"]/tbody/tr/td[4]')
for i in gsdp2_tags3[0:33]:
    details= i.text
    gsdp2.append(details)
    
share_tags3= driver3.find_elements(By.XPATH,'//table[@class="display dataTable"]/tbody/tr/td[6]')
for i in share_tags3[0:33]:
    details= i.text
    share3.append(details)
    
gdp_tags3= driver3.find_elements(By.XPATH,'//table[@class="display dataTable"]/tbody/tr/td[7]')
for i in gdp_tags3[0:33]:
    details= i.text
    gdp3.append(details)


# In[22]:


print(len(rank3),len(state3),len(gsdp2),len(gsdp1),len(share3),len(gdp3))


# In[23]:


df3= pd.DataFrame({'Rank':rank3,'State':state3,'GSDP(21-22)':gsdp1,'GSDP(22-23)':gsdp2,'Share(21-22)':share3,'GDP($billion)':gdp3})
df3


# # Question 4

# In[2]:


driver4= webdriver.Chrome()


# In[3]:


driver4.get('https://github.com/')


# In[5]:


#geting to trending page
explore= driver4.find_element(By.XPATH,'/html/body/div[1]/div[1]/header/div/div[1]/div[2]/button')
explore.click()

open_source= driver4.find_element(By.XPATH,'/html/body/div[1]/div[1]/header/div/div[2]/div/nav/ul/li[3]/button')
open_source.click()

trending= driver4.find_element(By.XPATH,'/html/body/div[1]/div[1]/header/div/div[2]/div/nav/ul/li[3]/div/div[3]/ul/li[2]/a')
trending.click()


# In[6]:


#scraping details
title4=[]
contributors4=[]
description4=[]
language4=[]

title_tags4= driver4.find_elements(By.XPATH,'//span[@class="text-normal"]')
for i in title_tags4:
    details= i.text
    title4.append(details)
    
contributors_tags4= driver4.find_elements(By.XPATH,'//div[@class="f6 color-fg-muted mt-2"]/a[2]')
for i in contributors_tags4:
    details= i.text
    contributors4.append(details)
    
try:
    description_tags4= driver4.find_elements(By.XPATH,'//p[@class="col-9 color-fg-muted my-1 pr-4"]')
    for i in description_tags4:
        details= i.text
        description4.append(details)   
    language_tags4= driver4.find_elements(By.XPATH,'//span[@class="d-inline-block ml-0 mr-3"]/span[2]')
    for i in language_tags4:
        details= i.text
        language4.append(details)    
except NoSuchElementException:
    description4.append('-')
    language4.append('-')


# In[7]:


print(len(title4),len(description4),len(language4),len(contributors4))


# # Question 5

# In[4]:


driver5= webdriver.Chrome()


# In[5]:


driver5.get('https:/www.billboard.com/')


# In[9]:


#getting hot 100 page
explore5= driver5.find_element(By.XPATH,'/html/body/div[3]/header/div/div[4]/div/div[1]/div[1]/button')
explore5.click()

charts5= driver5.find_element(By.XPATH,'/html/body/div[3]/div[9]/div/div/div/ul/li[1]/h3/a')
charts5.click()


# In[10]:


top100= driver5.find_element(By.XPATH,'/html/body/div[3]/main/div[2]/div[1]/div[1]/div/div/div[3]/a')
top100.click()


# In[11]:


#scraping details
s_name5=[]
a_name5=[]
w_rank5=[]
p_rank5=[]
wob5=[]

s_name_tags5= driver5.find_elements(By.XPATH,'//li[@class="lrv-u-width-100p"]/ul/li/h3')
for i in s_name_tags5:
    details= i.text
    s_name5.append(details)
    
a_name_tags5= driver5.find_elements(By.XPATH,'//li[@class="lrv-u-width-100p"]/ul/li[1]/span')
for i in a_name_tags5:
    details= i.text
    a_name5.append(details)
    
w_rank_tags5= driver5.find_elements(By.XPATH,'//li[@class="lrv-u-width-100p"]/ul/li[4]')
for i in w_rank_tags5:
    details= i.text
    w_rank5.append(details)
    
p_rank_tags5= driver5.find_elements(By.XPATH,'//li[@class="lrv-u-width-100p"]/ul/li[5]')
for i in p_rank_tags5:
    details= i.text
    p_rank5.append(details)
    
wob_tags5= driver5.find_elements(By.XPATH,'//li[@class="lrv-u-width-100p"]/ul/li[6]')
for i in wob_tags5:
    details= i.text
    wob5.append(details)


# In[12]:


df5= pd.DataFrame({'Song Name':s_name5,'Artist Name':a_name5,'Last Week Rank':w_rank5,'Peak Rank':p_rank5,'Weeks On Board':wob5})
df5


# # Question 6

# In[59]:


driver6= webdriver.Chrome()


# In[60]:


driver6.get('https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-grey-compare')


# In[61]:


#scraping details
name6=[]
author6=[]
sales6=[]
publisher6=[]
genre6=[]

name_tags6= driver6.find_elements(By.XPATH,'//table[@class="in-article sortable"]/tbody/tr/td[2]')
for i in name_tags6:
    details= i.text
    name6.append(details)
    
author_tags6= driver6.find_elements(By.XPATH,'//table[@class="in-article sortable"]/tbody/tr/td[3]')
for i in author_tags6:
    details= i.text
    author6.append(details)

sales_tags6= driver6.find_elements(By.XPATH,'//table[@class="in-article sortable"]/tbody/tr/td[4]')
for i in sales_tags6:
    details= i.text
    sales6.append(details)
    
publisher_tags6= driver6.find_elements(By.XPATH,'//table[@class="in-article sortable"]/tbody/tr/td[5]')
for i in publisher_tags6:
    details= i.text
    publisher6.append(details)
    
genre_tags6= driver6.find_elements(By.XPATH,'//table[@class="in-article sortable"]/tbody/tr/td[6]')
for i in genre_tags6:
    details= i.text
    genre6.append(details)


# In[62]:


df6= pd.DataFrame({'Book Name':name6,'Author Name':author6,'Volumes sold':sales6,'Publisher':publisher6,'Genre':genre6})
df6


# # Question 8

# In[3]:


driver8= webdriver.Chrome()


# In[4]:


driver8.get('https://archive.ics.uci.edu/')


# In[5]:


#clicking view data sets
view8= driver8.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/main/div/div[1]/div/div/div/a[1]')
view8.click()


# In[6]:


#clicking expand all
expand8= driver8.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/main/div/div[2]/div[1]/div/label[2]/div[2]/span[2]')
expand8.click()


# In[9]:


#scraping details
name8=[]
d_type8=[]
task8=[]
a_type8=[]
instances8=[]
attribute8=[]
year8=[]

name_tags8= driver8.find_elements(By.XPATH,'//h2[@class="truncate text-primary"]')
for i in name_tags8:
    details= i.text
    name8.append(details)
    
d_type_tags8= driver8.find_elements(By.XPATH,'//div[@class="my-2 hidden gap-4 md:grid grid-cols-12"]/div[2]')
for i in d_type_tags8:
    details= i.text
    d_type8.append(details)
    
task_tags8=driver8.find_elements(By.XPATH,'//div[@class="my-2 hidden gap-4 md:grid grid-cols-12"]/div[1]')
for i in task_tags8:
    details= i.text
    task8.append(details)
    
a_type_tags8= driver8.find_elements(By.XPATH,'//table[@class="col-span-full my-2 table sm:col-start-2"]/tbody/tr/td[2]')
for i in a_type_tags8:
    details= i.text
    a_type8.append(details)
    
attribute_tags8= driver8.find_elements(By.XPATH,'//div[@class="my-2 hidden gap-4 md:grid grid-cols-12"]/div[4]')
for i in attribute_tags8:
    details= i.text
    attribute8.append(details)
    
instances_tags8= driver8.find_elements(By.XPATH,'//div[@class="my-2 hidden gap-4 md:grid grid-cols-12"]/div[3]')
for i in instances_tags8:
    details= i.text
    instances8.append(details)
    
year_tags8= driver8.find_elements(By.XPATH,'//table[@class="col-span-full my-2 table sm:col-start-2"]/tbody/tr/td[4]')
for i in year_tags8:
    details= i.text
    year8.append(details)


# In[13]:


df8= pd.DataFrame({'Dataset Name':name8,'Data Type':d_type8,'Task':task8,'Attribute Type':a_type8,'No. Of Instances':instances8,'No. Of Attribute':attribute8,'Year':year8})
df8

