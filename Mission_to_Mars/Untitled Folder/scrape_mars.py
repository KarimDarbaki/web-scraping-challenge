#!/usr/bin/env python
# coding: utf-8

# In[28]:


from splinter import Browser
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


# In[3]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)






# In[3]:



url = 'https://mars.nasa.gov/news'
browser.visit(url)


# In[4]:


# Iterate through all pages
html = browser.html

soup = BeautifulSoup(html, 'html.parser')

articles = soup.find_all('div', class_="content_title")
content = soup.find_all('div', class_="article_teaser_body")


print(articles[1].get_text())
print(content[1].get_text())
    
news_title= articles[1].get_text()

news_p= content[0].get_text()
news_data= []
news_data = {
    "news_title": news_title,
    "news_p": news_data
}
# news_data["news_title"]= news_title
# news_title["news_p"]

# return news_data


# In[44]:



url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# In[45]:



id="full_image"
pic =browser.find_by_id("full_image")
pic.click()

browser.is_element_present_by_text('more info', wait_time=1)
more_info_elem = browser.find_link_by_partial_text('more info')
more_info_elem.click()


html2 = browser.html
soup2 = BeautifulSoup(html2, "html.parser")
#photo = soup.find_all("img", class_=)
#photo = soup.find_all("div", class_="fancybox-inner fancybox-skin fancybox-dark-skin fancybox-dark-skin-open")
#photo = soup('div', {class:"fancybox-inner fancybox-skin fancybox-dark-skin fancybox-dark-skin-open"})[0].find_all('src')
image_url = soup2.select_one('figure.lede a img').get("src")
print(image_url)
img_full_url= "https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA22949_hires.jpg"


# In[21]:


url = 'https://twitter.com/marswxreport?lang=en'
# url= "https://twitter.com/MarsWxReport/status/1271545615126802434"
browser.visit(url)


# In[26]:


#scrape mars weather tweets

# Iterate through all pages
html = browser.html

soup = BeautifulSoup(html, 'html.parser')

# tweets = soup.find_all('div', class_="css-1dbjc4n")
tweets = soup.find_all('div', class_=["css-901oao", "css-16my406"," r-1qd0xha", "r-ad9z0x", "r-bcqeeo", "r-qvutc0"])
content = soup.find_all('div', class_="article_teaser_body")


# for i,tweet in enumerate(tweets):
#     txt=tweet.get_text()
#     if "InSight sol 548" in txt: 
#         print(i)
#         print(txt)

#print(tweets[0].get_text())
#print(content[1].get_text())
    
mars_weather_tweets= tweets[23].get_text()

#news_p= content[0].get_text()
print(tweets[23].get_text())
# print(len(tweets))
# print(tweets)
print(mars_weather_tweets)


# In[ ]:





# In[30]:


mars_facts_table = pd.read_html("https://space-facts.com/mars/")[0]


# In[85]:


url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[86]:


var=browser.find_by_css("a.product-item h3")
var

img_list=[]

for j in range(len(var)):
    img_dict={}
    browser.find_by_css("a.product-item h3")[j].click()
    img=browser.find_by_text("Sample").first
    link= img["href"]
    
#     title=browser.find_by_text("Cerberus").first
    title=browser.find_by_tag("h2").text
#     title=browser.find_by_css("title", "h2").text
   
    img_dict["image_title"]=title
    img_dict["image_url"]=link
    img_list.append(img_dict)
    
    browser.back()
print(img_list)  
#     print(title)

    


# In[88]:


img_dict["image_title"]


# In[ ]:
def scrape():
    """ Mass Scrape"""
    mars_data = {}

    mars_data["news_data"] = news_data




# In[ ]:

def scrape():
    """Function: Main Scrape Funtionality
        calls other funtions
        Returns:combined mars_data dictionary"""

    mars_data={}

    mars_data["news_data"] = news_data()

    mars_data["full image"] = img_full_url()
    
    mars_data["mars_weather_tweets"] = mars_weather_tweets()

    mars_data["mars_facts_table"] = mars_facts_table()

    mars_data["mars_hemisphers"] = img_list()

    return mars_data


