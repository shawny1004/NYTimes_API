import requests
TOKEN = 'CGAc7KTGMZYyqENK8ffwp6cTadBHEM2F'
SEC = 'INUb6OToTxOCevnJ'

class nytimes_client:

    def get_news(self):
        return requests.get(f'https://api.nytimes.com/svc/search/v2/articlesearch.json?q=election&api-key={TOKEN}')