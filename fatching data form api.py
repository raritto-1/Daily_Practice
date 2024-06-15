import requests

def fetch_top_headlines(api_key, country='us'):
    url = 'https://newsapi.org/v2/top-headlines'
    params = {'country': country, 'apiKey': api_key}

    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)

    data = response.json()
    articles = data.get('articles', [])

    for article in articles:
        print(f"Title: {article['title']}\nDescription: {article['description']}\nURL: {article['url']}\n")

# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'c41c76eca92d439eab8013bd65eb6f9b'
fetch_top_headlines(api_key)
