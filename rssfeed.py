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




#returns a list of inactive companies 
def rss_activity(feeds , days ):
    
    today = datetime.now()


    #holds the inactive companies. will get printed and returned 
    inactiveCompanies = []
    

    #prints the number of days.. casts the int to a string.
    print(str(days) + " days")


    # loops through the items in the feeds dict and prints the company name in all caps and then loops through the entries in the given url
    for company, url in feeds.items():
        d = feedparser.parse(url)
        print( company.upper() )

        #holds the dates of the entries
        dates = []
        
        #loops through all of the entries on the rss feed
        for entry in range(0, len(d.entries)):
            
            #stores the updated time into a string
            entryUpdatedTime = d.entries[entry].updated
            #trims the last 6 characters off of the given entries time so that it can use strptime(). this contained the time zone.
            trimmedEntryUpdatedTime = entryUpdatedTime[:-6]

            #print(trimmedEntryUpdatedTime)
            
            #converts the trimmedEntryUpdatedTime into a datetime object for the subtraction
            #assumption: the time to be parsed contains every element that is necessary (year, month, days, hours, minutes, seconds, etc) 
            realTime = parse(trimmedEntryUpdatedTime)

            #appends the realTime variable into the orderedDates list
            dates.append(realTime)
            
            #sorts the dates list becuase 
            orderedDates = sorted(dates, reverse=True)


            #checks if the time from the most recent post to now is more or less than the days parameter

            
            if abs((today - orderedDates[0]).days) >= days:
                print(company + " has not had activity in the given number of days: " + str(0))
                #adds the name of the inactive company to the inactive companies list
                inactiveCompanies.append(company)
                break
 
        """
        #for troubleshooting the loops and stuff
        for i in range(0, len(orderedDates)):
            print(orderedDates[i])
       
        """

        
        #iterates through the list and compares every date to the date before it to check if the period between them was equal to the days parameter
        for x in range(1, len(orderedDates)):
            if abs((orderedDates[x - 1] - orderedDates[x]).days) >= days:
                print(company + " has not had activity in the given number of days: " + str(x))
                #adds the name of the inactive company to the inactive companies list
                inactiveCompanies.append(company)
                break

        
        print()
        print()

    
    print("LIST OF COMPANIES INACTIVE FOR " + str(days) + " DAYS.")
    for i in range(0, len(inactiveCompanies)):
            print(inactiveCompanies[i])

    return inactiveCompanies



a = rss_activity(feeds, 31)

print(a)











