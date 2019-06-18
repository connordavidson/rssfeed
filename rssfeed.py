#Given a Dictionary keyed by Company and valued by RSS feed url, write a function that determines which companies had no activity for a given number of days
#by Connor Davidson. created June 14,2019.



#used to parse rss feeds
import feedparser
#used to verify that ssl is working currectly
import ssl
#used for doing time math
from datetime import datetime
from dateutil.parser import parse


#assumtion:  the dictionary is similar to this one .. where every url links to a RSS feed. if not, can check if it is an xml file or not 
feeds = {
        "hackerNews" : "https://hnrss.org/newest",
        "craigslist" : "https://www.craigslist.org/about/best/all/index.rss",
        "Joe Rogan"  : "http://podcasts.joerogan.net/feed",
        "reddit1"    : "https://www.reddit.com/.rss",
        "reddit2"    : "https://www.reddit.com/r/news/.rss",
        "WSJ"        : "https://feeds.a.dj.com/rss/RSSWorldNews.xml",
        "WaPo1"      : "http://feeds.washingtonpost.com/rss/rss_fact-checker",
        "Wapo2"      : "http://feeds.washingtonpost.com/rss/rss_innovations"
         }


#makes sure ssl is working correctly
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context


def rss_activity(feeds , days ):
    
    today = datetime.now()

    #prints the number of days.. casts the int to a string.
    print(str(days) + " days")

    # loops through the items in the feeds dict and prints the company name in all caps and then loops through the entries in the given url
    for company, url in feeds.items():
        d = feedparser.parse(url)
        print( company.upper() )
        
        #loops through all of the entries on the rss feed
        for entry in range(0, len(d.entries)):
            #stores the updated time into a string
            entryUpdatedTime = d.entries[entry].updated
            #trims the last 6 characters off of the given entries time so that it can use strptime(). this contained the time zone.
            trimmedEntryUpdatedTime = entryUpdatedTime[:-6]
            
            #converts the trimmedEntryUpdatedTime into a datetime object for the subtraction
            #assumption: the time to be parsed contains every element that is necessary (year, month, days, hours, minutes, seconds, etc) 
            realTime = parse(trimmedEntryUpdatedTime)
            #checks if the updated time is more or less than the days parameter
            if (today - realTime).days >= days:
                print("more")
               
        print()
        print()


rss_activity(feeds, 5)











