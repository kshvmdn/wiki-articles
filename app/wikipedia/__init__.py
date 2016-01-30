import wikipedia
import random


def parse_articles(articles):
    data = {}
    for article in articles:
        try:
            article = wikipedia.page(article)
        except:
            articles.append(wikipedia.random(1))
        data[article.title] = {
            'title': article.title,
            'url': article.url,
            'summary': article.summary,
            'categories': article.categories,
            'content': article.content
        }
        print(article)
    return data



def get_articles_for_search(query):
    articles = wikipedia.search(query)
    random.shuffle(articles)
    return parse_articles(articles[:7])


def get_random_articles(n=5):
    return parse_articles(wikipedia.random(n))
