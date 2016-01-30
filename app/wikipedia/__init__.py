import wikipedia


def get_articles(n=2):
    articles = wikipedia.random(n)
    print(articles)
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
