#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


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

# In[51]:


driver1= webdriver.Chrome()


# In[52]:


#opening amazon page
driver1.get("https://www.amazon.in")


# In[53]:


#taking user input
input1= input('item to search on amazon')
input1


# In[54]:


#searching for the input given by user
item1= driver1.find_element(By.XPATH,'/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input')
item1.send_keys(input1)


# In[55]:


#clicking search
search1= driver1.find_element(By.XPATH,'/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input')
search1.click()


# # Question 2

# In[56]:


#fetching url to open each product to fetch details
url2= []
for page in range(0,3):
    url = driver1.find_elements(By.XPATH,'//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')
    for i in url:
        url2.append(i.get_attribute('href'))
    next_button= driver1.find_elements(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[68]/div/div/span/a[3]')


# In[57]:


print(len(url2))
print(url2)


# In[58]:


#scraping other details
brand_name2=[]
product_name2=[]
price2=[]
return_exchange2=[]
delivery2=[]
availability2=[]

for i in url2:
    driver1.get(i)
    try:
        brand= driver1.find_element(By.XPATH,'/html/body/div[2]/div/div[5]/div[3]/div[4]/div[48]/div/table/tbody/tr[1]/td[2]/span')
        product= driver1.find_element(By.XPATH,'/html/body/div[2]/div/div[5]/div[3]/div[4]/div[1]/div/h1/span')
        price= driver1.find_element(By.XPATH,'/html/body/div[2]/div/div[5]/div[3]/div[4]/div[13]/div/div/div[4]/div[1]/span[3]/span[2]/span[2]')
        r_e= driver1.find_element(By.XPATH,'/html/body/div[2]/div/div[5]/div[3]/div[4]/div[24]/div[2]/div/div/div/div[3]')
        delivery= driver1.find_element(By.XPATH,'/html/body/div[2]/div/div[5]/div[3]/div[1]/div[3]/div/div[1]/div/div/div/form/div/div/div/div/div[4]/div/div[3]/div[10]/div[1]/div/div/div/span/span')
        available= driver1.find_element(By.XPATH,'/html/body/div[2]/div/div[5]/div[3]/div[1]/div[3]/div/div[1]/div/div/div/form/div/div/div/div/div[4]/div/div[5]/div/div[1]/span')
        brand_name2.append(brand.text)
        product_name2.append(product.text)
        price2.append(price.text)
        return_exchange2.append(r_e.text)
        delivery2.append(delivery.text)
        availability2.append(available.text)
    except NoSuchElementException :
        brand_name2.append('-')
        product_name2.append('-')
        price2.append('-')
        return_exchange2.append('-')
        delivery2.append('-')
        availability2.append('-')


# In[59]:


print(len(brand_name2),len(product_name2),len(price2),len(return_exchange2),len(delivery2),len(availability2))


# In[60]:


amazon_page= pd.DataFrame({'Brand_Name':brand_name2,'Product_Name':product_name2,'Price_Of_Product':price2,'Return/Exchange':return_exchange2,'Expexted_Delivery':delivery2,'Availability_Of_Product':availability2,'Product_URL':url2})
amazon_page


# # Question 3

# In[61]:


driver3= webdriver.Chrome()


# In[62]:


driver3.get("https://images.google.com/")


# In[63]:


#typing in search bar
images= driver3.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea')
images.send_keys('fruits')


# In[64]:


#clicking search
search3= driver3.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/button')
search3.click()


# In[65]:


fruits=[]
fruit_tag= driver3.find_elements(By.XPATH,'//div[@class="fR600b islir"]/img')
for i in fruit_tag[0:10]:
    fruits.append(i.get_attribute('img-src'))


# In[66]:


print(len(fruits))


# # Question 4

# In[30]:


driver4= webdriver.Chrome()


# In[32]:


driver4.get('https://www.flipkart.com/')


# In[33]:


#entering serch
mobile= driver4.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div[1]/header/div[1]/div[2]/form/div/div/input')
mobile.send_keys('Oneplus Nord, pixel 4A')


# In[34]:


#clicking search
search4= driver4.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div[1]/header/div[1]/div[2]/form/div/button')
search4.click()


# In[36]:


#scraping details
brand_phone_colour=[]
tags4 = driver4.find_elements(By.XPATH,'//div[@class="_4rR01T"]')
for i in tags4:
    details=i.text
    brand_phone_colour.append(details)


# In[39]:


ram_rom=[]
storage_tags4 = driver4.find_elements(By.XPATH,'//li[@class="rgWa7D"][1]')
for i in storage_tags4:
    details=i.text
    ram_rom.append(details)


# In[41]:


cameras=[]
camera_tags4 = driver4.find_elements(By.XPATH,'//li[@class="rgWa7D"][3]')
for i in camera_tags4:
    details=i.text
    cameras.append(details)


# In[40]:


display=[]
display_tags4 = driver4.find_elements(By.XPATH,'//li[@class="rgWa7D"][2]')
for i in display_tags4:
    details=i.text
    display.append(details)


# In[42]:


battery=[]
battery_tags4 = driver4.find_elements(By.XPATH,'//li[@class="rgWa7D"][4]')
for i in battery_tags4:
    details=i.text
    battery.append(details)


# In[43]:


price=[]
price_tags4 = driver4.find_elements(By.XPATH,'//div[@class="_30jeq3 _1_WHN1"]')
for i in price_tags4:
    details=i.text
    price.append(details)


# In[44]:


url4=[]
url_tags4 = driver4.find_elements(By.XPATH,'//a[@class="_1fQZEK"]')
for i in url_tags4:
    url4.append(i.get_attribute('href'))


# In[45]:


df4= pd.DataFrame({'Name_Brand_Colur':brand_phone_colour,'Storage':ram_rom,'Camera':cameras,'Display_size':display,'Battery':battery,'Price':price,'URL':url4})
df4   


# In[47]:


df4.to_csv('assignment3_file1.csv',index= False)


# # Question 5

# In[3]:


driver5= webdriver.Chrome()


# In[4]:


driver5.get('https://maps.google.com')


# In[5]:


url_string= driver5.current_url


# In[6]:


print('URL Extracted:',url_string)


# In[12]:


lat_lng= re.findall(r'\d.*?entry',url_string)
print(lat_lng)


# In[15]:


for i in lat_lng:    
    pattern= r','
    splitting= re.split(pattern,i, 2)
    print(splitting[0:2])


# # Question 6

# In[30]:


driver6 =webdriver.Chrome()


# In[31]:


driver6.get('https://www.digit.in/')


# In[33]:


#clicking explore
explore= driver6.find_element(By.XPATH,'/html/body/div[1]/header/div/div[2]/div/div/div/button')
explore.click()    


# In[34]:


#clicking top 10
top10= driver6.find_element(By.XPATH,'/html/body/div[4]/div/ul/li[4]/a')
top10.click()


# In[35]:


#clicking top business laptops
business_laptops= driver6.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div[5]/p/a')
business_laptops.click()


# In[67]:


#scraping details
model_name6=[]
os6=[]
display6=[]
resolution6=[]
processor6=[]

try:
    model= driver6.find_elements(By.XPATH,'//h3[@class="font130 mt0 mb10 mobilesblockdisplay "]')
    os= driver6.find_elements(By.XPATH,'//div[@class="woo_code_loop_item font90"][1]/div/span[2]')
    display= driver6.find_elements(By.XPATH,'//div[@class="woo_code_loop_item font90"][2]/div/span[2]')
    resolution= driver6.find_elements(By.XPATH,'//div[@class="woo_code_loop_item font90"][3]/div/span[2]')
    processor= driver6.find_elements(By.XPATH,'//div[@class="woo_code_loop_item font90"][4]/div/span[2]')
    for i in model:
        model_name6.append(i.text)
    for i in os:
        os6.append(i.text)
    for i in display:
        display6.append(i.text)
    for i in resolution:
        resolution6.append(i.text)
    for i in processor:
        processor6.append(i.text)
        
except NoSuchElementException:
    model_name6.append('-')
    os6.append('-')
    display6.append('-')
    resolution6.append('-')
    processor6.append('-')


# In[68]:


print(len(model_name6),len(os6),len(display6),len(resolution6),len(processor6))


# # Question 7

# In[20]:


driver7= webdriver.Chrome()


# In[21]:


driver7.get('https://www.forbes.com/?sh=42e0b1682254')


# In[22]:


#clicking explore
explore= driver7.find_element(By.XPATH,'/html/body/div[1]/header/nav/div[1]/div[1]/div/div')
explore.click()


# In[23]:


#clicking billionaries
billion= driver7.find_element(By.XPATH,'/html/body/div[1]/header/nav/div[1]/div[1]/div/div[2]/ul/li[2]/div[1]')
billion.click()


# In[25]:


#clicking worlds billionaries
world_b= driver7.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/header/div[1]/div[1]/div[2]/ul/li[2]/div[2]/div[3]/ul/li[1]/a')
world_b.click()


# In[28]:


#scraping details
rank7=[]
name7=[]
worth7=[]
age7=[]
citizenship7=[]
source7=[]
industry7=[]

rank= driver7.find_elements(By.XPATH,'//div[@class="TableRow_row__L-0Km"][1]/div[1]')
for i in rank: 
    rank7.append(i.text)
name= driver7.find_elements(By.XPATH,'//div[@class="TableRow_row__L-0Km"][1]/div[2]')
for i in name:
    name7.append(i.text)
worth= driver7.find_elements(By.XPATH,'//div[@class="TableRow_row__L-0Km"][1]/div[3]')
for i in worth:
    worth7.append(i.text)
age= driver7.find_elements(By.XPATH,'//div[@class="TableRow_row__L-0Km"][1]/div[4]')
for i in age:
    age7.append(i.text)
citizenship= driver7.find_elements(By.XPATH,'//div[@class="TableRow_row__L-0Km"][1]/div[5]')
for i in citizenship:
    citizenship7.append(i.text)
source= driver7.find_elements(By.XPATH,'//div[@class="TableRow_row__L-0Km"][1]/div[6]')
for i in source:
    source7.append(i.text)
industry= driver7.find_elements(By.XPATH,'//div[@class="TableRow_row__L-0Km"][1]/div[7]')
for i in industry:
    industry7.append(i.text)


# In[29]:


df7=pd.DataFrame({'Rank':rank7,'Name':name7,'Worth':worth7,'Age':age7,'Citizenship':citizenship7,'Source':source7,'Industry':industry7})
df7


# # Question 8

# In[11]:


driver8= webdriver.Chrome()


# In[12]:


driver8.get('https://www.youtube.com/')


# In[13]:


#entering search
python= driver8.find_element(By.XPATH,'/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
python.send_keys('Python')


# In[14]:


#clicking search
search8= driver8.find_element(By.XPATH,'/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/button')
search8.click()


# In[15]:


#clicking a video to open
open8= driver8.find_element(By.XPATH,'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-playlist-renderer[1]/div/a')
open8.click()


# In[16]:


for _ in range(1000):
    driver8.execute_script("window.scrollBy(0,1000)")
comments8=[]  
comments= driver8.find_elements(By.XPATH,'//div[@class="style-scope ytd-expander"]')
for i in comments:
    comments8.append(i.text)


# In[17]:


print(len(comments8))


# In[19]:


df8= pd.DataFrame({'Comments':comments8})
df8


# # Question 9

# In[58]:


driver9= webdriver.Chrome()


# In[59]:


driver9.get('https://www.hostelworld.com/')


# In[60]:


#entering loacation
location9= driver9.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div[1]/div/div[2]/input')
location9.send_keys('London')


# In[62]:


#clicking london
london9= driver9.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div[2]/div/ul/li[2]/button/div[2]')
london9.click()


# In[63]:


#clicking search
search9= driver9.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/div[2]/div[2]/div/div/div/div[5]/button[2]')
search9.click()


# In[64]:


#scraping urls
url9=[]
url= driver9.find_elements(By.XPATH,'//a[@class="property-card-container horizontal"]')
for i in url:
    url9.append(i.get_attribute('href'))


# In[65]:


print(url9)


# In[66]:


name9=[]
distance9=[]
ratings9=[]
t_reviews9=[]
o_reviews9=[]
facility9=[]
proper_d9=[]
for i in url9:
    driver9.get(i)
    try:
        name= driver9.find_elements(By.XPATH,'//h1[@class="name title-4-bld"]')
        distance= driver9.find_elements(By.XPATH,'//li[@class="city-center"]')
        ratings= driver9.find_elements(By.XPATH,'//span[@class="number"]')
        t_reviews= driver9.find_elements(By.XPATH,'//span[@class="left-margin"]')
        o_reviews= driver9.find_elements(By.XPATH,'//div[@class="rating"]/div/div/span[2]')
        facility= driver9.find_elements(By.XPATH,'//div[@class="facilities snippet"]')
        proper_d= driver9.find_elements(By.XPATH,'//div[@class="about-description"]')
        name9.append(name)
        distance9.append(distance)
        ratings9.append(ratings)
        t_reviews9.append(t_reviews)
        o_reviews9.append(o_reviews)
        facility9.append(facility)
        proper_d9.append(proper_d)
    except NoSuchElementException :
        name9.append('-')
        distance9.append('-')
        ratings9.append('-')
        t_reviews9.append('-')
        o_reviews9.append('-')
        facility9.append('-')
        proper_d9.append('-')


# In[70]:


print(len(name9),len(distance9),len(ratings9),len(t_reviews9),len(o_reviews9),len(facility9),len(proper_d9))

