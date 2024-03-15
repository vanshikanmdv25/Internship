#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[2]:


import selenium
from selenium import webdriver
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# # Question1

# In[3]:


driver1 = webdriver.Chrome()


# In[4]:


#opening the naukri page on automated chrome browser
driver1.get("https://www.naukri.com/")


# In[5]:


#entering designation
designation1 = driver1.find_element(By.XPATH,"/html/body/div[1]/div[7]/div/div/div[1]/div/div/div/div[1]/div/input")
designation1.send_keys('Data Scientist')


# In[6]:


#clicking search
search1 = driver1.find_element(By.CLASS_NAME,"qsbSubmit")
search1.click()


# In[11]:


#applying location and salary filter
location1 = driver1.find_element(By.XPATH,"/html/body/div/div/main/div[1]/div[1]/div/div/div[2]/div[4]/div[2]/div[3]/label/i")
location1.click()


# In[12]:


salary1 = driver1.find_element(By.XPATH,"/html/body/div/div/main/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/div[2]/label/i")
salary1.click()


# In[13]:


#Scraping data
job_title1=[]
job_location1=[]
company_name1=[]
experience_required1=[]


# In[14]:


#scraping job title
title_tags1 = driver1.find_elements(By.XPATH,'//div[@class="cust-job-tuple layout-wrapper lay-2 sjw__tuple "]/div/a')
for i in title_tags1[0:10]:
    title=i.text
    job_title1.append(title)


# In[15]:


#scraping job location
location_tags1 = driver1.find_elements(By.XPATH,'//span[@class="locWdth"]')
for i in location_tags1[0:10]:
    location=i.text
    job_location1.append(location)


# In[16]:


#scraping company name
name_tags1 = driver1.find_elements(By.XPATH,'//span[@class=" comp-dtls-wrap"]/a[1]')
for i in name_tags1[0:10]:
    name=i.text
    company_name1.append(name)


# In[17]:


#scraping experience required
experience_tags1 = driver1.find_elements(By.XPATH,'//span[@class="expwdth"]')
for i in experience_tags1[0:10]:
    experience=i.text
    experience_required1.append(experience)


# In[18]:


print(len(job_title1),len(job_location1),len(company_name1),len(experience_required1))


# In[19]:


naukri_page = pd.DataFrame({'Job_title':job_title1,'Job_location':job_location1,'Company_name':company_name1,'Experience':experience_required1})
naukri_page


# # Question2

# In[40]:


driver2 = webdriver.Chrome()


# In[41]:


driver2.get("https://www.shine.com/")


# In[44]:


#entering designation
designation2 = driver2.find_element(By.XPATH,"/html/body/div/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[1]/div/input")
designation2.send_keys('Data Analyst')


# In[43]:


#entering location
location2 = driver2.find_element(By.XPATH,"/html/body/div/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[2]/div/input")
location2.send_keys('Bangalore')


# In[45]:


#clicking search
search2 = driver2.find_element(By.XPATH,"/html/body/div/div[4]/div/div[2]/div[2]/div/form/div/div[2]/div/button")
search2.click()


# In[39]:


#Scraping data
job_title2=[]
job_location2=[]
company_name2=[]
experience_required2=[]


# In[ ]:


#scraping job title
title_tags2 = driver2.find_elements(By.XPATH,'')
for i in title_tags2[0:10]:
    title=i.text
    job_title2.append(title)


# In[24]:


#scraping job location
location_tags2 = driver2.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2"]')
for i in location_tags2[0:10]:
    location=i.text
    job_location2.append(location)


# In[25]:


#scraping company name
name_tags2 = driver2.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_cName__mYnow"]/span')
for i in name_tags2[0:10]:
    name=i.text
    company_name2.append(name)


# In[26]:


#scraping experience required
experience_tags2 = driver2.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_jobIcon__3FB1t"]')
for i in experience_tags2[0:10]:
    experience=i.text
    experience_required2.append(experience)


# In[ ]:


print(len(job_title2),len(job_location2),len(company_name2),len(experience_required2))


# In[ ]:


shine_page = pd.DataFrame({'Job_title':job_title2,'Job_location':job_location2,'Company_name':company_name2,'Experience':experience_required2})
shine_page


# # Question3

# In[3]:


driver3 = webdriver.Chrome()


# In[4]:


