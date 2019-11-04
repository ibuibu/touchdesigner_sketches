import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

try:
	res.raise_for_status()
except Exception as exc:
	print('problem:{}'.format(exc))

print(res.text[:250])
