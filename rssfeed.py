#Given a Dictionary keyed by Company and valued by RSS feed url, write a function that determines which companies had no activity for a given number of days
#by Connor Davidson. created June 14,2019.




#might need recursion for the "some companies might have more than one feed" part. some companies just provide links to a page with several rss pages.
#get the parsed rss info from the URL, then iterate through it's info (something like: while x < len(entries)) and use .updated.
#if it hasn't been updated within the given number of days, then the company name gets put into an array. 


#might need to get the xml file and go through it looking for <link> tags..
#   get their contents and do a contains(.rss) on it to check if it has it in it 




import feedparser
import ssl


feeds = {
        "bbc1"       : "http://feeds.bbci.co.uk/news/rss.xml",
        "bbc2"       : "http://feeds.bbci.co.uk/news/world/rss.xml",
        "bbc3"       : "http://feeds.bbci.co.uk/news/education/rss.xml",
        "craigslist" : "https://www.craigslist.org/about/best/all/index.rss",
        "Joe Rogan"  : "http://podcasts.joerogan.net/feed",
        "espn1"      : "https://www.espn.com/espn/rss/news",
        "espn2"      : "https://www.espn.com/espn/rss/nfl/news",
        "espn3"      : "https://www.espn.com/espn/rss/espnu/news",
        "reddit1"    : "https://www.reddit.com/.rss",
        "reddit2"    : "https://www.reddit.com/r/news/.rss",
        "WSJ"        : "https://feeds.a.dj.com/rss/RSSWorldNews.xml",
        "WaPo1"      : "http://feeds.washingtonpost.com/rss/rss_fact-checker",
        "Wapo2"      : "http://feeds.washingtonpost.com/rss/rss_innovations"
         }




#makes sure ssl is working correctly
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context


#this 
for company, url in feeds.items():
    d = feedparser.parse(url)
    print(company.upper() )
    print(len(d.entries))
    for entry in range(0, len(d.entries)):
        print( str(entry) + " : " +d.entries[entry].title)
        print( d.entries[entry].updated )
        print()
    print()
    print()











