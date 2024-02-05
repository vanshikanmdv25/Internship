#!/usr/bin/env python
# coding: utf-8

# In[1]:


phrase="Python Exercises,PHP Exercises."


# In[2]:


import re


# In[3]:


replace= re.sub("\W",":",phrase)
print(replace)


# In[4]:


Dictionary= {'SUMMARY': ['hello, world!','XXXXX test', '123four, five:; six...']}


# In[5]:


import pandas as pd


# In[6]:


data= pd.DataFrame(data=Dictionary)


# In[7]:


data['SUMMARY']= data['SUMMARY'].str.replace('[^a-z\s]','',regex=True)
print(data)


# In[8]:


pattern= r"\w{4,}"


# In[9]:


string= "Amazon Go is a chain of convenience stores in the United States and the United Kingdom, operated by the online retailer Amazon."


# In[10]:


def character():
    comp= re.compile(pattern)
    result= comp.findall(string)
    print(result)


# In[11]:


character()


# In[12]:


pattern1= r"\w{3,5}"


# In[13]:


def character1():
    comp= re.compile(pattern1)
    result= comp.findall(string)
    print(result)


# In[14]:


character1()


# In[15]:


sample_text=["example(.com)","hr@fliprobo(.com)","github(.com)","Hello (Data Science World)","Data (Scientist)"]


# In[16]:


pattern2= r"\([^)]*\)"


# In[17]:


def remove_parentheses(strings):
    comp= re.compile(pattern2)
    result= [comp.sub('',s) for s in strings]
    print(result)


# In[18]:


remove_parentheses(sample_text)


# In[24]:


phrase1="ImportanceOfRegularExpressionsInPython"


# In[25]:


pattern1= re.compile(r"(^[A-Z][a-z]+)")


# In[28]:


result1= re.findall('[A-Z][^A-Z]*',phrase1)
print(result1)


# In[29]:


phrase2= "RegularExpression1IsAn2ImportantTopic3InPython"


# In[30]:


def insert_spaces(text):
    result= re.sub(r'([A-Za-z])(\d)',r'\1 \2',text)
    return result


# In[31]:


insert_spaces(phrase2)


# In[32]:


def insert_spaces1(text):
    result= re.sub(r'([A-Za-z])(\d)([A-Za-z])',r'\1 \2 \3',text)
    return result


# In[33]:


insert_spaces1(phrase2)


# In[41]:


happiness_score= pd.read_csv("https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv")


# In[42]:


happiness_score['first_five_letters']= happiness_score['Country'].str[:6]
print(happiness_score.head())


# In[43]:


string1= "String_123"
string2= "String@123"


# In[58]:


def text_match(text):
    if re.search('^[a-zA-Z0-9_]*$',text):
        print("matched")
    else:
        print("not matched")


# In[59]:


text_match(string1)
text_match(string2)


# In[69]:


def num_match(num):
    if re.match(r'^5',num):
        print('matched')
    else:
        print('not matched')


# In[70]:


num_match('567899')
num_match('899802')


# In[71]:


IP_address= "192.001.001.001"


# In[72]:


remove_zeros= re.sub('\.[0]*','.',IP_address)
remove_zeros


# In[73]:


dateandtime= "On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country."


# In[77]:


with open ('dateandtime.txt','w') as file:
    file.write(dateandtime)


# In[84]:


with open('dateandtime.txt', 'r') as file:
    text = file.read()

pattern = re.compile(r'([A-Za-z]+ \d{1,2}(st|nd|rd|th) \d{4})')
match = re.search(pattern, text)
print(match)


# In[91]:


strings= 'The quick brown fox jumps over the lazy dog.'
searched_words= ['fox','dog','horse']
for words in searched_words:
    matched= re.findall(words,strings)
    print(matched)


# In[93]:


strings= 'The quick brown fox jumps over the lazy dog.'
matched= re.search('fox',strings)
print(matched)


# In[94]:


substrings= "Python exercises, PHP exercises, C# exercises"
re.findall('exercises',substrings)


# In[104]:


re.search('exercises',substrings)


# In[118]:


for m in re.finditer("exercises",substrings):
    print(m.group(0))
    print("Index position:", m.start())


# In[105]:


date= "2022-04-25"


# In[109]:


formatdate= re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1',date)
formatdate


# In[110]:


numbers='01.12 0132.123 2.31875 145.8 3.01 27.25 0.25'


# In[111]:


pattern = re.compile(r'\b\d+\.\d{1,2}\b')
result = pattern.findall(numbers)
print(result)


# In[117]:


for m in re.finditer("\d+","The price of the item is 25"):
    print(m.group(0))
    print("Index position:", m.start())


# In[124]:


maximum= 'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
numbers=re.findall('\d+',maximum)
max(map(int,numbers))


# In[131]:


def add_spaces(exp):
    return re.sub(r"(\w)([A-Z])", r"\1 \2", exp)
add_spaces("RegularExpressionIsAnImportantTopicInPython")


# In[136]:


def find_sequences(text):
    pattern = re.findall(r'\b[A-Z][a-z]*\b',text)
    return pattern


# In[137]:


find_sequences("Environment Is Everything That Is Around Us")


# In[139]:


re.sub(r'\b(\w+)(\s+\1)+\b',r'\1',"Hello hello world world",flags= re.IGNORECASE)


# In[141]:


re.findall(r'#\w+','"RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"')


# In[144]:


re.sub(r"<U\+[A-Za-z0-9]+>","","@Jags123456 Bharat band on 28??<ed><U+00BD><ed><U+00BD><U+0082>Those who are protesting #demonitiZation")


# In[145]:


extractdates="Ron was born on 12-09-1992 and he was admitted to school 15-12-1999."


# In[146]:


with open ('extractdates.txt','w') as file:
    file.write(extractdates)


# In[147]:


with open('extractdates.txt', 'r') as file:
    text = file.read()
re.findall(r'\b\d{2}-\d{2}-\d{4}\b',text)


# In[148]:


phrase4= "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."


# In[149]:


wrds= re.compile(r'\b\w{2,4}\b')
answer= wrds.sub('',phrase4)
print(answer)


# In[ ]:




