import feedparser
import newspaper
from newspaper import Article
from time import mktime
from datetime import datetime



def getFeed():
    d = feedparser.parse('https://www.huffingtonpost.com/section/arts/feed')

    huffPostArticles =  []

    count = 0

    for entry in d.entries:
        if hasattr(entry, 'published'):
            count += 1
            article = {}
            article['link'] = entry.link
            date = entry.published_parsed
            article['published'] = datetime.fromtimestamp(mktime(date)).isoformat()

            try:
                content = Article(entry.link)
                content.download()
                content.parse()

            except Exception as e:

                print(e)
                continue

            article['title'] = content.title
            article['text'] = content.text
            huffPostArticles.append(article)

    for article in huffPostArticles:
        print(article['title'])


getFeed()