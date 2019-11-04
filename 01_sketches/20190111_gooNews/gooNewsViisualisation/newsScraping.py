import requests, bs4, sys, webbrowser

res = requests.get('https://news.goo.ne.jp/')

res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)

#print(res.text[:100])

articles = soup.select('.list-title-topics')
print(articles[0].string)

#<span class="list-title-topics">関東は午後に雨　初雪の可能性も</span>