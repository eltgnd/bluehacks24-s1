import streamlit as st
import pandas as pd
import numpy as np

import requests as r
import re
from dateutil import parser
from bs4 import BeautifulSoup

import control_flow as cf

def date_time_parser(dt):
    '''
    Function by Muralidhar (2021).
    Returns the time elapsed (in minutes) since the news was published
    
    dt: str
        published date
        
    Returns
    int: time elapsed (in minutes)
    '''
    return int(np.round((dt.now(dt.tz) - dt).total_seconds() / 60, 0))

def elapsed_time_str(mins):
    '''
    Function from Muralidhar (2021).
    Returns the word form of the time elapsed (in minutes) since the news was published
    
    mins: int
        time elapsed (in minutes)
        
    Returns
    str: word form of time elapsed (in minutes)
    '''
    time_str = '' # Initializing a variable that stores the word form of time
    hours = int(mins / 60) # integer part of hours. Example: if time elapsed is 2.5 hours, then hours = 2
    days = np.round(mins / (60 * 24), 1) # days elapsed
    # minutes portion of time elapsed in hours. Example: if time elapsed is 2.5 hours, then remaining_mins = 30
    remaining_mins = int(mins - (hours * 60))
    
    if (days >= 1):
        time_str = f'{str(days)} days ago' # Example: days = 1.2 => time_str = 1.2 days ago
        if days == 1:
            time_str = 'a day ago'  # Example: days = 1 => time_str = a day ago
            
    elif (days < 1) & (hours < 24) & (mins >= 60):
        time_str = f'{str(hours)} hours and {str(remaining_mins)} mins ago' # Example: 2 hours and 15 mins ago
        if (hours == 1) & (remaining_mins > 1):
            time_str = f'an hour and {str(remaining_mins)} mins ago' # Example: an hour and 5 mins ago
        if (hours == 1) & (remaining_mins == 1):
            time_str = f'an hour and a min ago' # Example: an hour and a min ago
        if (hours > 1) & (remaining_mins == 1):
            time_str = f'{str(hours)} hours and a min ago' # Example: 5 hours and a min ago
        if (hours > 1) & (remaining_mins == 0):
            time_str = f'{str(hours)} hours ago' # Example: 4 hours ago
        if ((mins / 60) == 1) & (remaining_mins == 0):
            time_str = 'an hour ago' # Example: an hour ago
            
    elif (days < 1) & (hours < 24) & (mins == 0):
        time_str = 'Just in' # if minutes == 0 then time_str = 'Just In'
        
    else:
        time_str = f'{str(mins)} minutes ago' # Example: 5 minutes ago
        if mins == 1:
            time_str = 'a minute ago'
    return time_str

def text_clean(desc):
    '''
    Function by Muralidhar (2021).
    Returns cleaned text by removing the unparsed HTML characters from a news item's description/title
    
    dt: str
        description/title of a news item
        
    Returns
    str: cleaned description/title of a news item
    '''
    desc = desc.replace("&lt;", "<")
    desc = desc.replace("&gt;", ">")
    desc = re.sub("<.*?>", "", desc)
    desc = desc.replace("#39;", "'")
    desc = desc.replace('&quot;', '"')
    desc = desc.replace('&nbsp;', '"')
    desc = desc.replace('#32;', ' ')
    return desc

def src_parse(rss_url):
    '''
    Function by Muralidhar (2021).
    Returns the source (root domain of RSS feed) from the RSS feed URL.
    
    rss_url: str
         RSS feed URL
         
    Returns
    str: root domain of RSS feed URL
    '''

    rss_url = rss_url.replace("https://www.", "") # removing "https://www." from RSS feed URL
    rss_url = rss_url.replace("https://", "") # If there was no www, remove the https://
    rss_url = rss_url.split("/") # splitting the remaining portion of RSS feed URL by '/'
    return rss_url[0] # first element/item of the split RSS feed URL is the root domain

def rss_parser(news_item):
    '''
    Function by Muralidhar (2021).
    Processes an individual news item.
    
    news_item: bs4.element.Tag
       single news item (<item>) of an RSS Feed
    
    Returns
    DataFrame: data frame of a processed news item (title, url, description, date, parsed_date)
    '''
    b1 = BeautifulSoup(str(news_item),"xml") # Parsing a news item (<item>) to BeautifulSoup object
    
    title = "" if b1.find("title") is None else b1.find("title").get_text() # If <title> is absent then title = ""
    title = text_clean(title) # cleaning title
    
    url = "" if b1.find("link") is None else b1.find("link").get_text() # If <link> is absent then url = "". url is the URL of the news article
    
    desc = "" if b1.find("description") is None else b1.find("description").get_text() # If <description> is absent then desc = "". desc is the short description of the news article
    desc = text_clean(desc) # cleaning the description
    desc = f'{desc[:300]}...' if len(desc) >= 300 else desc # limiting the length of description to 300 chars
    
    # If <pubDate> i.e. published date is absent then date is some random date from years ago so the the article appears at the end
    date = "Sat, 12 Aug 2000 12:00:00 +0800" if b1.find("pubDate") is None else b1.find("pubDate").get_text()
    
    # if url.find("businesstoday.in") >=0: # Time zone in the feed of 'businesstoday.in' is wrong, hence, correcting it
    #     date = date.replace("GMT", "+0530")
    
    date1 = parser.parse(date) # parsing the date to Timestamp object
    
    # data frame of the processed data
    return {"title": title,
                        "url": url,
                        "description": desc,
                        "date": date,
                        "parsed_date": date1}

def news_agg(rss_url, original_url):
    '''
    Function by Muralidhar (2021).
    Processes each RSS Feed URL passed as an input argument
    
    rss_url: str
         RSS feed URL
         
    Returns
    DataFrame: data frame of data processed from the passed RSS Feed URL
    '''
    rss_df_rows = [] # Initializing an empty list for dataframe rows
    # Response from HTTP request
    resp = r.get(
        rss_url,
        headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}
    )
    b = BeautifulSoup(resp.content, "xml") # Parsing the HTTP response

    items = b.find_all("item") # Storing all the news items
    
    for i in items:
        rss_df_rows.append(rss_parser(i)) # parsing each news item (<item>)

    # st.write(pd.DataFrame(rss_df_rows))
    # raise ValueError

    rss_df = pd.DataFrame(rss_df_rows)
    
    rss_df["description"] = rss_df["description"].replace([" NULL", ''], np.nan) # Few items have 'NULL' as description so replacing NULL with NA
    rss_df = rss_df.dropna()  # dropping news items with either of title, URL, description or date, missing
    rss_df["src"] = src_parse(rss_url) # extracting the source name from RSS feed URL
    rss_df["feed_site"] = original_url
    rss_df["elapsed_time"] = rss_df["parsed_date"].apply(date_time_parser) # Computing the time elapsed (in minutes) since the news was published
    rss_df["elapsed_time_str"] = rss_df["elapsed_time"].apply(elapsed_time_str) # Converting the the time elapsed (in minutes) since the news was published into string format

    return rss_df

if __name__ == "__main__":

    emoji = ":newspaper:"

    st.set_page_config(
        page_title = "Mental Health Feed",
        page_icon = emoji,
        initial_sidebar_state = "expanded",
    )

    # Load initial data if it hasn't already been loaded.
    cf.load_initial_data_if_needed()

    st.markdown("(PROJECT TITLE)") # Name of our project will be displayed in small text above the current page title.
    st.title(f"{emoji} Mental Health Feed")


    # -------Code below is from Muralidhar (2021)

    rss = {
        "https://www.sciencedaily.com/rss/mind_brain/mental_health.xml": "https://www.sciencedaily.com/news/mind_brain/mental_health/",
        "https://www.helpguide.org/feed": "https://www.helpguide.org/category/mental-health",
        "https://feeds.npr.org/1029/rss.xml": "https://www.npr.org/sections/mental-health/",
    }

    final_df_rows = [] # initializing the data frame to store all the news items from all the RSS Feed URLs
    for rss_url, original_url in rss.items():
        final_df_rows.append(news_agg(rss_url, original_url))
    
    final_df = pd.concat(
        objs = final_df_rows,
        axis = 0
    )

    final_df.sort_values(by='elapsed_time', inplace=True) # Sorting the news items by the time elapsed (in minutes) since the news was published
    
    final_df.drop(columns=[
        'date',
        'parsed_date',
        'elapsed_time',
    ], inplace=True) 
    final_df.drop_duplicates(subset='description', inplace=True) # Dropping news items with duplicate descriptions
    final_df = final_df.loc[(final_df['title'] != ''), :].reset_index(drop = True) # Dropping news items with no title

    # ---------Code above is from Muralidhar (2021)


    # ---------Code below is original

    num_articles_to_show = 20

    for index, row in final_df.loc[0 : num_articles_to_show + 1].iterrows():

        cols = st.columns([0.6,0.4])
        with cols[0]:

            st.caption(row["elapsed_time_str"])

            st.html("""<style> a {color: black; text-decoration: none;}</style>""")

            st.html(
                """<h4><a href = "{0}" style = "color: black; text-decoration: none;">{1}</a></h4>
                
<a href = "{2}" style = "color: black; text-decoration: none;">{3}</a>""".format(
                    row['url'],
                    row['title'],
                    row['feed_site'],
                    row['src']
                )
            )
            
        with cols[1]:
            st.markdown(row["description"])

        st.divider()
    
    cf.display_copyright()