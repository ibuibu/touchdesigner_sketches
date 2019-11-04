import requests, bs4, sys, webbrowser

res = requests.get('https://google.com/search?q='+''.join(sys.argv[1:]))

res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)
link_elms = soup.select('.r a')

num_open = min(2, len(link_elms))
for i in range(num_open):
	webbrowser.open('http://google.com' + link_elms[i].get('href'))

