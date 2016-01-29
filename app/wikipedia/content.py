import wikipedia


def get_articles(n):
    articles = wikipedia.random(n)
    data = {}

    for article in articles:
        article = wikipedia.page(article)
        data[article.title] = {
            'url': article.url,
            'summary': article.summary,
            'categories': article.categories,
            'content': article.content
        }

    return data
