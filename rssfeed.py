"""
Given a Dictionary keyed by Company and valued by RSS feed url, write a function that determines which companies had no activity for a given number of days
by Connor Davidson. created June 14,2019.


I interpreted this task to mean that I need to produce a function that will iterate through every entry in an rss feed and compare the time of all chonologically sequential entries.
if the time between these entries is equal to the given number of days, it will flag that company and return it.
This code prints out the list at the end and it also returns it so it can be used in other situations.
I have left in the dictionary that i used to  test my code with.
I tried to leave as many comments as possible 

assumptions:
I assumed that the URLs in the given dictionary are actually linked to a RSS feed.
I assumed that the given dates on the website provide all necessary information to determine the time (year, month, day, hour, minute, second) 
"""


#used to parse rss feeds
import feedparser
#used to verify that ssl is working currectly
import ssl
#used for doing time math
from datetime import datetime
#parse can parse almost any date format into a date time object
from dateutil.parser import parse


feeds = {
        "hackerNews" : "https://hnrss.org/newest",
        "craigslist" : "https://www.craigslist.org/about/best/all/index.rss",
        "Joe Rogan"  : "http://podcasts.joerogan.net/feed",
        "reddit"    : "https://www.reddit.com/.rss",
        "WSJ"        : "https://feeds.a.dj.com/rss/RSSWorldNews.xml",
        "WaPo"      : "http://feeds.washingtonpost.com/rss/rss_fact-checker",
         }




#returns a list of companies that didn't have activity for "days" amount of days 
def rss_activity(feeds , days ):

    #makes sure ssl is working correctly
    if hasattr(ssl, '_create_unverified_context'):
        ssl._create_default_https_context = ssl._create_unverified_context

    today = datetime.now()

    #holds the inactive companies. This gets printed at the bottom and gets returned
    inactiveCompanies = []

    #loops through the feeds dictionary.
    for company, url in feeds.items():
        #parses the url at the current spot in the  dictionary
        d = feedparser.parse(url)
        
        #holds the dates of the entries
        dates = []
        
        #loops through all of the entries on the rss feed from the current url 
        for entry in range(0, len(d.entries)):
            
            #stores the updated time into a string
            entryUpdatedTime = d.entries[entry].updated
            
            #trims the last 6 characters off of the given entries time so that it can use strptime(). this contained the time zone.
            trimmedEntryUpdatedTime = entryUpdatedTime[:-6]
            
            #converts the trimmedEntryUpdatedTime into a datetime object for the subtraction
            realTime = parse(trimmedEntryUpdatedTime)

            #appends the realTime variable into the orderedDates list
            dates.append(realTime)
            
            #sorts the dates list becuase the rss feed may not have them in chronological order
            orderedDates = sorted(dates, reverse=True)

            #checks if the time from the most recent post to now is more or less than the days parameter
            if abs((today - orderedDates[0]).days) == days:
                #adds the name of the inactive company to the inactive companies list
                inactiveCompanies.append(company)
                break
        
        #iterates through the list and compares every date to the date before it to check if the period between them was equal to the days parameter
        for x in range(1, len(orderedDates)):
            if abs((orderedDates[x - 1] - orderedDates[x]).days) == days:
                #adds the name of the inactive company to the inactive companies list
                inactiveCompanies.append(company)
                break

    #prints the list of the inactive companies 
    print("LIST OF COMPANIES INACTIVE FOR " + str(days) + " DAYS.")
    for i in range(0, len(inactiveCompanies)):
            print(inactiveCompanies[i])
            
    return inactiveCompanies


a = rss_activity(feeds, 2)
print(a)











