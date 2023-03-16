import requests

# r = requests.get("https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2023-2-23&to=2023-2-28&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c&apiKey=8e36ee183cb743169ac0a7f9e6d2904f")
# content = r.json()
# print(type(content))
# # print(content)
# articles = content["articles"]
# print(type(articles))

# for article in articles:
#     print('TITLE: ', article["title"],
#           '\nDESCRIPTION: ', article["description"])


def get_news(topic, from_date, to_date, language='en',
            api_key='8e36ee183cb743169ac0a7f9e6d2904f'):
    """get news from website

    Parameters
    ----------
    topic : string
        _description_
    from_date : date
        _description_
    to_date : date
        _description_
    language : str, optional
        _description_, by default 'en'
    api_key : str, optional
        _description_, by default '8e36ee183cb743169ac0a7f9e6d2904f'
    """
    url = f"https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={api_key}"
    r = requests.get(url)
    content = r.json()
    articles = content["articles"]
    results = []
    for article in articles:
        results.append(f"TITLE: ' {article['title']}, '\nDESCRIPTION: ', {article['description']}")
    return results

print(get_news(topic="space", from_date='2023-2-27', to_date='2023-2-28'))

import requests

# r = requests.get("https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2023-2-23&to=2023-2-28&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c&apiKey=8e36ee183cb743169ac0a7f9e6d2904f")
# content = r.json()
# print(type(content))
# # print(content)
# articles = content["articles"]
# print(type(articles))

# for article in articles:
#     print('TITLE: ', article["title"],
#           '\nDESCRIPTION: ', article["description"])


def get_news(country, language='en',
            api_key='8e36ee183cb743169ac0a7f9e6d2904f'):
    """get news from website

    Parameters
    ----------
    topic : string
        _description_
    from_date : date
        _description_
    to_date : date
        _description_
    language : str, optional
        _description_, by default 'en'
    api_key : str, optional
        _description_, by default '8e36ee183cb743169ac0a7f9e6d2904f'
    """
    url = f"https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={api_key}"
    r = requests.get(url)
    content = r.json()
    articles = content["articles"]
    results = []
    for article in articles:
        results.append(f"TITLE: ' {article['title']}, '\nDESCRIPTION: ', {article['description']}")
    return results