driver3.get("https://www.flipkart.com/apple-iphone-15-black-128-gb/p/itm6ac6485515ae4?pid=MOBGTAGPTB3VS24W&lid=LSTMOBGTAGPTB3VS24WVZNSC6&marketplace=FLIPKART&q=iphone+15&store=tyy/4io&srno=s_1_2&otracker=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&fm=organic&iid=b596c120-8114-44e8-9819-0b4dee130fa9.MOBGTAGPTB3VS24W.SEARCH&ppt=hp&ppn=homepage&ssid=s3c8i7dsvk0000001710403029549&qH=2f54b45b321e3ae5")


# In[5]:


#scraping data
rating=[]
review_summary=[]
full_review=[]


# In[7]:


all_reviews= driver3.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[1]/div[2]/div[10]/div[7]/div/a')
all_reviews.click()


# In[8]:


#scraping rating
for page in range(0,10):
    rating_path = driver3.find_elements(By.XPATH,'//div[@class="_3LWZlK _1BLPMq"]')
    for i in rating_path:
        r=i.text
        rating.append(r)
    next_button= driver3.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[11]')
    next_button.click()
    time.sleep(10)


# In[10]:


#scraping review summary
for page in range(0,10):
    summary_path = driver3.find_elements(By.XPATH,'//p[@class="_2-N8zT"]')
    for i in summary_path:
        rs=i.text
        review_summary.append(rs)
    next_button= driver3.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[11]')
    next_button.click()
    time.sleep(10)


# In[12]:


#scraping full review
for page in range(0,10):
    full_path = driver3.find_elements(By.XPATH,'//div[@class="t-ZTKy"]/div/div')
    for i in full_path:
        fr=i.text
        full_review.append(fr)
    next_button= driver3.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[11]')
    next_button.click()
    time.sleep(10)


# In[13]:


print(len(rating),len(review_summary),len(full_review))


# # Question 4

# In[14]:


driver4 = webdriver.Chrome()


# In[15]:


driver4.get('https://www.flipkart.com/')


# In[17]:


#entering search
search = driver4.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div[1]/header/div[1]/div[2]/form/div/div/input")
search.send_keys('Sneakers')


# In[18]:


#clicking search
search4 = driver4.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div[1]/header/div[1]/div[2]/form/div/button')
search4.click()


# In[28]:


brand4=[]
description4=[]
price4=[]


# In[29]:


#scraping brand
for page in range(0,2):
    brand_path = driver4.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
    for i in brand_path:
        b=i.text
        brand4.append(b)
    next_button= driver4.find_element(By.XPATH,'/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]')
    next_button.click()
    time.sleep(2)
    
for page in range(2,3):
    brand_path = driver4.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
    for i in brand_path[0:20]:
        b=i.text
        brand4.append(b)
    next_button= driver4.find_element(By.XPATH,'/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]')
    next_button.click()
    time.sleep(1)


# In[30]:


#scraping description
for page in range(0,2):
    description_path = driver4.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
    for i in description_path:
        d=i.text
        description4.append(d)
    next_button= driver4.find_element(By.XPATH,'/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]')
    next_button.click()
    time.sleep(2)
    
for page in range(2,3):
    description_path = driver4.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
    for i in description_path[0:20]:
        d=i.text
        description4.append(d)
    next_button= driver4.find_element(By.XPATH,'/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]')
    next_button.click()
    time.sleep(1)


# In[31]:


#scraping price
for page in range(0,2):
    price_path = driver4.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
    for i in price_path:
        p=i.text
        price4.append(p)
    next_button= driver4.find_element(By.XPATH,'/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]')
    next_button.click()
    time.sleep(2)
    
for page in range(2,3):
    price_path = driver4.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
    for i in price_path[0:20]:
        p=i.text
        price4.append(p)
    next_button= driver4.find_element(By.XPATH,'/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]')
    next_button.click()
    time.sleep(1)


# In[32]:


print(len(brand4),len(description4),len(price4))


# # Question 5

# In[17]:


driver5 = webdriver.Chrome()


# In[18]:


driver5.get('https://www.amazon.in/')


# In[19]:


#entering laptop
laptop = driver5.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input")
laptop.send_keys('laptop')


# In[20]:


search5 = driver5.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input")
search5.click()


# In[21]:


#applying filter
cpu_type = driver5.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[5]/ul[19]/span/span[8]/li/span/a/div/label/i")
cpu_type.click()


# In[38]:


#scraping data
title5=[]
ratings5=[]
price5=[]


# In[39]:


#scraping title
title_tags5 = driver5.find_elements(By.XPATH,'//h2[@class="a-size-mini a-spacing-none a-color-base s-line-clamp-2"]')
for i in title_tags5[0:10]:
    title=i.text
    title5.append(title)


