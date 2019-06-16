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
        "bbc" : "https://www.bbc.com/news/10628494",
        "craigslist" : "https://www.craigslist.org/about/rss",
        "espn" : "https://www.espn.com/espn/news/story?page=rssinfo",
        "fox news" : "https://www.foxnews.com/about/rss/",
        "NYT": "https://archive.nytimes.com/www.nytimes.com/services/xml/rss/index.html?mcubz=0",
        "reddit" : "https://www.reddit.com/wiki/rss",
        "Wall Street Journal" : "https://www.wsj.com/news/rss-news-and-feeds",
        "Washington Post" : "https://www.washingtonpost.com/discussions/2018/10/12/washington-post-rss-feeds/?noredirect=on"
         }




#makes sure ssl is working correctly
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context




url = "https://www.craigslist.org/about/best/all/index.rss"

d = feedparser.parse(url)

for e in range(0, len(d.entries)):
    
    print( str(e) + " : " + d.entries[e].title )
    
    print( d.entries[e].updated )
    print()
    print()









