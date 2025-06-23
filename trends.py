import feedparser
import random

NEWS_SOURCES = [
    "https://news.google.com/rss?hl=en",
    "https://www.reddit.com/r/worldnews/.rss",
    "https://trends.google.com/trends/trendingsearches/daily/rss?geo=US"
]

def get_trending_topics():
    headlines = []
    for url in NEWS_SOURCES:
        feed = feedparser.parse(url)
        for entry in feed.entries[:5]:
            headlines.append(entry.title)
    return headlines
