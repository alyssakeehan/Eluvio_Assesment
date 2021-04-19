#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import math


# In[2]:


use_data = pd.read_csv('Eluvio_DS_Challenge.csv')


# In[3]:


use_data.head()


# Based on looks alone, it looks like this data is taken from reddit. I can tell from the up votes and downvotes. All of them under then thread regarding world news. The variables taken into account are the data created, number of up and down votes, titels, whether the content is open to those over 18 years old and the author. 

# # Clean and Tidy the Data

# In[4]:


use_data[use_data.category != 'worldnews']


# Getting rid of the category column since they are all worldnews

# In[5]:


use_data = use_data.drop(columns = ['category'])
use_data.head()


# Separate the data into two tables: The news stories safe for minors or not safe.

# In[6]:


over_18 = use_data[use_data.over_18 == True].drop(columns = ['over_18'])
under_18 = use_data[use_data.over_18 == False].drop(columns = ['over_18'])


# In[7]:


over_18


# In[8]:


under_18


# Looking at just the titles for each subgroup of reddit posts, I want to see if the title could be a good indicator of what could be classified as 18+. I decided to find a csv file that contains certain words that may be classifed as 18+.

# In[9]:


import csv
file_swears = open('swearWords.csv')
data_swears = csv.reader(file_swears)
restricted_words = list(data_swears)[0]
# restricted_words (not gonna show because the words may be triggering)


# In[10]:


swears = '|'.join(restricted_words)


# In[11]:


over_18['title_lower'] = over_18['title'].str.lower()
under_18['title_lower'] = under_18['title'].str.lower()


# In[12]:


over_18_swears = over_18.title_lower.str.contains(swears)
under_18_swears = under_18.title_lower.str.contains(swears)


# Now I will perform and 2 prop Hypothesis Test.

# In[13]:


x1 = over_18_swears.sum()
n1 = len(over_18_swears)
p1 = over_18_swears.mean()
print(x1)
print(n1)
print(p1)


# In[14]:


x2 = under_18_swears.sum()
n2 = len(under_18_swears)
p2 = under_18_swears.mean()
print(x2)
print(n2)
print(p2)


# Ho: p1 = p2 (There **is not** difference between the proportion of posts that are 18+ and those that are not that contain cenosored words)
# 
# vs.
# 
# H1: p1 != p2 (There **is** a difference between the proportion of posts that are 18+ and those that are not that contain censored words)

# In[15]:


pooled_p = (p1*n1 + p2*n2)/(n1+n2)
pooled_p


# In[16]:


z = (p1-p2)/math.sqrt(pooled_p*(1-pooled_p)*((1/n1)+(1/n2)))
z


# # Conclusion
# With a z-value greater than 1.96 (the significance level at alpha = 0.05), we reject the null hypothesis. There is a difference between the proportion of posts that are 18+ and those that are not that contain censored words. Approximately 42% of the posts labeled as 18+ contained a censored word in the title while approximately 18.69% of the under 18 posts contained those words. 

# Although there is a significant difference between the proportions, it is also pretty interesting how 95,000+ posts classified as safe for minors contained swear words in the title. Because of this, I dont think the title of the post could solely predict whether the rating is restricted or not. If I had more time and more access to all the variables, I'd like to predict this using a machine learning model. 