# In[40]:


#scraping ratings
rating_tags5 = driver5.find_elements(By.XPATH,'//a[@class="a-popover-trigger a-declarative"]')
for i in rating_tags5[0:10]:
    rating=i.text
    ratings5.append(rating)


# In[41]:


#scraping price
price_tags5 = driver5.find_elements(By.XPATH,'//span[@class="a-price-whole"]')
for i in price_tags5[0:10]:
    price=i.text
    price5.append(price)


# In[42]:


print(len(title5),len(ratings5),len(price5))


# # Question 6

# In[44]:


driver6 = webdriver.Chrome()


# In[45]:


driver6.get('https://www.azquotes.com/')


# In[46]:


#clicking top quote
top = driver6.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div[3]/ul/li[5]/a')
top.click()


# In[47]:


quote6=[]
author6=[]
types6=[]


# In[ ]:


#scraping quote
quote_tags6 = driver6.find_elements(By.XPATH,'//a[@class="a-popover-trigger a-declarative"]')
for i in quote_tags6:
    quote=i.text
    quote6.append(quote)


# In[48]:


#scraping quote
for page in range(0,10):
    quote_tags6 = driver6.find_elements(By.XPATH,'//a[@class="title"]')
    for i in quote_tags6:
        quote=i.text
        quote6.append(quote)
    next_button= driver6.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[3]/li[12]/a')
    next_button.click()
    time.sleep(10)


# In[50]:


#scraping author
for page in range(0,10):
    author_tags6 = driver6.find_elements(By.XPATH,'//div[@class="author"]')
    for i in author_tags6:
        author=i.text
        author6.append(author)
    next_button= driver6.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[3]/li[12]/a')
    next_button.click()
    time.sleep(10)


# In[53]:


#scraping type
for page in range(0,10):
    type_tags6 = driver6.find_elements(By.XPATH,'//div[@class="tags"]')
    for i in type_tags6:
        ty=i.text
        types6.append(ty)
    next_button= driver6.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[3]/li[12]/a')
    next_button.click()
    time.sleep(10)


# In[54]:


print(len(quote6),len(author6),len(types6))


# In[55]:


quotes_data = pd.DataFrame({'Quotes':quote6,'Authors':author6,'Types of quote':types6})
quotes_data


# # Question 7

# In[3]:


driver7 = webdriver.Chrome()


# In[4]:


driver7.get('https://www.jagranjosh.com/general-knowledge/list-of-all-prime-ministers-of-india-1473165149-1')


# In[10]:


name7=[]
dates7=[]
tenure7=[]
remarks7=[]


# In[11]:


table= driver7.find_element(By.CLASS_NAME,'TableData')


# In[12]:


rows= table.find_elements(By.TAG_NAME,'tr')


# In[13]:


for row in rows[1:]:
    columns = row.find_elements(By.TAG_NAME, "td")
    name7= columns[1].text
    dates7= columns[2].text
    tenure7= columns[3].text
    remarks7= columns[4].text


# In[14]:


print(len(name7),len(dates7),len(tenure7),len(remarks7))


# In[ ]:





# # Question 8

# In[15]:


driver8 = webdriver.Chrome()


# In[16]:


driver8.get('https://www.motor1.com/')


# In[17]:


#typing data
cars= driver8.find_element(By.XPATH,'/html/body/div[9]/div[2]/div/div/div[3]/div/div/div/form/input')
cars.send_keys('50 most expensive cars')


# In[18]:


#click on search
search8 = driver8.find_element(By.XPATH,'/html/body/div[9]/div[2]/div/div/div[3]/div/div/div/form/button[1]')
search8.click()


# In[19]:


#click on text
text = driver8.find_element(By.XPATH,'/html/body/div[9]/div[9]/div/div[1]/div/div/div[1]/div/div[1]/h3/a')
text.click()


# In[29]:


car_name=[]
car_price=[]


# In[30]:


#scraping car name
name_tags8= driver8.find_elements(By.XPATH,'//h3[@class="subheader"]')
for i in name_tags8[0:50]:
    name=i.text
    car_name.append(name)


# In[31]:


#scraping car price
price_tags8= driver8.find_elements(By.TAG_NAME,'strong')
for i in price_tags8[0:50]:
    price=i.text
    car_price.append(price)


# In[32]:


print(len(car_name),len(car_price))


# In[33]:


data8= pd.DataFrame({'Cars':car_name,'Prices':car_price})
data8


# In[ ]:




